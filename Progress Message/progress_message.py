from tqdm import tqdm
import os
import time

os.system('clear')
print("\n\n\n")

send = str(input("To Send Type (Y/N) : "))
if send.upper() == 'Y':
    for i in tqdm(range(100), desc="Message Send : ", colour='white'):
        time.sleep(0.01)
    print("Message Send Succefuly .")
elif send.upper() == 'N':
    print("Process End .")

print("\n\n\n")
