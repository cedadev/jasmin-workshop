---
title: Exercise 10 Data transfers using Globus
author: Matt Pritchard
---

# Exercise 10: Data transfers using Globus

### Scenario

I want to do some data transfers using a method that's convenient, fast and suitable for transferring large amounts of data.

I want it to retry automatically if there are issues, and I want to get a notification when a transfer task completes. I don't want to have to stay connected as I want to close my laptop and go somewhere else once I've set a transfer going.

> [!NOTE]
> IMPORTANT - If you authenticate with your JASMIN account during this exercise, you MUST remember to unlink the training account you have used from your own Globus identity when you've finished. See step 23.

### Objectives

After completing this exercise I will be able to:

* Log into Globus and discover available collecitons.
* Transfer simple files between Globus tutorial collections using the web interface
* Access Globus collections on JASMIN and transfer data between different file systems.
* Use the Globus command-line interface (CLI) to access a collection
* Find out how Globus can be used, for data transfers and other tasks.

### JASMIN resources

* Account with valid `jasmin-login` access role
   * If you are using one of the training accounts this will have been set up for you
* JASMIN Globus Service (you'll learn how to access this)
* Home directory: `/home/users/<username>` (replace with the your username of your training account)
* `workshop` group workspace at `/gws/pw/j07/workshop`

### Local resources

* Web browser
* Terminal environment with Python (only needed for CLI task)

### Instructions

1. Navigate to https://app.globus.org and create yourself a Globus identity using either the drop-down list of institutions or one of the suggested alternative identity providers. If you have one already, feel free to use that.
1. In the Globus [File Manager](https://app.globus.org/file-manager) (click icon in left menu bar of Globus interface), search for **"Globus Tutorial Collection 1"**. It should have a green tick confirming its verified status. If you click its name in the search results, it will open that collection in File Manager. Or to view its details first, you can click the 3 vertical dots to see "collection details" and verify the collection's unique ID `6c54cade-bde5-45c1-bdea-f4bd71dba2cc`. From that view, click the "Open in File Manager" button, top-right.
1. In the same interface, make sure you have 2-pane view (middle option in selector, top-right, same line as "File Manager" title). In the second pane, repeat the above process to find **"Globus Tutorial Collection 2"**.
1. In the pane with Globus Tutorial Collection 1, you should see your auto-generated home directory, with a path like `/home/u_jgg6svmke5gcxnlyymlopdfebu/`. This should be empty to start with.
1. In the pane with Globus Tutorial Collection 2, navigate instead to `/home/share/godata`. You can either type the path and hit return, or use the navigation tools in the window below. You should see 3 simple files listed: `file1.txt, file2.txt, file3.txt`
1. Select one or more of the files. **Before** you click `Start`, look at the options in the drop-down "Transfer and timer options" (centre, between the 2 panes). Leave them as they are for now, but note the extra functionality they provide.
1. Cick `Start` to initiate the transfer. You should see a green confirmation box telling you that the task was submitted.
1. As these are small files, the task should complete quicky, but you can check on progress of a transfer with the "Activity" button in the left menu bar. This lists all your current & recent transfers. Click on the most recent one to see details.
1. Close the "Globus Tutorial Collection 2" by clicking the cross-in-circle icon to "close this collection".
1. Search for "JASMIN Default Collection". Either click its name to open it, or inspect its details before and select "Open in File Manager".
1. Since this is a new collection for you, there will be a series of steps to consent & authenticate with the new collection. You will need the username and password of your JASMIN training account. **IMPORTANT: If you do this, please remember to unlink at the end, see Step 23.**
1. Once the process has successfully linked your Globus identity with your JASMIN identity (there are several steps the first time: please be patient), you should see a listing of your training account home directory (which might be empty), but the path should be `/home/users/<username>`.
1. Do the same in the other pane, so that you have both connected to "JASMIN Default Collection". You should not need to go through all the steps this time.
1. In that pane (where you have also now accessed JASMIN Default Collection), navigate to `/gws/pw/j07/workshop/users/` and then the directory corresponding to your training account username, that you created in earlier exercises.
1. Try copying a file or multiple files between your training account home directory and your `/gws/pw/j07/workshop/users/<username>` directory.
1. Delete the files your just copied, either by right-clicking in the web interface on the file name, or by selecting it then "Delete selected" in the central menu.
1. In your terminal environment, create and activate a virtual environment to use the Globus CLI tools:
  ```bash
  python3 -m venv ./globus-cli-venv
  ```
18. Install the Globus CLI tools
  ```bash
  pip install globus-cli
  ```
19. Login to Globus using your Globus identity, the one you created in step 1. Follow the instructions in the terminal: you may need to copy an authorization code from your web browser.
  ```bash
  globus login
  ```
20. Try accessing one of the Globus tutorial collections. We'll set an environment variable to hold the unique ID of the collection, then use it in a `globus ls` command:
  ```bash
  export c1=6c54cade-bde5-45c1-bdea-f4bd71dba2cc
  globus ls $c1
  ```
You may need to complete the authorization / consent steps at this stage. Once done, try the above command again.

You should see a listing of the home directory you have on that collection. It might be empty, so try listing the 3 files we found at `/home/share/godata`:
  ```bash
  globus ls $c1:/home/share/godata
  ```
21. Repeat for the Globus tutorial collection 2 (more consent steps needed!)
22. Copy a file from collection 2 to collection 1, but first make sure that it doesn't already exist in 1 (delete it if so):
  ```bash
  globus rm $c1:file1.txt
  globus transfer $c2:/home/share/godata/file1.txt  $c1:file1.txt
  ```
You should see a transfer task ID each time a transfer task is submitted. You can view the details of that task with:
  ```bash
  globus task show <taskID> # replace with the UUID of the task
  ```
It should tell you whether the task is started, completed, or has some other status.

23. **IMPORTANT unlink the training account from your Globus identity**

> [!NOTE]
> ** DO NOT FORGET TO DO THIS if you are using a training account **

**UNLINK** your training account identity from your Globus identity.
  - Go to the globus web interface
  - Go to Settings (bottom of left menu bar)
  - Go to Manage Identities (top right)
  - Click the "unlink" icon to "unlink this identity"

### Review

This exercise demonstrates how to use Globus to:

* Copy small files such between the Globus tutorial endpoints.
  * These are "easy" ones, because although they require consent (to use the Globus service to access the data), they don't require authentication.
* Access the JASMIN Default Collection using Globus
  * This requires the extra step of linking your Globus identity with your JASMIN one, so that you can use Globus to do actions on JASMIN with the permissions of your JASMIN account.
* Copy data between locations on JASMIN
  * Globus is particularly good at copying large, recursive directory structures efficiently, so is a good option if you need to move data from your home directory, or scratch storage, to a GWS that you belong to (or vice versa).
  * For copying data into JASMIN from other places, you either need:
    * That other place to operate a Globus endpoint. An increasing number of research institutions and digital research infrastructures do.
    * To download and install "Globus Connect Personal" which makes your local machine (laptop, desktop) into a special type of Globus collection. You can then transfer data between it and another collection like the JASMIN one.

We have looked at the basic functionality of using Globus to transfer data. There's lots more it can do.

[Further examples in the JASMIN help docs](https://help.jasmin.ac.uk/docs/data-transfer/globus-command-line-interface/#examples) also show how to transfer some larger datasets, for example those available from the ESnet’s Anonymous read-only test Data Transfer Nodes (used for performance testing). Like the Globus Tutorial Collecitons, these are also public, so are easy to use here, but may only be available if you are connected via a Research or Education provider's network.

You may also wish to explore the Demo Jupyter Notebooks published by Globus, which highlight some of the other service functionality (not all of which is available on JASMIN).

See also:

- Full details of commands available in the [Globus command-line interface](https://docs.globus.org/cli/reference/)

> [!NOTE]
> IMPORTANT - Another reminder to unlink the training account you have used from your own Globus identity. See step 23.
