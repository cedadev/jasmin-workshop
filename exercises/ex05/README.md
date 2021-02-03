---
title: Exercise 05: 
author: Ag Stephens
---


# Exercise 05: 

### Scenario

Having established (in exercise 4) that I can extract the total cloud cover ("TCC") variable from a single ERA-Interim file I now wish to extract that data from an entire month. I will write some simple scripts to batch up separate processes that run CDO to extract the "TCC" variable from a series of ERA-Interim files. Each run of the script will loop through 4 x 6-hourly files for one day. I will run it 30 times, once for each day in September 2018. Each run will be sent to the LOTUS cluster.

### Objectives
 
After competing this exercise I will be able to:

 * **locate data** from the CEDA archive on the JASMIN file system
 * **write a script** to process data in the CEDA archive
 * **submit jobs to the LOTUS cluster**

### JASMIN resources

 * JASMIN account with SSH public key uploaded and `jasmin-login` privilege
 * login servers: `login[1-4].jasmin.ac.uk`
 * sci servers: `sci[1-6].jasmin.ac.uk`
 * common software: CDO (Climate Data Operators) tool
 * GWS (read/write): `/gws/nopw/j04/workshop`
 * CEDA Archive (read-only): requires a CEDA account
 * LOTUS batch processing cluster
 * help documentation at https://help.jasmin.ac.uk

### Local resources

 * Local SSH client and JASMIN credentials.

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

 1. Your starting point is on a JASMIN `login` server (see [exercise 01](../ex01))
 1. SSH to a scientific analysis server
 1. Write an "`extract-era-data.sh`" wrapper script that calls the CDO extraction command
 1. Write a script, called `submit-all.sh`, to loop over dates from **01**/09/2018 to **02**/09/2018 and submit the `extract-era-data.sh` script to LOTUS for each day
 1. Run the `submit-all.sh` script
 1. Examine which jobs are in the queue
 1. Examine the standard output and standard error files
 1. Modify `submit-all.sh` so that it will run for all 30 days in September 2018
 1. Re-run the `submit-all.sh` script
 1. Examine which jobs are in the queue
 1. Cancel one of the jobs - just to see how it is done

### Questions to test yourself

All too easy? Here are some questions to test your knowledge an understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

1. ***...?
1. ***...?

### Review / alternative approaches / best practice

This exercise demonstrates how to:
 * Create a script that takes an argument to process a single component (day) of an overall task. 
 * Create a wrapper script that loops through all the components that need to be processed.
 * Submit each component as a LOTUS job using the `sbatch` command.
 * Define the command-line arguments for the `sbatch` command.
 * Use other LSF commands, such as `squeue` (to monitor progress) and `scancel` (to cancel jobs).

This is a basic workflow suitable for small tasks and setting up your processing. When the amount of processing increases then it makes good sense to move on to using the LOTUS batch cluster.

Alternative appraoches could include:
 * Write the output to a `scratch` directory
   * There are two main scenarios in which you might write the output to a scratch directory:
     1. You only need to store the output file for temporary use (such as intermediate files in your workflow).
     1. You want to write outputs to scratch before moving them to a GWS.
   * The Help page ([https://help.jasmin.ac.uk/article/176-storage#diskmount](https://help.jasmin.ac.uk/article/176-storage#diskmount)) tells us that there are two types of scratch space:
        *   `/work/scratch` – supports parallel writes
        *   `/work/scratch-nompiio` – does NOT support parallel writes
    *   Since we do not need parallel write capability, we can use the "`nompiio`" version.
    *   You need to set up a directory under "`/work/scratch-nompiio"` as your username:

##### 
        MYSCRATCH=/work/scratch-nompiio/$USER


##### 
        mkdir -p $MYSCRATCH

    *   Then you would write output files/directories under your scratch space, e.g.:

##### 
        OUTPUT_FILE=$MYSCRATCH/output.nc


##### 
        ...some_process... > $OUTPUT_FILE

    *   When you have finished with the file, tidy up (good practice).

##### 
        rm $OUTPUT_FILE

    *   Do not leave data on the "scratch" areas when you have finished your workflow.
        *   Please remove any temporary files/directories that you have created.
        *   You cannot rely on the data persisting in the "scratch" areas.


 * Specify the memory requirements for your job
 * Have any files been accidentally left on the system? (E.g. in `/tmp/`)






*   Specify the memory requirements of your job:
    *   If your job has a significant memory footprint:
        *   Run a single iteration on LOTUS and review the standard output file to examine the memory usage.
        *   You can then reserve a memory allocation when you submit your subsequent jobs.
        *   See help pages:

            [https://help.jasmin.ac.uk/article/115-how-to-estimate-job-resources](https://help.jasmin.ac.uk/article/115-how-to-estimate-job-resources)


            [https://help.jasmin.ac.uk/article/112-how-to-allocate-resources#memcontrol](https://help.jasmin.ac.uk/article/112-how-to-allocate-resources#memcontrol)

*   _Have any files been accidentally left on the system? (E.g. in <code>/tmp/</code>)</em>
    *   It is important to clean up any temporary files that you no longer need. 
    *   Please check whether the tools you use have left any files in "<code>/tmp/</code>".


This demonstrates best practice:
 * Build up in stages before running your full workflow on LOTUS
   * This is really good practice!
      1. Check your code - is it _really_ doing what you think it is doing?
      2. Run locally (on a `sci` server) for one iteration.
      3. Run for one or two iterations on LOTUS.
      4. Check everything ran correctly on LOTUS.
      5. Submit your full batch of jobs to LOTUS.

### Cheat Sheet

1. Your starting point is on a JASMIN `login` server (see [exercise 01](../ex01))

2. SSH to a scientific analysis server

  ```
  $ ssh sci5.jasmin.ac.uk # Could use sci[1-6].jasmin.ac.uk
  ```

3. Identify path to the required data file
  * ERA-Interim surface analyses live under:

   ```
   /badc/ecmwf-era-interim/data/gg/as/
   ```

  * Sub-directories under that are: `YYYY/MM/DD/`, locate file for 1st January 2017 at midnight (00:00).
  * Set the input file:

   ```
   $ INPUT_FILE=/badc/ecmwf-era-interim/data/gg/as/2017/01/01/ggas201701010000.nc
   ```

4. Decide on the output file path:

  ```
  $ OUTPUT_FILE=/gws/nopw/j04/workshop/users/$USER/ex04/output.nc
  $ mkdir -p /gws/nopw/j04/workshop/users/$USER/ex04
  ```

5. Activate the environment containing the CDO tool

  ```
  $ module load jaspy
  ```

6. Run the CDO tool to subset the file and extract the `TCC` variable
  * Consult the CDO manual to see how to extract a variable by name:
    https://code.mpimet.mpg.de/projects/cdo/embedded/index.html#x1-1460002.3.3

  * Run CDO:

  ```
  $ cdo selname,TCC $INPUT_FILE $OUTPUT_FILE
  ```

7. Quick-check the contents of the output file with `ncdump` tool

  ```
  $ ncdump -h $OUTPUT_FILE

  netcdf output {
  dimensions:
          longitude = 512 ;
          latitude = 256 ;
          surface = 1 ;
          t = UNLIMITED ; // (1 currently)
  variables:
          float TCC(t, surface, latitude, longitude) ;
                  TCC:standard_name = "cloud_area_fraction" ;
                  TCC:long_name = "Total cloud cover" ;
  ```
