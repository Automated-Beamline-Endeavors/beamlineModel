print("Imported!")


# using miniconda3 to get access to Shadow3 library
import Shadow
import numpy

class beamline:
	def __init__(self):
		self.beam = Shadow.Beam()

		
# may want to think more about the naming convention (oex) or a list:
# oe = [Shadow.Source(), Shadow.OE(), Shadow.OE(), ...] 
#
# In the list case, _setElements could simply iterate through elements 
# 1-6 and the incoming motorVals could be a 2-d array (columns are 
# degree of freedom and rows are optical elements)
#
# either process still requires going though the laborious property 
# assignment process --> perhaps create a python script to create
# the beamline objects, then save them (however pickle doesn't seem 
# to work. When beamline object initialized it just as to unpack
		
		self.oe0 = Shadow.Source()
		self.oe1 = Shadow.OE()
		self.oe2 = Shadow.OE()
		self.oe3 = Shadow.OE()
		self.oe4 = Shadow.OE()
		self.oe5 = Shadow.OE()
		self.oe6 = Shadow.OE()

		# Set the properties of each element
		#  undulator
		self.oe0.FDISTR = 3
		self.oe0.F_COLOR = 3
		self.oe0.F_PHOT = 0
		self.oe0.HDIV1 = 0.5
		self.oe0.HDIV2 = 0.5
		self.oe0.IDO_VX = 0
		self.oe0.IDO_VZ = 0
		self.oe0.IDO_X_S = 0
		self.oe0.IDO_Y_S = 0
		self.oe0.IDO_Z_S = 0
		self.oe0.NPOINT = 100000
		self.oe0.NTOTALPOINT = 20000
		self.oe0.PH1 = 499.97
		self.oe0.PH2 = 500.03
		self.oe0.SIGDIX = 1.964e-05
		self.oe0.SIGDIZ = 1.6349401e-05
		self.oe0.SIGMAX = 0.27609399
		self.oe0.SIGMAZ = 0.0261531994
		self.oe0.VDIV1 = 0.5
		self.oe0.VDIV2 = 0.5

		#  plane mirror
		self.oe1.ALPHA = 90.0
		self.oe1.DUMMY = 0.1
		self.oe1.FHIT_C = 1
		self.oe1.FWRITE = 3
		self.oe1.F_MOVE = 1
		self.oe1.OFFX = P1.x
		self.oe1.OFFY = P1.y
		self.oe1.OFFZ = P1.z
		self.oe1.RLEN1 = 260.0
		self.oe1.RLEN2 = 260.0
		self.oe1.RWIDX1 = 20.0
		self.oe1.RWIDX2 = 20.0
		self.oe1.T_IMAGE = 0.0
		self.oe1.T_INCIDENCE = 89.599998
		self.oe1.T_REFLECTION = 89.599998
		self.oe1.T_SOURCE = 30800.0
		self.oe1.X_ROT = P1.xrot
		self.oe1.Y_ROT = P1.yrot
		self.oe1.Z_ROT = P1.zrot
		#  when taking into account reflectivity
		#oe1.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
		#oe1.F_REFLEC = 1

		#  plane mirror
		self.oe2.DUMMY = 0.1
		self.oe2.FHIT_C = 1
		self.oe2.FWRITE = 3
		self.oe2.F_MOVE = 1
		self.oe2.OFFX = P2.x
		self.oe2.OFFY = P2.y
		self.oe2.OFFZ = P2.z
		self.oe2.RLEN1 = 75.0
		self.oe2.RLEN2 = 75.0
		self.oe2.RWIDX1 = 22.5
		self.oe2.RWIDX2 = 22.5
		self.oe2.T_IMAGE = 0.0
		self.oe2.T_INCIDENCE = 88.5
		self.oe2.T_REFLECTION = 88.5
		self.oe2.T_SOURCE = 500.0
		self.oe2.X_ROT = P2.xrot
		self.oe2.Y_ROT = P2.yrot
		self.oe2.Z_ROT = P2.zrot
		#  reflect
		#oe2.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
		#oe2.F_REFLEC = 1

		#  plane mirror
		self.oe3.ALPHA = 90.0
		self.oe3.DUMMY = 0.1
		self.oe3.FHIT_C = 1
		self.oe3.FWRITE = 3
		self.oe3.F_MOVE = 1
		self.oe3.OFFX = P3.x
		self.oe3.OFFY = P3.y
		self.oe3.OFFZ = P3.z
		self.oe3.RLEN1 = 190.0
		self.oe3.RLEN2 = 190.0
		self.oe3.RWIDX1 = 15.0
		self.oe3.RWIDX2 = 15.0
		self.oe3.T_IMAGE = 0.0
		self.oe3.T_INCIDENCE = 86.810772
		self.oe3.T_REFLECTION = 86.810772
		self.oe3.T_SOURCE = 8265.8165
		self.oe3.X_ROT = P3.xrot
		self.oe3.Y_ROT = P3.yrot
		self.oe3.Z_ROT = P3.zrot
		#  reflect
		#oe3.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
		#oe3.F_REFLEC = 1

		#  plane grating
		self.oe4.ALPHA = 180.0
		self.oe4.DUMMY = 0.1
		self.oe4.FHIT_C = 1
		self.oe4.FWRITE = 2
		self.oe4.F_GRATING = 1
		self.oe4.F_MOVE = 1
		self.oe4.F_RULING = 5
		self.oe4.F_RUL_ABS = 1
		self.oe4.OFFX = P4.x
		self.oe4.OFFY = P4.y
		self.oe4.OFFZ = P4.z
		self.oe4.RLEN1 = 57.5
		self.oe4.RLEN2 = 57.5
		self.oe4.RULING = 1199.22002
		self.oe4.RUL_A1 = 0.165491998
		self.oe4.RUL_A2 = 1.0793e-05
		self.oe4.RUL_A3 = 1.99999999e-06
		self.oe4.RWIDX1 = 12.5
		self.oe4.RWIDX2 = 12.5
		self.oe4.T_IMAGE = 2000.0
		self.oe4.T_INCIDENCE = 87.771697
		self.oe4.T_REFLECTION = 85.049847
		self.oe4.T_SOURCE = 135.0
		self.oe4.X_ROT = P4.xrot
		self.oe4.Y_ROT = P4.yrot
		self.oe4.Z_ROT = P4.zrot

		#  ellipsoid mirror oe6 -> oe5 after removing slit
		self.oe5.ALPHA = 90.0
		self.oe5.AXMAJ = 33150.0
		self.oe5.AXMIN = 296.85199
		self.oe5.DUMMY = 0.1
		self.oe5.ELL_THE = 0.186719999
		self.oe5.FCYL = 1
		self.oe5.FHIT_C = 1
		self.oe5.FMIRR = 2
		self.oe5.FWRITE = 3
		self.oe5.F_EXT = 1
		self.oe5.F_MOVE = 1
		self.oe5.OFFX = P5.x
		self.oe5.OFFY = P5.y
		self.oe5.OFFZ = P5.z
		self.oe5.RLEN1 = 140.0
		self.oe5.RLEN2 = 140.0
		self.oe5.RWIDX1 = 7.5
		self.oe5.RWIDX2 = 7.5
		self.oe5.T_IMAGE = 0.0
		self.oe5.T_INCIDENCE = 88.5
		self.oe5.T_REFLECTION = 88.5
		self.oe5.T_SOURCE = 4600.0
		self.oe5.X_ROT = P5.xrot
		self.oe5.Y_ROT = P5.yrot
		self.oe5.Z_ROT = P5.zrot
		#  reflect
		#oe6.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
		#oe6.F_REFLEC = 1

		#  ellipsoid mirror oe7 -> oe6 after removing slit
		self.oe6.ALPHA = 90.0
		self.oe6.AXMAJ = 3300.0
		self.oe6.AXMIN = 66.6355972
		self.oe6.DUMMY = 0.1
		self.oe6.ELL_THE = 1.40167999
		self.oe6.FCYL = 1
		self.oe6.FHIT_C = 1
		self.oe6.FMIRR = 2
		self.oe6.FWRITE = 3
		self.oe6.F_EXT = 1
		self.oe6.F_MOVE = 1
		self.oe6.OFFX = P6.x
		self.oe6.OFFY = P6.y
		self.oe6.OFFZ = P6.z
		self.oe6.RLEN1 = 35.0
		self.oe6.RLEN2 = 35.0
		self.oe6.RWIDX1 = 10.0
		self.oe6.RWIDX2 = 10.0
		self.oe6.T_IMAGE = 1200.0
		self.oe6.T_INCIDENCE = 88.5
		self.oe6.T_REFLECTION = 88.5
		self.oe6.T_SOURCE = 800.0
		self.oe6.X_ROT = P6.xrot
		self.oe6.Y_ROT = P6.yrot
		self.oe6.Z_ROT = P6.zrot    
		#  reflect
		#oe6.FILE_REFL = b"C:/cygwin64/Oasys/Si.dat"
		#oe6.F_REFLEC = 1

		
		
	def elements(self):
		# The limits are from simulation runs, default position is whatever set at 
		# initialization, and still not sure on naming convention (is there a property
		# in Shadow.OE class?
		
		# return dictionaries of names, limits, default position of optical elements

	
	def _setElements(self, motorVals)
		# setup elements
		# loop through elements of motorVals and assign value (motorVals[element][dof]) 
		# It might be simplest to use the (element, dof) indexing.  But here oe1 is element 
		# 0 and dof:
		# xoff: 0
		# yoff: 1
		# zoff: 2
		# xrot: 3
		# zrot: 4
		# zrot: 5
	
	def sim(self, motorVals, debug = False)
		# I put a debug here for testing --> I imagine it would do something similar
		# to the print statements (iwrite flag) after each elements were processed 
		# in your original code

		self._setElements(motorVals)
		
		self.beam.genSource(oe0)
		self.beam.traceOE(oe1, 1)
		self.beam.traceOE(oe2, 2)
		self.beam.traceOE(oe3, 3)
		self.beam.traceOE(oe4, 4)
		self.beam.traceOE(oe5, 5)
		self.beam.traceOE(oe6, 6)

		# return the number of good rays
		# print(str(beam.nrays(nolost=1)))
		return beam.nrays(nolost=1)
