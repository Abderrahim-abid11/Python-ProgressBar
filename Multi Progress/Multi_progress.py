from tqdm import tqdm
import time

for i in tqdm(range(10), desc='Progress 1', colour='white'):
    time.sleep(1)

for j in tqdm(range(5), desc='Progress 2', colour='black'):
    time.sleep(1)
