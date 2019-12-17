import os

for root, dirs, files in os.walk("F:\Sample Pictures"):  
    for filename in files:
        name,ext = os.path.splitext(filename)
        if(ext=='.png' or ext=='.jpg'):
            print(filename)