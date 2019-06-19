# Exercise 06 - Managing a multi-step workflow 

## Scenario

I want to analyse a set of historical temperature records from weather stations in the UK. 

I am interested in calculating annual averages for each county. These are available from the "MIDAS-Open" in the CEDA archive.

## Objective

Read station data from the MIDAS-Open dataset and aggregate to annual mean time series averaged across all stations. 
Then plot a line graph of the county annual averaged time series together in a nice PNG file.

An example file can be found at:

`/badc/ukmo-midas-open/data/uk-daily-temperature-obs/dataset-version-201901/devon/01359_cheldon-barton/qc-version-1/midas-open_uk-daily-temperature-obs_dv-201901_devon_01359_cheldon-barton_qcv-1_1977.csv`

All outputs are written to a local `./outputs` directory.

There are 101 county/region directories. I will randomly select 20 of them.

## Workflow

 0. Pull code from github repository [x1]
 1. Run: create-counties-file.py [x1]
 2. Run: extract-annual-max-series.py [x20]
 3. Run: plot-county-temps.py [x1]

