---
title: Exercise 04 - Extract a variable from a file in the ERA-Interim dataset
author: Ag Stephens
---


# Exercise 04: Extract a variable from a file in the ERA-Interim dataset

### Scenario

I am working on a project studying global cloud cover. I am looking at a case study and I have identified that the ERA-Interim data set is an appropriate source for my data. It is held on disk in the CEDA archive (located on JASMIN). Extract the total cloud cover ("TCC") variable for 1st January 2017 at midnight (00:00), from the ERA-Interim data set. The data files contain a large set of variables so I want to use the Climate Data Operators (CDO) tool in order to extract only the "TCC" variable.

### Objectives
 
After completing this exercise I will be able to:

 * **locate data** from the CEDA archive on the JASMIN file system
 * **run a command-line tool** to extract data from the CEDA archive
 * **write** an output file to a JASMIN GWS

### JASMIN resources

 * JASMIN account with SSH public key uploaded and `jasmin-login` privilege
 * login servers: `login[1-4].jasmin.ac.uk`
 * sci servers: `sci[1-6].jasmin.ac.uk`
 * common software: CDO (Climate Data Operators) tool
 * GWS (read/write): `/gws/nopw/j04/workshop`
 * CEDA Archive (read-only): requires a CEDA account
 * help documentation at https://help.jasmin.ac.uk

### Local resources

 * Local SSH client and JASMIN credentials

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

 1. Your starting point is on a JASMIN `login` server (see [exercise 01](../ex01))
 1. SSH to a scientific analysis server
 1. Identify the path to the required data file
 1. Decide on the output file path
 1. Activate the environment containing the CDO tool
 1. Run the CDO tool to subset the file and extract the `TCC` variable
 1. Quick-check the contents of the output file with `ncdump` tool

### Questions to test yourself

All too easy? Here are some questions to test your knowledge an understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

 1. Where can you find out more about the software environments available on JASMIN? 
 2. Can you find out which other packages are available within the "jaspy" environment? 

### Review / alternative approaches / best practice

This exercise demonstrates how to:
 * Login to JASMIN and access the scientific analysis servers (`sci[1-6].jasmin.ac.uk`)
 * Run a command-line tool interactively to read data from the CEDA archive
 * Write outputs to a JASMIN Group Workspace

This is a basic workflow suitable for small tasks and setting up your processing. When the amount of processing increases then it makes good sense to move on to using the LOTUS batch cluster.

Alternative approaches could include:
 * Use the CEDA OpenDap server to extract the variable.
 * Use other tools to run the extraction.
 * Run as a batch job on LOTUS

Best practice considerations:
 * Have any files been accidentally left on the system? (E.g. in `/tmp/`)

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
    https://code.mpimet.mpg.de/projects/cdo/embedded/index.html#x1-1460002.3

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

### Answers to questions

> 1. Where can you find out more about the software environments available on JASMIN?

The JASMIN Help pages include an article about [software on JASMIN](https://help.jasmin.ac.uk/article/273-software-on-jasmin#common-software). This includes links to details of the "jaspy" and other software environments. 

> 2. Can you find out which other packages are available within the "jaspy" environment?

The "jaspy" environments are listed on our [jaspy Help page](https://help.jasmin.ac.uk/article/4729-jaspy-envs). You can follow links from there to find out about the different "jaspy" environments and the packages, and versions, they include.


