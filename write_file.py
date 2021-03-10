import platform
import os.path
from datetime import datetime

import getpass


user = getpass.getuser()

name = "Ali Raeisdanaei"

def write_header(complete_name):
	with open(complete_name, "w+", encoding='utf-8') as f:
		date = datetime.now()
		format = "%d/%m/%Y %H:%M"
		date = date.strftime(format)

		f.write("Blood Pressure Chart for " + name)
		f.write('\n')
		f.write("Chart created on " + date)
		f.write('\n')
		f.write('\n')
		f.write("Day, Month, Year, Time, Systolic, Diastolic, Pulse \\ Minute, Notes")

def getCompleteName(op_sys, full_name):
	if(op_sys == 'Linux' or op_sys == 'Darwin'):
		save_path = "/home/" + user  + "/Documents"
		file_name = "Blood_Pressure_" + full_name + ".xlsx"
		complete_name = os.path.join(save_path, file_name)
		return complete_name
	if(op_sys == 'Windows'):
		save_path = "C:\\Users" + user + "\\Documents"
		file_name = "Blood_Pressure_" + full_name + ".xlsx"
		complete_name = os.path.join(save_path, file_name)
	else:
		print("Unkown folder system.")
		exit()

def write_entry(rmt, systolic, diastolic, pulse, notes):
	complete_name = getCompleteName(platform.system(), name)
	
	if not (os.path.isfile(complete_name)):
		# file does not exist
		write_header(complete_name)
	
	with open(complete_name, "a", encoding='utf-8') as f:
		date = datetime.now()
		day = date.strftime("%d")
		month =  date.strftime("%m")
		year =  date.strftime("%Y")
		time = date.strftime("%H:%M")

		if(rmt != None):
			day = rmt[0]
			month = rmt[1]
			year = rmt [2]
			time = rmt [3]

		f.write('\n')
		f.write(day + "," + month + "," + year + "," + time + "," + systolic + "," + diastolic + "," + pulse + "," + notes)

	


		




	




