#
# Python script to run shadow3. Created automatically with ShadowTools.make_python_script_from_list().
#
# Code adapted by Trent Mathews
# Use code to create a .csv file for a sample space
#

import Shadow
import numpy
import random
import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns

# change this value to generate unique data for same sample space
random.seed(2)


# function for getting the FWHM in case you need this, currently not in use in the code
# call it as horizontal, vertical = calcFWHM(beam, 1, 3). 1 = x coord and 3 = z coord in shadow lib
def calcFWHM(beam, col_h, col_v):
    if isinstance(beam, str):
        beam1 = Shadow.Beam()
        beam1.load(beam)
        beam = beam1

    tmp = beam.histo2(col_h, col_v, nbins=101, nolost=1)

    h = tmp["fwhm_h"] * pow(10, 3)
    v = tmp["fwhm_v"] * pow(10, 3)

    h = format(h, '0.3f')
    v = format(v, '0.3f')
    return h, v


def sim(Motor):
    # write (1) or not (0) SHADOW files start.xx end.xx star.xx
    iwrite = 0

    #  Start the beam simulation
    #
    # initialize shadow3 source (oe0) and beam
    #
    beam = Shadow.Beam()
    oe0 = Shadow.Source()
    oe1 = Shadow.OE()
    oe2 = Shadow.OE()
    oe3 = Shadow.OE()
    oe4 = Shadow.OE()
    oe5 = Shadow.OE()
    oe6 = Shadow.OE()

    #
    # Define variables. See meaning of variables in:
    #  https://raw.githubusercontent.com/srio/shadow3/master/docs/source.nml
    #  https://raw.githubusercontent.com/srio/shadow3/master/docs/oe.nml
    #
    #  all of the values come from the OASYS model of the IEX beamline
    #  undulator
    oe0.FDISTR = 3
    oe0.F_COLOR = 3
    oe0.F_PHOT = 0
    oe0.HDIV1 = 0.5
    oe0.HDIV2 = 0.5
    oe0.IDO_VX = 0
    oe0.IDO_VZ = 0
    oe0.IDO_X_S = 0
    oe0.IDO_Y_S = 0
    oe0.IDO_Z_S = 0
    oe0.NPOINT = 100000
    oe0.NTOTALPOINT = 20000
    oe0.PH1 = 499.97
    oe0.PH2 = 500.03
    oe0.SIGDIX = 1.964e-05
    oe0.SIGDIZ = 1.6349401e-05
    oe0.SIGMAX = 0.27609399
    oe0.SIGMAZ = 0.0261531994
    oe0.VDIV1 = 0.5
    oe0.VDIV2 = 0.5

    #  plane mirror
    oe1.ALPHA = 90.0
    oe1.DUMMY = 0.1
    oe1.FHIT_C = 1
    oe1.FWRITE = 3
    oe1.F_MOVE = 1
    oe1.RLEN1 = 260.0
    oe1.RLEN2 = 260.0
    oe1.RWIDX1 = 20.0
    oe1.RWIDX2 = 20.0
    oe1.T_IMAGE = 0.0
    oe1.T_INCIDENCE = 89.599998
    oe1.T_REFLECTION = 89.599998
    oe1.T_SOURCE = 30800.0
    oe1.OFFX = Motor.xoff1
    oe1.OFFY = Motor.yoff1
    oe1.OFFZ = Motor.zoff1
    oe1.X_ROT = Motor.xrot1
    oe1.Y_ROT = Motor.yrot1
    oe1.Z_ROT = Motor.zrot1
    #  when taking into account reflectivity
    # oe1.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    # oe1.F_REFLEC = 1

    #  plane mirror
    oe2.DUMMY = 0.1
    oe2.FHIT_C = 1
    oe2.FWRITE = 3
    oe2.F_MOVE = 1
    oe2.RLEN1 = 75.0
    oe2.RLEN2 = 75.0
    oe2.RWIDX1 = 22.5
    oe2.RWIDX2 = 22.5
    oe2.T_IMAGE = 0.0
    oe2.T_INCIDENCE = 88.5
    oe2.T_REFLECTION = 88.5
    oe2.T_SOURCE = 500.0
    oe2.OFFX = Motor.xoff2
    oe2.OFFY = Motor.yoff2
    oe2.OFFZ = Motor.zoff2
    oe2.X_ROT = Motor.xrot2
    oe2.Y_ROT = Motor.yrot2
    oe2.Z_ROT = Motor.zrot2
    #  reflect
    # oe2.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    # oe2.F_REFLEC = 1

    #  plane mirror
    oe3.ALPHA = 90.0
    oe3.DUMMY = 0.1
    oe3.FHIT_C = 1
    oe3.FWRITE = 3
    oe3.F_MOVE = 1
    oe3.RLEN1 = 190.0
    oe3.RLEN2 = 190.0
    oe3.RWIDX1 = 15.0
    oe3.RWIDX2 = 15.0
    oe3.T_IMAGE = 0.0
    oe3.T_INCIDENCE = 86.810772
    oe3.T_REFLECTION = 86.810772
    oe3.T_SOURCE = 8265.8165
    oe3.OFFX = Motor.xoff3
    oe3.OFFY = Motor.yoff3
    oe3.OFFZ = Motor.zoff3
    oe3.X_ROT = Motor.xrot3
    oe3.Y_ROT = Motor.yrot3
    oe3.Z_ROT = Motor.zrot3
    #  reflect
    # oe3.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    # oe3.F_REFLEC = 1

    #  plane grating
    oe4.ALPHA = 180.0
    oe4.DUMMY = 0.1
    oe4.FHIT_C = 1
    oe4.FWRITE = 2
    oe4.F_GRATING = 1
    oe4.F_MOVE = 1
    oe4.F_RULING = 5
    oe4.F_RUL_ABS = 1
    oe4.RLEN1 = 57.5
    oe4.RLEN2 = 57.5
    oe4.RULING = 1199.22002
    oe4.RUL_A1 = 0.165491998
    oe4.RUL_A2 = 1.0793e-05
    oe4.RUL_A3 = 1.99999999e-06
    oe4.RWIDX1 = 12.5
    oe4.RWIDX2 = 12.5
    oe4.T_IMAGE = 2000.0
    oe4.T_INCIDENCE = 87.771697
    oe4.T_REFLECTION = 85.049847
    oe4.T_SOURCE = 135.0
    oe4.OFFX = Motor.xoff4
    oe4.OFFY = Motor.yoff4
    oe4.OFFZ = Motor.zoff4
    oe4.X_ROT = Motor.xrot4
    oe4.Y_ROT = Motor.yrot4
    oe4.Z_ROT = Motor.zrot4

    #  ellipsoid mirror oe6 -> oe5 after removing slit
    oe5.ALPHA = 90.0
    oe5.AXMAJ = 33150.0
    oe5.AXMIN = 296.85199
    oe5.DUMMY = 0.1
    oe5.ELL_THE = 0.186719999
    oe5.FCYL = 1
    oe5.FHIT_C = 1
    oe5.FMIRR = 2
    oe5.FWRITE = 3
    oe5.F_EXT = 1
    oe5.F_MOVE = 1
    oe5.RLEN1 = 140.0
    oe5.RLEN2 = 140.0
    oe5.RWIDX1 = 7.5
    oe5.RWIDX2 = 7.5
    oe5.T_IMAGE = 0.0
    oe5.T_INCIDENCE = 88.5
    oe5.T_REFLECTION = 88.5
    oe5.T_SOURCE = 4600.0
    oe5.OFFX = Motor.xoff5
    oe5.OFFY = Motor.yoff5
    oe5.OFFZ = Motor.zoff5
    oe5.X_ROT = Motor.xrot5
    oe5.Y_ROT = Motor.yrot5
    oe5.Z_ROT = Motor.zrot5
    #  reflect
    # oe6.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    # oe6.F_REFLEC = 1

    #  ellipsoid mirror oe7 -> oe6 after removing slit
    oe6.ALPHA = 90.0
    oe6.AXMAJ = 3300.0
    oe6.AXMIN = 66.6355972
    oe6.DUMMY = 0.1
    oe6.ELL_THE = 1.40167999
    oe6.FCYL = 1
    oe6.FHIT_C = 1
    oe6.FMIRR = 2
    oe6.FWRITE = 3
    oe6.F_EXT = 1
    oe6.F_MOVE = 1
    oe6.RLEN1 = 35.0
    oe6.RLEN2 = 35.0
    oe6.RWIDX1 = 10.0
    oe6.RWIDX2 = 10.0
    oe6.T_IMAGE = 1200.0
    oe6.T_INCIDENCE = 88.5
    oe6.T_REFLECTION = 88.5
    oe6.T_SOURCE = 800.0
    oe6.OFFX = Motor.xoff6
    oe6.OFFY = Motor.yoff6
    oe6.OFFZ = Motor.zoff6
    oe6.X_ROT = Motor.xrot6
    oe6.Y_ROT = Motor.yrot6
    oe6.Z_ROT = Motor.zrot6
    #  reflect
    # oe7.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    # oe7.F_REFLEC = 1

    # Run SHADOW to create the source
    if iwrite:
        oe0.write("start.00")

    beam.genSource(oe0)

    if iwrite:
        oe0.write("end.00")
        beam.write("begin.dat")

    #
    # run optical element 1
    #
    print("    Running optical element: %d" % (1))
    if iwrite:
        oe1.write("start.01")

    beam.traceOE(oe1, 1)

    if iwrite:
        oe1.write("end.01")
        beam.write("star.01")

    #
    # run optical element 2
    #
    print("    Running optical element: %d" % (2))
    if iwrite:
        oe2.write("start.02")

    beam.traceOE(oe2, 2)

    if iwrite:
        oe2.write("end.02")
        beam.write("star.02")

    #
    # run optical element 3
    #
    print("    Running optical element: %d" % (3))
    if iwrite:
        oe3.write("start.03")

    beam.traceOE(oe3, 3)

    if iwrite:
        oe3.write("end.03")
        beam.write("star.03")

    #
    # run optical element 4
    #
    print("    Running optical element: %d" % (4))
    if iwrite:
        oe4.write("start.04")

    beam.traceOE(oe4, 4)

    if iwrite:
        oe4.write("end.04")
        beam.write("star.04")

    #
    # run optical element 5
    #
    print("    Running optical element: %d" % (5))
    if iwrite:
        oe5.write("start.05")

    beam.traceOE(oe5, 5)

    if iwrite:
        oe5.write("end.05")
        beam.write("star.05")

    #
    # run optical element 6
    #
    print("    Running optical element: %d" % (6))
    if iwrite:
        oe6.write("start.06")

    beam.traceOE(oe6, 6)

    if iwrite:
        oe6.write("end.06")
        beam.write("star.06")

    return Shadow.Beam.nrays(beam, nolost=1)


