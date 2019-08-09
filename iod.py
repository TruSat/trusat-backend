#!/usr/bin/env python3
# Found code that also does all this (a little more complete)
# https://github.com/aerospaceresearch/orbitdeterminator/blob/866e5c031d5b1d836061d6ec2b105b8961c657d8/orbitdeterminator/satobs.py
import sys

if sys.version_info[0] != 3 or sys.version_info[1] < 7:
	print("This script requires Python version 3.7")
	sys.exit(1)

import os, re
from datetime import datetime

# This one works
iod_format_re = re.compile ('^(\d{5}\s\d{2}\s\d{3}\D*)*\s{1,16}(\d{4}\s)(\D)\s(\d{8})(\d{0,9}$|\d{0,9}\s+\d{2}\s*\d*\s*\d*\s*[-+]*\d*\s*\d{0,2}\s[EFIRSXBHPADMNV]{0,1})')

# REGEXP for valid angle string format with content
angle_content_re = re.compile('\d{1,7}\s*[+-]\d{1,7}')

# This string *should* work to detect the full format (uses several ORs) but python doesn't like it
#iod_format_re = re.compile ('^(\d{5}\s\d{2}\s\d{3}\D*)*\s{1,16}(\d{4}\s)(\D)\s(\d{8})(\d{0,9}$|\d{0,9}\s+\d{2}\s*\d*\s*\d*\s*[-+]*\d*\s*\d{0,2}\s[EFIRSXBHPADMNV]{0,1}$|\d{0,9}\s+\d{2}\s*\d*\s*\d*\s*[-+]*\d*\s*\d{0,2}\s[EFIRSXBHPADMNV]{0,1}[+-]\d+\s+\d+$|\d{0,9}\s+\d{2}\s*\d*\s*\d*\s*[-+]*\d*\s*\d{0,2}\s[EFIRSXBHPADMNV]{0,1}[+-]\d+\s+\d+\s+\d+$)')

# Simple format
#iod_format_re = re.compile ('^(\d{5}\s\d{2}\s\d{3}\D*)*\s{1,16}(\d{4}\s)(\D)\s(\d{8})(\d{0,9}$|\d{0,9}\s+\d\d.*)')

# A hack to provide user and station data for the test IOD data before we're done with coding parsing
Stations = {
	2007 : {
		'user'        : 'IOD Test User',
		'name'		  : 'Test Station',
		'lattitude'   : '0',
		'longitude'   : '0',
		'altitude'    : '0',
		'frame'		  : 'WGS84',
		'description' : 'Something so that the IOD examples do not break',
		'notes'		  : ''
		},
	4172 : {
		'user'        : 'Leo Barhorst',
		'name'		  : 'ALMERE',
		'lattitude'   : '52.3713 N',
		'longitude'   : '5.2580 E',
		'altitude'    : '–3 ASL',
		'frame'		  : 'WGS84',
		'description' : 'Setup: WATEC 910HX/RC, 50 mm F1:1.8, NTP, Celestron Nexstar',
		'notes'		  : 'Observations made and reduced with Sattools'
		},
	4353 : {
		'user'        : 'Marco Langbroek',
		'name'		  : 'Leiden',
		'lattitude'   : '52.15412 N',
		'longitude'   : '4.49081 E',
		'altitude'    : '+0 m ASL',
		'frame'		  : 'WGS84',
		'description' : 'New Camera: Canon 80D',
		'notes'		  : 'http://sattrackcam.blogspot.com'
		},
	4355 : {
		'user'        : 'Marco Langbroek',
		'name'		  : 'Cronesteyn',
		'lattitude'   : '52.13878 N',
		'longitude'   : '4.49937 E',
		'altitude'    : '-2 m ASL',
		'frame'		  : 'WGS84',
		'description' : 'unknown',
		'notes'		  : 'http://sattrackcam.blogspot.com'
		},
	7778 : {
		'user'        : 'Brad Young',
		'name'		  : 'Remote MPC Q62 - Siding Spring, NSW, Australia',
		'lattitude'   : '-31.2733',
		'longitude'   : '149.0644',
		'altitude'    : '3400ft',
		'frame'		  : 'unknown',
		'description' : 'unknown',
		'notes'		  : '22" f/4.2 UC Obsession'
		},
	8336 : {
		'user'        : 'Brad Young',
		'name'		  : 'TULSA1',
		'lattitude'   : '-31.2733',
		'longitude'   : '-95.983429',
		'altitude'    : '201m',
		'frame'		  : 'unknown',
		'description' : 'unknown',
		'notes'		  : 'Meade ETX-125'
		},
	4541 : {
		'user'        : 'Alberto Rango',
		'name'		  : 'Roma',
		'lattitude'   : '',
		'longitude'   : '',
		'altitude'    : '',
		'frame'		  : '',
		'description' : '',
		'notes'		  : ''
		}
}

