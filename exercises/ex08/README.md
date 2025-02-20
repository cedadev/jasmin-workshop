---
title: Exercise 08 - Compiling Fortran or C code on JASMIN
author: Fatima Chami
---

# Exercise 08: Compiling Fortran or C code on JASMIN

### Scenario

This exercise will demonstrate how to compile and test a serial Fortran code on JASMIN. 

The Fortran code generates two vectors X(n) and Y(n) of n=2**10 elements and then calculates a vector Z(n) as Z(i)= a - X(i) + Y(i). The code outputs the maximum value of the vector elements Z(i),  maxval(abs(Z))

A very important part of this workflow is that there are 2 separate steps:
1. Compilation of code:

   - On a single LOTUS host or on a physical sci machine
   - Test interactively

2. Execution of compiled code as a batch job

There are a limited number of licences available for compilers so please adhere to this 2-step approach.

### Objectives

After completing this exercise you will:

- **know*- about the Fortran/C compilers available on JASMIN
- **learn*- how to use the compilers 
- **compile*- a serial code on JASMIN and test it interactively
- **become aware*- of the Slurm submission options to request resources for a compiled executable

### JASMIN resources

- Scientific analysis servers: `sci-vm-0[1-6].jasmin.ac.uk`, `sci-ph-0[12].jasmin.ac.uk`
- Group workspace: `/gws/pw/j07/workshop`
- LOTUS batch queues: `workshop` (`short-serial` outside the event)
- Fortran source code is (available in the Github repository):
 `/gws/pw/j07/workshop/exercises/ex08/code/axpySerial.f90`
- Help documentation at https://help.jasmin.ac.uk

### Local resources

- SSH key & passphrase
- Terminal application or NX client
- A valid `jasmin-login` grant associated with your JASMIN account

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

1. Login to a physical JASMIN scientific analysis server
   - Launch two terminal sessions
   - Access a JASMIN login server on each terminal (see exercise 01)
   - Choose one of physical sci servers `sci-ph-0[12]` with the lowest load
   - Login to the chosen sci server on each terminal
   - Copy the Fortran source code from the exercise directory (shown in the JASMIN resources section) to your current working directory
   > **_NOTE:_*-  One terminal will be used for compiling and testing codes on LOTUS while the second terminal will be used for submitting and monitoring batch jobs.
1. Use the Intel compiler to test a Fortran code on a physical sci  `sci-ph-0[12]`
   - List all available Intel compilers `module avail intel/1 intel/2`
   - Load the Intel compiler module environment e.g. `module load intel/20.0.0`
   - Compile the Fortran source code `ifort axpySerial.f90 -o axpySerial_intel.exe`
   - Execute the binary `./axpySerial_intel.exe`
   - Unload the Intel compiler module `module rm intel/20.0.0`
1. Use the GNU compiler via JASPY environment 
   - Be aware `gfortran --version` will point to an old version of GNU compiler on JASMIN
   - Enable the JASPY environment `module load jaspy`
   - Check the GNU compiler available via JASPY `gfortran --version`
   - Compile the Fortran source code `gfortran axpySerial.f90 -o axpySerial_gnu.exe`
   - Execute the binary `./axpySerial_gnu.exe`
1. Compile a Fortran code interactively on LOTUS 
   - Invoke a pseudo-interactive session on LOTUS using the Slurm command `srun --ntasks=1 --partition=workshop --account=workshop  --pty /bin/bash`
   - Note the compute node allocated and the job ID associated
   - Enable a compiler e.g. `module load intel/20.0.0`
   - Compile the Fortran source code `ifort axpySerial.f90 -o axpySerial_intel_hostxxx.exe`
   - Run the executable interactively on LOTUS node `./axpySerial_intel_hostxxx.exe`
   - Exit the interactive session `exit`
1. Prepare a batch job script
   - Use the example job script file provided
   - Specify the memory and the runtime
   - Use the executable generated previously `axpySerial_intel_hostxxx.exe`
   - Submit the job to the Slurm scheduler
   - Monitor and inspect the job standard output/err files
   - Find out the resources used by the job
   - Resubmit the same job to an AMD node after adding the Slurm directive to job script
      `#SBATCH --constraint="amd"`
1. How to use the NetCDF C library and the NetCDF Fortran binding GNU 
   - Enable the JASPY environment `module load jaspy`
   - Compile and link the Fortran example `gfortran -I$CONDA_PREFIX/include simple_xy_wr.f90 -o simple_xy_wr.exe -L$CONDA_PREFIX/lib -lnetcdff -lnetcdf`   (note that the -I option in the first command is capital "eye" for "Include", whereas the -l in the second command is "ell" for "library") 
   > **_NOTE:_*- The ordering of the linker flags is important. Since netcdff uses functions from netcdf, it has to be listed in this order. Otherwise, you will get an undefined symbol error
   - Execute the binary `./simple_xy_wr.exe`

