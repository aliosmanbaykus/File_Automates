# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 09:37:50 2022

@author: ASUS
"""
import os

# Absolute path of a file
directory = r'PATH'
c=0 #starting number of iterations

for filename in os.listdir(directory):
    new_name = 'Your new file name'
    c+=1
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
