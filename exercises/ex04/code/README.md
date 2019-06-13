There are 101 county/region directories. We will randomly select 20 of them.

Workflow:

 1. create-counties-file.py [x1]
 2. extract-annual-max-series.py [x20]
 3. plot-county-temps.py [x1]


I want to analyse a set of historical temperature records from weather stations in the UK. 

I am interested in calculating annual averages for each county. These are available from the "MIDAS-Open" in the CEDA archive.

Objective:
Read station data from the MIDAS-Open dataset and aggregate to annual mean time series averaged across all stations. 
Then plot a line graph of the county annual averaged time series together in a nice PNG file.

An example file can be found at:
    /badc/ukmo-midas-open/data/uk-daily-temperature-obs/dataset-version-201901/devon/01359_cheldon-barton/qc-version-1/midas-open_uk-daily-temperature-obs_dv-201901_devon_01359_cheldon-barton_qcv-1_1977.csv

JASMIN Resources:
i.	Scientific analysis server: jasmin-sci4.ceda.ac.uk
ii.	Rose/cylc
iii.	Space to store the output file: /gws/nopw/j04/workshop/users/$USER/ex4
iv.	Access to the Python 3 (Jaspy) environment on JASMIN.
v.	Read-access to the MIDAS-Open data set in the CEDA archive

Local Resources:
i.	SSH client (to login to JASMIN)

Worked example:
i.	Start ssh-agent session and add JASMIN private key
<AS ABOVE>
ii.	SSH to a scientific analysis server
<AS ABOVE>

iii.	The following script can be used to extract a time-series of annual temperature measurements:
 /gws/nopw/j04/workshop/resources/ex4/extract-annual-mean-series.py

#!/usr/bin/env python

"""
extract-annual-mean-series.py
=============================

!!!ADD DOCS

"""

# Imports


/badc/ukmo-midas-open/data/uk-daily-temperature-obs/dataset-version-201901/${COUNTY}/*/qc-version-1/*qcv-1_2017.csv



def calculate_county_mean():



# The section below is run if the module is executed as a script
if __name__ == '__main__':

    calculate_county_mean()


iv.	A list of all the county directories is provided in the file:
 /gws/nopw/j04/workshop/resources/ex4/county_dirs.txt

v.	Write a script to cycle through the county directories and submitting them to the "extract-annual-mean-series.py" script on LOTUS.

vi.	Write a script to check that those files were successfully created.

vii.	Use this script to plot the output files:
 /gws/nopw/j04/workshop/resources/ex4/plot-annual-averages.py

