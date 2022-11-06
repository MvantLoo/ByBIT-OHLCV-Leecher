#!/usr/bin/env python3
"""

CorpusCrypto Leecher - Packer
Take the unpacked files and combine them in monthly, yearly and total files 
!!! THE EXISTING FOLDER WILL BE DELETED AND ALL "PACKED" FILES RECREATED

Requirements:

"""
import settings
import os,gzip,shutil,pathlib,sys

# Use the pair in the argument, or else the pair in the settings
try:
  pair = sys.argv[1]
except:
  pair = settings.pair

# Find the files in the unpack folder, pack and save in the pack folder
folder_unpack = settings.folder_unpack + "/" + pair + "/"
folder_pack = settings.folder_pack + "/" + pair + "/"

# Delete and recreate folder
shutil.rmtree(folder_pack, ignore_errors=True)
pathlib.Path(folder_pack).mkdir(parents=True, exist_ok=True)


for file in sorted(os.listdir(folder_unpack)): # IMPORTANT read the file list SORTED
  print(file, end="")
  file_split = file.split("-")
  file_all = folder_pack + settings.pair + ".csv"
  file_year = folder_pack + file_split[0] + ".csv"
  file_month = folder_pack + file_split[0] + "-" + file_split[1] + ".csv"

  # If the all file doesn't exist, write the header, else append
  if not os.path.exists(file_all):
    fa = open(file_all, "w")
    fa.write("start_at,symbol,period,open,high,low,close\n")
  else:
    fa = open(file_all, "a")

  # If the year file doesn't exist, write the header, else append
  if not os.path.exists(file_year):
    fy = open(file_year, "w")
    fy.write("start_at,symbol,period,open,high,low,close\n")
  else:
    fy = open(file_year, "a")

  # If the month file doesn't exist, write the header, else append
  if not os.path.exists(file_month):
    fm = open(file_month, "w")
    fm.write("start_at,symbol,period,open,high,low,close\n")
  else:
    fm = open(file_month, "a")

  # Loop through the file and write to both files
  line_nr = 0
  with open(folder_unpack + file) as fp:
    for line in fp:
        if line_nr: # To skip the first line, first time this is 0, next time this is 1
          fa.write(line)
          fy.write(line)
          fm.write(line)
        line_nr = 1

  fp.close()
  fa.close()
  fy.close()
  fm.close()

  print(" added")
