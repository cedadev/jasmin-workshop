#!/bin/bash

# submit-all.sh
#
# Usage:    submit-all.sh
#

EXTRACTOR=$PWD/extract-era-data.sh
OUTPUTS_DIR=/gws/pw/j05/workshop/users/$USER/ex05/lotus-outputs

CONTEXT=workshop

# Work out partition/account arguments for LOTUS based on usage context
if [ $CONTEXT = "workshop" ]; then
    sbatch_part_cmds="--partition=workshop --account=workshop"
else
    sbatch_part_cmds="--partition=short-serial"
fi

mkdir -p $OUTPUTS_DIR

for i in $(seq 1 3); do

    # Set the date
    day=$(printf "201801%02d" $i)
    echo "[INFO] Submitting job to LOTUS for date: $day"
    # Submit the job to LOTUS
    sbatch $sbatch_part_cmds -t 5 -o $OUTPUTS_DIR/${day}.%j.out \
           -e $OUTPUTS_DIR/${day}.%j.err $EXTRACTOR $day 

done