class Angle:
	"""Observed Angle

       Format 1: RA/DEC = HHMMSSs+DDMMSS MX   (MX in seconds of arc)
		   	  2: RA/DEC = HHMMmmm+DDMMmm MX   (MX in minutes of arc)
			  3: RA/DEC = HHMMmmm+DDdddd MX   (MX in degrees of arc)
			  4: AZ/EL  = DDDMMSS+DDMMSS MX   (MX in seconds of arc)
			  5: AZ/EL  = DDDMMmm+DDMMmm MX   (MX in minutes of arc)
			  6: AZ/EL  = DDDdddd+DDdddd MX   (MX in degrees of arc)
			  7: RA/DEC = HHMMSSs+DDdddd MX   (MX in degrees of arc)

	   Given a packed Angle string of two angle pairs matching the format above,
	   create one of the following formats.
	   RA =   HH.ddddd
	   DEC = DDD.ddddd

	   AZ =  DDD.ddddd
	   EL =   DD.ddddd

	   Where MX (Uncertainty) is not in degrees of arc, convert to degrees of arc

	"""

	def __init__(self,AngleFormatCode,Epoch,Angle1,Angle2,Uncertainty):
		self.AngleFormatCode = AngleFormatCode
		self.Epoch = Epoch
		self.Angle1 = Angle1
		self.Angle2 = Angle2
		self.Uncertainty = Uncertainty
		self.RA = 0.0
		self.DEC = 0.0
		self.AZ = 0.0
		self.EL = 0.0

		# 1: RA/DEC = HHMMSSs+DDMMSS MX   (MX in seconds of arc)
		if(self.AngleFormatCode == 1):
			try:
				RA_HH = int(self.Angle1[0:2])
			except:
				RA_HH = 0 # We should probably just declare it invalid...

			try:
				RA_MM = int(self.Angle1[2:4])
			except:
				RA_MM = 0

			try:
				RA_SS = int(self.Angle1[4:6])
			except:
				RA_SS = 0

			try:
				RA_s = int(self.Angle1[6])
			except:
				RA_s = 0

			self.RA = (360.0*RA_HH/24.0) + RA_MM/60.0 + RA_SS / 3600.0 + RA_s*(0.1/3600.0)

			DEC_SIGN = self.Angle2[0]
			DEC_SIGN = int(DEC_SIGN + "1") # This operation doesn't appear strictly necessary

			try:
				DEC_DD = int(self.Angle2[1:3])
			except:
				DEC_DD = 0 # We should probably just declare it invalid...

			try:
				DEC_MM = int(self.Angle2[3:5])
			except:
				DEC_MM = 0

			try:
				DEC_SS = int(self.Angle2[5:7])
			except:
				DEC_SS = 0

			self.DEC  = DEC_DD + DEC_MM/60.0 + DEC_SS / 3600.0
			self.DEC *= DEC_SIGN

			# Convert uncertainty in seconds of arc to fractional degrees
			self.Uncertainty *= (1/3600)

		# 2: RA/DEC = HHMMmmm+DDMMmm MX   (MX in minutes of arc)
		if(self.AngleFormatCode == 2):
			try:
				RA_HH = int(self.Angle1[0:2])
			except:
				RA_HH = 0 # We should probably just declare it invalid...

			try:
				RA_MM = int(self.Angle1[2:4])
			except:
				RA_MM = 0

			try:
				RA_mm_d1 = int(self.Angle1[4])
			except:
				RA_mm_d1 = 0

			try:
				RA_mm_d2 = int(self.Angle1[5])
			except:
				RA_mm_d2 = 0

			try:
				RA_mm_d3 = int(self.Angle1[6])
			except:
				RA_mm_d3 = 0

			self.RA = 15.0*((RA_HH) + RA_MM/60.0 + ((RA_mm_d1*0.1 + RA_mm_d2*0.01 + RA_mm_d3*0.001)/3600.0))

