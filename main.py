import playsound
import os
import random


path = "G:/Музыка"
files = os.listdir(path)
random.shuffle(files)
print(files)

for file in files:
    playsound.playsound(path + "/" + file)
