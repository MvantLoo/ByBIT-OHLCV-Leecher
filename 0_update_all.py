#!/usr/bin/env python3
"""

CorpusCrypto Leecher - Packer
Loop through all pairs and download/unpack/pack them

Requirements:

"""
import settings
import os,pathlib,sys
#import s1_download as p1


for pair in settings.pairs:
   print("1_download.py " + pair)
   os.system("./1_download.py " + pair)
   print("2_unpack.py " + pair)
   os.system("./2_unpack.py " + pair)
   print("3_pack.py " + pair)
   os.system("./3_pack.py " + pair)



