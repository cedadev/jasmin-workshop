---
title: Connecting to JASMIN
author: Author
contact: Email
draft: false
sensitive: false
reason: few words describing purpose of this doc
version: 0.1 \today
---

### Scenario

I want to connect to JASMIN from my own computer to do some work.

### Objectives

At the end of this exercise I will be able to:

 * **Connect** to a JASMIN login server using:
   * a simple terminal client
   * a graphical desktop client
 * **Locate** my home directory
 * **Make an onward connection** to a sci server
 * **Run** a simple command
 * **Run** a command which produces graphical output

### JASMIN resources
 * JASMIN account with SSH public key uploaded and `jasmin-login` privilege
 * login servers: `login[1234].jasmin.ac.uk`
 * nx-login servers: `nx-login[123].jasmin.ac.uk`

### Local resources
 * SSH private key & passphrase
 * Client applications:
   * a terminal client e.g. Mac/Linux Terminal, MobaXterm for Windows
   * NX Enterprise Client

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

1. Connect to a `login` server using a terminal client
  * Load your ssh key locally
  * Initiate an SSH connection to a login server
  * Note the list of availble `sci` servers 
  * Check what directory you are in
  * Check usage of your home directory
  * Check that your SSH key is availble to make an onward connection
1. Connect to a login server using the graphical NX client
  * Make a connection profile for one `nx-login` server
  * Connect to that server
  * Check that your SSH key is availble to make an onward connection
  * Bring up the list of available `sci` servers
1. Make an onward connection to a `sci` server
  * Login to the `sci` server
  * Run a simple command
  * Run a command which produces graphical output

### Questions to test yourself

All too easy? Here are some questions to test your knowledge and understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk).

1. What is different about servers `login2.jasmin.ac.uk` and `nx-login2.jasmin.ac.uk` compared to their siblings?
2. How often is your home directory backed up? How would you go about restoring files if you accidentally deleted something from your home directory?
3. What shell is used by default on JASMIN? How would you customise your shell environment (e.g. aliases, environment variables)?

### Review / alternative approaches / best practice



### Cheat Sheet

> **_NOTE:_**  The prerequisties to this exercise mentioned that you need to have an SSH key pair, have uploaded the public key to your JASMIN account profile and that your JASMIN account has been granted the `jasmin-login` privilege. If you are using one of the training accounts, then these steps will have been done for you and you should use the credentials which you will have been given for this workshop.
If you are using your own account, you will need to have completed these steps yourself: [start here](https://help.jasmin.ac.uk/article/185-generate-ssh-key-pair)).

1. Connect to a `login` server using a terminal client

   * Choose your `login` server from the list in the [help doc](https://help.jasmin.ac.uk/article/191-login-servers).
   * Choose your terminal client
      * This is the application with which you will make an SSH connection
   * On Windows:
      * MobaXterm is our recommended client.
   * Mac or Linux
      * Use the native Terminal app.

  * Load your ssh key locally
   * On Windows:
      * Use MobAgent to load your SSH private key ([see how to do this](https://help.jasmin.ac.uk/article/4832-mobaxterm)).  **Recommended method**
      * This ensures that it will be avialable for all sessions which you initiate.
      * An alternative, which just works within the **current** session, is to use the instructions for Mac and Linux, shown below (but if you open another terminal window you may need to repeat this step for each window).

   * On a Mac or Linux system:

```
$ eval $(ssh-agent -s)
$ ssh-add ~/.ssh/id_rsa_jasmin
Enter passphrase for /home/fredbloggs/.ssh/id_rsa_jasmin:
Identity added: /home/fredbloggs/.ssh/id_rsa_jasmin (/home/users/fred001/.ssh/id_rsa_jasmin)
```

> **_NOTE:_**  The `$` symbol preceding commands represents the command prompt on your system. You do not need to type this symbol. Lines not preceded by a `$` symbol represent output.

> **_NOTE:_**  The path to your key (e.g. `/home/fredbloggs/.ssh/`) relates to the location of your private key on your own machine, NOT on JASMIN. There should be NO NEED to put your private key anywhere on JASMIN, and you will keep it more secure by keeping it ONLY on your local machine.


   * On a Mac or Linux system, you can configure your shell to automatically load your key, by adding the `ssh-add` command (shown above) to your ~/.bash_profile file.
   * You will still be prompted for the passphrase in each new window you open, although Mac users can securely add their passphrase to KeyChain using the `-K` option with `ssh-add`.
   * On a Linux system, your Desktop Manager may provide a utility to load your key at login time and have it persistently available to any new terminal session you open (this is what the MobAgent utility emulates in MobaXterm on Windows).

  * Check that your key is loaded
```
$ ssh-add -l
2048 SHA256:iqX3NkPCpschVdqPxVde/ujap2cM0mYaAYYedzBGPaI /home/fredbloggs/.ssh/id_rsa_jasmin (RSA)
```
If it has not worked, you may see something like this:
```
$ ssh-add -l
The agent has no identities.
```
In this case, you will need to work out what is wrong before you will be able to connect.

  * Initiate an SSH connection to a login server

```
$ ssh -A fred001@login1.jasmin.ac.uk
```
> **_NOTE:_**  Your username on JASMIN (`fred001`) may not be the same as your username on your local machine (`fredbloggs`). You must specify the username associated with your JASMIN account.

> **_NOTE:_**  The -A option is needed for "agent forwarding", which enables your key to be made available for an onward connection to a subsequent server: we need this for our connection to a `sci` machine.

  * Note the list of availble `sci` servers

Once you have successfully logged in, you should be present with the "message of the day" (MOTD), which includes a list of the available `sci` servers and lists the number of users and the available memory on each. This is useful in selecting one which is not overloaded: 

![](https://d33v4339jhl8k0.cloudfront.net/docs/assets/564b4bd3c697910ae05f445c/images/5fc92e11de1bfa158fb55239/file-dKz1hO4aLb.png)

  * Check what directory you are in
```
$ pwd
/home/users/fred001
```
  * Check usage of your home directory
```
$ pdu -sh 
16G
```
This shows 16G (gigabytes) being used, against your quota of 100G.

  * Check that your SSH key is availble to make an onward connection

As before, we can use the ssh-add command to check that our key is loaded. Again, the path it mentions relates to where it came from on your local system, not the path on JASMIN, since it should not be stored on JASMIN: 

On the login server:

```
$ ssh-add -l
4096 SHA256:L7D9ATLsBVl5zIPI6EZGsXqHn31pQVyXFhYhphEj7hU /Users/fredbloggs/.ssh/id_rsa_jasmin (RSA)
```
A message like `error fetching identities for protocol 1: agent refused operation` can be ignored as long as at least 1 identity is listed, as above.

1. Connect to a login server using the graphical NX client
  * Make a connection profile for one `nx-login` server
  * Connect to that server
  * Check that your SSH key is availble to make an onward connection
  * Bring up the list of available `sci` servers
1. Make an onward connection to a `sci` server
  * Login to the `sci` server
  * Run a simple command
  * Run a command which produces graphical output

