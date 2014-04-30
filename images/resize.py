# -*- coding: utf-8 -*-
"""
Resizes android icons

Dependence :
        Pillow: pip install Pillow

You should put the images to be resized in the "images" folder.
Then the icons are resized in their respective folders.
"""
from PIL import Image
import glob

def resize(size, destiny):
        out = im.resize((size,size))
        out.save(destiny+fn, 'PNG')
        
size=32
for fn in glob.glob("*.png"):
        
        im = Image.open(fn)

        resize(size,"../drawable-mdpi/")

        sizeTemp=int(size*1.5)
        resize(sizeTemp,"../drawable-hdpi/")        

        sizeTemp=int(size*2)
        resize(sizeTemp,"../drawable-xhdpi/")  

        sizeTemp=int(size*3)
        resize(sizeTemp,"../drawable-xxhdpi/")  

        sizeTemp=int(size*4)
        resize(sizeTemp,"../drawable-xxxhdpi/")  
        



