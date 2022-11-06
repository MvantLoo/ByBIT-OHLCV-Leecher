#!/usr/bin/env python3
"""

CorpusCrypto Leecher - Downloader
Download all files found in the URL

Requirements:
pip install beautifulsoup4

"""
import settings
import requests,os,pathlib,sys
import urllib.request
from bs4 import BeautifulSoup

# Use the pair in the argument, or else the pair in the settings
try:
  pair = sys.argv[1]
except:
  pair = settings.pair

# Create folders if not exist
folder_download = settings.folder_download + "/" + pair + "/"
pathlib.Path(folder_download).mkdir(parents=True, exist_ok=True)
  
# Read the HTML file and parse by BS
url = settings.url + pair + "/"
print(url)
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

# Loop through the page and download the files if they don't exist
for link in soup.find_all("a"):
  filename = link.get("href")
  print(filename, end="")
  if filename.endswith("gz"):
    link = url + filename
    saveas = folder_download + filename

    # If file does not exist, download and save
    if not os.path.exists(saveas):
      urllib.request.urlretrieve(link, saveas)
      print(" downloaded")
    else:
      print(" exists")
