#!/usr/bin/env python

"""
plot-county-temps.py
====================

Plots a graph of annual maximum temperature time series for a set of UK counties.
Input data is found in a set of CSV files. The plot is written to a PNG file.

"""

# Imports
import glob
import os

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')

# Global variables
OUTPUT_DIR = './outputs'


def plot_time_series():
    """
    Reads in a set of CSV files and plots the time series for each county on a
    single line graph which is written to a PNG file.

    :return: None
    """
    dfs = []
    county_files = glob.glob(os.path.join(OUTPUT_DIR, '*.csv'))
    county_labels = [os.path.basename(_).split('.')[0].title() for _ in county_files]

    for fpath in county_files:
        _df = pd.read_csv(fpath, index_col=0)
        dfs.append(_df)

    df = pd.concat(dfs, axis=1).reindex()
    df.columns = county_labels

    title = 'Max Temp time series for 20 UK Counties'
    x_label = 'Time (year)'
    y_label = 'Annual maximum temperature (°C)'

    # Get the axes object and modify
    ax = df.plot(title=title)
    ax.set(xlabel=x_label, ylabel=y_label)
    ax.set_xticks([2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028])
    ax.legend(fontsize='x-small')

    # Write the output file
    output_file = os.path.join(OUTPUT_DIR, 'annual-max-temp-time-series.png')
    plt.savefig(output_file)
    print('[INFO] Wrote: {}'.format(output_file))


# The section below is run if the module is executed as a script
if __name__ == '__main__':

    plot_time_series()

