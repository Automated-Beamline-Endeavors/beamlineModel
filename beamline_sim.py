# using miniconda3 to get access to Shadow3 library
import Shadow
import numpy
import random
import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

random.seed(2)


def sim(Motor):
    # write (1) or not (0) SHADOW files start.xx end.xx star.xx
    iwrite = 0

    #
    # Start the beam simulation
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
    oe1.OFFX = Motor.xoff1
    oe1.OFFY = Motor.yoff1
    oe1.OFFZ = Motor.zoff1
    oe1.RLEN1 = 260.0
    oe1.RLEN2 = 260.0
    oe1.RWIDX1 = 20.0
    oe1.RWIDX2 = 20.0
    oe1.T_IMAGE = 0.0
    oe1.T_INCIDENCE = 89.599998
    oe1.T_REFLECTION = 89.599998
    oe1.T_SOURCE = 30800.0
    oe1.X_ROT = Motor.xrot1
    oe1.Y_ROT = Motor.yrot1
    oe1.Z_ROT = Motor.zrot1
    #  when taking into account reflectivity
    #oe1.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    #oe1.F_REFLEC = 1

    #  plane mirror
    oe2.DUMMY = 0.1
    oe2.FHIT_C = 1
    oe2.FWRITE = 3
    oe2.F_MOVE = 1
    oe2.OFFX = Motor.xoff2
    oe2.OFFY = Motor.yoff2
    oe2.OFFZ = Motor.zoff2
    oe2.RLEN1 = 75.0
    oe2.RLEN2 = 75.0
    oe2.RWIDX1 = 22.5
    oe2.RWIDX2 = 22.5
    oe2.T_IMAGE = 0.0
    oe2.T_INCIDENCE = 88.5
    oe2.T_REFLECTION = 88.5
    oe2.T_SOURCE = 500.0
    oe2.X_ROT = Motor.xrot2
    oe2.Y_ROT = Motor.yrot2
    oe2.Z_ROT = Motor.zrot2
    #  reflect
    #oe2.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    #oe2.F_REFLEC = 1

    #  plane mirror
    oe3.ALPHA = 90.0
    oe3.DUMMY = 0.1
    oe3.FHIT_C = 1
    oe3.FWRITE = 3
    oe3.F_MOVE = 1
    oe3.OFFX = Motor.xoff3
    oe3.OFFY = Motor.yoff3
    oe3.OFFZ = Motor.zoff3
    oe3.RLEN1 = 190.0
    oe3.RLEN2 = 190.0
    oe3.RWIDX1 = 15.0
    oe3.RWIDX2 = 15.0
    oe3.T_IMAGE = 0.0
    oe3.T_INCIDENCE = 86.810772
    oe3.T_REFLECTION = 86.810772
    oe3.T_SOURCE = 8265.8165
    oe3.X_ROT = Motor.xrot3
    oe3.Y_ROT = Motor.yrot3
    oe3.Z_ROT = Motor.zrot3
    #  reflect
    #oe3.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    #oe3.F_REFLEC = 1

    #  plane grating
    oe4.ALPHA = 180.0
    oe4.DUMMY = 0.1
    oe4.FHIT_C = 1
    oe4.FWRITE = 2
    oe4.F_GRATING = 1
    oe4.F_MOVE = 1
    oe4.F_RULING = 5
    oe4.F_RUL_ABS = 1
    oe4.OFFX = Motor.xoff4
    oe4.OFFY = Motor.yoff4
    oe4.OFFZ = Motor.zoff4
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
    oe5.OFFX = Motor.xoff5
    oe5.OFFY = Motor.yoff5
    oe5.OFFZ = Motor.zoff5
    oe5.RLEN1 = 140.0
    oe5.RLEN2 = 140.0
    oe5.RWIDX1 = 7.5
    oe5.RWIDX2 = 7.5
    oe5.T_IMAGE = 0.0
    oe5.T_INCIDENCE = 88.5
    oe5.T_REFLECTION = 88.5
    oe5.T_SOURCE = 4600.0
    oe5.X_ROT = Motor.xrot5
    oe5.Y_ROT = Motor.yrot5
    oe5.Z_ROT = Motor.zrot5
    #  reflect
    #oe6.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    #oe6.F_REFLEC = 1

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
    oe6.OFFX = Motor.xoff6
    oe6.OFFY = Motor.yoff6
    oe6.OFFZ = Motor.zoff6
    oe6.RLEN1 = 35.0
    oe6.RLEN2 = 35.0
    oe6.RWIDX1 = 10.0
    oe6.RWIDX2 = 10.0
    oe6.T_IMAGE = 1200.0
    oe6.T_INCIDENCE = 88.5
    oe6.T_REFLECTION = 88.5
    oe6.T_SOURCE = 800.0
    oe6.X_ROT = Motor.xrot6
    oe6.Y_ROT = Motor.yrot6
    oe6.Z_ROT = Motor.zrot6
    #  reflect
    #oe6.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    #oe6.F_REFLEC = 1

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

    # return the number of good rays
    # print(str(beam.nrays(nolost=1)))
    return beam.nrays(nolost=1)


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


