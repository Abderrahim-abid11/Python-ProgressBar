from tqdm import tqdm
import time 
import shutil
import os

try:
    filename = str(input("Enter File Name : "))
    newfile = str(input("Enter New File Name : "))
    if os.path.exists(filename):
        shutil.copy2(filename, newfile)
        for i in tqdm(range(5), desc='Copy Process : ', colour='green'):
            time.sleep(0.5)
        light_green = "\033[1;32m"
        print(light_green, end="")
        print(f"File {filename} Copyed in {newfile}")
except FileNotFoundError:
    light_red = "\033[1;31m"
    print(light_red, end="")
    print("File Not Found !")
