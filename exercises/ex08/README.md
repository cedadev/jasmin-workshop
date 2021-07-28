---
title: Exercise 08 - Compiling Fortran or C code on JASMIN
author: Fatima Chami
---

# Exercise 08: Compiling Fortran or C code on JASMIN

### Scenario

This exercise will demonstrate how to compile and test a serial Fortran code on JASMIN. 

The Fortran code generates two vectors X(n) and Y(n) of n=2**10 elements and then calculates a vector Z(n) as Z(i)= a * X(i) + Y(i). The code outputs the maximum value of the vector elements Z(i),  maxval(abs(Z))

A very important part of this workflow is that there are 2 separate steps:
1. Compilation of code:
   * On a single LOTUS host or on a physical sci machine
   * Test interactively
2. Execution of compiled code as a batch job

There are a limited number of licences available for compilers so please adhere to this 2-step approach.

### Objectives 

After completing this exercise you will:
 * **know** about the Fortran/C compilers available on JASMIN
 * **learn** how to use the compilers 
 * **compile** a serial code on JASMIN and test it interactively
 * **become aware** of the SLURM submission options to request resources for a compiled code
 
 ### JASMIN resources

 * Scientific analysis servers: `sci[1-6,8].jasmin.ac.uk`
 * Group workspace: `/gws/pw/j05/workshop`
 * LOTUS batch queues: 'workshop' (`short-serial` outside the event)
 * Fortran source code is (available in the Github repository): 
 `/gws/pw/j05/workshop/exercises/ex08/src/axpySerial.f90`
 * Help documentation at https://help.jasmin.ac.uk

### Local resources

 * SSH key & passphrase 
 * Terminal application or NX client
 * A valid `jasmin-login` grant associated with your JASMIN account 


### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.


1. Login to a physical JASMIN scientific analysis server 
   * Launch two terminal sessions
   * Access a JASMIN login server on each terminal (see exercise 01)
   * Choose one of physical Sci servers `sci[3,6,8]` with the lowest load 
   * Login to the chosen sci server on each terminal
   * Copy the Fortran source code from the exercise directory (shown in the JASMIN resources section) to your current working directory            
   > **_NOTE:_**  One terminal will be used for compiling and testing codes on LOTUS while the second terminal will be used for submitting and monitoring batch jobs. 
1. Use the Intel compiler to test a Fortran code on a physical Sci  `sci[3,6,8]` 
   * List all available Intel compilers `module av intel/1 intel/2`
   * Load the Intel compiler module environment e.g. `module load intel/20.0.0`
   * Compile the Fortran source code `ifort axpySerial.f90 -o axpySerial_intel.exe`
   * Execute the binary `./axpySerial_intel.exe`
   * Unload the Intel compiler module `module rm intel/20.0.0`
1. Use the GNU compiler via JASPY environment 
   * Be aware `gfortran --version` will point to an old version of GNU compiler on JASMIN
   * Enable the JASPY environment `module load jaspy`
   * Check the GNU compiler available via JASPY `gfortran --version`
   * Compile the Fortran source code `gfortran axpySerial.f90 -o axpySerial_gnu.exe`
   * Execute the binary `./axpySerial_gnu.exe`
1. Compile a Fortran code interactively on LOTUS 
   * Invoke a pseudo-interactive session on LOTUS using the SLURM command `srun --ntasks=1 --partition=workshop --account=workshop  --pty /bin/bash`
   * Note the compute node allocated and the job ID associated 
   * Enable a compiler e.g. `module load intel/20.0.0`
   * Compile the Fortran source code `ifort axpySerial.f90 -o axpySerial_intel_hostxxx.exe`
   * Run the executable interactively on LOTUS node `./axpySerial_intel_hostxxx.exe`
   * Exit the interactive session `exit`
1. Prepare a batch job script 
   * Use the example job script file provided
   * Specify the memory and the runtime 
   * Use the executable `axpySerial_intel_hostxxx.exe`
   * Submit the job to LOTUS 
   * Monitor and inspect the job standard output/err files
1. CPU architecture targeted code to be aware
   * Login to the Intel Sci machine `sci8`
   * Load the Intel compiler module environment e.g. `module load intel/20.0.0`
   * Compile the code for Intel CPU `ifort -Aavx  axpySerial.f90 -o axpySerial_intel_avx.exe`
   * Execute the binary `./axpySerial_intel_avx.exe`
   * Logout from `sci8` and then login to `sci3` or `sci6`
   * Execute the binary `./axpySerial_intel_avx.exe`
   * Did the execution fail?
1. How to use the NetCDF GNU library and link it to the Fortran code
   * Enable the JASPY environment `module load jaspy`
   * Compile and link the Fortran example `gfortran -I$CONDA_PREFIX/include simple_xy_wr.f90 -o simple_xy_wr.exe -L$CONDA_PREFIX/lib -lnetcdff -lnetcdf`   (note that the -I option in the first command is capital "eye" for "Include", whereas the -l in the second command is "ell" for "library")
   * Execute the binary `./simple_xy_wr.exe`

### Questions to test yourself

All too easy? Here are some questions to test your knowledge and understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

1. Where to compile a serial Fortran/C code?
1. Is it possible to run a serial Fortran/C code that was compiled on a different system? 
1. What type of work scratch is suitable for serial code?
1. Can I use GNU compiler available via `module av gnu`?
1. How to check that the binary does not use any parallelism?
1. Why my Fortran code is running slow?
1. What are the SLURM partitions to use for serial Fortran code?

### Review / alternative approaches / best practice

By completing this exercise you will be able to compile and test a serial Fortran code interactively on the sci machine and on LOTUS. You will be able to use compilers provided via the module environment.

* LOTUS short-serial and long-serial are dedicated queues for single core serial jobs
* Keep your source code in your home directory which is backed up
* There is a limited number of licences available for Intel compiler, so please do not submit many jobs to compile the same code. 
* Estimate the memory and runtime required for the job otherwise the default (1 hour and 8GB) apply
* Group many short jobs into a single longer job for efficient use of LOTUS/SLURM 

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



### Answers to questions

> 1. Is there a limit on the number of parallel tasks an MPI job can have? 

tba  

> 1. Where to compile a Fortran/C code?

tba

> 1. Is it possible to run a sequential Fortran/C code that was compiled on a different system? 

> 1. What type of work scratch is suitable for sequential code?

> 1. How to check that the binary does not use any parallelism?

> 1. Why my Fortran code is running slow?

> 1. What are the SLURM partitions to use for serial compiled code?



<!--- how to specify memory, install a software, how to compile and link, compiler specific architecture, when to compile on a sci 8,3,6, Explain what is srun versus sbatch, where is GNU compiler.  partition listing and account listing 


<!--- ### Videos
You can follow this exercise by watching the videos below, or by following the text of this article, or a combination of both.
|  |  |
| --- | --- |
#| Task | [![](https://img.youtube.com/vi/_09pMUX6fLQ/mqdefault.jpg )](https://www.youtube.com/watch?v=_09pMUX6fLQ) |
| Solutions & Discussion | coming soon | 