#  O.E. positions in mm and ccw,deg initialization
#  class for assigning degrees of freedom
def sample():
    # use 20 if the number is too large for offset
    # ranges from intensityData_90.csv
    sample_motor = motor
    sample_motor.xoff1 = float(format(random.uniform(-19.8, 19.8), '0.4f'))
    sample_motor.xoff2 = float(format(random.uniform(-20.0, 20.0), '0.4f'))
    sample_motor.xoff3 = float(format(random.uniform(-14.5, 14.5), '0.4f'))
    sample_motor.xoff4 = float(format(random.uniform(-12.0, 12.0), '0.4f'))
    sample_motor.xoff5 = float(format(random.uniform(-7.1, 7.1), '0.4f'))
    sample_motor.xoff6 = float(format(random.uniform(-10.8, 10.8), '0.4f'))

    sample_motor.yoff1 = float(format(random.uniform(-20, 20), '0.4f'))
    sample_motor.yoff2 = float(format(random.uniform(-20, 20), '0.4f'))
    sample_motor.yoff3 = float(format(random.uniform(-20, 20), '0.4f'))
    sample_motor.yoff4 = float(format(random.uniform(-20, 20), '0.4f'))
    sample_motor.yoff5 = float(format(random.uniform(-20, 20), '0.4f'))
    sample_motor.yoff6 = float(format(random.uniform(-20, 20), '0.4f'))

    sample_motor.zoff1 = float(format(random.uniform(-0.8, 0.8), '0.4f'))
    sample_motor.zoff2 = float(format(random.uniform(-1.5, 1.5), '0.4f'))
    sample_motor.zoff3 = float(format(random.uniform(-0.4, 0.4), '0.4f'))
    sample_motor.zoff4 = float(format(random.uniform(-0.4, 0.4), '0.4f'))
    sample_motor.zoff5 = float(format(random.uniform(-3.1, 3.1), '0.4f'))
    sample_motor.zoff6 = float(format(random.uniform(-0.9, 0.9), '0.4f'))

    sample_motor.xrot1 = float(format(random.uniform(-0.006, 0.006), '0.4f'))
    sample_motor.xrot2 = float(format(random.uniform(-0.005, 0.005), '0.4f'))
    sample_motor.xrot3 = float(format(random.uniform(-0.003, 0.003), '0.4f'))
    sample_motor.xrot4 = float(format(random.uniform(-0.002, 0.002), '0.4f'))
    sample_motor.xrot5 = float(format(random.uniform(-0.319, 0.319), '0.4f'))
    sample_motor.xrot6 = float(format(random.uniform(-1.38, 1.38), '0.4f'))

    sample_motor.yrot1 = float(format(random.uniform(-0.218, 0.218), '0.4f'))
    sample_motor.yrot2 = float(format(random.uniform(-0.024, 0.024), '0.4f'))
    sample_motor.yrot3 = float(format(random.uniform(-0.160, 0.160), '0.4f'))
    sample_motor.yrot4 = float(format(random.uniform(-0.144, 0.144), '0.4f'))
    sample_motor.yrot5 = float(format(random.uniform(-0.5, 0.5), '0.4f'))
    sample_motor.yrot6 = float(format(random.uniform(-20.0, 20.0), '0.4f'))

    sample_motor.zrot1 = float(format(random.uniform(-10.6, 10.6), '0.4f'))
    sample_motor.zrot2 = float(format(random.uniform(-20, 20), '0.4f'))
    sample_motor.zrot3 = float(format(random.uniform(-20, 20), '0.4f'))
    sample_motor.zrot4 = float(format(random.uniform(-4.6, 4.6), '0.4f'))
    sample_motor.zrot5 = float(format(random.uniform(-10.4, 10.4), '0.4f'))
    sample_motor.zrot6 = float(format(random.uniform(-20, 20), '0.4f'))

    return sample_motor


