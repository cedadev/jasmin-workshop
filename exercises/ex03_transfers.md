---
title: Exercise 03 Transferring and sharing data
author: Matt Pritchard
---

### Scenario

I want to copy some code from my own machine to my home directory on JASMIN. I also want to copy some data from to a Group Workspace on JASMIN so that I can share it with colleagues. My colleagues and I all belong to the "workshop" Group Workspace.

### Objectives

After competing this exercise I will be able to:

* Copy a small text file from my local machine to my JASMIN home directory using a transfer server.
* Copy a directory tree of data files recursively from my local machine to the `workshop` group workspace.
* Understand permissions and ownership needed for group access.
* Understand the limitations of some transfers methods.
* Pull in data from an external data source using a transfer server

### JASMIN resources

* Transfer server: `xfer[12].jasmin.ac.uk`
* Home directory: `/home/users/fred001`
* `workshop` group workspace at `/group_workspaces/jasmin2/workshop`

### Local resources

*   A terminal client on my local machine
*   Local directory: `/Users/fredbloggs/`

### Instructions

1. Make a simple text file or script on your local machine
1. Copy it to your home directory on a jasmin transfer server
1. Make a directory on your local machine and create a few simple files in it (representingo some data that you want to share)
1. Make a destination directory for yourself within the `workshop` group workspace
1. Copy the the directory and its contents to the destination directory using the transfer server
1. Check that the ownership and persmissions on your directory within the group workspace allow reading, and, if you choose, writing, by other members.
1. Using command line tools, download a test file from http://speedtest.tele2.net/100MB.zip, then delete it.

### Review

This exercise demonstrates how to use a transfer server to:

* Copy source code/scripts to your home directory
* Copy data to a group workspace
* Check permissions on the data to make sure it’s visible by collaborators
* Download some data from an external data source

We have looked at some basic methods suitable for small datasets or where speed is not critical. For larger data transfers or over longer distances (international/intercontinental), it is recommended to consider other available options which could be more efficient, depending on source & destination. See [ex10](ex10_advanced_data_transfer.md) or consult the [documentation here](https://help.jasmin.ac.uk/article/219-data-transfer-overview)


### Alternative approaches and best practice

*   In addition to `scp`, `sftp` and `rsync` also enable simple data transfer. See equivalent commands shown in the Cheat Sheet below.
* `rsync` can be used to synchronise a local and remote directory: it can be configured to only copy those data that have changed.
* Some 3rd party tools exist which provide graphical interfaces for transfers using `sftp`, e.g. [FileZilla](https://filezilla-project.org/), [CyberDuck](https://cyberduck.io/)
* Some editors (e.g. [VS Code](https://code.visualstudio.com/)) have extensions which enable you to setup SSH connections to edit & save files remotely. This can be useful for editing files on JASMIN, but from the convenience of your own deskop environment on your local machine.
* NONE of the transfer methods we have looked at based on the SSH protocol perform well for large volumes of data or over long distances. Define "large" or "long"?
* see [ex10](ex10_advanced_data_transfer.md) for advice about:
    * More efficient data transfers for large data / longer distances
    * Automated transfers
    * Transfers within JASMIN



### Questions to test yourself

All too easy? Here are some questions to test your knowledge an understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk)

1. How would you set the permissions on a file/directory so that it can be
   * written by any other member of the workspace?
   * readable by any user of JASMIN?

    > **_NOTE:_**  NEVER set permissions so that a file or directory is readable and writable by everyone (777).

1. How could you share data on JASMIN with users outside of JASMIN?

1. Why are transfer methods based on SSH not very efficient?

# Cheatsheet

1. Make a small text file on your local machine containing a bash script which you could run on JASMIN.
    ```
    $ echo "This is a readme file" > README.txt
    $ scp test_file.txt fred001@xfer1.jasmin.ac.uk:~/
    ```

    The `echo` command makes the text file for us. Use some other file if you have one handy.
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
    First log in to the transfer server: (substitute `fred001` for your own JASMIN username)
    ```
    $ ssh -A fred001@xfer1.jasmin.ac.uk
    ```
    Go to the workspace directory and make your own user directory there, then log out:
    ```
    $ cd /group_workspaces/jasmin2/workshop/
    $ mkdir $USER
    $ exit
    ```

    > **_NOTE:_**  Above, we used the `$USER` environment variable which contains your JASMIN username.

    Back on your local machine, recursively copy the directory using `scp`:
    ```
    scp -r mydata fred001@xfer1.jasmin.ac.uk:/group_workspaces/jasmin2/workshop/fred001/
    ```

    Log back in to the transfer server to inspect your destination directory:
    ```
    $ ssh -A fred001@xfer1.jasmin.ac.uk
    $ cd /group_workspaces/jasmin2/workshop/$USER
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
    drwx------ 1 fred001 users 0 Dec  4 11:59 01
    drwx------ 1 fred001 users 0 Dec  4 12:02 02

    mydata/01:
    total 0
    -rw------- 1 fred001 users 20 Dec  4 11:59 file01.txt

    mydata/02:
    total 0
    -rw------- 1 fred001 users 25 Dec  4 11:59 file02.txt
    ```
    This looks OK but at the moment only `fred001` can read or write the files. We want anyone in the same group workspace to be able to read them, but only `fred001` to be able to write/modify them.
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
    drwxr-x--- 1 fred001 gws_workshop 0 Dec  4 11:59 01
    drwxr-x--- 1 fred001 gws_workshop 0 Dec  4 12:02 02

    mydata/01:
    total 0
    -rw-r----- 1 fred001 gws_workshop 20 Dec  4 11:59 file01.txt

    mydata/02:
    total 0
    -rw-r----- 1 fred001 gws_workshop 25 Dec  4 11:59 file02.txt
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
    $ $ curl -o /dev/null http://speedtest.tele2.net/100MB.zip
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100  100M  100  100M    0     0   195M      0 --:--:-- --:--:-- --:--:--  196M
    ```

    Both `wget` and `curl` are very useful, feature-rich transfer tools and can do a lot more than shown here: read the relevant `man` pages for more information. You can also build your own transfer tools using packages such as `requests` in Python (see [ex10](ex10_advanced_data_transfer.md))