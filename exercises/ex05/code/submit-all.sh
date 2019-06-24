#!/bin/bash

# submit-all.sh
#
# Usage:    submit-all.sh
#

EXTRACTOR=$PWD/extract-era-data.sh
OUTPUTS_DIR=/group_workspaces/jasmin2/workshop/users/$USER/ex05/lotus-outputs

mkdir -p $OUTPUTS_DIR
queue=workshop


for i in $(seq 0 1); do
    day=$(date -d "2018-01-01 $i days" +%Y%m%d)
    echo "[INFO] Submitting job to LOTUS for date: $day"
    bsub -q $queue -W 00:05 -o $OUTPUTS_DIR/${day}.%J.out -e $OUTPUTS_DIR/${day}.%J.err $EXTRACTOR $day 
done

