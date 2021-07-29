#!/bin/bash

# SLURM directives 
#SBATCH --partition=workshop
#SBATCH --account=workshop
#SBATCH --job-name=axpyMPI
#SBATCH -o %j.out 
#SBATCH -e %j.err
#SBATCH --time=05:00
#SBATCH --mem=100
#SBATCH --ntasks=4

##SBATCH --constraint=""
##SBATCH --nodes=4   If -N is not specified, the default behavior is to allocate enough nodes to satisfy the requirements

module load intel/20.0.0
module load eb/OpenMPI/intel/3.1.1

# executable 
mpirun ./axpyMPI.exe


