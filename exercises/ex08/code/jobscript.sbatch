#!/bin/bash

# SLURM directives 
#SBATCH --partition=workshop
#SBATCH --account=workshop
#SBATCH --job-name=axpy
#SBATCH -o %j.out 
#SBATCH -e %j.err
#SBATCH --time=05:00
#SBATCH --mem=100


# executable 
./axpySerial_intel_host118.exe


