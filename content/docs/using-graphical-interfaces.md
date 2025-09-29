---
title: Using graphical interfaces
weight: 60
---

There's two options for using programs with a graphical user interface
on GenomeDK.

# GenomeDK Desktop (recommended) {#desktop}

The most convenient and reliable way to get a graphical interface on GenomeDK is
through the [GenomeDK Desktop](https://desktop.genome.au.dk/). You can log in
with your existing (open) user credentials and two-factor token.

The Desktop provides a full virtual desktop inside your browser and requires no
software to be installed on your own machine. Once connected, you can access all
of your projects as usual and launch graphical applications directly.

The desktop environment runs on the frontend, so **all of the usual guidelines
about not running computations on the frontend still apply**. However, you can
start an interactive job and launch a graphical application (e.g. Rstudio)
inside the job.

## Session persistence

Desktop sessions are *persistent*, meaning that you can log out of the Desktop and
log in later and all of your applications, windows, etc. will still be available.

However, sessions time out after 72 hours of inactivity (not logging in or using
the session). This kills all processes in the session. Unsaved files will be lost.

## Clipboard

The Desktop runs directly in your browser and is thus limited by browser functionality
and security measures. This is mostly noticeable in the way copy-paste is handled, as
browsers do not allow direct access for the Desktop to manipulate your clipboard.

To paste text from your local computer into the Desktop:

* copy the text as usual on your local computer,
* go to the Desktop and click "Show clipboard" in the top menu,
* paste the text into the text area and click "Hide clipboard",
* inside the Desktop session, focus the application you wish to paste into,
  then right-click and select "Paste".

To copy text from inside the Desktop to your local computer:

* inside the Desktop, select the text you wish to copy,
* click "Show clipboard" in the top menu,
* the text you selected should be present in the text area,
* select the text, right click and select "Copy",
* you can now paste the text into any application on your local computer.

# X-forwarding (legacy) {#xforwarding}

You can use X-forwarding to tunnel individual graphical programs to your local
desktop.

On Linux you simply need to tell SSH that you wish to enable X-forwarding. To do
this, add `-X` to the `ssh` command when logging in to the cluster, for example:

```bash
[local]$ ssh -X USERNAME@login.genome.au.dk
```

You should then be able to open e.g. Firefox on the frontend:

```bash
[fe-open-01]$ firefox
```

Since macOS does not include an X server, you will need to download and
install [XQuartz](https://www.xquartz.org/) on your computer. When
installed, reboot the computer. Now, you just need to tell SSH that you
wish to enable X-forwarding. To do this, add `-X` to the
`ssh` command when logging in to the
cluster, for example:

```bash
[local]$ ssh -X USERNAME@login.genome.au.dk
```

You should then be able to open e.g. Firefox on the frontend:

```bash
[fe-open-01]$ firefox
```

On Windows, we recommend that you use
[MobaXterm](https://mobaxterm.mobatek.net/) which has an integrated X
server.
