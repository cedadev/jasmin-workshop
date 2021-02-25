---
title: Exercise 05 - Batch computing - running a script on LOTUS  
author: Ag Stephens
---


# Exercise 05: Batch computing - running a script on LOTUS 

### Scenario

Having established (in exercise 4) that I can extract the total cloud cover (`TCC`) variable from a single ERA-Interim file I now wish to extract that data from an entire month. I will write some simple scripts to batch up separate processes that run CDO to extract the `TCC` variable from a series of ERA-Interim files. Each run of the script will loop through 4 x 6-hourly files for one day. I will run it 30 times, once for each day in September 2018. Each run will be submitted to the LOTUS cluster.

### Objectives
 
After completing this exercise I will be able to:

* **write** scripts to batch up tasks
* **submit** scripts to the LOTUS cluster 

### JASMIN resources

* LOTUS batch processing cluster
* Space to store the output file: `/gws/nopw/j04/workshop/users/$USER/ex05`
* Access to the CDO (Climate Data Operators) tool
* Read-access to the ERA-Interim data set in the CEDA archive - requires a CEDA account

### Local resources

* SSH client (to login to JASMIN)

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

 1. Your starting point is on a JASMIN `login` server (see [exercise 01](../ex01))
 1. SSH to a scientific analysis server
 1. Write an "`extract-era-data.sh`" wrapper script that calls the CDO extraction command
 1. Write a script, called "`submit-all.sh`", to loop over dates from **01**/09/2018 to **02**/09/2018 and submit the "`extract-era-data.sh`" script to LOTUS for each day
 1. Run the "`submit-all.sh`" script
 1. Examine which jobs are in the queue
 1. Examine the standard output and standard error files
 1. Modify "`submit-all.sh`" so that it will run for all 30 days in September 2018
 1. Re-run the "`submit-all.sh`" script
 1. Examine which jobs are in the queue
 1. Kill one of the jobs - just to see how it is done

### Questions to test yourself

All too easy? Here are some questions to test your knowledge an understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

 1. You have learnt about some basic commands to interact with SLURM scheduler (such as `sbatch` and `squeue`). This manages the submission and execution of jobs via the LOTUS queues. Which other commands might be useful when interacting with the scheduler? 
 1. Which queues are available on LOTUS? What is the difference between them? Why would you choose one over another?
 1. How can you instruct SLURM to allocate CPUs and memory to specific jobs when you run them? Can you change the allocations when the job is queuing? 

### Review / alternative approaches / best practice

This exercise demonstrates how to:
 1. Create a script that takes an argument to process a single component (day) of an overall task. 
 1. Create a wrapper script that loops through all the components that need to be processed.
 1. Submit each component as a LOTUS job using the `sbatch` command.
 1. Define the command-line arguments for the `sbatch` command.
 1. Use other LSF commands, such as `squeue` (to monitor progress) and `scancel` (to cancel jobs).

This is a basic workflow suitable for small tasks and setting up your processing. When the amount of processing increases then it makes good sense to move on to using the LOTUS batch cluster.

