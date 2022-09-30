"""

CorpusCrypto Leecher - Downloader
Download all files found in the URL

Requirements:
pip install beautifulsoup4

"""
import settings
import requests,os
import urllib.request
from bs4 import BeautifulSoup

# Create folders if not exist
try: # folder of Pair
  os.mkdir(settings.pair)
except:
  pass
try: # folder of script-name
  os.mkdir(settings.pair + "/" + os.path.basename(__file__))
except:
  pass

# Read the HTML file and parse by BS
print(settings.url)
r  = requests.get(settings.url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

# Loop through the page and download the files if they don't exist
for link in soup.find_all('a'):
    filename = link.get('href')
    print(filename, end="")
    if filename.endswith('gz'):
      link = settings.url + filename
      saveas = settings.pair + "/" + os.path.basename(__file__) + '/' + filename

      # If file does not exist, download and save
      if not os.path.exists(saveas):
        urllib.request.urlretrieve(link, saveas)
        print(" downloaded")
      else:
        print(" exists")
