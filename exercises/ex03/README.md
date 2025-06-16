---
title: Exercise 3 Transferring and sharing data
author: Matt Pritchard
---

# Exercise 3: Transferring and sharing data

### Scenario

I want to copy some code from my own machine to my home directory on JASMIN. I also want to copy some data to a Group Workspace on JASMIN so that I can share it with colleagues. My colleagues and I all belong to the `workshop` Group Workspace.

### Objectives

After completing this exercise I will be able to:

* Copy a small text file from my local machine to my JASMIN home directory using a transfer server.
* Copy a directory tree of data files recursively from my local machine to the `workshop` group workspace.
* Understand permissions and ownership needed for group access.
* Be aware of the limitations of some transfers methods.

### JASMIN resources

* Account with valid `jasmin-login` access role
   * If you are using one of the training accounts this will have been set up for you
* Transfer server: `xfer-vm-01.jasmin.ac.uk`
* Home directory: `/home/users/train050` (replace with your username)
* `workshop` group workspace at `/gws/pw/j07/workshop`

### Local resources

*  Local machine set up as per [exercise 0](../ex00), with:
    * SSH client application (use a command-line client for this exercise: you won't need the graphical desktop)
    * SSH key and JASMIN credentials
    * suitable network connection
*  Directory on your local machine: `/Users/fredbloggs/` (choose your own)

### Instructions

1. Make a simple text file on your local machine
1. Copy it to your home directory on a jasmin transfer server
1. Make a directory on your local machine and create a few simple files in it (representing some data that you want to share). This is the **source** directory.
1. Make a **destination** directory for yourself within the `workshop` group workspace
1. Copy the the source directory and its contents to the destination directory using the transfer server
1. Check that the ownership and permissions on your directory within the group workspace allow reading, and, if you choose, writing, by other members.

### Review

This exercise demonstrates how to use a transfer server to:

* Copy small files such as source code/scripts to your home directory
* Copy data to a group workspace
* Check permissions on the data to make sure it’s visible by collaborators

We have looked at some basic methods suitable for small datasets or where speed is not critical. For larger data transfers or over longer distances (international/intercontinental), it is recommended to consider other available options which could be more efficient, depending on source & destination. Consult the [documentation here](https://help.jasmin.ac.uk/article/219-data-transfer-overview).

### Alternative approaches and best practice

* In addition to `scp`, alternative tools `sftp` and `rsync` also enable simple data transfer.
* We have seen that `rsync` can be used to synchronise a local and remote directory: it can be configured to only copy those data that are new or have changed: more efficient if you're running it repeatedly.
  * `rsync` is not pre-installed on Windows, so instead of trying it out between your local machine and JASMIN, you could try `rsync` between two JASMIN machines.
* `sftp` is very useful and is also the underlying protocol used in many third-party tools.
* [rclone](https://rclone.org) can be configured to interace with various storage backends, including an SFTP server (like the transfer server used above), and can do synchronisation like `rsync`. It also talks to a whole variety of other storage backends such as cloud and object storage.
* Please **don't** install DropBox or other file-sharing software on JASMIN.
* Some third-party tools exist which provide graphical interfaces for transfers using `sftp`, e.g. [FileZilla](https://filezilla-project.org/), [CyberDuck](https://cyberduck.io/). These are applications which you can install on your own machine, to talk to JASMIN via the protocols it supports.
* Some editors (e.g. [VS Code](https://code.visualstudio.com/)) have extensions which enable you to setup SSH connections to edit & save files remotely. This can be useful for editing files on JASMIN, but from the convenience of your own local desktop environment.
* NONE of the SSH-based transfer methods we have looked at perform well for large volumes of data (TBs) or over long distances (international/intercontinental).
* Further reading:
  * [Improving your transfer rates](https://help.jasmin.ac.uk/docs/data-transfer/data-transfer-overview/#improving-your-transfer-rates)
  * [Data transfer tools](https://help.jasmin.ac.uk/docs/data-transfer/data-transfer-tools/) with information on further choices of tools available on JASMIN and their pros/cons.

### Questions to test yourself

All too easy? Here are some questions to test your knowledge an understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

1. How would you set the permissions on a file/directory so that it can be
   * written by any other member of the workspace?
   * readable by any user of JASMIN?

> [!CAUTION]
> NEVER set permissions so that a file or directory is readable and writable by everyone (777). This is not safe.

2. How could you share data on JASMIN with users outside of JASMIN?

3. **Why** are transfer methods based on SSH not very efficient over long distances?

# Cheatsheet

1. Make a small text file on your local machine.

    ```
    echo "This is a readme file" > README.txt
    scp README.txt train050@xfer-vm-01.jasmin.ac.uk:~/
    ```

    The `echo` command makes the text file for us. Use some other small file if you have one handy, or create one
    in your favorite text editor on your local machine.
    Copy it using the `scp` command, specifying our home directory `~/` as the path.

    Log into the xfer server itself, to see the file that you copied in place in the destination directory:

    ```
    ssh -A train050@xfer-vm-01.jasmin.ac.uk
    pwd
    ls -l README.txt
    ```

2. Make a small tree of directories on your **local** machine and create 2 files somewhere in those directories.

    ```
    mkdir -p mydata/01 mydata/02
    echo "This is a test file" > mydata/01/file01.txt
    echo "This is also a test file" > mydata/02/file02.txt
    ```

    Check what you have created:

    ```console
    $ find mydata
    mydata
    mydata/02
    mydata/02/file02.txt
    mydata/01
    mydata/01/file01.txt
    ```

    Make yourself a directory in the `workshop` group workspace:
    First log in to the transfer server: (substitute `train050` for your own JASMIN username).
    You may find it useful to open another terminal window for this (don't forget to check first whether your
    SSH key is loaded: see [exercise 01](../ex01) ).
    
    ```
    ssh -A train050@xfer-vm-01.jasmin.ac.uk
    ```

    Go to the workspace directory and make your own user directory there:

    ```console
    $ cd /gws/pw/j07/workshop
    $ ls
    ...
    users
    ...
    ```

    We have set out the GWS so that it has a directory called `users` where you can make your own sub-directories
    for working through these exercises.
    This helps keep things orgnanised. Make a directory for yourself, named as per your account
    username:
    
    <table>
      <thead>
        <tr>
          <td align="left">
            :information_source: Note
          </td>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>
            Below, we use the <code>$USER</code> environment variable which contains your JASMIN username. We will clear out these directories, and the home directories of the training accounts, after each workshop event. Normally you will have ~48hrs after the end of the workshop event to collect any data or code which you may want to keep. If you are working through these exercises outside of an organised event, please clean up after yourself and do not expect these data to persist.
          </td>
        </tr>
      </tbody>
    </table>

    ```console
    $ echo $USER             # check what is held in this environment variable
    train050
    $ mkdir users/$USER      # make a directory for yourself underneath the "users" directory
    $ ls -ld users/$USER      # check what you have created: note the ownership & permissions
    drwxr-sr-x 2 train050 gws_workshop 4096 Jan 26 11:26 users/train050
    ```

    Back on your local machine, recursively copy the directory using `scp`:  (replace `train050` with your username)

    ```
    scp -r mydata train050@xfer-vm-01.jasmin.ac.uk:/gws/pw/j07/workshop/users/train050/
    ```

    In your other terminal window on (or log back in to) the transfer server, inspect your destination directory:

    ```console
    $ cd /gws/pw/j07/workshop/users/$USER
    $ find .
    ./mydata
    ./mydata/02
    ./mydata/02/file02.txt
    ./mydata/01
    ./mydata/01/file01.txt
    ```

    The `find` command just shows the structure. To examine the permissions, use `ls -l`, or `ls -lR` to show the child directories too:

    ```console
    $ ls -lR mydata
    mydata:
    total 0
    drwxr-xr-x 1 train050 gws_workshop 0 Dec  4 11:59 01
    drwxr-xr-x 1 train050 gws_workshop 0 Dec  4 12:02 02

    mydata/01:
    total 0
    -rw-r--r-- 1 train050 gws_workshop 20 Dec  4 11:59 file01.txt

    mydata/02:
    total 0
    -rw-r--r-- 1 train050 gws_workshop 25 Dec  4 11:59 file02.txt
    ```

    While there are plenty of good tutorials out there on UNIX permissions, let's talk about how they affect things on JASMIN.

    These permissions may be what we want, but let's close them down for now, then work out how to open them up to people we want to share our data with: 

    Try the following command, which will restrict the group and world permissions on everything in the `mydata` directory and below:

    ```console
    $ chmod -R go-rX mydata         # note capital X
    $ ls -lR mydata
    mydata:
    total 128
    drwx------ 2 train050 gws_workshop 4096 Feb 23 10:51 01
    drwx------ 2 train050 gws_workshop 4096 Feb 23 10:51 02

    mydata/01:
    total 48
    -rw------- 1 train050 gws_workshop 20 Feb 23 10:51 file01.txt

    mydata/02:
    total 48
    -rw------- 1 train050 gws_workshop 25 Feb 23 10:51 file02.txt
    ```

    The directories `01` and `02` are signified by the extra `d` at the start, but all the files and directories have 3 sets of permissions: *User*, *Group* and *wOrld* (u, g, o). We are also told about which user and what group they belong to.

    ```
    drwx------ 1 train050 gws_workshop 0 Dec  4 11:59 01
     rwx         : user
        ---      : group
           ---   : world

    ```

    This tells us that directory `01` belongs to user `train050` and group `gws_workshop`. Its user permissions are `rwx` (read, write, execute) but its group and world permissions are now not set (`---`).

    If we want to open up directory `01` so that members of the same group `gws_workshop` can read it, but non-members still can't, we could set the group read permission. For directories, we need to add the `x` or execute permission as well: the capital `X` in the command means that it will work out the right change to make for files and directories:

    ```console
    $ chmod -R g+rX mydata/01
    $ ls -lR mydata
    mydata:
    total 0
    drwxr-x--- 1 train050 gws_workshop 0 Dec  4 11:59 01
    drwx------ 1 train050 gws_workshop 0 Dec  4 12:02 02

    mydata/01:
    total 0
    -rw-r----- 1 train050 gws_workshop 20 Dec  4 11:59 file01.txt

    mydata/02:
    total 0
    -rw------- 1 train050 gws_workshop 25 Dec  4 11:59 file02.txt
    ```

    Here, we've changed the permissions on a directory recursively, i.e. including everything beneath it as well. You can modify the permissions on a file or set of files individually, but bear in mind they will also be affected by any directories they sit in.

    Note that the group ownership of a file or directory in a group workspace might be different from any files you've created in your home directory. Check the permissions on the README.txt file you wrote there earlier:

    ```console
    $ ls -l ~/README.txt
    -rw-r--r-- 1 train050 users 22 Feb 23 10:48 /home/users/train050/README.txt
    ```

    By default, files you create in your home directory belong to group `users` (which is the default group for all users with `jasmin-login` privilege). You can check what groups you belong to with the `groups` command:

    ```console
    $ groups
    users open gws_workshop
    ```

    Normally, the top-level directory of a group workspace is set so that files and directories created beneath them inherit the group ownership of the top-level directory, but this can be over-ridden. If for some reason you've got files which belong to the `users` group, then the group permissions which are set on those files are affected by whether a user belongs to *that* group instead, so you might need to change them to belong to the `gws_workshop` group first.

    You can do this with the `chgrp` command, and it can be used recursively on a directory to change all the items in a directory tree (...but you have to have the right permissions to be able to modify them!)

    ```
    chgrp -R gws_workshop mydata
    ```

### Answers to questions

> 1. How would you set the permissions on a file/directory so that it can be
>    * written by any other member of the workspace?
>    * readable by any user of JASMIN?

You can first check the existing permissions on a file with:

```console
$ ls -l myfile.txt
-rw-r--r-- 1 train050 gws_workshop 0 Jan 22 17:01 myfile.txt
```

The group "read" permission is already set: this is the second "r", whereas the user permissions are currently set to `rw`, i.e. read and write.

You can add group write permission by a command such as:

```
chmod g+rw myfile.txt
```

or numerically with

```
chmod 664 myfile.txt
```

Check again:

```console
$ ls -l myfile.txt
-rw-rw--r-- 1 train050 gws_workshop 0 Jan 22 17:01 myfile.txt
```

Now we can see that the second set of permissions also has the `w` permission for write. You'd need to do similar for directories, but remember that for directories you also need to set the `x` (execute) permission.

By default, the top-level directory of the GWS is set so that new child directories inherit the fact that they're owned by the same group: `gws_workshop` as opposed to `users`, which would otherwise be the default (a file which you create in your home directory would normally belong to group `users`). But you still might need to set the **permissions** on the file to control what can be done with the file by other members of the same group.

Talk to your Group Workspace manager about how they would like users to organise their data and keep things tidy: it's their responsibility to set policies like this for the group.

> 2. How could you share data on JASMIN with users outside of JASMIN?

Using the logic above, you could set the permissions on the file/directory so that they're "world-readable" ...but can the outside "world" see the file? Not by default. File systems on JASMIN aren't visible outside of JASMIN, and can't be mounted remotely.

This can be arranged, however:

* Ask your Group Workspace manager to consider requesting that the GWS is set up with a `public` area which is [shared via HTTP](https://help.jasmin.ac.uk/article/202-share-gws-data-via-http). This means that the data below that `public` directory is openly available to anyone on the internet with a HTTP client such as a browser or a tool like `wget` or `curl`. That can be a good way of disseminating results and small amounts of data to external collaborators who are not users of JASMIN. But this should be used with care, and must not be used for hosting a project web site: that's not what that service is for.

* Using [Object Storage](https://help.jasmin.ac.uk/docs/short-term-project-storage/using-the-jasmin-object-store/) could provide more flexible sharing options: use of this is something your GWS manager would need to discuss with the JASMIN team.

> 3. **Why** are transfer methods based on SSH not very efficient?

For the interested reader, see [ESnet](https://fasterdata.es.net/)'s resources about faster data transfers including some reasons why [`scp` should be avoided over WAN](https://fasterdata.es.net/data-transfer-tools/say-no-to-scp/): to do with a buffer of limited size built in to the software stack that they're built on.

Tools like BBCP, GridFTP and Globus Online can help with more efficient use of available bandwidth and give much better performance for moving large volumes of data. See our documentation on [Data Transfer Tools](https://help.jasmin.ac.uk/article/3809-data-transfer-tools), in particular [Globus Transfers with JASMIN](https://help.jasmin.ac.uk/docs/data-transfer/globus-transfers-with-jasmin).

For short-distance transfers (by "distance" here we mean a network round-trip-time of <20ms), `scp` and other SSH-based tools can still be a good choice, for convenience and ease of use if nothing else.
