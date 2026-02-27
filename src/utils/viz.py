import numpy as np
import matplotlib.pyplot as plt


def plot_time_series(data,
                     timestamps=None,
                     title='Time Series',
                     xlabel='Time',
                     ylabel='Value',
                     figsize=(12, 6),
                     color='blue',
                     grid=True
                     ):

    plt.figure(figsize=figsize)

    if timestamps is not None:
        plt.plot(timestamps, data, color=color)
        plt.xticks(rotation=45)
    else:
        plt.plot(data, marker='o', color=color)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    if grid:
        plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