### Questions to test yourself

All too easy? Here are some questions to test your knowledge and understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

1. Is it possible to run a serial Fortran code that was compiled on a different system? 
1. What are the Slurm partitions to use for serial Fortran code?
1. Why my Fortran code is running slow?
1. Can I use GNU compiler available via `module avail gnu`?

### Review / alternative approaches / best practice

By completing this exercise you will be able to compile and test a serial Fortran code interactively on the sci machine and on LOTUS. You will be able to use compilers provided via the module environment.

- LOTUS `short-serial` and `long-serial` are dedicated queues for single core serial jobs
- Keep your source code in your home directory which is backed up
- There is a limited number of licences available for Intel compiler, so please do not submit many jobs to compile the same code.
- Estimate the memory and runtime required for the job otherwise the default (1 hour and 4GB) apply
- Group many short jobs into a single longer job for efficient use of LOTUS/Slurm

### Cheat Sheet

1. Login to a JASMIN scientific analysis server
   - Login to one of the physical sci `sci-ph-0[12]` machines from a JASMIN login server
   ```
   $ ssh -A <username>@sci-ph-01.jasmin.ac.uk
   ```
   For example the user `train049` connects to sci-ph-01:
   ```
   $ ssh -A train049@sci-ph-01.jasmin.ac.uk
   [train049@sci-ph-01 ~]$
   ```
   - Copy the Fortran source code from the exercise directory 
   ```
   sci-ph-01 ~]$ cp /gws/pw/j07/workshop/exercises/ex08/code/axpySerial.f90 .
   ```
 1. Use the Intel compiler on a physical Sci `sci-ph-01`
    - List all available Intel compilers
    ```
     $ module avail intel/1 intel/2
        ---------------------------------- /apps/modulefiles ----------------------------------
        intel/12.1.5 intel/14.0   intel/15.1   intel/17.0   intel/17.0.2
        intel/13.1   intel/15.0   intel/16.1   intel/17.0.1 intel/19.0.0
         ---------------------------------- /apps/modulefiles    ----------------------------------
        intel/20.0.0
    ```
    - Load the Intel compiler module environment 
    ```
     $ module load intel/20.0.0
     $ module list
     Currently Loaded Modulefiles:
     1) intel/cce/20.0.0   2) intel/fce/20.0.0   3) intel/20.0.0
    ```
    - Compile the Fortran source code
    ```
    $ ifort axpySerial.f90 -o axpySerial_intel.exe
    $ ls
     axpySerial.f90 axpySerial_intel.exe
    ```
    - Execute the binary
    ```
    $ ./axpySerial_intel.exe`
      1.31633257373645       0.000000000000000E+000
    ```
    - Unload the Intel compiler module
    ```
    $ module rm intel/20.0.0
    $ module li
    No Modulefiles Currently Loaded.
    ```
1. Use the GNU compiler via JASPY environment
   - Be aware `gfortran --version` will point to an old version of GNU compiler on JASMIN
   ```
   $ gfortran --version
   GNU Fortran (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44)
   ...
   ```
   - Enable the JASPY environment
   ```
   $ module load jaspy
   $ module li
   Currently Loaded Modulefiles:
   1) jaspy/3.7/r20210320
   ```
   - Check the GNU compiler available via JASPY
   ```
   $ gfortran --version
    GNU Fortran (crosstool-NG 1.24.0.133_b0863d8_dirty) 7.5.0
   ```
   - Compile the Fortran source code
   ```
   $ gfortran axpySerial.f90 -o axpySerial_gnu.exe
   ```
   - Execute the binary `./axpySerial_gnu.exe`
   ```
   $ ./axpySerial_gnu.exe
     1.7589903551334058        0.0000000000000000 
   ```
1. Compile a Fortran code interactively on LOTUS
   - On a sci machine e.g. `sci-ph-01`, invoke a pseudo-interactive session on LOTUS using the Slurm command:
   ```
   $ srun  --partition=workshop --account=workshop --pty /bin/bash
   srun: job 64104941 queued and waiting for resources
   srun: job 64104941 has been allocated resources
   cpu-bind=MASK - host173, task  0  0 [19884]: mask 0x4000 set
   ```
   - Note the compute node allocated and the job ID associated which are also shown from running Slurm command `squeue` from a Sci machine:
   ```
   [train049@sci-ph-01.jasmin.ac.uk ~]$ squeue -u train049
    JOBID PARTITION     NAME     USER    ST     TIME  NODES NODELIST(REASON)
    64104941  workshop  bash train049    R      0:21      1 host173
   ```
   - Enable a compiler on LOTUS node
   ```
   [train049@host173 ~]$ module load intel/20.0.0
   ```
   - Compile the Fortran source code `ifort axpySerial.f90 -o axpySerial_intel_hostxxx.exe`
   ```
   [train049@host173 ~]$ ifort axpySerial.f90 -o axpySerial_intel_host173.exe
   ```
   - Run the executable interactively on LOTUS node `./axpySerial_intel_hostxxx.exe`
   ```
   [train049@host173 ~]$ ./axpySerial_intel_hostxxx.exe
      1.05141810870815       0.000000000000000E+000

   ```
   - Exit the interactive session `exit`
   ```
   [train049@host173 ~]$ exit
   exit
   [train049@sci-ph-01.jasmin.ac.uk ~]$

   ```
1. Prepare and submit a Slurm job script
   - Copy the Slurm job submission script provided
   ```
   $ cp  /gws/pw/j07/workshop/exercises/ex08/code/jobscript.sbatch .
   ```
   - Specify the memory and the runtime using
   ```
   #SBATCH --time=05:00
   #SBATCH --mem=100  
   ```
   - Use the executable `axpySerial_intel_hostxxx.exe`
   ```
   ./axpySerial_intel_host118.exe
   ```
   - Submit the job to the scheduler
   ```
   $ sbatch jobscript.sbatch 
   Submitted batch job 64107476
   ```
   - Inspect the job standard output/err files
   ```
   $ cat 64107476.out
   1.37750806547772       0.000000000000000E+000
   $ cat 64107476.err
   cpu-bind=MASK - host225, task  0  0 [9117]: mask 0x1000 set
   ```
   - Find out the resources used by the job
   ```
   $ sacct -j 64107476 --format=Jobname,partition,state,time,elapsed,MaxRss,reqmem,reqcpu
       JobName  Partition      State  Timelimit    Elapsed     MaxRSS     ReqMem  
    ------------ ---------- ---------- ---------- ---------- ---------- ---------- 
        axpy   workshop  COMPLETED   00:05:00   00:00:01                 100Mn      
    64107476.ba+  batch  COMPLETED              00:00:01       948K      100Mn  

   ```
   Note: This is a very short task to be considered as a batch job. It is intended for illustration only.
   - Resubmit the same job to an AMD node after adding the Slurm directive to job script
   ```
   #SBATCH --constraint="amd"
   sbatch: error: Batch job submission failed: Requested node configuration is not available
   ```
   The job submission will fail because there are no AMD nodes allocated to the workshop queue
1. How to use the NetCDF GNU library and link it to the Fortran code
   - Copy the Fortran NetCDF example and enable the JASPY environment
   ```
   $ cp /gws/pw/j07/workshop/exercises/ex08/code/simple_xy_wr.f90 .
   $ module load jaspy
   ```
   - Compile and link the Fortran example 
   ```
   $ gfortran -I$CONDA_PREFIX/include simple_xy_wr.f90 -o simple_xy_wr.exe -L$CONDA_PREFIX/lib -lnetcdff -lnetcdf
   ```
   (note that the -I option in the first command is capital "eye" for "Include", whereas the -l in the second command is "ell" for "library")
   - Execute the binary 
   ```
   $ ./simple_xy_wr.exe
    **- SUCCESS writing example file simple_xy.nc! 
   ```

### Answers to questions

1. Is it possible to run a serial Fortran code that was compiled on a different system?

   Recompiling a code to run on JASMIN is recommended
1. What are the Slurm partitions to use for serial Fortran code?

   `test`, `short-serial` and `long-serial` 
1. Why my Fortran code is running slow? 

This could indicate that the job requires more resources than the allocated resources.
1. Can I use GNU compiler available via `module avail gnu`?

   The GNU compiler available via environment module is not maintained. 





<!--- how to specify memory, install a software, how to compile and link, compiler specific architecture, when to compile on a physical sci.  Explain what is srun versus sbatch, where is GNU compiler.  partition listing and account listing 


<!--- ### Videos
You can follow this exercise by watching the videos below, or by following the text of this article, or a combination of both.
|  |  |
| --- | --- |
#| Task | [![](https://img.youtube.com/vi/_09pMUX6fLQ/mqdefault.jpg )](https://www.youtube.com/watch?v=_09pMUX6fLQ) |
| Solutions & Discussion | coming soon | 

```
$ command prefixed by "$"
output would show here
```
-x<code> where code is AVX 
May generate Intel® AVX, SSE4.2, SSE4.1, SSSE3, SSE3, SSE2 and SSE instructions for Intel® processors. Optimizes for 2nd generation Intel® Core™ i7, i5 and i3 processor families and the Intel® Xeon® Processor E5 and E3 families.

