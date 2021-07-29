---
title: Exercise 11 - MPI on JASMIN
author: Fatima Chami
---

# Exercise 11: MPI on JASMIN

### Scenario

Parallel computing is the use of two or more processors to solve a large problem size. There are different forms of parallelism, Shared Memory parallelism (threading) e.g. OpenMP and Distributed Memory parallelism which uses the Message Passing Interface (MPI). This exercise will demonstrate how to compile and test a parallel MPI Fortran code on LOTUS. 

The Fortran code generates two vectors X(n) and Y(n) of n=2**10 elements and then calculates a vector Z(n) as Z(i)= a * X(i) + Y(i). The code outputs the maximum value of the vector elements Z(i),  maxval(abs(Z))

A very important part of this workflow is that there are 2 separate steps:
1. Compilation of code:
   * On a single LOTUS host
   * Run interactively
2. Execution of compiled code:
   * On the required number of LOTUS hosts
   * Run as batch job(s) 

There are a limited number of licences available for compilers so please adhere to this 2-step approach.


### Objectives 

After completing this exercise you will:
 * **know** about the MPI implementation on JASMIN
 * **learn** about the Fortran/C compilers and how to use them 
 * **compile** an MPI parallel code on a LOTUS compute node interactively
 * **become aware** of the special SLURM submission options to request resources for an MPI parallel job 
 
 
 ### JASMIN resources

 * Scientific analysis servers: `sci[1-6].jasmin.ac.uk`
 * Group workspace: `/gws/pw/j05/workshop`
 * LOTUS batch queues: 'workshop' (par-single or par-multi outside the event)
 * Fortran MPI source code is (available in the Github repository): 
 `/gws/pw/j05/workshop/exercises/ex11/src/axpyMPI.f90`
 * Help documentation at https://help.jasmin.ac.uk

### Local resources

 * SSH key & passphrase 
 * Terminal application or NX client
 * A valid `jasmin-login` grant associated with your JASMIN account 

### Videos
You can follow this exercise by watching the videos below, or by following the text of this article, or a combination of both.
|  |  |
| --- | --- |
#| Task | [![](https://img.youtube.com/vi/_09pMUX6fLQ/mqdefault.jpg )](https://www.youtube.com/watch?v=_09pMUX6fLQ) |
| Solutions & Discussion | coming soon |

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

1. Login to a JASMIN scientific analysis server 
   * Launch two terminal sessions
   * Access a JASMIN login server on each terminal (see exercise 01)
   * Choose a Sci server with the lowest load 
   * Login to the chosen sci server on each terminal
   * Copy the Fortran source code from the exercise directory (shown in the JASMIN resources section) to your current working directory            
   > **_NOTE:_**  One terminal will be used for compiling and testing codes on LOTUS while the second terminal will be used for submitting and monitoring batch jobs. 
1. Compile and test a Fortran code interactively on LOTUS 
   * On terminal 1, invoke a pseudo-interactive session on LOTUS using the SLURM command`srun` with two CPU cores allocation: `srun --ntasks=2 --partition=workshop --account=workshop  --pty /bin/bash`
   * What is the compute node allocated and what type of CPU model the node has?
   * On the LOTUS compute node, load the Intel compiler module `module load intel/20.0.0`and the OpenMPI library module: `module load eb/OpenMPI/intel/3.1.1` and check that the two modules are loaded.
   * Compile the Fortran code using the command `mpif90 axpyMPI.f90 -o axpyMPI.exe`
   * Execute the binary using 1 core and then using two cores: `mpirun -np 2 axpyMPI.exe`
   * What is the ouput?
   * On terminal 2, check the job ID associated to this pseudo-interactive session on LOTUS 
   * Exit the interactive session on LOTUS `exit`. The Job should be cleared from SLURM
1. Prepare a script to submit the parallel MPI code to SLURM
   * On terminal 1, launch a text editor to prepare the job script e.g. `axpyMPI.sbatch` to submit the binary MPI compiled earlier.
   * Specify the number of parallel MPI tasks
   * Submit the job e.g. job1 to SLURM scheduler and note the job ID `sbatch axpyMPI.sbatch`
   * On terminal 2, monitor the job state using SLURM command `squeue` 
   * What is the name of the compute node the job run on? is it the same node type on which the code was compiled?
   * Check the resources used by the job memory,CPU using 'scontrol show job jobID'
   * Inspect the job output and error file 
1. Estimate and refine an MPI job requirements
   * Specify the memory required per core   
   * Specify the node type    
   * Define a distribution of cores across nodes e.g. job2 or on a single node e.g. job3 
   * Submit the same job script file but pass the new memory and core distribution to the SLURM 'sbatch'
   * What is the job wait time?
   * What is the elapsed time for job2 and job3?
1. Writing to the scratch area    
   *     
   *     
   *    


### Questions to test yourself

All too easy? Here are some questions to test your knowledge and understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

1. Is there a limit on the number of parallel tasks an MPI job can have? 
1. What is the MPI implementation supported on JASMIN?
1. Is it possible to run an MPI binary that was compiled on a different system?
1. What is the difference between an MPI code and a code that uses MPI IO only?
1. How to find out about the MPI libray that the code was compiled against?
1. What type of storage is suitable for pararallel MPI IO?
1. Can I run a Python script in parallel using MPI4py?

### Review / alternative approaches / best practice

By completing this exercise you will be able to compile and test a parallel MPI Fortran code interactively on LOTUS.  You will be able to use the special submission flags to submit an MPI job to SLURM. You will be able to use compilers via the module environment. MPI message passing interface is a library to facilitate data sharing and communication between CPU cores -often called ranks- as each rank accesses its own data space. 


* LOTUS par-single and par-multi are dedicated queues for MPI and OpenMP parallel codes
* Use `mpirun` to execute MPI parallel codes and to ensure that the MPI communications runs over the private MPI network.
* The OpenMPI library is the only supported MPI library on LOTUS. OpenMPI v3.1.1 and v4.0.0 are provided which are fully MPI3 compliant. 
*  MPI I/O features are fully supported *only* on the LOTUS `/work/scratch-pw` directory as this uses a Panasas fully parallel file system
* Run the MPI code on two cores before scaling up to many cores
* Keep your source code in your home directory which is backed up
* There is a limited number of licences available for Intel compiler, so please do not submit many jobs to compile the same code. 
* Run the MPI code on the same CPU model used to compile the MPI source code.



### Cheat Sheet

1. Login to a JASMIN scientific analysis server 
   * Login to the chosen sci server from a JASMIN login server
   ```
   $ ssh -A <username>@sci<number>.jasmin.ac.uk
   ```
   For example the user `train049` connects to sci4:
   ```
   $ ssh -A train049@sci4.jasmin.ac.uk
   [train049@sci4 ~]$ 
   ```
1. Compile and test a Fortran code interactively on LOTUS 
* tba
   ```
   
   ```
   For example the user `train049` connects to sci4:
1. Prepare a job submission script the parallel MPI code
* scontrol show job jobid   check the Features=intel   Features=ivybridge128G if a specific Intel model is explicitely specified 

### Answers to questions

> 1. Is there a limit on the number of parallel tasks an MPI job can have? 

tba   
> 2. What is the MPI implementation supported on JASMIN?

tba  
> 3. Is it possible to run an MPI binary that was compiled on a different system?

tba  
> 4. What is the difference between an MPI code and a code that uses MPI IO only?

tbc   
> 5. How to find out about the MPI libray that the code was compiled against?

tba 
> 6. What type of storage is suitable for pararallel MPI IO?

tba  
> 7. Can I run a Python script in parallel using MPI4py?

tba 

>