#  class for assigning degrees of freedom
#  leave the class set to 0
#  to change values,
class motor:
    xoff1 = 0.00
    yoff1 = 0.00
    zoff1 = 0.00
    xrot1 = 0.00
    yrot1 = 0.00
    zrot1 = 0.00

    xoff2 = 0.00
    yoff2 = 0.00
    zoff2 = 0.00
    xrot2 = 0.00
    yrot2 = 0.00
    zrot2 = 0.00

    xoff3 = 0.00
    yoff3 = 0.00
    zoff3 = 0.00
    xrot3 = 0.00
    yrot3 = 0.00
    zrot3 = 0.00

    xoff4 = 0.00
    yoff4 = 0.00
    zoff4 = 0.00
    xrot4 = 0.00
    yrot4 = 0.00
    zrot4 = 0.00

    xoff5 = 0.00
    yoff5 = 0.00
    zoff5 = 0.00
    xrot5 = 0.00
    yrot5 = 0.00
    zrot5 = 0.00

    xoff6 = 0.00
    yoff6 = 0.00
    zoff6 = 0.00
    xrot6 = 0.00
    yrot6 = 0.00
    zrot6 = 0.00


# create the sample space for testing
def sample(Motor):
    # use 20 if the number is too large for offset
    # ranges from intensityData_90.csv
    Motor.xoff1 = float(format(random.uniform(-19.8, 19.8), '0.4f'))
    Motor.xoff2 = float(format(random.uniform(-20.0, 20.0), '0.4f'))
    Motor.xoff3 = float(format(random.uniform(-14.5, 14.5), '0.4f'))
    Motor.xoff4 = float(format(random.uniform(-12.0, 12.0), '0.4f'))
    Motor.xoff5 = float(format(random.uniform(-7.1, 7.1), '0.4f'))
    Motor.xoff6 = float(format(random.uniform(-10.8, 10.8), '0.4f'))

    Motor.yoff1 = float(format(random.uniform(-20, 20), '0.4f'))
    Motor.yoff2 = float(format(random.uniform(-20, 20), '0.4f'))
    Motor.yoff3 = float(format(random.uniform(-20, 20), '0.4f'))
    Motor.yoff4 = float(format(random.uniform(-20, 20), '0.4f'))
    Motor.yoff5 = float(format(random.uniform(-20, 20), '0.4f'))
    Motor.yoff6 = float(format(random.uniform(-20, 20), '0.4f'))

    Motor.zoff1 = float(format(random.uniform(-0.8, 0.8), '0.4f'))
    Motor.zoff2 = float(format(random.uniform(-1.5, 1.5), '0.4f'))
    Motor.zoff3 = float(format(random.uniform(-0.4, 0.4), '0.4f'))
    Motor.zoff4 = float(format(random.uniform(-0.4, 0.4), '0.4f'))
    Motor.zoff5 = float(format(random.uniform(-3.1, 3.1), '0.4f'))
    Motor.zoff6 = float(format(random.uniform(-0.9, 0.9), '0.4f'))

    Motor.xrot1 = float(format(random.uniform(-0.006, 0.006), '0.4f'))
    Motor.xrot2 = float(format(random.uniform(-0.005, 0.005), '0.4f'))
    Motor.xrot3 = float(format(random.uniform(-0.003, 0.003), '0.4f'))
    Motor.xrot4 = float(format(random.uniform(-0.002, 0.002), '0.4f'))
    Motor.xrot5 = float(format(random.uniform(-0.319, 0.319), '0.4f'))
    Motor.xrot6 = float(format(random.uniform(-1.38, 1.38), '0.4f'))

    Motor.yrot1 = float(format(random.uniform(-0.218, 0.218), '0.4f'))
    Motor.yrot2 = float(format(random.uniform(-0.024, 0.024), '0.4f'))
    Motor.yrot3 = float(format(random.uniform(-0.160, 0.160), '0.4f'))
    Motor.yrot4 = float(format(random.uniform(-0.144, 0.144), '0.4f'))
    Motor.yrot5 = float(format(random.uniform(-0.5, 0.5), '0.4f'))
    Motor.yrot6 = float(format(random.uniform(-20.0, 20.0), '0.4f'))

    Motor.zrot1 = float(format(random.uniform(-10.6, 10.6), '0.4f'))
    Motor.zrot2 = float(format(random.uniform(-20, 20), '0.4f'))
    Motor.zrot3 = float(format(random.uniform(-20, 20), '0.4f'))
    Motor.zrot4 = float(format(random.uniform(-4.6, 4.6), '0.4f'))
    Motor.zrot5 = float(format(random.uniform(-10.4, 10.4), '0.4f'))
    Motor.zrot6 = float(format(random.uniform(-20, 20), '0.4f'))

    return motor


