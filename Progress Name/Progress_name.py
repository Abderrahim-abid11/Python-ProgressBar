from tqdm import tqdm
import time

for i in tqdm(range(100), desc="Progress Bar : "):
    time.sleep(1)
