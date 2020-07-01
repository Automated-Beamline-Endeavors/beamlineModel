#
# Python script to run shadow3. Created automatically with ShadowTools.make_python_script_from_list().
#
import Shadow
import numpy
import random
import matplotlib.pyplot as plt


random.seed()


def my_range(start, end, step):
    while start <= end:
        yield start
        start += step


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


def maximum(rays):
    maxima = 0
    instance = 0
    for x in range(len(rays)):
        if rays[x] > maxima:
            maxima = rays[x]
            instance = x + 1

    return maxima, instance


def sim(x, i, o, step):
    # write (1) or not (0) SHADOW files start.xx end.xx star.xx
    iwrite = 0
    x += 1

    #  O.E. positions in mm and ccw,deg initialization
    #  plane mirror
    class P1:
        x = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        y = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        z = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        xrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
        yrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
        zrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))

    #  plane mirror
    class P2:
        x = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        y = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        z = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        xrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
        yrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
        zrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))

    #  plane mirror
    class P3:
        x = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        y = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        z = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        xrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
        yrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
        zrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))

    #  plane grating
    class P4:
        x = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        y = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        z = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        xrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
        yrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
        zrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))

    ##  screen slits
    #class P5:
    #    x = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
    #    y = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
    #    z = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
    #    xrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
    #    yrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
    #    zrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))

    #  ellipsoid mirror
    class P6:
        x = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        y = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        z = 0  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        xrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
        yrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))
        zrot = 0  # float(format((random.random() * 2) - 1, '0.4f'))

    #  ellipsoid mirror
    class P7:
        x = step.x  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        y = step.y  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        z = step.z  # float(format((random.random() * 0.01) - 0.005, '0.4f'))
        xrot = step.xrot  # float(format((random.random() * 2) - 1, '0.4f'))
        yrot = step.yrot  # float(format((random.random() * 2) - 1, '0.4f'))
        zrot = step.zrot  # float(format((random.random() * 2) - 1, '0.4f'))

    #  Start the beam simulation
    #  Sweep from -0.0005 to 0.0005 with step size = 0.0005
    #  Sweep from -3 to 3 with step size = 1

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
    #oe7 = Shadow.OE()

    #  print the input arguments for each instance
    i.write("Instance: " + str(x) + "\nOptical Element 1\n")
    i.write("Offset X = " + str(P1.x) + " mm\n")
    i.write("Offset Y = " + str(P1.y) + " mm\n")
    i.write("Offset Z = " + str(P1.z) + " mm\n")
    i.write("Rotation X = " + str(P1.xrot) + " CCW,deg\n")
    i.write("Rotation Y = " + str(P1.yrot) + " CCW,deg\n")
    i.write("Rotation Z = " + str(P1.zrot) + " CCW,deg\n\n")

    i.write("Optical Element 2:\n")
    i.write("Offset X = " + str(P2.x) + " mm\n")
    i.write("Offset Y = " + str(P2.y) + " mm\n")
    i.write("Offset Z = " + str(P2.z) + " mm\n")
    i.write("Rotation X = " + str(P2.xrot) + " CCW,deg\n")
    i.write("Rotation Y = " + str(P2.yrot) + " CCW,deg\n")
    i.write("Rotation Z = " + str(P2.zrot) + " CCW,deg\n\n")

    i.write("Optical Element 3:\n")
    i.write("Offset X = " + str(P3.x) + " mm\n")
    i.write("Offset Y = " + str(P3.y) + " mm\n")
    i.write("Offset Z = " + str(P3.z) + " mm\n")
    i.write("Rotation X = " + str(P3.xrot) + " CCW,deg\n")
    i.write("Rotation Y = " + str(P3.yrot) + " CCW,deg\n")
    i.write("Rotation Z = " + str(P3.zrot) + " CCW,deg\n\n")

    i.write("Optical Element 4:\n")
    i.write("Offset X = " + str(P4.x) + " mm\n")
    i.write("Offset Y = " + str(P4.y) + " mm\n")
    i.write("Offset Z = " + str(P4.z) + " mm\n")
    i.write("Rotation X = " + str(P4.xrot) + " CCW,deg\n")
    i.write("Rotation Y = " + str(P4.yrot) + " CCW,deg\n")
    i.write("Rotation Z = " + str(P4.zrot) + " CCW,deg\n\n")

    #i.write("Optical Element 5:\n")
    #i.write("Offset X = " + str(P5.x) + " mm\n")
    #i.write("Offset Y = " + str(P5.y) + " mm\n")
    #i.write("Offset Z = " + str(P5.z) + " mm\n")
    #i.write("Rotation X = " + str(P5.xrot) + " CCW,deg\n")
    #i.write("Rotation Y = " + str(P5.yrot) + " CCW,deg\n")
    #i.write("Rotation Z = " + str(P5.zrot) + " CCW,deg\n\n")

    i.write("Optical Element 6:\n")
    i.write("Offset X = " + str(P6.x) + " mm\n")
    i.write("Offset Y = " + str(P6.y) + " mm\n")
    i.write("Offset Z = " + str(P6.z) + " mm\n")
    i.write("Rotation X = " + str(P6.xrot) + " CCW,deg\n")
    i.write("Rotation Y = " + str(P6.yrot) + " CCW,deg\n")
    i.write("Rotation Z = " + str(P6.zrot) + " CCW,deg\n\n")

    i.write("Optical Element 7:\n")
    i.write("Offset X = " + str(P7.x) + " mm\n")
    i.write("Offset Y = " + str(P7.y) + " mm\n")
    i.write("Offset Z = " + str(P7.z) + " mm\n")
    i.write("Rotation X = " + str(P7.xrot) + " CCW,deg\n")
    i.write("Rotation Y = " + str(P7.yrot) + " CCW,deg\n")
    i.write("Rotation Z = " + str(P7.zrot) + " CCW,deg\n\n")

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
    oe1.OFFX = P1.x
    oe1.OFFY = P1.y
    oe1.OFFZ = P1.z
    oe1.RLEN1 = 260.0
    oe1.RLEN2 = 260.0
    oe1.RWIDX1 = 20.0
    oe1.RWIDX2 = 20.0
    oe1.T_IMAGE = 0.0
    oe1.T_INCIDENCE = 89.599998
    oe1.T_REFLECTION = 89.599998
    oe1.T_SOURCE = 30800.0
    oe1.X_ROT = P1.xrot
    oe1.Y_ROT = P1.yrot
    oe1.Z_ROT = P1.zrot
    #  when taking into account reflectivity
    #oe1.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    #oe1.F_REFLEC = 1

    #  plane mirror
    oe2.DUMMY = 0.1
    oe2.FHIT_C = 1
    oe2.FWRITE = 3
    oe2.F_MOVE = 1
    oe2.OFFX = P2.x
    oe2.OFFY = P2.y
    oe2.OFFZ = P2.z
    oe2.RLEN1 = 75.0
    oe2.RLEN2 = 75.0
    oe2.RWIDX1 = 22.5
    oe2.RWIDX2 = 22.5
    oe2.T_IMAGE = 0.0
    oe2.T_INCIDENCE = 88.5
    oe2.T_REFLECTION = 88.5
    oe2.T_SOURCE = 500.0
    oe2.X_ROT = P2.xrot
    oe2.Y_ROT = P2.yrot
    oe2.Z_ROT = P2.zrot
    #  reflect
    #oe2.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    #oe2.F_REFLEC = 1

    #  plane mirror
    oe3.ALPHA = 90.0
    oe3.DUMMY = 0.1
    oe3.FHIT_C = 1
    oe3.FWRITE = 3
    oe3.F_MOVE = 1
    oe3.OFFX = P3.x
    oe3.OFFY = P3.y
    oe3.OFFZ = P3.z
    oe3.RLEN1 = 190.0
    oe3.RLEN2 = 190.0
    oe3.RWIDX1 = 15.0
    oe3.RWIDX2 = 15.0
    oe3.T_IMAGE = 0.0
    oe3.T_INCIDENCE = 86.810772
    oe3.T_REFLECTION = 86.810772
    oe3.T_SOURCE = 8265.8165
    oe3.X_ROT = P3.xrot
    oe3.Y_ROT = P3.yrot
    oe3.Z_ROT = P3.zrot
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
    oe4.OFFX = P4.x
    oe4.OFFY = P4.y
    oe4.OFFZ = P4.z
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
    oe4.X_ROT = P4.xrot
    oe4.Y_ROT = P4.yrot
    oe4.Z_ROT = P4.zrot

    ##  screen slits
    #oe5.DUMMY = 0.1
    #oe5.FSTAT = 1
    #oe5.FWRITE = 3
    #oe5.F_REFRAC = 2
    #oe5.F_SCREEN = 1
    #oe5.I_SLIT = numpy.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    #oe5.N_SCREEN = 1
    #oe5.RX_SLIT = numpy.array([10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    #oe5.RZ_SLIT = numpy.array([0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    #oe5.T_IMAGE = 0.0
    #oe5.T_INCIDENCE = 0.0
    #oe5.T_REFLECTION = 180.0
    #oe5.T_SOURCE = 20000.0

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
    oe5.OFFX = P6.x
    oe5.OFFY = P6.y
    oe5.OFFZ = P6.z
    oe5.RLEN1 = 140.0
    oe5.RLEN2 = 140.0
    oe5.RWIDX1 = 7.5
    oe5.RWIDX2 = 7.5
    oe5.T_IMAGE = 0.0
    oe5.T_INCIDENCE = 88.5
    oe5.T_REFLECTION = 88.5
    oe5.T_SOURCE = 4600.0
    oe5.X_ROT = P6.xrot
    oe5.Y_ROT = P6.yrot
    oe5.Z_ROT = P6.zrot
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
    oe6.OFFX = P7.x
    oe6.OFFY = P7.y
    oe6.OFFZ = P7.z
    oe6.RLEN1 = 35.0
    oe6.RLEN2 = 35.0
    oe6.RWIDX1 = 10.0
    oe6.RWIDX2 = 10.0
    oe6.T_IMAGE = 1200.0
    oe6.T_INCIDENCE = 88.5
    oe6.T_REFLECTION = 88.5
    oe6.T_SOURCE = 800.0
    oe6.X_ROT = P7.xrot
    oe6.Y_ROT = P7.yrot
    oe6.Z_ROT = P7.zrot
    #  reflect
    #oe7.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
    #oe7.F_REFLEC = 1

    # Run SHADOW to create the source
    beamloss = []

    if iwrite:
        oe0.write("start.00")

    beam.genSource(oe0)
    beamloss.append(beam.nrays(nolost=1))

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
    beamloss.append(beam.nrays(nolost=1))

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
    beamloss.append(beam.nrays(nolost=1))

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
    beamloss.append(beam.nrays(nolost=1))

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
    beamloss.append(beam.nrays(nolost=1))

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
    beamloss.append(beam.nrays(nolost=1))

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
    beamloss.append(beam.nrays(nolost=1))

    if iwrite:
        oe6.write("end.06")
        beam.write("star.06")

    ##
    ## run optical element 7
    ##
    #print("    Running optical element: %d" % (7))
    #if iwrite:
    #    oe7.write("start.07")
