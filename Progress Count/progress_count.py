from tqdm import tqdm
import time
import os

os.system('clear')
print("\n\n\n")
data = []
size = int(input("Enter List Size : "))

for i in tqdm(range(0,size), colour='blue', desc="prog"):
    values = int(input(f"Enter Value {i + 1} : "))
    data.append(values)
    os.system('clear')
    print("\n\n\n\n")

print("\n\n\n")

print("this is the your list : ", end="")
for value in data:
    print(f"{value} ", end="")
print(".\n\n\n")
