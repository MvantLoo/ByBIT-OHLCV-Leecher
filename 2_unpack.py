"""

CorpusCrypto Leecher - Unpacker
Look in Download folder and unpack the files.

Requirements:
#pip install beautifulsoup4

"""
import settings
import os,gzip,shutil
#import requests
#import urllib.request
#from bs4 import BeautifulSoup

# Create folders if not exist
try: # folder of Pair
  os.mkdir(settings.pair)
except:
  pass
try: # folder of script-name
  os.mkdir(settings.pair + "/" + os.path.basename(__file__))
except:
  pass

# Find the files in the download folder, unpack and save in the unpack folder
download_folder = settings.pair + "/1_download.py/"
unpack_folder = settings.pair + "/" + os.path.basename(__file__) + "/"

for file in os.listdir(download_folder):
  print(file, end="")
  file_in = download_folder + file
  file_out = unpack_folder + file.replace(".gz","")

  # If unzipped file does not exist, unzip and save
  if not os.path.exists(file_out):
    with gzip.open(file_in, 'rb') as f_in:
      with open(file_out, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    print(" unzipped")
  else:
    print(" exists")