#
    #beam.traceOE(oe7, 7)
    #beamloss.append(beam.nrays(nolost=1))
#
    #if iwrite:
    #    oe7.write("end.07")
    #    beam.write("star.07")

    for j in range(len(beamloss)):
        beamloss[j] = [str(j + 1), beamloss[j]]

    #  plot rays per element
    #  labels, ys = zip(*beamloss)
    #  xs = numpy.arange(len(labels))
    #  plt.plot(xs, ys)
    #  plt.ylim(0, 100000)
    #  plt.xticks(xs, labels)
    #  plt.title('Rays lost per OE (all param = 0)')
    #  plt.ylabel('Number of Good Rays')
    #  plt.xlabel('OE Number')
    #  for j in range(len(beamloss)):
    #      plt.text(xs[j] - 0.4, ys[j] + 0.2, str(ys[j]), size=6)
    #  plt.savefig('ray loss.png')

    #  this line will plot the the beamline
    #  Shadow.ShadowTools.plotxy(beam, 1, 3, nbins=101, nolost=1, title="Real space")
    grays = 0
    if str(format(Shadow.Beam.intensity(beam, nolost=1), '.2f')) != "0.00":
        nrays = Shadow.Beam.nrays(beam, nolost=0)
        grays = Shadow.Beam.nrays(beam, nolost=1)
        o.write("Instance: " + str(x) + "\n")
        #  o.write("Intensity = " + str(format(Shadow.Beam.intensity(beam, nolost=1), '.2f')) + "\n")
        #  o.write("Total number of Rays = " + str(nrays) + "\n")
        o.write("Total good rays = " + str(grays) + "\n")
        #  o.write("Total lost rays = " + str(nrays - grays) + "\n")
        if grays > 100:
            try:
                h, v = calcFWHM(beam, 1, 3)
                o.write("fwhm H = " + str(h) + " um\n")
                o.write("fwhm V = " + str(v) + " um\n\n")
            except:
                print("Error computing fwhm\n")
        else:
            print("\n")
    else:
        o.write("Instance: " + str(x) + "\n")
        o.write("No good rays.\n\n")

    return grays


