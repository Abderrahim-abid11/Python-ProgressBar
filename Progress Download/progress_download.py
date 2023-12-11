from tqdm import tqdm
import time

for i in tqdm(range(100), colour='magenta', desc="Download : "):
    time.sleep(0.5)
