# Exercise 2 

Interactive computing using a sci server

### Scenario

I need to do a random sampling of my dataset to estimate the distribution of sample mean. I need to use the random number generator function available in the numpy library in Python. I need to test this function by running a standalone Python script on the scientific analysis servers prior to running the statistical analysis script.

### Objectives 

After competing this exercise I will be able to:
* **execute** a computing task on the sci machine from a command line
 * **monitor** CPU and memory resources usage of my computing task
 * **understand** the modules environemnt e.g. JASPY and software on JASMIN
 * **learn** about the capabilities and limitations of the scientific analysis servers
 
 ### JASMIN resources

 * Scientific analysis servers: `sci[1-6].jasmin.ac.uk`
 * Group workspace: `/gws/pw/j05/workshop`
 * A Python example script is provided: 
 `/gws/pw/j05/workshop/exercises/ex02/src/random-number-gen.py`

### Local resources

 * SSH key & passphrase 
 * Terminal application or NX client
 * A valid `jasmin-login` grant associated with your JASMIN account 
 

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

1. Login to a JASMIN scientific analysis server 
   * Launch two terminal sessions
   * Access a JASMIN login server on each terminal (see exercise 01)
   * Choose a Sci server with the lowest load 
   * Login to the chosen sci server on each terminal
 > **_NOTE:_**  The purpose of having two SSH terminal sessions running on the same sci server is to facilitate compute and monitoring. One terminal is for executing commands on the sci while the second terminal is for monitoring user processes (or editing a script)
1. Execute the Python example script on the sci 
   * Copy the Python example script (shown in the JASMIN resources section) to your current working directory 
   * Enable a Python environemnt via the module `jaspy` by executing  the command `module add jaspy`
   * Execute the command `python random-number-gen.py` 
   * Check the process ID (pid), state, memory and CPU usage on the monitoring terminal
   * How many random numbers did the `random-number-gen.py` generate?
1. Monitor your processes on the sci server
   * Execute the Linux command `top -u <username>` 
   * Which process is running?
   * How many users are sharing the sci server?
   * Sort all processes per CPU usage Execute `top` 
   * To exit the monitoring tool `top` press the keyboard letter `q` 
1. Make changes to the Python example and re-execute it
   * Open the Python script file in a text editor e.g. vim, emacs
   * Decrease the size of the random numbers from 1024 to 500
   * Save the file and exit the text editor
1. Compare the compute resources to generate the set 1024 and 500 random number 
   * Execute `python random-number-gen.py`
   * Monitor and note the memory and CPU usage 
   * What can you conclude?
1. Logout from the sci server to end your SSH session on JASMIN 


### Questions to test yourself

All too easy? Here are some questions to test your knowledge an understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

1. Is there a limit on the number of processes running on the sci server at any given time per a user?
1. What software is available via module environment?
1. What text editor are available on JASMIN?

### Review / alternative approaches / best practice

You will be able to run a Python script on the scientific analysis servers. You will be able to monitor the resources used by your script on the scientific analysis servers. You can scale up by using the high-memory scientific sci[3,6].jasmin.ac.uk server for a large set of random numbers

* Do not run processes with execution time over two hours
* Do not use `/tmp` on the scientific servers and transfer servers. Using /tmp can cause the scientific analysis server to crash, resulting in loss of work. Set the environment variable TMPDIR to a temporary directory under a GWS area- `export TMPDIR=/GWS-path/<your_project>/<your_username>/tmp`
* Do not generate huge numbers of files (>1000) in a single directory
* Do not run data transfer processes on the scientific analysis servers. Please use `xfer[1,2].jasmin.ac.uk` (Except when moving data from `/work/scratch-pw` to a GWS because `/work/scratch-pw` is not mounted on the `xfer` servers)

* Do not run parallel applications e.g. MPI or OpenMP, high threaded codes on the scientific analysis servers 
* Limit the number of threads when testing a multithreaded code on scientific analysis servers
* Use the high memory scientific analysis servers `sci[3,6,8].jasmin.ac.uk` for testing high memory and/or multithreaded code (sci3 (48 CPUs, 1000GB RAM), sci8 (24 CPUs, 384GB RAM))
* Many instances of e.g. Ipython or IDL  can impact the performance of the scientific servers. Please note that for IDL, we have a large pool of run-time licences and a much more limited pool of development licences.
* It is necessary to consider moving a processing task to the batch system LOTUS when the resources demand is high.  


https://help.jasmin.ac.uk/article/121-sci-servers 
https://help.jasmin.ac.uk/article/176-storage   

### Cheat Sheet


1. Login to a JASMIN scientific analysis server
   * Login to the chosen sci server from a JASMIN login server
   ```
   $ ssh -A sci<number>.jasmin.ac.uk
   ```
1. Execute the Python example script on the sci 
   * Copy the Python example script (shown in the JASMIN resources section) to your current working directory 
   ```
   $ cp /gws/pw/j05/workshop/exercises/ex02/src/random-number-gen.py .
   ```
   * Enable a Python environemnt via the module `jaspy` by executing  the command `module add jaspy`
   ```
   $ module add jaspy
   ```
   * Execute the Python script `python random-number-gen.py` 
   ```
   $ python random-number-gen.py
   1024  ======>>> random numbers
   I am sleeping for 40 seconds so you can check the resources usage   
   ```
   * Check the process ID (pid), state, memory and CPU usage on the monitoring terminal

   * How many random numbers did the `random-number-gen.py` generate?
   ```
   1024  ======>>> random numbers
   ```
1. Monitor your processes on the sci server
   * Execute the Linux command `top -u <username>` 
   ```
   $ top -u <username>
    output a table   
   ```
   * Which process is running?
   The Python process and the monitoring utility `top`
   * How many users are sharing the sci server?
   * Sort all processes per CPU usage Execute `top` 
   * To exit the monitoring tool `top` press the keyboard letter `q` 


