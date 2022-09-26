#!/bin/bash

# extract-era-data.sh
#
# Usage:    extract-era-data.sh <YYYYMMDD>
#

# Get the date from the command line, and break into: YYYY, MM, DD 
day=$1
YYYY=$(echo $day | cut -c1-4)
MM=$(echo $day | cut -c5-6)
DD=$(echo $day | cut -c7-8)

OUTPUT_DIR=/gws/pw/j07/workshop/users/$USER/ex05/outputs
mkdir -p $OUTPUT_DIR

VAR_ID=TCC
files=/badc/ecmwf-era-interim/data/gg/as/$YYYY/$MM/$DD/ggas*.nc

# Activate the environment containing CDO
module load jaspy

# Loop through the available files and process them
for INPUT_FILE in $files; do

    echo "[INFO] Subsetting: $INPUT_FILE"
    fname=${VAR_ID}-$(basename $INPUT_FILE)
    OUTPUT_FILE=$OUTPUT_DIR/$fname
    cdo selname,$VAR_ID $INPUT_FILE $OUTPUT_FILE

done

