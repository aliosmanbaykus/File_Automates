# -*- coding: utf-8 -*-
"""
@author: aliosmanbaykus
"""

from PIL import Image
import os

# Add your Path here that is include your jfif file

directory = r'PATH that includes .jfif extended files'
save_directory = r'Path that you want to save your .jpeg extended files'
c=1
for filename in os.listdir(directory):
    
    if filename.endswith(".jfif"):
        im = Image.open(os.path.join(directory, filename))
        name='img'+str(c)+'.jpg'
        rgb_im = im.convert('RGB')
        rgb_im.save(os.path.join(save_directory, name))
        c+=1
        print(os.path.join(directory, filename))
        continue
    else:
        continue