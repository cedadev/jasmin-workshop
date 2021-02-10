---
title: Getting set up for the JASMIN Workshop
author: Matt Pritchard
---

> **_NOTE:_**  This exercise is written for participants of the **JASMIN Workshop** events. At these events, training accounts are temporarily assigned to course participants. In this way we can make sure that all participants have access to all the necessary resources and can minimise logistical issues during the events.
For continued use of JASMIN beyound the duration of these workshop events, or for use of the training materials outside of one of the organised events, users are asked to apply for their own, regular JASMIN account via the normal process if they don't already have one.

# Exercise 0: Getting set up for the JASMIN Workshop

### Scenario

I want to get my environment set up on my local machine so that I am ready to work through exercise 1 of the JASMIN Workshop.

### Objectives

After competing this exercise I will be able to:

 * Get hold of the resources I need for setting up my environment.
 * Set them up ready for working through exercise 1.

### JASMIN resources

 * Training account
    * You will be provided with access to an account which is already set up with all the privileges you need to complete the workshop exercises.
    * Normally, users manage their accounts and these privileges via the [JASMIN Accounts Portal](https://accounts.jasmin.ac.uk) - you may see or hear this mentioned in the exercises, but if you are using a training account you should not need to use it at least for exercises 1-5.

### Local resources

 * **Email address**
    * You will have been contacted in advance of the workshop event to provide an email address.
    * The JASMIN team will have linked your email address to a specific training account.
 * **Training account credentials**. These will shared with you via this email address. You will be sent the items in the list below, and the instructions in this exercise will cover how to set up your local machine to use them:
    * SSH Key pair
    * Passphrase for SSH Key
    * username for the training account
    * password for the training account


### Introduction

The [Overview presentation](../overview) given at the start of the workshop will cover much of the what / why / where / how questions you may have, so this initial exercise is about setting up what you will need in order to take part, rather than learning about how you can use JASMIN.

The course does assume some basic knowledge listed below. There are plenty of good learning resources and tutorials in existence already, so rather than duplicate these, we have concentrated in the workshop on aspects specific to working on JASMIN.

Important things to know about:
   * Using a command-line (also known as terminal or shell) environment to execute commands to carry out tasks
      * If you have only ever used a computer in "point-and-click" mode, for example in Windows or MacOS, you will need to learn some basics about using a command-line environment first before this workshop.
      * The operating system used on JASMIN is Linux (currently CentOS7).
      * The default shell used on JASMIN is `bash`.
      * We will show our recommended way of getting to a command-line environment on each of Windows, MacOS and Linux.
   * Concepts such as "client", "server" and that particular protocols (methods) enable you to connect from your local machine (i.e. your laptop or desktop) to a remote machine and run commands on it.
   * Organising data into files and directories (also known as folders)

### Which tool should I use to connect to JASMIN?

This depends on whether the things you want to do on JASMIN are likely to need to display graphics, or whether the programs or applications you plan to use just produce text output.
You can use both, but your choice of tool might be different for each.

Here are our recommendations:

| Local machine | Text only | Graphical output |
| - | - | - |
| Windows | `MobaXterm`* | NoMachine Enterprise Client* |
| MacOS | `Terminal` app | NoMachine Enterprise Client* |
| Linux | `xterm` | NoMachine Enterprise Client* |

<br>

> **_NOTE:_**  We recommend using NoMachine Enterprise Client, in combination with specific servers JASMIN, instead of standard (also known as X11) graphics, because performance is much better over the network. This is particularly recommended if you need to use a graphical user interface to control an application, for example manipulating a large satellite image.

> **_NOTE:_**  We recognise that other applications are available for each of these choices, but in order to keep the instructions as similar as possible between different platforms, we would ask that you stick to these recommendations at least for use during the workshop. If you choose another option and it doesn't work, we may not be able to help.

For the options marked `*` above, you'll need to download and install software to run on your local machine. You should check that you have sufficient privileges (permissions) on your local machine to do this. If in doubt, ask the IT support team responsible for your **local** machine.

We'll cover all of these combinations, so please follow the instructions relevant to your local machine to ensure you have everything you need for the workshop.

The overall concept is as follows. All the applications we'll cover follow the same overall process:

* You have an SSH key consisting of 2 parts: public and private. The private key stays with you on your local machine. For your training account, the public key is already put into the right place at the JASMIN end for you.
* The software which you use to connect to JASMIN needs to "present" your private key, but to do that, first you have to load it, which involves "unlocking" it with its passphrase. You will also need to enable "agent forwarding", meaning that the same key can be used for onward connections to other machines as well as the first one. Different applications have different ways of applying this setting.
* When you use your application to connect to a JASMIN server, under the hood there's a check that the 2 halves of your key match. If they don't, you're denied access.
* Once you're connected, you can make onward connections to other machines inside JASMIN using the same key. But importantly, the private key does not need to be copied to JASMIN: it should stay **only** on your local machine.

The details of how each software tool does this may look different, but they're all doing the same thing. Setting up each application will involve (not necessarily in the same order):
1. Installing the software, unless it's something built-in to your operating system
2. Telling it where your private key is, on your local machine
3. Loading that private key, using the passphrase, and enabling agent forwarding
4. (in some cases) Setting up "connection profiles" to connect to particular remote machines of your choice

In most cases, you are able to load your key into an "agent" or key manager, which means that your key remains loaded across any individual terminal sessions you open using that software. The alternative is that you need to load your key each time you open a new terminal session. Either should work, but the former can be more convenient as you only need to enter your passphrase when you first open the software, rather than for each connection.

Once all that is done, you're (almost) ready to make a connection to a remote machine.

For all the methods below, you will need to locate and refer to the private key which the JASMIN team will have sent you prior to the workshop event. You should save this somewhere safe as follows: (create the directory indicated if it doesn't exist already)

|System|Location|
|-|-|
|Windows|`Desktop\ssh` (a folder called `ssh` on your Desktop)|
|MacOS|`~/.ssh` (a directory called `.ssh` in your `$HOME` directory)|
|Linux|`~/.ssh` (a directory called `.ssh` in your `$HOME` directory)|

> **_NOTE:_**  On MacOS, you may not see "hidden" directories in Finder unless you have enabled this in your Preferences, but you can temporarily enable this with `cmd + L-Shift + .` 

<br>

### Windows

Our recommended choice for a terminal application on Windows is MobaXterm.


#### Software installation
* Download from [MobaXterm](https://mobaxterm.mobatek.net/).
* Choose the "Home Edition" (free), then either the "Installer edition" or "Portable Edition" and follow the instructions.|

[![MobaXterm v20.6 setup on Windows, loading private key](https://img.youtube.com/vi/yG8yyTt2R-0/0.jpg)](https://www.youtube.com/watch?v=yG8yyTt2R-0)

In the above video, you can see the steps needed to load the key, i.e:

* Tick "Use internal SSH agent "MobAgent"
* UN-tick "Use external Pageant"
* Tick "Forward SSH agents" **important**
* Click the "+" symbol to locate your private key file (e.g. id_rsa_jasmin)
* Click OK to save the settings. MobaXterm will now need to restart.
* When you restart MobaXterm you will be prompted for the passphrase associated with your private key.

Click "Start local terminal".

You can then check that your key is correctly loaded with this command in the terminal window: 

```
$ ssh-add -l
```
If you see a message similar to the following, your key is correctly loaded:
```
2048 SHA256:0y7Oh7J+kN6hPotWCerXsZBlRBL205UMGlJVZ1I0A8c you@somewhere.ac.uk (RSA)

```
If not, you will need to try again before you will be able to log in to a remote host using the key.

### MacOS

Our recommended choice for a terminal application on MacOS is the `terminal` app. Find this by searching in the "spotlight search" (magnifying glass, usually top-right in the Apple menu bar).

In a new terminal window:
```
$ ssh-add -K ~/.ssh/id_rsa_jasmin
```
The `-K` is optional, but stores the passphrase in your KeyChain, so that it's available whenever you're logged in to your Mac. Obviously, only do this on a machine where your initial login after rebooting is protected by a strong password and/or fingerprint ID.

You'll be prompted for your passphrase at this point.

> **_NOTE:_**  [Advanced users] You can also add that same line to your `~/.bashrc` so that this is automatically done for you in each new terminal window you open. Only when you reboot your machine will you be prompted for your passphrase.
For full details see the `man` page for `ssh-add`.

In the same terminal window, check that your key is now loaded:

```
$ ssh-add -l
```
You should see output like this:
```
2048 SHA256:0y7Oh7J+kN6hPotWCerXsZBlRBL205UMGlJVZ1I0A8c you@somewhere.ac.uk (RSA)

```
If not, you will need to try again before you will be able to log in to a remote host using the key.

### Linux

The Linux platform has different terminal applications available depending on which flavour of Linux and which desktop manager you use. We will use Ubuntu and demonstrate using the `Terminal` app. An alternative would be `xterm`, which is commonly installed on many Linux systems: the process demonstrated here should be similar.

First, initiate an agent to store your key:
```
$ eval $(ssh-agent -s)
Agend pid XXX       (where XXX is some process ID)
```

Now, load your key, having stored it in your `~/.ssh` directory:
```
$ ssh-add ~/.ssh/id_rsa_jasmin
```

Check it's loaded
```
$ ssh-add -l
```
You should see output like this:
```
2048 SHA256:0y7Oh7J+kN6hPotWCerXsZBlRBL205UMGlJVZ1I0A8c you@somewhere.ac.uk (RSA)

```
If not, you will need to try again before you will be able to log in to a remote host using the key.

### Network Considerations

### Graphical desktop



