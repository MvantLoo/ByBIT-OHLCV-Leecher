#!/usr/bin/env python3
"""

CorpusCrypto Leecher - Unpacker
Look in Download folder and unpack the files.

Requirements:
#pip install beautifulsoup4

"""
import settings
import os,gzip,shutil,pathlib
#import requests
#import urllib.request
#from bs4 import BeautifulSoup

# Create folders if not exist
pathlib.Path(settings.pair + "/" + settings.folder_unpack).mkdir(parents=True, exist_ok=True)

# Find the files in the download folder, unpack and save in the unpack folder
download_folder = settings.pair + "/" + settings.folder_download + "/"
unpack_folder = settings.pair + "/" + settings.folder_unpack + "/"

for file in os.listdir(download_folder):
  print(file, end="")
  file_in = download_folder + file
  file_out = unpack_folder + file.replace(".gz","") # Remove .gz to keep .csv

  # If unzipped file does not exist, unzip and save
  if not os.path.exists(file_out):
    with gzip.open(file_in, 'rb') as f_in:
      with open(file_out, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    print(" unzipped")
  else:
    print(" exists")
