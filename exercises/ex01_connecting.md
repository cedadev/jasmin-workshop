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

1. Connect to a login server using a terminal client
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



