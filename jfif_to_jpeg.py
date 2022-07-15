# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 01:53:50 2022

@author: ASUS
"""
# You should put this file into your directory that you want to store .jpg files

from PIL import Image
import os

# Add your Path here that is include your jfif file

directory = r'PATH'
c=1
for filename in os.listdir(directory):
    
    if filename.endswith(".jfif"):
        im = Image.open(os.path.join(directory, filename))
        name='img'+str(c)+'.jpg'
        rgb_im = im.convert('RGB')
        rgb_im.save(name)
        c+=1
        print(os.path.join(directory, filename))
        continue
    else:
        continue