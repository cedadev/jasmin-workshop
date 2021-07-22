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
years = range(2000, 2018)  # results in list 2000..2017 - python range rule
dir_template = '/badc/ukmo-midas-open/data/uk-daily-temperature-obs/dataset-version-201901/{}'

VAR_NAME = 'max_air_temp'
OUTPUT_DIR = './outputs'


def get_county(index):
    """
    Reads the 'counties.txt' file and returns the county at index `index`.
    Index is counted from 1..20.

    :param index: index of county to extract [int]
    :return: county name 
    """
    counties = open(os.path.join(OUTPUT_DIR, 'counties.txt')).read().strip().split()
    return counties[index - 1]


def _count_header(fpath):
    """
    Detects and returns the length of the header section in a CSV file where
    the header ends with a line "data".

    :param fpath: File path [string]
    :return: length of the header [int]
    """
    with open(fpath) as reader:

        for count, line in enumerate(reader):
            if line.strip() == 'data':
                return count + 1
        else:
            raise Exception('Cannot find "data" line in file: {}'.format(fpath))


def calculate_max(files, var_name=VAR_NAME):
    """
    Calculate the maximum value of the variable `var_name` found in all `files`.
    Loops through a set of station CSV files and returns the maximum value found.

    :param files: sequence of file paths [list]
    :param var_name: variable name indicated in column name [string]
    :return: maximum value [float]
    """
    # Set an initial maximum that will definitely be overtaken
    mx = -1000.

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


def calculate_county_max(county, var_name=VAR_NAME):
    """
    Calculate a time series of maximum annual values for the given `county` and
    variable `var_name`.
    All stations within the county are read and the maximum is extracted from all
    of them per year.
    The time series is written to a CSV file.

    :param county: name of county/region [string]
    :param var_name: variable name indicated in column name [string]
    :return: None
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
    Main function to manage the workflow. Parses command-line arguments
    before calculating country annual time series.

    :return: None
    """
    # Parse command-line arguments first
    parser = argparse.ArgumentParser()
    parser.add_argument('county_index', type=int, 
                        help='The index of the county in the "counties.txt" file')
    args = parser.parse_args()

    county = get_county(args.county_index)
  
    try:
        calculate_county_max(county) 
    except Exception as err:
        print('[ERROR] Unable to extract data for: {}'.format(county))


# The section below is run if the module is executed as a script
if __name__ == '__main__':

    main()


