---
title: Getting set up for the JASMIN Workshop
author: Matt Pritchard
---

## Introduction
This exercise is for participants of JASMIN Workshop training events.

It helps you set up your computer with the software and training account credentials needed to undertake the exercises in the workshop.

For the [reasons explained below](#own-vs-training-account), we provide workshop participants with a temporary training account for the duration of the workshop event (see also [training account expiry](#training-account-expiry)).

Please also see the set of [FAQs](#faq).

## Instructions

These instructions are in 3 parts

1. Common instructions to obtain your training account credentials
1. Specific instructions (for the computer you have in front of you) to set up your environment
1. Testing your connection

Let's get started...

(Click the arrow symbols to expand the sets of instructions in each case)

## 1. Common instructions: extracting credentials

<details>
   <summary id="extracting">Extracting the credentials sent to your registered email</summary>

   - Locate the email sent by the JASMIN team using OneDrive. It should have "shared the folder" in the subject line.
      - If you can't find the email, search for "shared the folder" in your emails, but also check your spam/junk folders before asking for help. 
   - Follow the "Open" link in the email from the JASMIN Team.
   - It may ask you to comfirm the email address and enter a verification code: follow the instructions.
   - You should eventually reach an online view of the folder containing the 4 credential file(s)
      - `username`
      - `passphrase`
      - `id_rsa_jasmin_training`
      - `id_rsa_jasmin_training.pub`
   - Save each of these locally: hover over each item, a 3-dot menu should appear with a "Download" option. Use that to download the file to your default downloads location. We can move the files from there later.
   - It's easiest to download each file separately, otherwise they'll get put into a zip file from where you'll have to extract them individually.
</details>

## 2. Specific instructions: setting up your environment

The same overall process applies to each method, i.e:

   ```mermaid
   flowchart TD
      id1(Store credential files locally) 
      --> id2(Unlock and load private key into local SSH client software)
      --> id3(Use SSH client to connect to remote host)
   ```

Each of the methods involves using a piece of software which provides a "terminal" environment on your computer. For Windows, you may need to download and install this if you don't have the one we recommend, but for Mac and Linux you should be able to use tools already available on your local machine. This software will include an "SSH Agent" which stores your private key, once you've unlocked it with the passphrase, then makes it available for making a conneciton to a remote computer (like a JASMIN login node).

Click the arrow next to each section to expand the instructions:

<details>

   <summary id="windows">Windows instructions</summary>

   - Move the files from the Downloads folder
     - create an empty folder called `ssh` to put these files in: perhaps on your Desktop, but it's up to you.
     - Use File Explorer to drag & drop the 4 files from the Downloads folder to the folder you just made.
     - Don't try to open either of the `id_rsa_jasmin_training*` files: they're not meant to be readable.
     - Try opening the `username` and `passphrase` files in a text editor (e.g. `Notebook`): you'll need them shortly.

   - Download and install "MobaXterm"
   
     This is an emulator of the terminal environment that Mac and Linux users have, and provides the tools you need to connect. There are other options, but we'd recommend this one if you want us to help you with any problems.

     - Go to https://mobaxterm.mobatek.net/
       - Go to [Download](https://mobaxterm.mobatek.net/download.html)
       - Choose the "Home edition", then "Download now"
       - Choose the **installer edition**
       - Right-click the downloaded zip file and choose "extract all"
       - Run the installer, then follow the instructions.

   - Open Mobaxterm, and follow the steps in this video to load your private key and check it's loaded in a terminal session.
     - [mobaxterm setup (video)](#)

</details>

## Test your connection

First, check that your key is loaded:

```bash
ssh-add -l
```

   - Now try a connection to `login2.jasmin.ac.uk`, replacing `USERNAME` with the name of your training account:
   
   > **_NOTE:_**  Don't forget the `-A` option for "agent forwarding". This makes your key available to any onward connections you need to make, after connecting to the login node.

   ```bash
   ssh -A USERNAME@login2.jasmin.ac.uk
   ```

   Once you have connected, try `ssh-add -l` again as above, to check that your key is available for an onward connection.

   Here's what the connection test looks like on Windows, but it's the same commands on Mac & Linux:

   - [connection test with windows & mobaxterm](#)


## FAQ

<details>

   <summary id="own-vs-training-account">Can I use my own JASMIN account?</summary>

   Here's the answer

</details>

<details>

   <summary>I haven't received my account credentials</summary>

   Here's the answer

</details>

<details>

   <summary>Another question</summary>

   Here's the answer

</details>

<details>

   <summary>I can't open the `*.pub` file when I double-click it (on Windows)</summary>

   Here's the answer

</details>
