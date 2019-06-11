#!/usr/bin/env python

"""
extract-annual-max-series.py
=============================

Script to extract a time series of maximum temperature observations from
all measurements for a given county. The resulting time series is written
to an output file for later use.

Usage:
------

    extract-annual-max-series.py <county>

"""

# Imports
import argparse
import glob
import os

# Third-party packages
import pandas


# Global variables
years = range(2000, 2018) # maxs 2000..2017 - python range rule
dir_template = '/badc/ukmo-midas-open/data/uk-daily-temperature-obs/dataset-version-201901/{}'
var_name = 'max_air_temp'

OUTPUT_DIR = '../outputs'


def _count_header(fpath):
    """
!!!DOC
    """
    with open(fpath) as reader:

        for count, line in enumerate(reader):
            if line.strip() == 'data':
                return count + 1
        else:
            raise Exception('Cannot find "data" line in file: {}'.format(fpath))


def calculate_max(files):
    """

    """
    # Set an initial maximum that will definitely be overtaken
    mx = -1000

    for fpath in files:
        header_count = _count_header(fpath)
        df = pandas.read_csv(fpath, skiprows=header_count, skipfooter=1, engine='python',
                             usecols=[var_name])

        value = df[var_name].max()
        if value > mx: 
            mx = value

    # Set maximum to NaN (missing value) if no data found
    if mx == -1000:
        mx = pandas.np.nan 

    return mx


def calculate_county_max(county):
    """

    """
    dr = dir_template.format(county)

    if not os.path.isdir(dr):
        raise Exception('Cannot find data for county: {}'.format(county))

    values = []

    for year in years:
        fname_pattern = os.path.join(dr, '*/qc-version-1/*qcv-1_{}.csv'.format(year))
        files = glob.glob(fname_pattern)

        if files:
            max = calculate_max(files)
            values.append(max)

    df = pandas.DataFrame(values, index=years, columns=['annual_' + var_name])

    county_file = os.path.join(OUTPUT_DIR, '{}.csv'.format(county))
    df.to_csv(county_file, float_format='%.02f')
    print('[INFO] Wrote county file: {}'.format(county_file))
    

def main():
    """
    !!!DOCUMENT

    """
    # Parse command-line arguments first
    parser = argparse.ArgumentParser()
    parser.add_argument("county", type=str, help="The name of a county")
    args = parser.parse_args()

    county = args.county.lower()
  
    try:
        calculate_county_max(county) 
    except Exception as err:
        print('[ERROR] Unable to extract data for: {}'.format(county))


# The section below is run if the module is executed as a script
if __name__ == '__main__':

    main()


