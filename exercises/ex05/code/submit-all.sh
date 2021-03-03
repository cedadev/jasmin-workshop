#!/bin/bash

# submit-all.sh
#
# Usage:    submit-all.sh
#

EXTRACTOR=$PWD/extract-era-data.sh
OUTPUTS_DIR=/gws/nopw/j04/workshop/users/$USER/ex05/lotus-outputs

mkdir -p $OUTPUTS_DIR
queue=short-serial


for i in $(seq 1 2); do

    # Set the date
    day=$(printf "201801%02d" $i)
    echo "[INFO] Submitting job to LOTUS for date: $day"
    # Submit the job to LOTUS
    sbatch -p $queue -t 5 -o $OUTPUTS_DIR/${day}.%j.out \
           -e $OUTPUTS_DIR/${day}.%j.err $EXTRACTOR $day 

done

