import pandas as pd
import numpy as np
from itertools import chain, product

import torch

from time import process_time
from time import time

from torch.utils.data.sampler import SubsetRandomSampler
from torch.utils.data.dataloader import DataLoader
import torch.utils.data as data_utils
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import torch.nn.functional as F
import torch.nn as nn

import pickle


# simple extension of base clase to handle
class MLModel(nn.Module):
    def __init__(self, in_size, hidden_sizes, out_size):
        super().__init__()
        self.inputLayer = nn.Linear(in_size, hidden_sizes[0])
        self.nHiddenLayers = len(hidden_sizes)
        self.hiddenLayers = nn.ModuleList()
        if self.nHiddenLayers > 1:
            for x in range(self.nHiddenLayers - 1):
                self.hiddenLayers.append(nn.Linear(hidden_sizes[x], hidden_sizes[x + 1]))
        self.outputLayer = nn.Linear(hidden_sizes[-1], out_size)

    def forward(self, xb):
        xb = xb.view(xb.size(0), -1)
        out = self.inputLayer(xb)
        out = F.relu(out)
        for layer in self.hiddenLayers:
            out = layer(out)
            out = F.relu(out)
        out = self.outputLayer(out)
        return out


# Send data to device
def to_device(data, device):
    if isinstance(data, (list, tuple)):
        return [to_device(x, device) for x in data]
    return data.to(device, non_blocking=True)


# load data onto device
class DeviceDataLoader():
    def __init__(self, dl, device):
        self.dl = dl
        self.device = device

    def __iter__(self):
        for b in self.dl:
            yield to_device(b, self.device)

    def __len__(self):
        return len(self.dl)


# Returns the loss of a batch of evalutations
def loss_batch(model, loss_func, xb, yb, opt=None, metric=None):
    preds = model(xb)
    loss = loss_func(preds, yb)

    if opt is not None:
        loss.backward()
        opt.step()
        opt.zero_grad()

    metric_result = None
    if metric is not None:
        metric_result = metric(preds, yb)

    return loss.item(), len(xb), metric_result


# Evaluate the model on validation or test data with given metric
def evaluate(model, loss_fn, valid_dl, metric=None):
    with torch.no_grad():
        results = [loss_batch(model, loss_fn, xb.float(), yb.float(), metric=metric) for xb, yb in valid_dl]
        losses, nums, metrics = zip(*results)
        total = np.sum(nums)
        avg_loss = np.sum(np.multiply(losses, nums)) / total
        avg_metric = None
        if metric is not None:
            numnums = np.tile(nums, 1).reshape(np.asarray(metrics).shape)
            avg_metric = np.sum(np.multiply(metrics, numnums), axis=0) / total
        return avg_loss, total, avg_metric


# Handles the fitting of the weights to the data and provides updates as training progresses
def fit(epochs, lr, model, loss_fn, train_dl, valid_dl, l2=0.0001, metric=None, opt_fn=None
        , update=5):
    hFormat1 = ' |{0:^22}|{1:^12}|{2:^12}|'
    hFormat2 = ' |{0:>11}{1:<11d}|{2:^12}|{3:^12}|'
    dFormat = ' |{0:^22d}|{1:>12.4f}|{2:>12.4f}|'

    losses, metrics, tmetrics, tepochs = [], [], [], []
    if opt_fn is None: opt_fn = torch.optim.Adam
    opt = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=l2)
    for epoch in range(epochs):
        for xb, yb in train_dl:
            loss, _, train_metric = loss_batch(model, loss_fn, xb.float(), yb.float(), opt)
        result = evaluate(model, loss_fn, valid_dl, metric)
        val_loss, total, val_metric = result
        losses.append(val_loss)
        metrics.append(val_metric)
        if epoch == 0:
            print(hFormat1.format('Epoch', 'Training', 'Validation'))
            print(hFormat2.format('Total: ', epochs, 'Loss (MAE)', 'Loss (MAE)'))
            print(' ' + '-' * 50)
        if (((epoch + 1) % update == 0) or (epoch == 0) or (epoch + 1 == epochs)):
            tresult = evaluate(model, loss_fn, train_dl, metric)
            _, _, train_metric = tresult
            tmetrics.append(train_metric)
            tepochs.append(epoch)
            if metric is None:
                print('Epoch [{}/{}], loss: {:.4f}'.format(epoch + 1, epochs, val_loss))
            else:
                print(dFormat.format(epoch + 1, *train_metric, *val_metric))
    return losses, metrics, tepochs, tmetrics


