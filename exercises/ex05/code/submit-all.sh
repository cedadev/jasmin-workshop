#!/bin/bash

# submit-all.sh
#
# Usage:    submit-all.sh
#

EXTRACTOR=exercises/ex5/extract-era-data.sh
OUTPUTS_DIR=exercises/users/$USER/ex5/lotus-outputs

mkdir -p $OUTPUTS_DIR


for i in $(seq 0 29); do
    day=$(date -d "2018-01-01 $i days" +%Y%m%d)
    echo "[INFO] Submitting job to LOTUS for date: $day"
    bsub -q workshop -W 00:05 -o $OUTPUTS_DIR/${day}.%J.out -e $OUTPUTS_DIR/${day}.%J.err $EXTRACTOR $day 
done

