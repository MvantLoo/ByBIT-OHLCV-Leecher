#!/usr/bin/env python3
"""

CorpusCrypto Leecher - Unpacker
Look in Download folder and unpack the files.

Requirements:

"""
import settings
import os,gzip,shutil,pathlib,sys

# Use the pair in the argument, or else the pair in the settings
try:
  pair = sys.argv[1]
except:
  pair = settings.pair

# Find the files in the download folder, unpack and save in the unpack folder
folder_download = settings.folder_download + "/" + pair + "/"
folder_unpack = settings.folder_unpack + "/" + pair + "/"

# Create folders if not exist
pathlib.Path(folder_unpack).mkdir(parents=True, exist_ok=True)

for file in os.listdir(folder_download):
  print(file, end="")
  file_in = folder_download + file
  file_out = folder_unpack + file.replace(".gz","") # Remove .gz to keep .csv

  # If unzipped file does not exist, unzip and save
  if not os.path.exists(file_out):
    with gzip.open(file_in, 'rb') as f_in:
      with open(file_out, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    print(" unzipped")
  else:
    print(" exists")