# Calcluate the mean average error
def mae_score(outputs, labels):
    return mean_absolute_error(outputs.cpu(), labels.cpu(), multioutput='raw_values')


# function for training model and getting validation scores
def runNN(train_dl, valid_dl, tFeatures, vFeatures, hidden_sizes=None, learning_rate=0.5, epochs=20, l2_penalty=0.01,
          update=5, model=None):
    if hidden_sizes is None:
        hidden_sizes = [32, 32, 32]
    print(' ' + '-' * 50)
    input_size = 36
    num_outputs = 1

    # running model on cpu
    device = torch.device('cpu')

    # send data to device
    train_dl = DeviceDataLoader(train_dl, device)
    valid_dl = DeviceDataLoader(valid_dl, device)

    # if not adding to a model, need to create one
    if model is None:
        model = MLModel(in_size=input_size, hidden_sizes=hidden_sizes, out_size=num_outputs)

    # send model to device
    to_device(model, device)

    # train model
    t0 = time()
    pt0 = process_time()
    losses, metrics, tepochs, tmetrics = fit(epochs, learning_rate, model, F.mse_loss, train_dl, valid_dl,
                                             metric=mae_score, l2=l2_penalty, update=update)

    # print summary of training
    print(' ' + '-' * 50)
    t1 = time()
    pt1 = process_time()
    print('-' * 40)
    print('Model fitting/training time using: ', device)
    print('Process time: {:10.2f}'.format(pt1 - pt0))
    print('Wall time: {:10.2f}'.format(t1 - t0))
    print('-' * 40)

    # get training and validation scores
    tpredictions = model(to_device(tFeatures.float(), device))
    vpredictions = model(to_device(vFeatures.float(), device))
    lformat = ' |{0:>22}|{1:>10.6f}|'
    print(lformat.format('Training Error ', mean_absolute_error(Y_train, tpredictions.cpu().detach().numpy(), )))
    print(lformat.format('Validation Error ', mean_absolute_error(Y_validation,
                                                                  vpredictions.cpu().detach().numpy())))

    return model, losses, metrics, tepochs, tmetrics


# import the data as dataframe
df = pd.read_csv("intensityData_90.csv")

# create dataframes from data
X = df[df.columns[0:36]]
Y = df[df.columns[36:]]

# Scaling data -- needed to put all inputs on same "scale"
# i.e. mean of 0 and variance of 1; typically this improves training performance
scaling = StandardScaler()
scaling.fit(X)
scaled_X = scaling.fit_transform(X)
scaled_X = pd.DataFrame(scaled_X, columns=X.columns)

# This fit can be used later on as well, when used on real data
with open('scaling.pkl', 'wb') as f:
    pickle.dump(scaling, f)

X_train, X_test, Y_train, Y_test = train_test_split(scaled_X, Y, test_size=0.2, random_state=1)
X_train, X_validation, Y_train, Y_validation = train_test_split(X_train, Y_train, test_size=0.25, random_state=1)

# Set data up for pytorch (define features [inputs] and target [output], convert to tensors, batch it and load it)
batch_size = 64
tFeatures = torch.tensor(X_train.values)
tTargets = torch.tensor(Y_train.values)
train = data_utils.TensorDataset(tFeatures, tTargets)
train_dl = data_utils.DataLoader(train, batch_size=batch_size, shuffle=True)
vFeatures = torch.tensor(X_validation.values)
vTargets = torch.tensor(Y_validation.values)
validation = data_utils.TensorDataset(vFeatures, vTargets)
valid_dl = data_utils.DataLoader(validation, batch_size=batch_size, shuffle=True)

# Setup model (this is a bigger model originally meant for a GPU
# the hidden layers can be shrunk/trimmed.
hidden_sizes = [72, 72, 72, 72, 72, 72]
epochs = 3315
ep_update = 100
learning_rate = 0.001
l2p = 0.01

# run the model
pytNN4, losses4, metrics4 = runNN(train_dl, valid_dl, tFeatures, vFeatures, hidden_sizes=hidden_sizes
                                  , learning_rate=learning_rate, epochs=epochs
                                  , l2_penalty=l2p, update=ep_update)

# In[ ]:




