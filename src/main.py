import numpy as np
from utils import data

ts_w5 = data.ts_w5_index_values
np.save("ts_w5.npy", ts_w5)

print(ts_w5)