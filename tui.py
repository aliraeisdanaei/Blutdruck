import write_file
import sys

rmt = None

if(sys.argv[1] == "rmt"):
    day = input("Enter day in dd: ")
    month = input("Enter month in mm: ")
    year = input("Enter year in yyyy: ")
    time = input("Enter time in 24hr hh:mm: ")
    rmt = [day, month, year, time]


systolic = input("Enter systolic: ")
diastolic = input("Enter diastolic: ")
pule = input("Enter pulse per minute: ")
notes = input("Enter any notes: ")

write_file.write_entry(rmt, systolic, diastolic, pule, notes)