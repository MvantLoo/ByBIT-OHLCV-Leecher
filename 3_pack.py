#!/usr/bin/env python3
"""

CorpusCrypto Leecher - Packer
Take the unpacked files and combine them in monthly, yearly and total files 
!!! THE EXISTING FOLDER WILL BE DELETED AND ALL "PACKED" FILES RECREATED

Requirements:

"""
import settings
import os,gzip,shutil,pathlib
#import requests
#import urllib.request
#from bs4 import BeautifulSoup

# Delete and recreate folder
shutil.rmtree(settings.pair + "/" + settings.folder_pack, ignore_errors=True)
pathlib.Path(settings.pair + "/" + settings.folder_pack).mkdir(parents=True, exist_ok=True)

# Find the files in the unpack folder, pack and save in the pack folder
unpack_folder = settings.pair + "/" + settings.folder_unpack + "/"
pack_folder = settings.pair + "/" + settings.folder_pack + "/"

for file in sorted(os.listdir(unpack_folder)): # IMPORTANT read the file list SORTED
  print(file, end="")
  file_split = file.split("-")
  file_year = pack_folder + file_split[0] + ".csv"
  file_month = pack_folder + file_split[0] + "-" + file_split[1] + ".csv"

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
  with open(unpack_folder + file) as fp:
    for line in fp:
        if line_nr: # To skip the first line, first time this is 0, next time this is 1
          fy.write(line)
          fm.write(line)
        line_nr = 1

  fp.close()
  fy.close()
  fm.close()

  print(" added")
