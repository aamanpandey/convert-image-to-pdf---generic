# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:09:43 2020

@author: Aman
"""

from PIL import Image
import os

file_list = []

for i in os.listdir():
    if i[-1:-5:-1] == "gpj.":
        file_name = os.getcwd() + "/" + i
        file_list.append(file_name)

image_rgb_list = []

for i in range(0,len(file_list),1):
    if i == 0:
        Image1 = Image.open(file_list[i])
        FirstImage = Image1.convert('RGB')
        
    else:
        Imagenext = Image.open(file_list[i])
        imnext = Imagenext.convert('RGB')
        image_rgb_list.append(imnext)
  
if "Combined.pdf" in os.listdir():
    for j in range(1,9999,1):        
        newfilename = "Combined" + str(j) + ".pdf"
        if newfilename not in os.listdir():
            Target_Save_Dir = os.getcwd() + "/" + newfilename
            break
else:
    Target_Save_Dir = os.getcwd() + "/" + "Combined.pdf"

if len(image_rgb_list) > 0:
    FirstImage.save(Target_Save_Dir,save_all=True, append_images=image_rgb_list)
else:
    FirstImage.save(Target_Save_Dir)
    