#			print(self.RA)
#			print(RA_HH, RA_MM, RA_mm_d1, RA_mm_d2, RA_mm_d3)

			DEC_SIGN = self.Angle2[0]
			DEC_SIGN = int(DEC_SIGN + "1") # This operation doesn't appear strictly necessary

			try:
				DEC_DD = int(self.Angle2[1:3])
			except:
				DEC_DD = 0 # We should probably just declare it invalid...

			try:
				DEC_MM = int(self.Angle2[3:5])
			except:
				DEC_MM = 0

			try:
				DEC_mm_d1 = int(self.Angle2[5])
			except:
				DEC_mm_d1 = 0

			try:
				DEC_mm_d2 = int(self.Angle2[6])
			except:
				DEC_mm_d2 = 0

			self.DEC = DEC_DD + DEC_MM/60.0 + DEC_mm_d1*(0.1/60.0) + DEC_mm_d2*(0.01/60.0)
			self.DEC *= DEC_SIGN

			# Convert uncertainty in minutes of arc to fractional degrees
			self.Uncertainty *= (1/60)

#			print(self.DEC)
#			print(DEC_DD, DEC_MM, DEC_mm_d1, DEC_mm_d2)

		# 3: RA/DEC = HHMMmmm+DDdddd MX   (MX in degrees of arc, no need to convert)
		if(self.AngleFormatCode == 3):
			try:
				RA_HH = int(self.Angle1[0:2])
			except:
				RA_HH = 0 # We should probably just declare it invalid...

			try:
				RA_MM = int(self.Angle1[2:4])
			except:
				RA_MM = 0

			try:
				RA_mmm =  int(self.Angle1[4:7])
			except:
				RA_mmm = 0

			self.RA = 15.0*(RA_HH + RA_MM/60.0 + (RA_mmm * (0.001/60.0)))

			try:
				DEC_SIGN = self.Angle2[0]
			except:
				DEC_SIGN = 0

			try:
				DEC_DD = int(self.Angle2[1:3])
			except:
				DEC_DD = 0 # We should probably just declare it invalid...

			try:
				DEC_d1 = int(self.Angle2[3])
			except:
				DEC_d1 = 0

			try:
				DEC_d2 = int(self.Angle2[4])
			except:
				DEC_d2 = 0

			try:
				DEC_d3 = int(self.Angle2[5])
			except:
				DEC_d3 = 0

			try:
				DEC_d4 = int(self.Angle2[6])
			except:
				DEC_d4 = 0

			DEC_SIGN =  int(DEC_SIGN + "1") # This operation doesn't appear strictly necessary
			self.DEC =  DEC_DD + (DEC_d1 * .1) + (DEC_d2 * 0.01) + (DEC_d3 * .001) + (DEC_d4 * 0.0001)
			self.DEC *= DEC_SIGN

#			print(self.RA,self.DEC)
#			print(Angle1, RA_HH, RA_MM, RA_mmm)
#			print(Angle2, DEC_DD, DEC_d1, DEC_d2, DEC_d3, DEC_d4)

		# 4: AZ/EL  = DDDMMSS+DDMMSS MX   (MX in seconds of arc)
		if(self.AngleFormatCode == 4):
			try:
				AZ_DDD = int(self.Angle1[0:3])
			except:
				AZ_DDD = 0 # We should probably just declare it invalid...

			try:
				AZ_MM = int(self.Angle1[3:5])
			except:
				AZ_MM = 0

			try:
				AZ_SS = int(self.Angle1[5:7])
			except:
				AZ_SS = 0

			self.AZ = AZ_DDD + AZ_MM/60.0 + AZ_SS/3600.0

			EL_SIGN = self.Angle2[0]
			# It's theoretically possible for someone to submit an EL > 90, but not a negative AZ.
			EL_SIGN = int(EL_SIGN + "1") # This operation doesn't appear strictly necessary

			try:
				EL_DD = int(self.Angle2[1:3])
			except:
				EL_DD = 0 # We should probably just declare it invalid...

			try:
				EL_MM = int(self.Angle2[3:5])
			except:
				EL_MM = 0

			try:
				EL_SS = int(self.Angle2[5:7])
			except:
				EL_SS = 0

			self.EL  = EL_DD  + EL_MM/60.0 + EL_SS/3600.0
			self.EL *= EL_SIGN

			# Convert uncertainty in seconds of arc to fractional degrees
			self.Uncertainty *= (1/3600)

