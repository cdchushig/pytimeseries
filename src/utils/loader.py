import numpy as np
import importlib.resources as pkg_resources


def load_data_ts_w1():
    with pkg_resources.open_binary("data", "ts_w1.npy") as f:
        return np.load(f)

def load_data_ts_w2():
    with pkg_resources.open_binary("data", "ts_w2.npy") as f:
        return np.load(f)


def load_data_ts_w3():
    with pkg_resources.open_binary("data", "ts_w3.npy") as f:
        return np.load(f)

def load_data_ts_w4():
    with pkg_resources.open_binary("data", "ts_w4.npy") as f:
        return np.load(f)

def load_data_ts_w5():
    with pkg_resources.open_binary("data", "ts_w5.npy") as f:
        return np.load(f)