# function for displaying all of the values in the motor class
def print_motors(motors):
    print("motors.xoff1 = " + str(motors.xoff1))
    print("motors.yoff1 = " + str(motors.yoff1))
    print("motors.zoff1 = " + str(motors.zoff1))
    print("motors.xrot1 = " + str(motors.xrot1))
    print("motors.yrot1 = " + str(motors.yrot1))
    print("motors.zrot1 = " + str(motors.zrot1) + "\n")

    print("motors.xoff2 = " + str(motors.xoff2))
    print("motors.yoff2 = " + str(motors.yoff2))
    print("motors.zoff2 = " + str(motors.zoff2))
    print("motors.xrot2 = " + str(motors.xrot2))
    print("motors.yrot2 = " + str(motors.yrot2))
    print("motors.zrot2 = " + str(motors.zrot2) + "\n")

    print("motors.xoff3 = " + str(motors.xoff3))
    print("motors.yoff3 = " + str(motors.yoff3))
    print("motors.zoff3 = " + str(motors.zoff3))
    print("motors.xrot3 = " + str(motors.xrot3))
    print("motors.yrot3 = " + str(motors.yrot3))
    print("motors.zrot3 = " + str(motors.zrot3) + "\n")

    print("motors.xoff4 = " + str(motors.xoff4))
    print("motors.yoff4 = " + str(motors.yoff4))
    print("motors.zoff4 = " + str(motors.zoff4))
    print("motors.xrot4 = " + str(motors.xrot4))
    print("motors.yrot4 = " + str(motors.yrot4))
    print("motors.zrot4 = " + str(motors.zrot4) + "\n")

    print("motors.xoff5 = " + str(motors.xoff5))
    print("motors.yoff5 = " + str(motors.yoff5))
    print("motors.zoff5 = " + str(motors.zoff5))
    print("motors.xrot5 = " + str(motors.xrot5))
    print("motors.yrot5 = " + str(motors.yrot5))
    print("motors.zrot5 = " + str(motors.zrot5) + "\n")

    print("motors.xoff6 = " + str(motors.xoff6))
    print("motors.yoff6 = " + str(motors.yoff6))
    print("motors.zoff6 = " + str(motors.zoff6))
    print("motors.xrot6 = " + str(motors.xrot6))
    print("motors.yrot6 = " + str(motors.yrot6))
    print("motors.zrot6 = " + str(motors.zrot6))


#  set motors based off
def setMotors(mvalues):

    Motors = motor
    if len(mvalues) == 36:
        print("Assigning motor values to user specified values...")
        Motors.xoff1 = mvalues[0]
        Motors.yoff1 = mvalues[1]
        Motors.zoff1 = mvalues[2]
        Motors.xrot1 = mvalues[3]
        Motors.yrot1 = mvalues[4]
        Motors.zrot1 = mvalues[5]

        Motors.xoff2 = mvalues[6]
        Motors.yoff2 = mvalues[7]
        Motors.zoff2 = mvalues[8]
        Motors.xrot2 = mvalues[9]
        Motors.yrot2 = mvalues[10]
        Motors.zrot2 = mvalues[11]

        Motors.xoff3 = mvalues[12]
        Motors.yoff3 = mvalues[13]
        Motors.zoff3 = mvalues[14]
        Motors.xrot3 = mvalues[15]
        Motors.yrot3 = mvalues[16]
        Motors.zrot3 = mvalues[17]

        Motors.xoff4 = mvalues[18]
        Motors.yoff4 = mvalues[19]
        Motors.zoff4 = mvalues[20]
        Motors.xrot4 = mvalues[21]
        Motors.yrot4 = mvalues[22]
        Motors.zrot4 = mvalues[23]

        Motors.xoff5 = mvalues[24]
        Motors.yoff5 = mvalues[25]
        Motors.zoff5 = mvalues[26]
        Motors.xrot5 = mvalues[27]
        Motors.yrot5 = mvalues[28]
        Motors.zrot5 = mvalues[29]

        Motors.xoff6 = mvalues[30]
        Motors.yoff6 = mvalues[31]
        Motors.zoff6 = mvalues[32]
        Motors.xrot6 = mvalues[33]
        Motors.yrot6 = mvalues[34]
        Motors.zrot6 = mvalues[35]
        print_motors(Motors)

    else:
        print("Error in user specified values:")
        if len(mvalues) > 36:
            print("Too many values, motors set to sample values...")
        elif len(mvalues) < 36:
            print("Not enough values, motors set to sample values...")
        Motors = sample()
        print_motors(Motors)

    return Motors


if __name__ == "__main__":
    sim(motor)