#			print(self.AZ,self.EL)
#			print(Angle1, AZ_DDD, AZ_MM, AZ_SS)
#			print(Angle2, EL_DD, EL_MM, EL_SS)


		# 5: AZ/EL  = DDDMMmm+DDMMmm MX   (MX in minutes of arc)
		if(self.AngleFormatCode == 5):
			try:
				AZ_DDD = int(self.Angle1[0:3])
			except:
				AZ_DDD = 0 # We should probably just declare it invalid...

			try:
				AZ_MM = int(self.Angle1[3:5])
			except:
				AZ_MM = 0

			try:
				AZ_mm_d1 = int(self.Angle1[5])
			except:
				AZ_mm_d1 = 0

			try:
				AZ_mm_d2 = int(self.Angle1[6])
			except:
				AZ_mm_d2 = 0

			self.AZ = AZ_DDD + AZ_MM/60.0 + AZ_mm_d1*(0.1/60.0) + AZ_mm_d2*(0.01/60.0)

			EL_SIGN = self.Angle2[0]
			# It's theoretically possible for someone to submit an EL > 90, but not a negative AZ.
			EL_SIGN = int(EL_SIGN + "1") # This operation doesn't appear strictly necessary

			try:
				EL_DD = int(self.Angle2[1:3])
			except:
				EL_DD = 0 # We should probably just declare it invalid...

			try:
				EL_MM = int(self.Angle2[3:5])
			except:
				EL_MM = 0

			try:
				EL_mm_d1 = int(self.Angle2[5])
			except:
				EL_mm_d1 = 0

			try:
				EL_mm_d2 = int(self.Angle2[6])
			except:
				EL_mm_d2 = 0

			self.EL = EL_DD + EL_MM/60.0 + EL_mm_d1*(0.1/60.0) + EL_mm_d2*(0.01/60.0)

			# Convert uncertainty in minutes of arc to fractional degrees
			self.Uncertainty *= (1/60)


		# 6: AZ/EL  = DDDdddd+DDdddd MX   (MX in degrees of arc, no need to convert)
		if(self.AngleFormatCode == 6):
			try:
				AZ_DDD = int(self.Angle1[0:3])
			except:
				AZ_DDD = 0 # We should probably just declare it invalid...

			try:
				AZ_d1 = int(self.Angle1[3])
			except:
				AZ_d1 = 0

			try:
				AZ_d2 = int(self.Angle1[4])
			except:
				AZ_d2 = 0

			try:
				AZ_d3 = int(self.Angle1[5])
			except:
				AZ_d3 = 0

			try:
				AZ_d4 = int(self.Angle1[6])
			except:
				AZ_d4 = 0

			self.AZ =  AZ_DDD + (AZ_d1 * .1) + (AZ_d2 * 0.01) + (AZ_d3 * .001) + (AZ_d4 * 0.0001)

#			print(self.AZ)
#			print(AZ_DDD, AZ_d1, AZ_d2, AZ_d3, AZ_d4)

			EL_SIGN = self.Angle2[0]
			# It's theoretically possible for someone to submit an EL > 90, but not a negative AZ.
			EL_SIGN = int(EL_SIGN + "1") # This operation doesn't appear strictly necessary

			try:
				EL_DD = int(self.Angle2[1:3])
			except:
				EL_DD = 0 # We should probably just ELlare it invalid...

			try:
				EL_d1 = int(self.Angle2[3])
			except:
				EL_d1 = 0

			try:
				EL_d2 = int(self.Angle2[4])
			except:
				EL_d2 = 0

			try:
				EL_d3 = int(self.Angle2[5])
			except:
				EL_d3 = 0

			try:
				EL_d4 = int(self.Angle2[6])
			except:
				EL_d4 = 0

			self.EL =  EL_DD + (EL_d1 * .1) + (EL_d2 * 0.01) + (EL_d3 * .001) + (EL_d4 * 0.0001)
			self.EL *= EL_SIGN

