#!/bin/bash

# submit-all.sh
#
# Usage:    submit-all.sh
#

EXTRACTOR=$PWD/extract-era-data.sh

# If you are doing exercise 05 outside of a training event, change CONTEXT from `workshop`
# to the account associated with your group workspace. For more info see the following link:
# https://help.jasmin.ac.uk/docs/batch-computing/slurm-queues/#new-slurm-job-accounting-hierarchy
# You'll also need to update OUTPUTS_DIR with your group workspace's root path
CONTEXT=workshop
OUTPUTS_DIR=/gws/pw/j07/workshop/users/$USER/ex05/lotus-outputs

# Work out partition/account arguments for LOTUS based on usage context
if [ $CONTEXT = "workshop" ]; then
    sbatch_part_cmds="--partition=standard --qos=workshop --account=workshop"  
else
    sbatch_part_cmds="--partition=standard --qos=debug --account=$CONTEXT"
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

