---
title: Connecting to JASMIN
author: Matt Pritchard
---

# Exercise 1: Connecting to JASMIN

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
 * help documentation at https://help.jasmin.ac.uk

### Local resources
 * SSH private key & passphrase
 * Client applications:
   * a terminal client e.g. Mac/Linux Terminal, [MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html) for Windows
   * [NX Enterprise Client](https://www.nomachine.com/download-enterprise#NoMachine-Enterprise-Client)
 * Network connection matching [JASMIN requirements](https://help.jasmin.ac.uk/article/190-check-network-details)

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

1. Connect to a `login` server using a terminal client
   * Load your ssh key locally
   * Initiate an SSH connection to a login server
   * Note the list of available `sci` servers 
   * Check what directory you are in
   * Check usage of your home directory
   * Check that your SSH key is available to make an onward connection
1. Connect to a login server using the Nomachine Enterprise Client
   * Make a connection profile for one `nx-login` server
   * Connect to that server
   * Check that your SSH key is available to make an onward connection
   * Bring up the list of available `sci` servers
1. Make an onward connection to a `sci` server
   * Login to the `sci` server
   * Run a simple command
   * Run a command which produces graphical output

### Questions to test yourself

All too easy? Here are some questions to test your knowledge and understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk).

1. What is different about servers `login2.jasmin.ac.uk` and `nx-login2.jasmin.ac.uk` compared to their siblings?
2. How often is your home directory backed up? How would you go about restoring files if you accidentally deleted something from your home directory?
3. What shell is used by default on JASMIN? How can you tell? How would you customise your shell environment (e.g. aliases, environment variables)?

### Review / alternative approaches / best practice

* Your SSH key must be protected with a strong passphrase.
* You must not share your SSH key with any other user.
* You must not edit your ~/.ssh/authorized_keys file on JASMIN. This is populated automatically with the (one) key you upload to your JASMIN account profile, so will be over-written if you edit it.
* The login servers perform 1 simple function and so should not be used for any processing, just as a "hop" to other systems within JASMIN.
* Check for a less-busy `sci` machine before connecting. Setting up an alias to 1 particular machine can be counter-productive.
* Don't use the `nx-login` servers for a regular terminal session: only use them via the NX client for a graphical desktop. This preserves resources and performance for those users who need it.

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


          * You can configure your shell to load your key automatically, by adding the `ssh-add` command (shown above) to your ~/.bash_profile file. This will be executed as open each new session.
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

    * Note the list of available `sci` servers

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

    * Check that your SSH key is available to make an onward connection

      As before, we can use the `ssh-add` command to check that our key is loaded. Remember that path it mentions relates to where it was loaded from on your local system. On the login server:

      ```
      $ ssh-add -l
      2048 SHA256:iqX3NkPCpschVdqPxVde/ujap2cM0mYaAYYedzBGPaI /home/fredbloggs/.ssh/id_rsa_jasmin (RSA)
      ```


1. Connect to a login server using the graphical NX client
   * Follow the steps [described here](https://help.jasmin.ac.uk/article/4810-graphical-linux-desktop-access-using-nx) for setting up NoMachine Enterprise Client for making a connection to JASMIN.
   * Open a "Terminal" window from the Activities menu
   * Type the following to retreive the "Message of the Day", listing available `sci` servers and their current usage:
   ```
   $ cat /etc/motd
   ``` 

1. Make an onward connection to a `sci` server
     * Login to the `sci` server

        It can be useful to repeat the `ssh-add -l` command to check that your SSH key is still available (now on the login server) before making your onward connection. You should get a similar result to that above. If not, go back and check that you enabled "forward authentication" in the NX connection profile settings for this login server.

        This time, because we want graphics to enable any graphics output to be sent back to this virtual desktop, we need to include the `-X` option with the `ssh` command:
        ```
        $ ssh -AX fred001@sci1.jasmin.ac.uk
        ```

     * Run a simple command

        We are now able to run a simple command on the sci server (you should see that the prompt has changed, but this command returns the name of the host so should confirms that you are now on the `sci` server)
        ```
        $ hostname
        sci1.jasmin.ac.uk
        ```
     * Run a command which produces graphical output

        Try running a (very) simple graphical application and check that it appears normally:
        ```
        $ xclock
        ```
        You should see a clock face appear on your desktop. Close this with `CTRL + c`.

  > **_NOTE:_**  You may find that the NX graphical desktop client is a more convenient interface to use for everyday use, and can be easier to set up than the various SSH Agent configurations needed on different platforms.

  > **_NOTE:_**  As [described here](https://help.jasmin.ac.uk/article/4810-graphical-linux-desktop-access-using-nx), the `nx-login` servers include a Firefox web browser which can be used for using some web-based tools which may only be available within JASMIN. Please do not use them for general web browsing, and please use firefox on the `nx-login` machines rather than the `sci` machines, to preserve resources for processing on the `sci` machines. The same article also discusses why using the NX client significantly improves performance for graphical applications run on JASMIN, if you're viewing the output somewhere remote to JASMIN.

  ### Answers to questions

> 1. What is different about servers `login2.jasmin.ac.uk` and `nx-login2.jasmin.ac.uk` compared to their siblings?

These provide a contingency option for users whose home network can't be configured to provide a forward and reverse DNS lookup. Details in the ["Check network details"](https://help.jasmin.ac.uk/article/190-check-network-details) help doc. If you're not sure what that means, please speak to your local IT support desk. 

> 2. How often is your home directory backed up? How would you go about restoring files if you accidentally deleted something from your home directory?

See [this article](https://help.jasmin.ac.uk/article/176-storage) about how you can restore data accidentally deleted from your home directory for up to a week. It also mentions the tape backups which run on a 3-4 week cycle.

> 3. What shell is used by default on JASMIN? How can you tell? How would you customise your shell environment (e.g. aliases, environment variables)?

You can check what shell is being used by checking the value of the `$SHELL` environment variable wherever you are logged in on JASMIN:
```
$ echo $SHELL
/bin/bash
```
The `bash` shell is used on JASMIN. Please refer to [official documentation](https://www.gnu.org/software/bash/) to learn about its capabilities and how to customise your own environment.