Alternative approaches could include:
1. Write the output to a `scratch` directory
    1. There are two main scenarios in which you might write the output to a scratch directory:
        1. You only need to store the output file for temporary use (such as intermediate files in your workflow).
        1. You want to write outputs to scratch before moving them to a GWS.
    1. The Help page ([https://help.jasmin.ac.uk/article/176-storage#diskmount](https://help.jasmin.ac.uk/article/176-storage#diskmount)) tells us that there are two types of scratch space:
        1.   `/work/scratch` – supports parallel writes
        1.   `/work/scratch-nompiio` – does NOT support parallel writes
    1.   Since we do not need parallel write capability, we can use the "`nompiio`" version.
    1.   You need to set up a directory under "`/work/scratch-nompiio"` as your username:
 
            MYSCRATCH=/work/scratch-nompiio/$USER
            mkdir -p $MYSCRATCH
 
    1.   Then you would write output files/directories under your scratch space, e.g.:

            OUTPUT_FILE=$MYSCRATCH/output.nc
            ...some_process... > $OUTPUT_FILE

    1.   When you have finished with the file, tidy up (good practice).

            rm $OUTPUT_FILE

    1.   Do not leave data on the "scratch" areas when you have finished your workflow.
        1.   Please remove any temporary files/directories that you have created.
        1.   You cannot rely on the data persisting in the "scratch" areas.

*   Specify the memory requirements of your job:
    1.   If your job has a significant memory footprint:
        1.   Run a single iteration on LOTUS and review the standard output file to examine the memory usage.
        1.   You can then reserve a memory allocation when you submit your subsequent jobs.
        1.   See help pages:

            [https://help.jasmin.ac.uk/article/115-how-to-estimate-job-resources](https://help.jasmin.ac.uk/article/115-how-to-estimate-job-resources)

            [https://help.jasmin.ac.uk/article/112-how-to-allocate-resources#memcontrol](https://help.jasmin.ac.uk/article/112-how-to-allocate-resources#memcontrol)


This demonstrates best practice:
1. Build up in stages before running your full workflow on LOTUS
    1. Check your code - is it _really_ doing what you think it is doing?
    1. Run locally (on a `sci` server) for one iteration.
    1. Run for one or two iterations on LOTUS.
    1. Check everything ran correctly on LOTUS.
    1. Submit your full batch of jobs to LOTUS.

1.  _Have any files been accidentally left on the system? (E.g. in `/tmp/`)_
    1.   It is important to clean up any temporary files that you no longer need. 
    1.   Please check whether the tools you use have left any files in "`/tmp/`".

### Cheat Sheet

1. Your starting point is on a JASMIN `login` server (see [exercise 01](../ex01))

1. SSH to a scientific analysis server

        ssh jasmin-sci5 # Could use sci[123456]

1. Write an "`extract-era-data.sh`" wrapper script that calls the CDO extraction command, that:
    1. Takes a date string ("`YYYYMMDD`") as a command-line argument
    1. Locates the 4 x 6-hourly input file paths for the date provided
    1. Activates environment containing the CDO tool
    1. For each 6-hourly file:
        1. Defines the output file path
        1. Run the CDO tool to extract the "TCC" variable from the input file to the output file
    1. If you are stuck, you can use the script located at:

        `/gws/nopw/j04/workshop/exercises/ex05/code/extract-era-data.sh`

        [ Source: [https://github.com/cedadev/jasmin-workshop/blob/master/exercises/ex05/code/extract-era-data.sh](https://github.com/cedadev/jasmin-workshop/blob/master/exercises/ex05/code/extract-era-data.sh) ]

1. Write a script, called "`submit-all.sh`", to loop over dates from 01/09/2018 to 02/09/2018 and submit the "`extract-era-data.sh`" script to LOTUS for each day:

    1. You should define the following LOTUS directives:
        1. Standard output file - please ensure this is unique to each job by including the "`%j`" variable in the file name.
        1. Standard error file - please ensure this is unique to each job by including the "`%j`" variable in the file name.
    1. Queue name:
        1. We will use the main queue for quick serial jobs: "`short-serial`"
    1. Job duration - to allocate a maximum run-time to the job, e.g.: "`00:05`" (5 mins)
    1. Estimated duration - to hint the actual run-time of the job, e.g.: "`00:01`" (1 min)
        1. Setting a low estimate will increase the likelihood of the job being scheduled to run quickly.

    1. The Help page on submitting LOTUS jobs is here:
        [https://help.jasmin.ac.uk/article/4890-how-to-submit-a-job-to-slurm](https://help.jasmin.ac.uk/article/4890-how-to-submit-a-job-to-slurm)

    1. And use the "`sbatch`" command to submit each job.

    1. If you need some advice you can use the script at:

        `/gws/nopw/j04/workshop/exercises/ex05/code/submit-all.sh`

        [ Source: [https://github.com/cedadev/jasmin-workshop/blob/master/exercises/ex05/code/submit-all.sh](https://github.com/cedadev/jasmin-workshop/blob/master/exercises/ex05/code/submit-all.sh) ]

1. Run the "`submit-all.sh`" script

1. Examine which jobs are in the queue
    1. Type "`squeue`" to review any running jobs.

1. Examine the standard output and standard error files.

1. If you are happy that the job is doing the right thing, now modify "`submit-all.sh`" so that it will run for all 30 days in September 2018.

1. Re-run the "`submit-all.sh`" script.

1. Examine which jobs are in the queue

1. Kill one of the jobs whilst it is still running - just to see how it is done:
    1. Use the "`scancel`" command:

            scancel <job_id>