#			print(self.EL)
#			print(EL_DD, EL_d1, EL_d2, EL_d3, EL_d4)


		# 7: RA/DEC = HHMMSSs+DDdddd MX   (MX in degrees of arc, no need to convert)
		if(self.AngleFormatCode == 7):
			try:
				RA_HH = int(self.Angle1[0:2])
			except:
				RA_HH = 0 # We should probably just declare it invalid...

			try:
				RA_MM = int(self.Angle1[2:4])
			except:
				RA_MM = 0

			try:
				RA_SS = int(self.Angle1[4:6])
			except:
				RA_SS = 0

			try:
				RA_s = int(self.Angle1[6])
			except:
				RA_s = 0

			self.RA = 15.0*(RA_HH + RA_MM/60.0 + RA_SS / 3600.0 + RA_s*(0.1/3600.0))

			try:
				DEC_SIGN = self.Angle2[0]
			except:
				DEC_SIGN = 0

			try:
				DEC_DD = int(self.Angle2[1:3])
			except:
				DEC_DD = 0 # We should probably just declare it invalid...

			try:
				DEC_d1 = int(self.Angle2[3])
			except:
				DEC_d1 = 0

			try:
				DEC_d2 = int(self.Angle2[4])
			except:
				DEC_d2 = 0

			try:
				DEC_d3 = int(self.Angle2[5])
			except:
				DEC_d3 = 0

			try:
				DEC_d4 = int(self.Angle2[6])
			except:
				DEC_d4 = 0

			DEC_SIGN =  int(DEC_SIGN + "1") # This operation doesn't appear strictly necessary
			self.DEC =  DEC_DD + (DEC_d1 * .1) + (DEC_d2 * 0.01) + (DEC_d3 * .001) + (DEC_d4 * 0.0001)
			self.DEC *= DEC_SIGN

# End of the Angle parsing cases

class IOD:
	"""IOD Observation

	   NameCode, or NameString indicates packed data requiring further processing (to disentagle variable names)

       # Array of variable names for IOD parsing.
       # NameCode, or NameString indicates packed data requiring further processing (to disentagle variable names)
	"""
	def __init__(self, line):					# (Element #, start_col, end_col)
		self.line = line
		self.UserString = None 					# A preMVP hack before we're parsing it fully.
		self.ObjectNumber = None				# (0, 0, 4)  	Object number (NORAD)
		self.LaunchYear = None					# (1, 6, 7)  	Launch year. Implied century.
		self.InternationalDesignation = None	# (2, 9, 14)  	International Designation (COSPAR)
		self.Station = 9999						# (3, 16, 19)  	Four digit station number
		self.StationStatusCode = None			# (4, 21, 21)  	Station status code
		self.StationStatus = None
		self.DateTimeString = None				# (5, 23, 39)  	DateTime string YYYYMMDDHHMMSSsss
		self.DateTime = None
		self.TimeUncertainty = None				# (6, 41, 42)  	Time Uncertainty, expressed as MX, Evaluated as M*10E(X-8).
		self.AngleFormatCode = None				# (7, 44, 44)  	Angle format code
		self.Epoch = None						# (8, 45, 45)  	Epoch code
		self.AngleString = None					# (9, 47, 60)  	AngleString
		self.RA = None
		self.DEC = None
		self.AZ = None
		self.EL = None
		self.ValidPosition = -1
		self.PositionUncertainty = None			# (10, 62, 63) 	Positional uncertainty, expressed as MX, Evaluated as M*10E(X-8).
		self.OpticalCode = None					# (11, 65, 65) 	Optical behavior code
		self.VisualMagnitude = None				# (12, 66, 69) 	Visual magnitude. Implied decimal point.
		self.MagnitudeUncertainty = None		# (13, 71, 72) 	Magnitude uncertainty. Implied decimal point.
		self.FlashPeriod = None					# (14, 74, 79) 	Flash period in seconds. Implied decimal point.
# end of class IOD

def iod_format_test(line=False):
	match = iod_format_re.search(line)
	if match:
		return line.rstrip('\n')	# Have to use this until we figure out the whole REGEXP match
	else:
		return False

