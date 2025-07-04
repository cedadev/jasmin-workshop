---
title: Connecting to JASMIN
author: Matt Pritchard
---

# Exercise 1: Connecting to JASMIN

> [!NOTE]
> This exercise assumes that you have already completed [exercise 0: Getting set up for the JASMIN workshop](../ex00), about setting up your local machine with everything you need to connect to JASMIN.

### Scenario

I want to connect to JASMIN from my own computer to do some work.

```mermaid
flowchart TD
   id1(My computer)
   -- terminal client -->id2(login server)
   -- terminal client -->id3(sci server)
   -->id4(do some work)
```

### Objectives

At the end of this exercise I will be able to:

- **Connect** to a JASMIN login server using a simple terminal client
- **Locate** my home directory
- **Make an onward connection** to a sci server
- **Run** a simple command

### JASMIN resources

- JASMIN account with SSH public key uploaded and `jasmin-login` access role
- Login server: `login-01.jasmin.ac.uk`
- Help documentation at https://help.jasmin.ac.uk

### Local resources

- Local machine set up as per [exercise 0](../ex00), including:
  - SSH client application
  - JASMIN credentials

### Your task

This is the outline of what you need to do. The recommended way of doing each step is covered in the "Cheat Sheet" but you may wish to try solving it for yourself first.

In the text below, you can see the steps needed to do this task, i.e:

1. Connect to a `login` server using a terminal client
   - (Your key should already be loaded, as per ex00)
   - Initiate an SSH connection to a login server
   - Note the list of available `sci` servers
   - Check what directory you are in
   - Check usage of your home directory
   - Check that your SSH key is available to make an onward connection
1. Make an onward connection to a `sci` server
   - Login to the `sci` server
   - Run a simple command

### Questions to test yourself

