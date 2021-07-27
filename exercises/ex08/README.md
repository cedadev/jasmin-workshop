---
title: Exercise 08 - Compiling Fortran or C code on JASMIN
author: Fatima Chami
---

# Exercise 08: Compiling Fortran or C code on JASMIN

### Scenario

This exercise will demonstrate how to compile and test a serial/sequential Fortran code on LOTUS. 

The Fortran code generates two vectors X(n) and Y(n) of n=2**10 elements and then calculates a vector Z(n) as Z(i)= a * X(i) + Y(i). The code outputs the maximum value of the vector elements Z(i),  maxval(abs(Z))

A very important part of this workflow is that there are 2 separate steps:
1. Compilation of code:
   * On a single LOTUS host or on a physical sci machine
   * Run interactively
2. Execution of compiled code as a batch job

There are a limited number of licences available for compilers so please adhere to this 2-step approach.


### Objectives 

After completing this exercise you will:
 * **know** about the compiler available on JASMIN
 * **learn** about the Fortran/C compilers and how to use them 
 * **compile** a serial/sequential code on a LOTUS compute node interactively
 * **become aware** of the differences between SLURM submission options to request resources for an MPI parallel job 
 
 
 ### JASMIN resources

 * Scientific analysis servers: `sci[1-6,8].jasmin.ac.uk`
 * Group workspace: `/gws/pw/j05/workshop`
 * LOTUS batch queues: 'workshop' (short-serial outside the event)
 * Fortran source code is (available in the Github repository): 
 `/gws/pw/j05/workshop/exercises/ex08/src/axpy.f90`
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


1. Login to a physical JASMIN scientific analysis server 
   * Launch two terminal sessions
   * Access a JASMIN login server on each terminal (see exercise 01)
   * Choose a Sci server from `sci[3,6,8]` with the lowest load 
   * Login to the chosen sci server on each terminal
   * Copy the Fortran source code from the exercise directory (shown in the JASMIN resources section) to your current working directory            
   > **_NOTE:_**  One terminal will be used for compiling and testing codes on LOTUS while the second terminal will be used for submitting and monitoring batch jobs. 
1. Compile a Fortran code on physical Sci 

1. Compile a Fortran code interactively on LOTUS 

1. Use the GNU compiler via JASPY environment

1. CPU architecture and optimisation compiler flags

1. Install a software/library and link it to the Fortran code

### Questions to test yourself

All too easy? Here are some questions to test your knowledge and understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

1. Where to compile a Fortran/C code?
1. Is it possible to run a sequential Fortran/C code that was compiled on a different system? 
1. What type of work scratch is suitable for sequential code?
1. How to check that the binary does not use any parallelism?
1. Why my Fortran code is running slow?
1. What are the SLURM partitions to use?

### Review / alternative approaches / best practice

By completing this exercise you will be able to compile and test a serial Fortran code interactively on the sci machine and on LOTUS. You will be able to use compilers provided via the module environment.


* LOTUS short-serial and long-serial are dedicated queues for single core serial jobs
* Keep your source code in your home directory which is backed up
* There is a limited number of licences available for Intel compiler, so please do not submit many jobs to compile the same code. 
* Estimate the memory and runtime required fro the job otherwise the default (1 hour and 8GB) apply
* Group many serial jobs into a single longer job for efficient use of LOTUS/SLURM

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

> 1. What are the SLURM partitions to use?



<!--- how to specify memory, install a software, how to compile and link, compiler specific architecture, when to compile on a sci 8,3,6, Explain what is srun versus sbatch, where is GNU compiler.  partition listing and account listing 




