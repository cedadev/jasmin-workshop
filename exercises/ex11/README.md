---
title: Exercise 11 - MPI on JASMIN
author: Fatima Chami
---

# Exercise 11: MPI on JASMIN

### Scenario
I am using the community code JULES for my research work. I need to add a new feature in the code. I need to edit the source code and then compile and build it on JASMIN. JULES is an MPI parallel code. This exercise will demonstrate how to compile from source an MPI parallel code and test it on LOTUS.
Parallel computing is the use of two or more processors to solve a large problem size. There are different forms of parallelism, Shared Memory parallelism (threading) e.g. OpenMP and Distributed Memory parallelism which uses the Message Passing Interface (MPI). 

The Fortran example generates two vectors X(n) and Y(n) of n=2**10 elements and then calculates a vector Z(n) as Z(i)= a * X(i) + Y(i). The code outputs the maximum value of the vector elements Z(i),  maxval(abs(Z))

A very important part of this workflow is that there are 2 separate steps:
1. Compilation of code:
   * On a single LOTUS host
   * Run interactively
2. Execution of compiled code:
   * On the required number of LOTUS hosts
   * Run as batch job(s) 

There are a limited number of licences available for the Intel compiler so please adhere to this 2-step approach.


### Objectives 

After completing this exercise you will:
 * **know** about the MPI library available on JASMIN
 * **learn how to compile** an MPI parallel code on a LOTUS compute node interactively
 * **become aware** of the special SLURM submission options to request resources for an MPI parallel job 
 
 
 ### JASMIN resources

 * Scientific analysis servers: `sci-vm-0[1-6].jasmin.ac.uk`, `sci-ph-0[1-2].jasmin.ac.uk`
 * Group workspace: `/gws/pw/j07/workshop`
 * LOTUS batch queues: `workshop` (`par-single` or `par-multi` outside the event)
 * Fortran MPI source code is (available in the Github repository): 
 `/gws/pw/j07/workshop/exercises/ex11/code/axpyMPI.f90`
 * Help documentation at https://help.jasmin.ac.uk

### Local resources

 * SSH key & passphrase 
 * Terminal application or NX client
 * A valid `jasmin-login` grant associated with your JASMIN account 


### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

1. Login to a JASMIN scientific analysis server 
   * Launch two terminal sessions: terminal 1 will be used for compiling and testing codes on LOTUS while terminal 2 will be used for submitting and monitoring jobs 
   * Access a JASMIN login server on each terminal (see exercise 01)
   * Choose a Sci server with the lowest load 
   * Login to the chosen sci server on each terminal
   * Copy the Fortran source code from the exercise directory (shown in the JASMIN resources section) to your current working directory            
   > [!NOTE]
   > One terminal will be used for compiling and testing codes on LOTUS while the second terminal will be used for submitting and monitoring batch jobs. 
1. Compile and test a Fortran code interactively on LOTUS 
   * On terminal 1, invoke a pseudo-interactive session on LOTUS using the SLURM command `srun` with two CPU cores allocation: `srun --ntasks=2 --partition=workshop --account=workshop  --pty /bin/bash`
   * What is the compute node allocated and what type of CPU model the node has?
   * On the LOTUS compute node, load the Intel compiler module `module load intel/20.0.0` and the OpenMPI library module: `module load eb/OpenMPI/intel/3.1.1` and check that the two modules are loaded.
   * Build the Fortran code executable using the command `mpif90 axpyMPI.f90 -o axpyMPI.exe`
   * Execute the binary on a single CPU core and then on two cores: `mpirun -np 2 axpyMPI.exe`
   * What is the ouput?
   * On terminal 2, check the job ID associated to this pseudo-interactive session on LOTUS 
   * Exit the interactive session on LOTUS `exit`. The Job should be cleared from SLURM
1. Prepare a script to submit the parallel MPI code to SLURM
   * On terminal 1, launch a text editor to prepare the job script e.g. `jobscriptMPI.sbatch` to submit the binary MPI compiled earlier.
   * Specify the number of parallel MPI tasks
   * Submit the job to SLURM scheduler and note the job ID `sbatch axpyMPI.sbatch`
   * On terminal 2, monitor the job state using SLURM command `squeue -u <username>`
   * What is the name of the compute node the job run on? is it the same node type on which the code was compiled?
   * Check the resources used by the job memory,CPU using `scontrol show job <jobID>`
1. Explore MPI job requirements -**Optional**-
   * Specify the memory required per CPU using `--mem-per-cpu=<size[units]>` Default value is 4 GB ( which is defined `DefMemPer‐CPU`)
   * Define a distribution of tasks across nodes using `--ntasks-per-node=ntasks` and `--nodes=<minnodes[-maxnodes]>` 
   > [!NOTE]
   > The `--ntasks` option will take  precedence  and the `--ntasks-per-node` will be treated as a maximum count of tasks per node.
   * Submit the same job script but pass the new memory and core distribution arguments to SLURM `sbatch`
   * What is the job wait time?
   * What is the elapsed time per job? 
   * Now add the node type specification `--constraint="intel"`
   * Rerun the job