def main():
    #
    rays = []
    plotCount = 1

    # code for create a .csv file
    with open('intensityData.csv', 'w', newline='') as file:
        fieldnames = ['oe1-x', 'oe1-y', 'oe1-z', 'oe1-rotx', 'oe1-roty', 'oe1-rotz',
                      'oe2-x', 'oe2-y', 'oe2-z', 'oe2-rotx', 'oe2-roty', 'oe2-rotz',
                      'oe3-x', 'oe3-y', 'oe3-z', 'oe3-rotx', 'oe3-roty', 'oe3-rotz',
                      'oe4-x', 'oe4-y', 'oe4-z', 'oe4-rotx', 'oe4-roty', 'oe4-rotz',
                      'oe5-x', 'oe5-y', 'oe5-z', 'oe5-rotx', 'oe5-roty', 'oe5-rotz',
                      'oe6-x', 'oe6-y', 'oe6-z', 'oe6-rotx', 'oe6-roty', 'oe6-rotz', 'intensity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for x in range(10000):
            Motor = motor
            Motor = sample(Motor)
            nrays = sim(Motor)
            rays.append(nrays)
            # code for writing the .csv file
            writer.writerow({'oe1-x': str(Motor.xoff1), 'oe1-y': str(Motor.yoff1), 'oe1-z': str(Motor.zoff1),
                             'oe1-rotx': str(Motor.xrot1), 'oe1-roty': str(Motor.yrot1), 'oe1-rotz': str(Motor.zrot1),
                             'oe2-x': str(Motor.xoff2), 'oe2-y': str(Motor.yoff2), 'oe2-z': str(Motor.zoff2),
                             'oe2-rotx': str(Motor.xrot2), 'oe2-roty': str(Motor.yrot2), 'oe2-rotz': str(Motor.zrot2),
                             'oe3-x': str(Motor.xoff3), 'oe3-y': str(Motor.yoff3), 'oe3-z': str(Motor.zoff3),
                             'oe3-rotx': str(Motor.xrot3), 'oe3-roty': str(Motor.yrot3), 'oe3-rotz': str(Motor.zrot3),
                             'oe4-x': str(Motor.xoff4), 'oe4-y': str(Motor.yoff4), 'oe4-z': str(Motor.zoff4),
                             'oe4-rotx': str(Motor.xrot4), 'oe4-roty': str(Motor.yrot4), 'oe4-rotz': str(Motor.zrot4),
                             'oe5-x': str(Motor.xoff5), 'oe5-y': str(Motor.yoff5), 'oe5-z': str(Motor.zoff5),
                             'oe5-rotx': str(Motor.xrot5), 'oe5-roty': str(Motor.yrot5), 'oe5-rotz': str(Motor.zrot5),
                             'oe6-x': str(Motor.xoff6), 'oe6-y': str(Motor.yoff6), 'oe6-z': str(Motor.zoff6),
                             'oe6-rotx': str(Motor.xrot6), 'oe6-roty': str(Motor.yrot6), 'oe6-rotz': str(Motor.zrot6),
                             'intensity': str(nrays)})

    # plot a histogram for the data
    # reads the .csv to create a plot
    percent_max = 99  # change this to whatever the sample space is
    sns.set(font_scale=1.4)
    plt.tight_layout()
    histo_plot = pd.read_csv('intensityData.csv')
    histo_plot.hist('intensity', bins=100, log=True)
    plt.xlabel('Intensity')
    plt.ylabel('Configurations')
    plt.title(str(percent_max) + '% cutoff histogram')
    plt.savefig(str(percent_max) + '% histogram.png')
    print(str(percent_max) + '% has {}% zeros'.format(sum(histo_plot['intensity'] == 0) / 1e2))




if __name__ == "__main__":
    main()