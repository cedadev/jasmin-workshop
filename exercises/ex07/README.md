---
title: Exercise 07 - Building your own python 3 environment
author: Ag Stephens
---

# Exercise 07: Build your own python 3 environment

### Scenario

I need to use a Python 3 environment for my analysis work. I have seen that CEDA has Python 3 available in its `Jaspy` environment but I need a specific package called `fixnc` (fix netCDF files).

### Objectives
 
After completing this exercise I will be able to:

 * create a python environment using the virtual environment package (`venv`)
 * activate/deactivate the virtual environment
 * install packages into the virtual environment 

### JASMIN resources

 * JASMIN account with SSH public key uploaded and `jasmin-login` privilege
 * login servers: `login[1-4].jasmin.ac.uk`
 * sci servers: `sci[1-6].jasmin.ac.uk`
 * help documentation at https://help.jasmin.ac.uk

### Local resources

* SSH client (to login to JASMIN)

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

 1. Your starting point is on a JASMIN `login` server (see [exercise 01](../ex01))
 1. SSH to a scientific analysis server
 1. Activate the Jaspy Python 3 environment with the `module` command
 1. Create a Python 3 virtual environment in your `$HOME` directory
 1. Activate your new virtual environment
 1. Pip install the `fixnc` package from the PyPI remote repository
 1. Test that the package can be imported in a python session
 1. Deactivate the virtual environment and test the import again
 1. Write a setup script (`~/setup-workshop-env.sh`) so that you can activate the virtual environment in a single line each time you log in
 1. Now, whenever you login you can run `source ~/setup-workshop-env.sh` and your own Python 3 virtual environment will be activated

### Questions to test yourself

All too easy? Here are some questions to test your knowledge an understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

 1. Which packages are available in the default `jaspy` environment on JASMIN? Are there any non-Python packages included? Can you find out their versions?
 2. A different approach would be to use `miniconda` to install your own Python environment (independent of `jaspy`). Can you install miniconda in your `$HOME` directory and then create a new Python 3 environment inside it?

### Review / alternative approaches / best practice

This exercise demonstrates how to:
 1. Activate the default Jaspy Python environment on JASMIN.
 1. Create a Python 3 "virtual environment".
 1. Install additional packages into your virtual environment.
 1. Create a setup script for activating your virtual environment when you log in.

Alternative approaches could include:

 1. Share your environment with others:

     If you need to create your own environment it is important to be aware of which file system you are working on:

       * "SOF" (e.g. `/gws/nopw/j0*`, `/gws/pw/j0*`): does not perform well with small files at present.
       * "SSD" (e.g. `$HOME` and `/gws/smf/j0*`): performs much better with small files.

     If you are building an environment for your use only then it makes sense to create it under your `$HOME` directory.

     If you need to share an environment with other JASMIN users you can:
     
       * Request a "small files" Group Workspace (GWS).
       * Install the software environment within the "small files" GWS.

     All users with access to that GWS will then be able to access the environment.
     See: [https://help.jasmin.ac.uk/article/4732-share-software-envs](https://help.jasmin.ac.uk/article/4732-share-software-envs)

 2. Request that your software dependencies are added to the common Python 3 "jaspy" environment on JASMIN:

     See more details at:
        https://help.jasmin.ac.uk/article/4729-jaspy-envs#request-updates

 3. Set up a virtual environment _without_ "system site packages":

     We called the "venv" module with this argument: `--system-site-packages`
     That means that all the packages in the base jaspy Python 3 environment are available in the virtual environment.

     However, you might prefer to only keep the core Python 3 packages. If that is the case then simply remove the `--system-site-packages` flag.

### Cheat Sheet

1. Your starting point is on a JASMIN `login` server (see [exercise 01](../ex01))

1. SSH to a scientific analysis server

        ssh sci5 # Could use sci[123456]

1. Activate the Jaspy Python 3 environment with the `module` command

        module load jaspy

1. Create a Python 3 virtual environment in your `$HOME` directory

        python -m venv ~/my-workshop-venv --system-site-packages

1. Activate the virtual environment

        source ~/my-workshop-venv/bin/activate

1. Pip install the `fixnc` package from the PyPI remote repository

        pip install fixnc

1. Test that the package can be imported in a python session

        python -c 'import fixnc; print(dir(fixnc))'

1. Deactivate the virtual environment and test the import again

        deactivate                 # Deactivates the virtual environment
        python -c 'import fixnc'   # Now fails to import because cannot find "fixnc"
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
        ModuleNotFoundError: No module named 'fixnc'

1. Write a setup script (`~/setup-workshop-env.sh`) so that you can activate the virtual environment in a single line each time you log in

        echo "module load jaspy" > ~/setup-workshop-env.sh
        echo "source ~/my-workshop-venv/bin/activate" >> ~/setup-workshop-env.sh

1. Now, whenever you login you can run `source ~/setup-workshop-env.sh` and your own Python 3 environment will be activated

### Answers to questions

> 1. Which packages are available in the default `jaspy` environment on JASMIN? Are there any non-Python packages included? Can you find out their versions?

The "jaspy" environments are listed on our [jaspy Help page](https://help.jasmin.ac.uk/article/4729-jaspy-envs). You can follow links from there to find out about the different "jaspy" environments and the packages, and versions, they include.

> 2. A different approach would be to use `miniconda` to install your own Python environment (independent of `jaspy`). Can you install miniconda in your `$HOME` directory and then create a new Python 3 environment inside it?

The general workflow for installing `miniconda` is as follows. You will create a `conda` environment by downloading and installing `miniconda` as your package management tool:
  1. Download the [miniconda installer](https://docs.conda.io/en/latest/miniconda.html)
  2. Install miniconda, e.g.: `bash Miniconda3-latest-Linux-x86_64.sh -b -p miniconda`
  3. Create a `conda` environment using the `miniconda` installation, e.g.: `miniconda/bin/conda create -n mypy3 python=3`

See this [explanation of why you might use `miniconda`](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda).

`miniconda` uses `conda` which is a very versatile and powerful tool for managing Python, and other, packages. See the [conda documentation](https://docs.conda.io) for more info.