### Questions to test yourself

All too easy? Here are some questions to test your knowledge and understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

1. Is there a limit on the number of parallel tasks an MPI job can have? 
1. What is the MPI implementation supported on JASMIN?
1. Is it possible to run an MPI binary that was compiled on a different system?
1. How to find out about the MPI libray that the code was compiled against?
1. What type of storage is suitable for parallel MPI IO?
1. Can I run a Python script in parallel using MPI4py?

### Review / alternative approaches / best practice

By completing this exercise you will be able to compile and test a parallel MPI Fortran code interactively on LOTUS.  You will be able to use the special submission flags to submit an MPI job to SLURM. You will be able to use compilers via the module environment. MPI message passing interface is a library to facilitate data sharing and communication between CPU cores -often called ranks- as each rank accesses its own data space. 


* `par-single` and `par-multi` are dedicated queues for MPI and OpenMP parallel codes
* Use `mpirun` to execute MPI parallel codes and to ensure that the MPI communications runs over the private MPI network.
* The OpenMPI library is the only supported MPI library on LOTUS. OpenMPI v3.1.1 and v4.0.0 are provided which are fully MPI3 compliant. 
*  MPI I/O features are fully supported *only* on `/work/scratch-pw` disk as this uses a Panasas fully parallel file system
* Run the MPI code on two cores before scaling up to many cores
* Keep your source code in your home directory which is backed up
* There is a limited number of licences available for Intel compiler, so please do not submit many jobs to compile the same code. 
* If the code is compiled for a specific CPU architecture, then the binary should be executed on the same CPU architecture

### Cheat Sheet

1. Login to a JASMIN scientific analysis server 
   * Login to the chosen sci server on each terminal
   ```
   $ ssh -A train049@sci-ph-01.jasmin.ac.uk
   [train049@sci-ph-01 ~]$ 
   ```
   * Copy the Fortran source code from the exercise directory (shown in the JASMIN resources section) to your current working directory 
   ```
   $ cp /gws/pw/j07/workshop/exercises/ex11/code/axpyMPI.f90 .
   ```           
   > [!NOTE]
   > One terminal will be used for compiling and testing codes on LOTUS while the second terminal will be used for submitting and monitoring batch jobs. 
1. Compile and test a Fortran code interactively on LOTUS 
   * On terminal 1, invoke a pseudo-interactive session on LOTUS using the SLURM command `srun` with two CPU cores allocation
   ```
   $ srun --ntasks=2 --partition=workshop --account=workshop  --pty /bin/bash
   srun: job 64164115 queued and waiting for resources
   srun: job 64164115 has been allocated resources
   cpu-bind=MASK - host149, task  0  0 [11224]: mask 0x1 set
   [train049@host149 ] $
   ```
   * What is the compute node allocated and what is its CPU model?

   From the command line prompt, the LOTUS compute node allocated is `host149`. The CPU model is Intel 'ivybridge' and the node has 128 GB memory. This info can be found from SLURM or from `/proc/cpuinfo` as shown below:
   ```
   @host149 ] $ scontrol show node host149 | grep Features
    AvailableFeatures=ivybridge128G,lotus241,lotus2,intel
   ActiveFeatures=ivybridge128G,lotus241,lotus2,intel
   ```
   or 
   ```
   @host149 ] $ cat /proc/cpuinfo
   ...
   model name	: Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz
   ...
   ```
   `CPU E5-2650 v2` corresponds to hostgroup `ivybridge128G` see the Table in this help page   https://help.jasmin.ac.uk/article/4932-lotus-cluster-specification 
   
   * On the LOTUS compute node, load the Intel compiler `module load intel/20.0.0` and the OpenMPI library module: `module load eb/OpenMPI/intel/3.1.1` and check that the two modules are loaded.
   ```
   @host149 ] $ module load intel/20.0.0
   @host149 ] $ module load eb/OpenMPI/intel/3.1.1
   @host149 ] $ module li
   Currently Loaded Modulefiles:
    1) intel/cce/20.0.0         2) intel/fce/20.0.0         3) intel/20.0.0             4) eb/OpenMPI/intel/3.1.1
   ```
   * Compile the Fortran code using the command 
   ```
   @host149 ] $ mpif90 axpyMPI.f90 -o axpyMPI.exe
   ```
   * Execute the binary using 1 core and then using two cores: 
   ```
   @host149 ] $ mpirun -np 2 axpyMPI.exe
     1.07598934124890       0.000000000000000E+000
   ```
   * On terminal 2, check the job ID associated with this pseudo-interactive session on LOTUS and the number of cores allocated 
   ```
    @sci-ph-01 ~ ]$ squeue -u trai049
             JOBID PARTITION     NAME    USER   ST     TIME  NODES NODELIST(REASON)
          64164115  workshop     bash   train049 R      24:17      1 host149
   ```
   The number of nodes and CPUs allocated can also be found from this SLURM command:
   ```
   @sci-ph-01 ~ ]$ scontrol show job 64164115 
   ...
   NumNodes=1 NumCPUs=2 NumTasks=2 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
   ...
   ```
   * Exit the interactive session on LOTUS `exit`. The Job should be cleared from SLURM
   ```
    @host149 ] $ exit
    [train049@sci-ph-01 ~]$ 
   ```
