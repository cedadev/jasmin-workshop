---
title: Exercise 3 Transferring and sharing data
author: Matt Pritchard
---

# Exercise 3: Transferring and sharing data

### Scenario

I want to copy some code from my own machine to my home directory on JASMIN. I also want to copy some data to a Group Workspace on JASMIN so that I can share it with colleagues. My colleagues and I all belong to the `workshop` Group Workspace.

### Objectives

After competing this exercise I will be able to:

* Copy a small text file from my local machine to my JASMIN home directory using a transfer server.
* Copy a directory tree of data files recursively from my local machine to the `workshop` group workspace.
* Understand permissions and ownership needed for group access.
* Be aware of the limitations of some transfers methods.
* Pull in data from an external data source using a transfer server

### JASMIN resources

* Account with valid `jasmin-login` privilege
   * If you are using one of the training accounts this will have been set up for you
* Transfer server: `xfer[12].jasmin.ac.uk` (`1` or `2`)
* Home directory: `/home/users/train050` (replace with your username)
* `workshop` group workspace at `/gws/pw/j05/workshop`

### Local resources

*  Local machine set up as per [exercise 0](..ex00), with:
    * SSH client application (use a command-line client for this exercise: you won't need the graphical desktop)
    * SSH key and JASMIN credentials
    * suitable network connection
*  Directory on your local machine: `/Users/fredbloggs/` (choose your own)

### Instructions

1. Make a simple text file or script on your local machine
1. Copy it to your home directory on a jasmin transfer server
1. Make a directory on your local machine and create a few simple files in it (representing some data that you want to share). This is the **source** directory.
1. Make a **destination** directory for yourself within the `workshop` group workspace
1. Copy the the source directory and its contents to the destination directory using the transfer server
1. Check that the ownership and permissions on your directory within the group workspace allow reading, and, if you choose, writing, by other members.
1. Using command line tools, download a test file from http://speedtest.tele2.net/100MB.zip to your destination directory in the `workshop` group workspace, then delete it.

### Review

This exercise demonstrates how to use a transfer server to:

* Copy small files such as source code/scripts to your home directory
* Copy data to a group workspace
* Check permissions on the data to make sure it’s visible by collaborators
* Download some data from an external data source

We have looked at some basic methods suitable for small datasets or where speed is not critical. For larger data transfers or over longer distances (international/intercontinental), it is recommended to consider other available options which could be more efficient, depending on source & destination. See [exercise 10](../ex10) or consult the [documentation here](https://help.jasmin.ac.uk/article/219-data-transfer-overview)


### Alternative approaches and best practice

* In addition to `scp`, alternative tools `sftp` and `rsync` also enable simple data transfer.
* We have seen that `rsync` can be used to synchronise a local and remote directory: it can be configured to only copy those data that are new or have changed: more efficient if you're running it repeatedly.
* `sftp` is very useful and is also the underlying protocol used in many third-party tools.
* [rclone](https://rclone.org) can be configured to interace with various storage backends, including an SFTP server (like the transfer server used above), and can do synchronisation like `rsync`. It also talks to a whole variety of other storage backends such as cloud and object storage.   
* Some third-party tools exist which provide graphical interfaces for transfers using `sftp`, e.g. [FileZilla](https://filezilla-project.org/), [CyberDuck](https://cyberduck.io/)
* Some editors (e.g. [VS Code](https://code.visualstudio.com/)) have extensions which enable you to setup SSH connections to edit & save files remotely. This can be useful for editing files on JASMIN, but from the convenience of your own local desktop environment.
* NONE of the SSH-based transfer methods we have looked at perform well for large volumes of data or over long distances. Define "large" or "long"?
* see [ex10](../ex10) for advice about:
    * More efficient data transfers for large data / longer distances
    * Automated transfers
    * Transfers within JASMIN



### Questions to test yourself

All too easy? Here are some questions to test your knowledge an understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

1. How would you set the permissions on a file/directory so that it can be
   * written by any other member of the workspace?
   * readable by any user of JASMIN?

    > **_NOTE:_**  NEVER set permissions so that a file or directory is readable and writable by everyone (777). This is not safe.

1. How could you share data on JASMIN with users outside of JASMIN?

1. **Why** are transfer methods based on SSH not very efficient over long distances?

# Cheatsheet

1. Make a small text file on your local machine containing a bash script which you could run on JASMIN.
    ```
    $ echo "This is a readme file" > README.txt
    $ scp README.txt train050@xfer1.jasmin.ac.uk:~/
    ```

    The `echo` command makes the text file for us. Use some other small file if you have one handy, or create one
    in your favorite text editor on your local machine.
    We then copy it using the `scp` command, specifying our home directory `~/` as the path.

1. Make a small tree of directories on your **local** machine and create 2 files somewhere in those directories.
    ```
    $ mkdir -p mydata/01 mydata/02
    $ echo "This is a test file" > mydata/01/file01.txt
    $ echo "This is also a test file" > mydata/02/file02.txt
    ```
    Check what you have created:
    ```
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
    $ ssh -A train050@xfer1.jasmin.ac.uk
    ```
    Go to the workspace directory and make your own user directory there:
    ```
    $ cd /gws/pw/j05/workshop
    $ ls
    users
    ```
    We have set out the GWS so that it has a directory called `users` where you can make your own sub-directories
    for working through these exercises.
    This helps keep things orgnanised. Make a directory for yourself, named as per your account
    username:
    
    > **_NOTE:_** Below, we use the `$USER` environment variable which contains your JASMIN username.
    
    > **_NOTE:_** We will clear out these directories, and the home directories of the training accounts, after each workshop event. 
    Normally you will have ~48hrs after the end of the workshop event to collect any data or code which you may want to keep.
    If you are working through these exercises outside of an organised event, please clean up after yourself and 
    do not expect these data to persist.
    
    ```
    $ echo $USER             # check what is held in this environment variable
    $ mkdir users/$USER      # make a directory for yourself underneath the "users" directory
    $ ls -ld users/$USER      # check what you have created: note the ownerhsip & permissions
    drwxr-sr-x 2 train050 gws_workshop 4096 Jan 26 11:26 users/train050
    ```

    Back on your local machine, recursively copy the directory using `scp`:
    ```
    scp -r mydata train050@xfer1.jasmin.ac.uk:/gws/pw/j05/workshop/users/train050/
    ```

    In your other terminal window on (or log back in to) the transfer server, inspect your destination directory:
    ```
    $ cd /gws/pw/j05/workshop/users/$USER
    $ find .
    ./mydata
    ./mydata/02
    ./mydata/02/file02.txt
    ./mydata/01
    ./mydata/01/file01.txt
    ```
    The `find` command just shows the structure. To examine the permissions, use `ls -l`, or `ls -lR` to show the child directories too:
    ```$ ls -lR mydata
    mydata:
    total 0
    drwx------ 1 train050 users 0 Dec  4 11:59 01
    drwx------ 1 train050 users 0 Dec  4 12:02 02

    mydata/01:
    total 0
    -rw------- 1 train050 users 20 Dec  4 11:59 file01.txt

    mydata/02:
    total 0
    -rw------- 1 train050 users 25 Dec  4 11:59 file02.txt
    ```
    This looks OK but at the moment only `train050` can read or write the files. We want anyone in the same group workspace to be able to read them, but only `train050` to be able to write/modify them.
    If we were to leave them with group ownership of `users`, then when we change the permissions, they would become readable by anyone on JASMIN: this might not be what we want.
    Each Group Workspace has its own group. In this case, it's `gws_workshop`. You can check that you belong to that group with the following command:
    ```
    $ groups
    users gws_workshop
    ```
    Now we can change the group ownership of the files and directories (all in one go) to `workshop` with the `chgrp` command:
    ```
    $ chgrp -R gws_workshop mydata
    ```
    Now all the files/directories belong to the workshop group, but we haven't yet granted read permission to other people in the group. Since files need to be `rw-r-----` (`640`) and directories need to be (`rwxr-x---`) (`755`), we could set these at the top level as follows,
    ```
    chmod -R g+rX mydata
    ```
    This sets the group execute permission on the directories as well, in one go. An alternative would be
    ```
    $ find mydata -type f -exec chmod 640 {} \;
    $ find mydata -type d -exec chmod 750 {} \;
    ```

    This gives us the permissions we want:
    ```
    $ ls -lR mydata
    mydata:
    total 0
    drwxr-x--- 1 train050 gws_workshop 0 Dec  4 11:59 01
    drwxr-x--- 1 train050 gws_workshop 0 Dec  4 12:02 02

    mydata/01:
    total 0
    -rw-r----- 1 train050 gws_workshop 20 Dec  4 11:59 file01.txt

    mydata/02:
    total 0
    -rw-r----- 1 train050 gws_workshop 25 Dec  4 11:59 file02.txt
    ```

1. Using command line tools or a script you have written, download a test file from http://speedtest.tele2.net/100MB.zip, then delete it.

    We can use either `curl` or `wget` to fetch a remote data file via HTTP from within JASMIN. These utilities are installed on the transfer servers.

    The speed test site http://speedtest.tele2.net/ provides a number of different files which can be used to test download performance, but also to test the functionality of any tools to check they're working properly.

    ```
    $ wget http://speedtest.tele2.net/100MB.zip
    ```
    Followed by this to delete the file:
    ```
    $ rm 100MB.zip
    ```
    We're deleting the file straight after downloading it, so an alternative is to specifying the output file as the null device, which means it's not actually written to storage:
    ```
    $ wget -O/dev/null http://speedtest.tele2.net/100MB.zip
    $ wget -O/dev/null http://speedtest.tele2.net/100MB.zip
    --2020-12-04 12:38:16--  http://speedtest.tele2.net/100MB.zip
    Resolving speedtest.tele2.net (speedtest.tele2.net)... 90.130.70.73, 2a00:800:1010::1
    Connecting to speedtest.tele2.net (speedtest.tele2.net)|90.130.70.73|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 104857600 (100M) [application/zip]
    Saving to: ‘/dev/null’

    100%[==============================================================================>] 104,857,600  179MB/s   in 0.6s   

    2020-12-04 12:38:16 (179 MB/s) - ‘/dev/null’ saved [104857600/104857600]
    ```
    Here, we've got a result of 179MB/s which is pretty good. All sorts of factors can contribute to slow transfer performance but this apprach can be helpful in eliminating this particular machine as the bottleneck. Quite often the reason is a slow server at the other end, or complex directory structures full of small files which slow things down. For more discussion of transfer performance, see [ex10](ex10_advanced_data_transfer.md).

    The equivalent using `curl` would be:
    ```
    $ curl -o /dev/null http://speedtest.tele2.net/100MB.zip
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100  100M  100  100M    0     0   195M      0 --:--:-- --:--:-- --:--:--  196M
    ```

    Both `wget` and `curl` are very useful, feature-rich transfer tools and can do a lot more than shown here: read the relevant `man` pages for more information. You can also build your own transfer tools using packages such as `requests` in Python (see [ex10](ex10_advanced_data_transfer.md))

### Answers to questions

> 1. How would you set the permissions on a file/directory so that it can be
   * written by any other member of the workspace?
   * readable by any user of JASMIN?

You can first check the existing permissions on a file with:
```
$ ls -l myfile.txt
-rw-r--r-- 1 train050 gws_workshop 0 Jan 22 17:01 myfile.txt
```

The group "read" permission is already set: this is the second "r", whereas the user permissions are currently set to `rw`, i.e. read and write.

You can add group write permission by a command such as:
```
$ chmod g+rw myfile.txt
```
or numerically with
```
$ chmod 664 myfile.txt
```
Check again:
```
$ ls -l myfile.txt
-rw-rw--r-- 1 train050 gws_workshop 0 Jan 22 17:01 myfile.txt
```
Now we can see that the second set of permissions also has the `w` permission for write. You'd need to do similar for directories, but remember that for directories you also need to set the `x` (execute) permission. 

By default, the top-level directory of the GWS is set so that new child directories inherit the fact that they're owned by the same group: `gws_workshop` as opposed to `users`, which would otherwise be the default (a file which you create in your home directory would normally belong to group `users`). But you still might need to set the **permissions** on the file to control what can be done with the file by other members of the same group.

Talk to your Group Workspace manager about how they would like users to organise their data and keep things tidy: it's their responsibility to set policies like this for the group.

> 1. How could you share data on JASMIN with users outside of JASMIN?

Using the logic above, you could set the permissions on the file/directory so that they're "world-readable" ...but can the outside "world" see the file? Not by default. File systems on JASMIN aren't visible outside of JASMIN, and can't be mounted remotely.

There are a couple of methods by which this can be done, however:

* Ask your Group Workspace manager to consider requesting that the GWS is set up with a `public` area which is [shared via HTTP](https://help.jasmin.ac.uk/article/202-share-gws-data-via-http). This means that the data below that `public` directory is openly available to anyone on the internet with a HTTP client such as a browser or a tool like `wget` or `curl`. That can be a good way of disseminating results and small amounts of data to external collaborators who are not users of JASMIN. But this should be used with care, and must not be used for hosting a project web site: that's not what that service is for.

* A similar service OPeNDAP4GWS can be used to provide an OPeNDAP interface on top of data inside a GWS. Ask your GWS manager to contact the helpdesk for further details. 

> 1. Why are transfer methods based on SSH not very efficient?

For the interested reader, see [ESnet](https://fasterdata.es.net/)'s resources about faster data transfers including some reasons why [scp should be avoided over WAN](https://fasterdata.es.net/data-transfer-tools/say-no-to-scp/): to do with a buffer of limited size built in to the software stack that they're built on.

Tools like BBCP, GridFTP and Globus Online can help with more efficient use of available bandwidth and give much better performance for moving large volumes of data. See our documentation on [Data Transfer Tools](https://help.jasmin.ac.uk/article/3809-data-transfer-tools).
For short-distance transfers (by "distance" here we mean a network round-trip-time of <20ms), `scp` and other SSH-based tools can still be a good choice, for convenience and ease of use if nothing else.