def iod_parse_line(line=False):
	match = iod_format_test(line) # Handle this separately? I.E. assume its properly formatted?  Would require more exception handling below.
	if (match):
		line = line.rstrip()

		IOD_line = IOD(line)
		#print(line)

		IOD_line.ObjectNumber = int(line[0:5])

		LaunchYearTwoDigit = int(line[6:8])
		if (LaunchYearTwoDigit < 57):		# Year of Sputnik launch, first cataloged object
			IOD_line.LaunchYear = 2000 + LaunchYearTwoDigit
		else:
			IOD_line.LaunchYear = 1900 + LaunchYearTwoDigit

		IOD_line.InternationalDesignation = str(IOD_line.LaunchYear) + ' ' + line[9:15]
		IOD_line.Station = int(line[16:20])
		IOD_line.StationStatusCode = line[21]	# Future TODO - Expand out the short and long description of the codes

		# The following is a hack to support user / station data in the IOD object
		# until we get those functions scripted
		#IOD_line.UserString = Stations[IOD_line.Station]['user']

		IOD_line.DateTimeString = line[23:40]
		YEAR = int(IOD_line.DateTimeString[0:4])
		MONTH = int(IOD_line.DateTimeString[4:6])
		DAY = int(IOD_line.DateTimeString[6:8])

		try:
			HOUR = int(IOD_line.DateTimeString[8:10])
			try:
				MINUTE = int(IOD_line.DateTimeString[10:12])
				try:
					SECOND = int(IOD_line.DateTimeString[12:14])
				except:
					SECOND = SUBSECOND = 0
			except:
				MINUTE = SECOND = SUBSECOND = 0
		except:
			HOUR = MINUTE = SECOND = SUBSECOND = 0

		try:
			DECISEC = int(IOD_line.DateTimeString[14])*100000
		except:
			DECISEC = 0

		try:
			CENTISEC = int(IOD_line.DateTimeString[15])*10000
		except:
			CENTISEC = 0

		try:
			MILLISEC = int(IOD_line.DateTimeString[16])*1000
		except:
			MILLISEC = 0

		SUBSECOND = DECISEC + CENTISEC + MILLISEC

		IOD_line.DateTime = datetime(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, SUBSECOND)

		# Expressed as MX, where M = mantissa, and X = exponent input. Evaluated as M*10E(X-8).
		IOD_line.TimeUncertainty = float(line[41]) * 10 **(int(line[42]) - 8)

		try:
			IOD_line.AngleFormatCode = int(line[44])
		except:
			IOD_line.AngleFormatCode = 0
			IOD_line.ValidPosition = -1	# Need format code to parse angle

		try:
			IOD_line.EpochCode = int(line[45])
		except:
			IOD_line.EpochCode = 0
			IOD_line.ValidPosition = -1	# If EpochCode as read as Zero (not blank), we won't trigger this error

		IOD_line.AngleString = line[47:61]
		angle_content = angle_content_re.search(IOD_line.AngleString)

		try:
			IOD_line.PositionUncertainty = float(line[62]) * 10 **(int(line[63]) - 8)
		except:
			IOD_line.PositionUncertainty = None # Don't really need this (initialized state)

#		print(line)
		if ( (IOD_line.AngleFormatCode>=0) & (IOD_line.EpochCode>=0) & (angle_content is not None) ):
			try:
				angle = Angle(IOD_line.AngleFormatCode, IOD_line.EpochCode, IOD_line.AngleString[0:7], IOD_line.AngleString[7:14], IOD_line.PositionUncertainty)
#				print("ANGLE: ",IOD_line.AngleString,angle.AZ,angle.EL,angle.RA,angle.DEC, "\n")
				IOD_line.AZ = angle.AZ
				IOD_line.EL = angle.EL
				IOD_line.RA = angle.RA
				IOD_line.DEC = angle.DEC
			except:
#				print("Problem angle")
				IOD_line.ValidPosition = -1
		else:
#			print("No Position Data\n")
			IOD_line.ValidPosition = -1

		return IOD_line
	else:
		# print("Error: Call iod_parse_line with a properly formatted IOD line comfirmed by iod_format_test")
		return(False)