#  class for assigning degrees of freedom
class step:
    x = 0.00
    y = 0.00
    z = 0.00
    xrot = 0.00
    yrot = 0.00
    zrot = 0.00


def main():
    i = open("input.txt", "w+")
    o = open("output.txt", "w+")
    o.write("Output data: Real Space\n")

    #  sweep each degree of freedom for an optical element
    step.xrot = 0
    for x in range(100):
        nrays = sim(x, i, o, step)
        if nrays < 690.0:
            print("Limit at: " + str(x))
            break
        step.xrot = step.xrot + -1
        step.xrot = float(format(step.xrot, '0.4f'))

    i.close()
    o.close()

    rays = []
    read = open("output.txt", "r")
    for y in read:
        if y == "No good rays.\n":
            rays.append(0)
        if y[0:5] == "Total":
            rays.append(int(y[18:]))

    max, instance = maximum(rays)
    print("Most rays at instance: " + str(instance) + " = " + str(max))
    #  print(rays)

    read.close()

    # code to plot instances vs intensity (greater than 25 instances will look bad)
    for j in range(len(rays)):
        rays[j] = [str(j + 1), rays[j]]

    labels, ys = zip(*rays)
    xs = numpy.arange(len(labels))
    width = 1

    #plt.bar(xs, ys, width, align='center', color=['blue', 'cyan'], edgecolor='black')
    plt.plot(xs, ys)
    plt.title('OE6 xrot sweep limit')
    plt.ylabel('Number of Good Rays')
    plt.xlabel('Instance Number')
    plt.ylim(0, 100000)
    plt.xlim(100, 0)

    #plt.xticks(xs, labels)  # Replace default x-ticks with xs, then replace xs with labels
    #for j in range(len(rays)):
    #    plt.text(xs[j] - 0.4, ys[j] + 0.2, str(ys[j]), size=6)
    #plt.yticks(ys)

    plt.savefig('instanceplot.png')


if __name__ == "__main__":
    main()