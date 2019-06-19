#!/bin/bash

# extract-era-data.sh
#
# Usage:    extract-era-data.sh <YYYYMMDD>
#

day=$1
YYYY=$(echo $day | cut -c1-4)
MM=$(echo $day | cut -c5-6)
DD=$(echo $day | cut -c7-8)

OUTPUT_DIR=/gws/nopw/j04/workshop/users/$USER/ex3
OUTPUT_DIR=~/workshop/users/$USER/ex3
mkdir -p $OUTPUT_DIR

VAR_ID=TCC

files=/badc/ecmwf-era-interim/data/gg/as/$YYYY/$MM/$DD/ggas*.nc

module load jaspy

for INPUT_FILE in $files; do

    echo "[INFO] Subsetting: $INPUT_FILE"
    fname=${VAR_ID}-$(basename $INPUT_FILE)
    OUTPUT_FILE=$OUTPUT_DIR/$fname
    cdo selname,$VAR_ID $INPUT_FILE $OUTPUT_FILE

done

