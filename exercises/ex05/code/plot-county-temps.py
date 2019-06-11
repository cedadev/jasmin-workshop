#!/usr/bin/env python

"""



"""


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

import glob
import os

DATA_DIR = '../data'
OUTPUT_DIR = '../outputs'


def plot_time_series():

    dfs = []
    county_files = glob.glob(os.path.join(OUTPUT_DIR, '*.csv'))
    county_labels = [os.path.basename(_).split('.')[0].title() for _ in county_files]

    for fpath in county_files:
        _df = pd.read_csv(fpath, index_col=0)
        dfs.append(_df)

    df = pd.concat(dfs, axis=1, join_axes=[dfs[0].index])
    df.columns = county_labels

    title = 'Max Temp time series for 20 UK Counties'
    x_label = 'Time (year)'
    y_label = 'Annual maximum temperature (°C)'

    ax = df.plot(title=title)
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.set_xticks([2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028])
    ax.legend(fontsize='x-small')

    output_file = os.path.join(OUTPUT_DIR, 'annual-max-temp-time-series.png')
    plt.savefig(output_file)
    print('[INFO] Wrote: {}'.format(output_file))


if __name__ == '__main__':

    plot_time_series()

