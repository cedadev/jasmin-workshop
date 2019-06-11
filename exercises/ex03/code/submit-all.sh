#!/bin/bash

# submit-all.sh
#
# Usage:    submit-all.sh
#

EXTRACTOR=exercises/ex3/extract-era-data.sh
OUTPUTS_DIR=exercises/users/$USER/ex3/lotus-outputs

mkdir -p $OUTPUTS_DIR


for i in $(seq 0 29); do
    day=$(date -d "2018-01-01 $i days" +%Y%m%d)
    echo "[INFO] Submitting job to LOTUS for date: $day"
    bsub -q short-serial -W 00:05 -o $OUTPUTS_DIR/${day}.out -e $OUTPUTS_DIR/${day}.err $EXTRACTOR $day 
done

