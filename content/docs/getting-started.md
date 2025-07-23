---
title: Getting started
weight: 20
---

This page will tell you everything you need to know to get up and
running on GenomeDK. However, we assume that you have some experience
with the command line/terminal.

# Get access to the cluster {#request_access}

You should check out our [terms of service](/terms).

To request a user, fill out the [user request
form](https://console.genome.au.dk/user-requests/create/).

Once you've been granted access, you'll receive an e-mail. You'll
then be able to connect to the cluster.

# Connecting to the cluster {#connecting_to_the_cluster}

GenomeDK is divided into multiple *zones*. Most users belong to the open
zone. If you're in doubt about which zone you belong to, check your
account confirmation e-mail. If it doesn't mention a specific zone, you
belong to the open zone. If still in doubt, please contact support.

There are three ways to connect to GenomeDK:

* [Connecting with SSH (open zone)](#ssh)
* [Connecting with GenomeDK Desktop (open zone)](#desktop)
* [Connecting with NoMachine (closed zones)](#zone_connect)

In any case, you must first [prepare for two-factor authentication](#2fa).

## Prepare for two-factor authentication {#2fa}

You must first install an authenticator app on your phone (if you don't already
have one). Popular authenticator apps include:

* Microsoft Authenticator
* Google Authenticator
* FreeOTP

All of these apps will allow you to scan a QR code and generate tokens for
future logins.

## Connecting to the open zone with SSH {#ssh}

{% warning() %}
On your first login, you must set up two-factor authentication. If you do not
set up two-factor on the first login, you will not be able to access your
account. Read the instructions to the end before logging in for the first time.
{% end %}

On Linux, open the terminal of your choice. On macOS, you may use `Terminal.app`
which can be found in the `/Applications/Utilities` folder. In both cases, you
should now be able to log in to the frontend by typing this command:

```bash
[local]$ ssh USERNAME@login.genome.au.dk
```

On Windows, you have multiple options. On Windows 10, open `PowerShell`. You
should then be able to type:

```bash
[local]$ ssh.exe USERNAME@login.genome.au.dk
```

Older versions of Windows do not include the `ssh` command and thus you will
need to install an alternative yourself. We recommend
[MobaXterm](https://mobaxterm.mobatek.net/).

### Set up two-factor

You must now set up two-factor authentication. Run the following command on
GenomeDK:

    gdk-auth-show-qr

This will show a QR code in your terminal. Open the the authenticator app on
your phone and scan the QR code.

## Connecting via the GenomeDK Desktop {#desktop}

GenomeDK Desktop provides access to a graphical desktop environment (virtual
desktop) running on the frontend node of the open zone. The Desktop is available
directly in your browser.

* Go to the [GenomeDK Desktop](https://desktop.genome.au.dk/) and log in with
  your usual GenomeDK credentials.
* Choose the service you wish to connect to (in most cases "Frontend - Open", to
  access the frontend in the open zone).
* If this is your first login, you will be guided through the process of setting
  up two-factor authentication.

Once logged in, a virtual desktop will appear within a few seconds.

Please note that the session **should not be used for heavy computations**.
Instead, submit a job to the queuing system inside your Desktop session.

You can [learn more about using the Desktop here](@/docs/using-graphical-interfaces.md#desktop).

## Connecting to a closed zone {#zone_connect}

{% warning() %}
On your first login, you must set up two-factor authentication. If you do not
set up two-factor on the first login, you will not be able to access your
account. Read the instructions to the end before logging in for the first time.
{% end %}

Download and install the remote desktop client for your operating system on your
local machine.

- [Download client for Windows](https://www.nomachine.com/download/download&id=8)
- [Download client for macOS](https://www.nomachine.com/download/download&id=7)
- [Download client for Linux](https://www.nomachine.com/download/linux&id=1)

Download the connection file for the zone you wish to connect to:

* [iPSYCH](/zones/ipsych.nxs) ([guidelines](/assets/iPSYCH_Guidelines_GDK_2021_04_13.pdf))
* [Brain](/zones/brain.nxs)

Using the login information received in your mailbox. Login by entering your
username and password.

Assuming you entered correctly you will get access to the virtual desktop.

### Set up two-factor

Open the the authenticator app on your phone and scan the `QRCode.png` located
on your NoMachine desktop. From now on you will need to generate a one-time
password with the authenticator app every time you log in.

# I forgot my password

If you forgot your password, send an e-mail to support to request a password
reset. You will receive a password reset mail with a new, temporary password.

You should change the temporary password immediately after logging in (see the
next section).

# Change your password {#change_password}

You may change your password at any time using the `gdk-auth-change-password`
command.

```bash
[fe-open-01]$ gdk-auth-change-password
```

It will ask you for your current password, then ask what your new password
should be. Finally, it will ask you to confirm your new password by typing it
again.

# Public-key authentication

{% note() %}
These instructions are for Mac/Linux only.
{% end %}

A public-key setup is a way to be able to access one computer from
another computer with SSH, but without typing a password every time you
want to log in.

On your own computer, open the terminal of your choice and type:

```bash
[local]$ ssh-keygen -t ed25519 -q -N ""
```

This will generate a private/public key-pair with no password. If you
have a key already, you can just use that (the command will warn you
if you do).

Now copy the public key to GenomeDK:

```bash
[local]$ ssh-copy-id -i ~/.ssh/id_ed25519 <username>@login.genome.au.dk
```

You will be asked to enter your password for the cluster to transfer the
public key.

You should now be able to log in to the cluster without typing your password.
Test this by runnning:

```bash
[local]$ ssh <username>@login.genome.au.dk
```

You should not be prompted for a password this time.

# Using a terminal multiplexer

Using a terminal multiplexer allows you to keep your SSH session open, even when
you disconnect from the cluster. You can even reconnect from a different
computer and get your session back. This is especially useful when downloading
large amounts of data, as you can keep the download running even if your
connection to GenomeDK is lost, or if intentionally logging out.

We recommend that you use either `tmux` or `screen`.

-   [tmux](https://github.com/tmux/tmux/wiki)
-   [screen](https://www.gnu.org/software/screen/manual/screen.html).


# Cite us!

We provide GenomeDK as a resource to research. If you publish results
from computations performed on GenomeDK, it is important that you
acknowledge/cite GenomeDK in your publications.

We recommend phrasing it like this:

> *Some/all of the computing for this project was performed on the
> GenomeDK cluster. We would like to thank GenomeDK and Aarhus
> University for providing computational resources and support that
> contributed to these research results.*
