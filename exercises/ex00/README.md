---
title: Getting set up for the JASMIN Workshop
author: Matt Pritchard
---

## Introduction
This exercise is for participants of JASMIN Workshop training events.

It helps you set up your computer with the software and training account credentials needed to undertake the exercises in the workshop.

For the [reasons explained below](#faq), we provide workshop participants with a temporary training account for the duration of the workshop event. Even if you have your own JASMIN account, please use the training account for the workshop event.

Please also see the set of [FAQs](#faq).

## Instructions

These instructions are in 3 parts:

1. Common instructions to obtain your training account credentials
1. Specific instructions (for the computer you have in front of you) to set up your environment
1. Testing your connection

Let's get started...

## 1. Common instructions: extracting credentials

(Click the arrow to expand the set of instructions)

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
      id1(Store your key locally) 
      --> id2(Load private key into SSH client software)
      --> id3(Use SSH client to connect to remote host)
   ```

Each of the methods involves using a piece of software which provides a "terminal" environment on your computer. For Windows, you may need to download and install this if you don't have the one we recommend, but for Mac and Linux you should be able to use tools already available on your local machine. This software will include an "SSH Agent" which stores your private key, once you've unlocked it with the passphrase, then makes it available for making a conneciton to a remote computer (like a JASMIN login node).

(Click the arrow to expand the relevant set of instructions)

<details>

   <summary id="windows">Windows instructions</summary>

   - Move the 2 `id_rsa_jasmin_training*` key files from the Downloads folder. The `username` and `passphrase` files can stay where they are.
     - create an empty folder called `ssh` to put these files in: perhaps on your Desktop, but it's up to you.
     - use File Explorer to drag & drop the 2 key files from the Downloads folder to the folder you just made.
     - don't try to open either of the `id_rsa_jasmin_training*` files: they're not meant to be readable.
     - try opening the `username` and `passphrase` files in a text editor (e.g. `Notebook`): you'll need them shortly.

   - Download and install "MobaXterm"
   
     This is an emulator of the terminal environment (Mac and Linux have this environment built-in), and provides the tools you need to connect. There are other options, but we'd recommend this one if you want us to help you with any problems.

     - Go to https://mobaxterm.mobatek.net/
       - go to [Download](https://mobaxterm.mobatek.net/download.html)
       - choose the "Home edition", then "Download now"
       - Choose the **installer edition**
       - right-click the downloaded zip file and choose "extract all"
       - run the installer, then follow the instructions.

   - Open Mobaxterm, and follow the steps in this video to load your private key and check it's loaded in a terminal session.
     - [![mobaxterm setup (video)](https://img.youtube.com/vi/qm8PcD24Xsc/0.jpg)](https://youtu.be/qm8PcD24Xsc)

</details>

<details>
  <summary>Mac or Linux instructions</summary>

  In the Mac or Linux environments, it's best to put your SSH-related files in a standard place. This is a directory called `.ssh` in your home directory (the `.` means it's hidden).


  - open the `Terminal` utility (use the search in the top menu bar to find this if you haven't used it before)
  - this should open a command-line terminal, starting in your home directory. The shorthand for your home directory is `~/`

  Check if you have a directory `~/.ssh` already:

  ```
  ls ~/.ssh
  ```

  If this exists already, the `ls` command will list its contents (it could be empty, that's fine).

  If you see `No such file or directory`, make this directory with the command:

  ```
  mkdir -p ~/.ssh
  ```
  and set permissions on it so that it's only read/writable by you:
  ```
  chmod 700 ~/.ssh
  ```

  Now, move the 2 key files `id_rsa_training_jasmin*` from your download location (where your browser puts downloaded files) to the directory you just created. The `username` and `passphrase` files can stay where they are.

  ```
  mv ~/Downloads/id_rsa_training_jasmin* ~/.ssh/
  ```

  Set the permissions on these files to be only read/writable by you:

  ```
  chmod 600 ~/.ssh/id_rsa_training_jasmin*
  ```

  Now, check whether you have an SSH-agent running:

  ```
  ssh-add -l
  ```

  If you see
  ```
  The agent has no identities.
  ```

  that's fine: it's running, but just doesn't have any keys loaded yet. Skip the step below.

  If you see `Could not open a connection to your authentication agent` or `Error connecting to agent` this means you haven't got one running, so you need to start one with the following command:

  ```
  eval $(ssh-agent -s)
  ```

  You're now able to load your private key, as follows:

  ssh-add ~/.ssh/id_rsa_jasmin_training

  Note that it's the private key file (without the `.pub`) extension, that we're loading here.

  You will be prompted for your passphrase: don't try and type it in, copy and paste it from the `passphrase` file which you should have open in a text editor. Similarly, your `username` will be in the corresponding file, where you downlaoded it. You can usually paste by CTRL-V or by right-clicking and choosing "paste", but this may vary depending on your system.

  Be careful not to copy any whitespace either side of the passphrase.
  
  Note that the terminal does not echo back any characters or placeholders for a passphrase. So don't paste it again just because it's not displaying!

  Now, heck with the `ssh-add -l` command as before, and the key fingerprint should be displayed, e.g.

```
ssh-add -l
2048 SHA256:e1rIzWgm0BAF396xNAYc8TdjjSs8IuMyr+iwSryHeb4 fred.bloggs@ncas.ac.uk (RSA)
```

If you don't see this, go back and check the steps above carefully before asking for help.

</details>

## 3. Test your connection

First, check that your key is loaded:

```bash
ssh-add -l
```

You should see your key fingerprint, i.e. something like this:

```
2048 SHA256:e1rIzWgm0BAF396xNAYc8TdjjSs8IuMyr+iwSryHeb4 fred.bloggs@ncas.ac.uk (RSA)
```

Now try a connection to `login2.jasmin.ac.uk`, replacing `USERNAME` with the name of your training account:
   
> **_NOTE:_**  Don't forget the `-A` option for "agent forwarding". This makes your key available to any onward connections you need to make, after connecting to the login node.

```bash
ssh -A USERNAME@login2.jasmin.ac.uk
```

Once you have connected, try `ssh-add -l` again as above, to check that your key is available for an onward connection.

Here's a video showing what the connection test looks like on Windows, but it's the same commands on Mac & Linux:

[![connection test with windows & mobaxterm](https://img.youtube.com/vi/XmwOMbigyf0/0.jpg)](https://youtu.be/XmwOMbigyf0)

### Success?

If:
- you have successfully logged in to the login server
- you have your key available for an onward connection as above

...then you're all set, and you're ready for the rest of the exercises in the workshop.

If not, check through the FAQ below, and make sure you've done everything as per the instructions and videos, then if you're still having trouble, please ask for help.

## FAQ

(Click the arrow to expand each FAQ)

<details>

   <summary id="own-vs-training-account">Can I use my own JASMIN account?</summary>

   For the JASMIN workshop training events, we prefer that you use the supplied training accounts. 

   This is because we have pre-configured each training account with access roles for all the resources you need for the training workshop, including:
    - the `workshop` group workspace
    - the `workshop` LOTUS queue (for responsive wait times during workshops)
    - a corresponding CEDA Archive account with access to certain datasets used in the exercises
    - access to the transfer server `xfer3`
    - access to high-performance data transfer services

    We cannot configure all these resources on a temporary basis, so ask you to use the training account during events. You are welcome to transfer over any data created during a workshop, to your own account (but beware there is a time limit for this, before training accounts are wiped: ask your course organiser for details).

</details>

<details>

   <summary>I haven't received my account credentials</summary>

   - make sure you are checking in the email account which you gave to the course organisers: the training account will be set up with this email address.
   - make sure you have searched for "shared the folder" in your email application. Sometimes emails from OneDrive get hidden.
   - make sure you have checked your spam/junk folders
   - ask your course organiser for help if you still can't find it: it should be possible to get it re-sent.

</details>

<details>

   <summary>I can't open the `*.pub` file when I double-click it (on Windows)</summary>

   That's OK. It's not a file that you need to open. The `.pub` file extension is sometimes recognised by Windows as a Microsoft Publisher file, but this one isn't: it's your public key (part of your public/private key pair).

</details>

<details>

   <summary>Message about "unprotected key"</summary>

   If you see a message like the following, this means that you need to restrict the permissions on your key file so that only you (and no other users on your system) can read your key.

   ```
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   Permissions 0644 for 'id_rsa_jasmin_training' are too open.
   It is required that your private key files are NOT accessible by others.
   This private key will be ignored.

   ```
   You can do this with a command like this (you'll need to do this in a terminal window):
   ```
   chmod 600 <path>/id_rsa_jasmin_training  
   ```
   where `<path>` is wherever you saved your key (see above: this can vary by platform).

   Alternatively (particularly for Windows users), making another copy of the private key file (and deleting the original) can help. You can still go back to the original from the OneDrive email if you need it.

</details>

<details>
  <summary>Message "Agent refused connection"</summary>

  This isn't necessarily a problem.

  If the output of `ssh-add -l` is something like the examples above in the Windows or Mac/Linux instructions, showing your key fingerprint, then you should still be good to go.
</details>

<details>
  <summary>Message "Could not open a connection to your authentication agent" or "Error connecting to agent: No such file or directory"
  </summary>

  This means that you don't have an SSH-agent running, so there isn't an agent to load your key into.

  For windows/mobaxterm, review the setup video to make sure you've got the key loaded correctly.


  For Mac/Linux, you may need to run the following command to start the agent:

```
eval $(ssh-agent -s)
```

You should see output similar to this:

```
agent pid 1234
```

Then try loading your key again with the ssh-add command:

```
ssh-add <path to your key>
```

and enter the passphrase when prompted.

</details>