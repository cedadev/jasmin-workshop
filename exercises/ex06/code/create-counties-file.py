#!/usr/bin/env python

"""
create-counties-file.py
=======================

A script to create a file containing a set of randomly selected counties from the
MIDAS-Open UK daily temperature data set.

Writes counties list to an output file.

Usage:
------

    create-counties-file.py

"""

# Imports
import os
import random


# Global variables
counties_dir = '/badc/ukmo-midas-open/data/uk-daily-temperature-obs/dataset-version-201901'
LIMIT = 20
    
OUTPUT_DIR = './outputs'
if not os.path.isdir(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)


def create_counties_file(limit=LIMIT):
    """
    Gets a list of available counties for which data exists based
    on the directories found. Writes a random set of these of length
    `LIMIT` to the output file.

    Output file format is one county name per line.

    :param limit: number of counties to write to output file [string].
    :return: None
    """
    counties = os.listdir(counties_dir)
    counties = [county for county in counties
                if county[0] != '0' and not county.startswith('midas')]

    random.shuffle(counties)
    counties = sorted(counties[:LIMIT])

    output_file = os.path.join(OUTPUT_DIR, 'counties.txt')

    with open(output_file, 'w') as writer:
        writer.write('\n'.join(counties[:LIMIT]))

    print('[INFO] Wrote counties to: {}'.format(output_file))


# The section below is run if the module is executed as a script
if __name__ == '__main__':

    create_counties_file()


