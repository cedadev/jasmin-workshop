---
title: Exercise 09 - Using Jupyter Notebooks on JASMIN
author: Ag Stephens
---

# Exercise 09: Using Jupyter Notebooks on JASMIN

### Scenario

I want to demonstrate how data in the CEDA Archive can be read, processed and
visualised using the an interactive Jupyter Notebook. The JASMIN Notebook Service:
* provides an interactive programming interface through a web browser
* includes a set of python libraries for data analysis
* can read directly from the CEDA Archive
* can include formatted documentation and visualisations within a Notebook 

Specifically, I want to:
* read some hourly temperature data from the ECMWF ERA5 dataset on a global grid
* calculate the daily maximum and minimum over the time axis (all hours)
* plot the global maps of the daily maximum and minimum variables
* write the outputs to netCDF files on JASMIN
* add some inline annotations

### Objectives
 
After completing this exercise I will be able to:

 * login to the JASMIN Notebook Service
 * create a Jupyter Notebook
 * import modules and run Python code interactively using a notebook
 * create visualisations in a notebook
 * write outputs to the JASMIN file system
 * add inline annotations to a notebook

### JASMIN resources

 * JASMIN account with `jasmin-login` privilege
 * JASMIN Notebook Service: https://notebooks.jasmin.ac.uk
 * Help documentation at: https://help.jasmin.ac.uk/article/4851-jasmin-notebook-service

### Local resources

* Web browser (such as `Firefox`, `Chrome`, `Safari`)

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

 1. Login to the JASMIN Notebook Service in your browser
 2. Create a new Notebook
 3. Import the `xarray` module and load some surface temperature data from 01/01/2005
 4. Review the content of the loaded `Dataset`
 5. Calculate the max and min over all timesteps in the dataset
 6. Plot the daily maximum and minimum
 7. Write the outputs to your JASMIN `$HOME` directory
 8. Add inline documentation

### Questions to test yourself

All too easy? Here are some questions to test your knowledge an understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

 1. How can you add extra software packages to your Notebook?
 2. How can you set up and use an entirely separate `conda` environment in your Notebook?

### Review / alternative approaches / best practice

This exercise demonstrates how to:
 1. Get started with the JASMIN Notebook Service
 2. Import and use software packages in your notebooks
 3. Read and write from/to the JASMIN file system
 4. View the outputs inline
 5. Add annotations inline

Alternative approaches could include:

 1. Using other Notebooks services, for example:
   * Google Colaboratory: https://colab.research.google.com/
   * Binder: https://mybinder.org/

 2. Sharing your code on github:
   * You can view notebooks directly in GitHub
   * Here is an example: https://github.com/cedadev/ceda-notebooks/blob/master/notebooks/data-notebooks/cmip6/cmip6-zarr-jasmin.ipynb

### Cheat Sheet

1. Login to the JASMIN Notebook Service in your browser

   Visit: https://notebooks.jasmin.ac.uk/

   It should look like this:

   ![Launch page](./images/launch_page.png)

2. Create a new Notebook

   On the "Launcher" page, click the "Python 3 + Jaspy" button.

   ![Add notebook](./images/add_notebook.png)

   Right-click on the "Untitled.ipynb" tab at the top of the notebook and rename it to:
   `ex09_notebook.ipynb`

   ![Rename notebook](./images/rename_notebook.png)
   
3. Import the `xarray` module and load some surface temperature data from 01/01/2005

   In the first cell 
   
4. Review the content of the loaded `Dataset`
   
5. Calculate the max and min over all timesteps in the dataset
   
6. Plot the daily maximum and minimum
   
7. Write the outputs to your JASMIN `$HOME` directory
   
8. Add inline documentation

### Answers to questions

> 1. How can you add extra software packages to your Notebook?

See this example notebook to create your own `virtual environment` to install
extra packages into your `$HOME` directory for use in a notebook:

https://github.com/cedadev/ceda-notebooks/blob/master/notebooks/training/virtualenvs-on-jasmin.ipynb

> 2. How can you set up and use an entirely separate `conda` environment in your Notebook?

See this example notebook to create new `conda` environments and make them visible
to the JASMIN Notebook Service when you select a _kernel_:

https://github.com/cedadev/ceda-notebooks/blob/master/notebooks/docs/add_conda_envs.ipynb