All too easy? Here are some questions to test your knowledge and understanding. You might find the answers by exploring the [JASMIN Documentation](https://help.jasmin.ac.uk).

1. How often is your home directory backed up? How would you go about restoring files if you accidentally deleted something from your home directory?
2. What shell is used by default on JASMIN? How can you tell? How would you customise your shell environment (e.g. aliases, environment variables)?

### Review / alternative approaches / best practice

- Your SSH key must be protected with a strong passphrase.
- You must not share your SSH key with any other user.
- You must not edit your `~/.ssh/authorized_keys` file on JASMIN. This is populated automatically with the (one) key you upload to your JASMIN account profile, so will be over-written if you edit it.
- The login servers perform one simple function so should not be used for any processing, only as a "hop" to other systems within JASMIN.
- Check for a less-busy `sci` machine before connecting. Setting up an alias to one particular machine can be counter-productive.

### Cheat Sheet

> [!NOTE]
> Please make sure you have read all the information in [exercise 0](../ex00), in particular the recommendation to use a preconfigured training account, and the reasons why. If you are using your **own** account, outside of one of our organised training events, you will need to have completed these steps yourself: [start here](https://help.jasmin.ac.uk/article/185-generate-ssh-key-pair), but not all the steps can be done temporarily for a workshop event.

1. Connect to a `login` server using a terminal client

   * For the workshop, use server `login-01.jasmin.ac.uk` but the full list is in the [help doc](https://help.jasmin.ac.uk/article/191-login-servers).

    * If you have set up your own machine as suggested in [exercise 0: Getting set up for the JASMIN workshop](../ex00), your SSH private key should already be loaded.

    * Check that your key is loaded with `ssh-add -l`. You should see a key fingerprint, similar to this (with either an email address or path after the random text, but won't be exactly the same!)
      ```console
      $ ssh-add -l
      2048 SHA256:e1rIzWgm0BAF396xNAYc8TdjjSs8IuMyr+iwSryHeb4 fred.bloggs@ncas.ac.uk (RSA)
      ```
      Note that the path, if included, is the path where the key was loaded from on your **local** machine.

      If it **has not** worked, you may see something like this:
      ```console
      $ ssh-add -l
      The agent has no identities.
      ```
      In this case, you will need to work out what is wrong before you will be able to connect. Please see the advice in exercise 0 before proceeding.

    * Initiate an SSH connection to a login server

      ```console
      $ ssh -A train050@login-01.jasmin.ac.uk
      ```
      <table>
        <thead>
          <tr>
            <td align="left">
              ℹ️ Note
            </td>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>
              Your username on JASMIN (<code>train050</code> in this example, but yours may be different) may not be the same as your username on your local machine (<code>fredbloggs</code>). In the <code>ssh</code> command, you must specify the username associated with your JASMIN account.
              The <code>-A</code> option is needed for "agent forwarding", which enables your key to be made available for an onward connection to a subsequent server: we need this for our connection to a <code>sci</code> machine.
            </td>
          </tr>
        </tbody>
      </table>

    * Note the list of available `sci` servers

      Once you have successfully logged in, you should see the "message of the day" (MOTD), which includes a list of the available `sci` servers and lists the number of users and the available memory on each. This is useful in selecting one which is not too busy:

      ![](images/motd-r9.png)

      Here we can see that `sci-vm-01` has 25 active user sessions, with 8G of free memory and a 15-minute average load of 1.007. Compare that to the other machines listed and choose one which suits the needs of what you plan to do. Note that some (not shown here, named `sci-ph-*`) are physical servers and have more memory to start with (see [sci servers documentation](https://help.jasmin.ac.uk/article/121-sci-servers))

    * Check what directory you are in
      ```console
      $ pwd
      /home/users/train050
      ```
    * Check usage of your home directory
      ```console
      $ pdu -sh 
      16G
      ```
      This shows 16G (gigabytes) being used, against your quota of 100G.

    * Check that your SSH key is available to make an onward connection

      As before, we can use the `ssh-add` command to check that our key is loaded. Remember that path it mentions relates to where it was loaded from on your local system. On the login server:

      ```console
      $ ssh-add -l
      2048 SHA256:iqX3NkPCpschVdqPxVde/ujap2cM0mYaAYYedzBGPaI /home/fredbloggs/.ssh/id_rsa_jasmin (RSA)
      ```

      Don't worry if this output includes the following message:
      ```
      error fetching identities for protocol 1: agent refused operation
      ```
      ...as long as the output includes the information about your key, showing that it's loaded. If it's not listed, or you get this message: 
      
      ```
      Could not open a connection to your authentication agent.
      ```
      then you'll need to go back and try again (did you forget to enable "agent forwarding" on your initial connection? (`-A` option or tickbox, depending on your client)

1. Make an onward connection to a `sci` server
     * Login to the `sci` server

        ```console
        $ ssh -A USERNAME@sci-vm-01.jasmin.ac.uk
        ```

        But remember to a) replace with your own username and b) choose which of the sci machines to connect to

        If you get "permission denied", it can be useful to repeat the `ssh-add -l` command to check that your SSH key is still available (now on the login server) before making your onward connection. You should get a similar result to that above. If not, go back and check that you enabled "forward authentication" in the NX connection profile settings for this login server.

     * Run a simple command

        We are now able to run a simple command on the sci server (you should see that the prompt has changed, but this command returns the name of the host so should confirms that you are now on the `sci` server)
        ```console
        $ hostname
        sci-vm-01.jasmin.ac.uk
        ```

  ### Answers to questions

#### 1. How often is your home directory backed up? How would you go about restoring files if you accidentally deleted something from your home directory?

See [this article](https://help.jasmin.ac.uk/article/176-storage) about how you can restore data accidentally deleted from your home directory for up to a week.

#### 2. What shell is used by default on JASMIN? How can you tell? How would you customise your shell environment (e.g. aliases, environment variables)?

You can check what shell is being used by checking the value of the `$SHELL` environment variable wherever you are logged in on JASMIN:
```console
$ echo $SHELL
/bin/bash
```
The `bash` shell is used on JASMIN. Please refer to [official documentation](https://www.gnu.org/software/bash/) to learn about its capabilities and how to customise your own environment.

### Further learning (optional)

#### Graphical linux desktop access using NoMachine NX

An alternative way of connecting to JASMIN provides a virtual desktop within JASMIN, useful if:

- you plan to use graphics-heavy applications, or
- you need to access any web-based services available only within JASMIN

But it's NOT needed if you're just making a basic connection to JASMIN.

Here's how this scenario (right) compares to our original scenario (left):

```mermaid
flowchart TD
   id1(My computer)
   -- terminal client -->id2(login server)
   -- terminal client -->id3(sci server)
   -->id4(do some work)

   id4-. view terminal output .->id1

   id5(My computer)
   -- special client -->id6(nx server)
   -- terminal client + X11-forwarding -->id7(sci server)
   -->id8(work using graphics)
   
   id8-. view graphics .->id5
```

The service is [fully documented here](https://help.jasmin.ac.uk/docs/interactive-computing/graphical-linux-desktop-access-using-nx/), including installation and troubleshooting tips, so we recommend you follow those to get set up.

Once you have estabished a connection to an `nx` server, return here to complete the rest of this exercise.

Your onward connection to the sci machine needs to "enable X11 forwarding" using the `-X` option as well as the `-A` relating to the key:

```console
> ssh -AX train050@sci-vm-01.jasmin.ac.uk
```

Once logged in to the sci machine, you can run a simple graphical command like `xeyes` or `xclock` and observe the output on the desktop. You can kill these applications with `CTRL-c`.

> [!NOTE]
> As [described here](https://help.jasmin.ac.uk/article/4810-graphical-linux-desktop-access-using-nx), the `nx` servers include a Firefox web browser which can be used for using some web-based tools which may only be available within JASMIN. Please do not use them for general web browsing, and please use Firefox on the `nx` machines rather than the `sci` machines, to preserve resources for processing on the `sci` machines. The same article also discusses why using the NX client significantly improves performance for graphical applications run on JASMIN, if you're viewing the output somewhere remote to JASMIN.
