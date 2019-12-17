import os
f=open("commands.txt", "r")
if f.mode == 'r':
    contents =f.read()
    print(contents)