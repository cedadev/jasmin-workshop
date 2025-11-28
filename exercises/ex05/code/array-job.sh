#!/bin/bash 

# extractall-job-array.sh

#SBATCH --partition=standard
#SBATCH --account=workshop
#SBATCH --qos=workshop
#SBATCH --job-name=extractall
#SBATCH -o %A_%a.out 
#SBATCH -e %A_%a.err
#SBATCH --time=05:00
#SBATCH --array=1-3

EXTRACTOR=$PWD/extract-era-data.sh

OUTPUTS_DIR=/gws/pw/j07/workshop/users/$USER/ex05/lotusjobarray-outputs
mkdir -p $OUTPUTS_DIR

module add jaspy

# get the day from the array indes in two digits, e.g. 01, 02, etc
i=${SLURM_ARRAY_TASK_ID}

day=$(printf "201801%02d" $i)

echo "[INFO] array-job index for date: $day"

$EXTRACTOR $day