1. Prepare a script to submit the parallel MPI code to SLURM
   * On terminal 1, launch a text editor to prepare a Bash script to submit the MPI executable generated earlier (use the template jobscript `jobscriptMPI.sbatch` shown below)
   ```
   #!/bin/bash

   # SLURM directives:
   #SBATCH --partition=workshop
   #SBATCH --account=workshop
   #SBATCH --job-name=axpyMPI
   #SBATCH -o %j.out 
   #SBATCH -e %j.err
   #SBATCH --time=05:00
   #SBATCH --mem=100
   #SBATCH --ntasks=xxx
   
   # User specific environment 
   module load intel/20.0.0
   module load eb/OpenMPI/intel/3.1.1

   # executable 
   mpirun ./axpyMPI.exe

   ```
   * Specify the number of parallel MPI tasks
   ```
   #SBATCH --ntasks=4
   ```
   * Submit the job to SLURM scheduler and note the job ID `sbatch axpyMPI.sbatch`
   ```
   [train049@sci-ph-01 ~]$ sbatch axpyMPI.sbatch
    Submitted batch job 4815542
   ```
   * On terminal 2, monitor the job state using SLURM command:
   ```
   [train049@sci-ph-02 ~]$ squeue -u train049
     JOBID PARTITION     NAME     USER ST    TIME  NODES NODELIST(REASON)
   4815542  workshop  axpyMPI train049 PD    0:00      1 (None)
   ```
   The job is pending `PD`. Once the job starts running the job state will change from `PD` to `R` and the elapsed runtime will show in the column `TIME` 
   * What is the name of the compute node the job run on? is it the same node type on which the code was compiled?
   ```
   [train049@sci-ph-02 ~]$ scontrol show job 4815542 
   UserId=train049(7052227) GroupId=users(26030) MCS_label=N/A
   Priority=998385 Nice=0 Account=workshop QOS=normal
   JobState=COMPLETED Reason=None Dependency=(null)
   ...
   NodeList=host[195,267]
   NumNodes=2 NumCPUs=4 NumTasks=4 CPUs/Task=1
   ...
   ```
   For this run, host[195,267] are of node type Intel

   * What is the total memory allocated for this job? 
   From the output`scontrol show job 4815542` scroll down to the line where `mem` is specified:
   ```
   mem=200M,node=2
   ```
   The total memory allocated for the job is 200 MB. The specified memory `#SBATCH --mem=100` is the minimum memory required per node in MB units `MinMemoryNode=100M`.
   To find out about the memory usage, use the SLURM command `sacct`:
   ```
    sacct -j 4815542  --format=jobid%20,reqmem,maxrss,nodelist,ncpu
               JobID     ReqMem     MaxRSS        NodeList      NCPUS 
    -------------------- ---------- ---------- --------------- ---------- 
             4815542      100Mn              host[195,267]          4 
       4815542.batch      100Mn       924K         host195          1 
           4815542.0      100Mn      1016K         host267          1 
   ```
1. Explore MPI job requirements -Optional-
   * Specify the memory required per core using `--mem-per-cpu=XXX`
   * Define a distribution of tasks across nodes using `--ntasks-per-node=XXX` and `--nodes=<minnodes[-maxnodes]>` 
   * Submit the same job script but pass the new memory and core distribution arguments to SLURM `sbatch`
   * What is the job wait time?
   * What is the elapsed time per job? 
   * Now add the node type specification `--constraint="intel"`
   * Rerun the job


### Answers to questions

> 1. Is there a limit on the number of parallel tasks an MPI job can have? 

The limit is 16 cores for the `par-single` queue and 256 cores for the `par-multi` queue. https://help.jasmin.ac.uk/article/4881-lotus-queues
> 2. What is the MPI implementation supported on JASMIN?

The OpenMPI library is the only supported MPI library on LOTUS. OpenMPI v3.1.1 and v4.0.0 are provided which are fully MPI3 compliant: 
```
eb/OpenMPI/gcc/3.1.1
eb/OpenMPI/gcc/4.0.0   
eb/OpenMPI/intel/3.1.1 
eb/OpenMPI/intel/4.1.0
```
> 3. Is it possible to run an MPI parallel code that was compiled on a different system?

Recompilation on JASMIN is recommended 

> 4. How to find out about the MPI libray that the code was compiled against?

Use the Linux command `ldd <name-of-executable>`
> 5. What type of storage is suitable for pararallel MPI IO?

MPI I/O features are fully supported *only* on the LOTUS `/work/scratch-pw` directory as this uses a Panasas fully parallel file system

> 6. Can I run a Python script in parallel using MPI4py?

This needs rewriting/converting the Python serial code in parallel using the MPI4py library


