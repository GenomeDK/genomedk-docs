---
title: Working with data
weight: 35
---

On your laptop, all files reside on your local hard disk. However, on GenomeDK
that is not the case. To achieve high performance and accommodate the huge
amounts of data located on the cluster, data is saved on network file systems.

# Where to put your data {#data_locations}

Each of these file systems have their own advantages and disadvantages. Thus,
you need to put your data on the right file system to utilize GenomeDK
optimally.

* `/home/<username>`
  * **Filesystem:** NFS
  * **Quota:** 100 GB
  * **Backup:** No
  * **Snapshots:** Yes
  * **Persistent:** Yes, data stays until it is deleted by the user.
  * **Note:** Only you can access this folder. Subfolders can not be shared with other users.
* `/faststorage/project/<project name>` or `/faststorage/jail/project/<project name>`
  * **Filesystem:** BeeGFS
  * **Quota:** None
  * **Backup:** Yes, this location is eligible for backup.
  * **Snapshots:** No
  * **Persistent:** Yes, data stays until it is deleted by the user.
  * **Note:** Can be accessed by all members of the project in question.
* `/tmp/$SLURM_JOB_ID`, `$TMPDIR`, `$TMP`
  * **Filesystem:** XFS
  * **Quota:** Limited the the available scratch disk space on the particular compute node.
  * **Backup:** No
  * **Snapshots:** No
  * **Persistent:** No, data is deleted whenever the job in question finishes.
  * **Note:** Can not be accessed from multiple nodes. Use this for (1) temporary files that
    are not needed later, or (2) for output files that are written in small chunks.

# Backing up data {#backup}

We provide backup to our own disk-based backup solution at a remote site. By
default, *nothing is backed up*.

## Marking files for backup

To back up a file, it should be put in a directory called either `BACKUP`,
`Backup` or `backup`. The directory can be located in any location that is
eligible for backup (see above). You may have many `backup` directories in
such a location.

To check if you have correctly marked data for backup, you can use the `realpath`
command:

```bash
[fe-open-01]$ realpath path/to/file
```

This will output the full, canonical path to the file. If the output contains either
`BACKUP`, `Backup` or `backup`, the file is correctly marked for backup and will be
included in the next backup run.

## Listing backup runs

Backup runs are initiated once per week with a retention period of 14 days.

You can see the time and duration of the last backup run with:

```bash
[fe-open-01]$ gdk-project-events <project name>
```

You may see that one or more of the backup runs for a project have timed out.
This happens when a lot of new data has been added to a project and thus must be
transferred to the backup location. If a run takes more than 120 hours (5 days),
it will time out, but will start where it left off at the next backup run.
Eventually, all of the data will have been synchronized.

## Recommended backup use

It is important to be considerate when using the backup:

* Do not back up temporary data files that can easily be reproduced. Computation
  is cheap, but backup is expensive. The backup is meant for scripts/source code
  and important raw data.
* When data is marked for backup, moving or renaming files and directories will
  cause _a complete re-transfer_ of the data. To the backup mechanism, it's
  simply new data. Please think of data in backup folders as "archived". You may
  add new data and remove files when necessary, but do not modify, rename or
  move the files around.
* Compress files before marking them for backup. For example, store your raw FASTQ
  files outside of backup, but put compressed SPRING files in the backup.

Also, note that marking data for backup will not affect the performance of
accessing the data, as it doesn't move the data to another filesystem. Instead,
the data is copied to the backup location

# Snapshots {#snapshots}

All home folders are automatically snapshotted. As a user you do not have to do
anything to enable this.

Snapshots do not provide the same data safety as a backup since the data is not
stored at an off-site location. Instead, a snapshot of the data is taken on a
regular basis and stored on the local server. This means that if you e.g.
deleted a file by mistake, the file can be recovered from a previous snapshot.

Snapshots are currently taken with the following intervals and retention times:

-   15 minutes, last 4 are kept
-   1 hour, last 24 are kept
-   24 hours, last 31 are kept
-   Weekly, last 8 are kept
-   Monthly, last 12 are kept

Contact support if you need to recover a file from a snapshot.

# Editing files

If you mounted GenomeDK on your computer, you can edit files directly by just
opening them with your prefered text editor on your computer. Otherwise you can
use one of the solutions listed here.

## Terminal-based editors

With editors like `nano`, `vim` and `emacs` you can edit files directly on the
cluster. The editor itself also runs on the cluster and thus your editor
settings etc. are conserved, even if you log in from another computer. Also,
these editors don't require a graphical user interface, so you don't need
X-forwarding or VNC.

The `nano` editor is by far the simplest editor of three, but also the least
powerful. However, it's just fine for quickly editing scripts or looking at
output files. The documentation for `nano` can be reached by running the
command:

```bash
[fe-open-01]$ man nano
```

You can open `nano` by running:

```bash
[fe-open-01]$ nano name-of-file.txt
```

Documentation for each editor can be found on their respective websites.

## Gedit

If you want a graphical user interface and a more familiar editing experience,
you may use the *Gedit* editor through the [GenomeDK
Desktop](/docs/using-graphical-interfaces/#desktop).

Log in to the desktop and go to `Applications" > Accessories > Text Editor`.
This will open the *Gedit* editor in a new window. Since the editor runs on the
frontend, you have access to all of your files on the cluster.

# Encrypting data

Encrypting data makes it impossible for strangers to look at it without
decrypting it, which requires a password chosen by you.

Encrypt:

```bash
[fe-open-01]$ openssl aes-256-cbc -a -salt -in data.txt -out data.txt.enc
```

This will encrypt `data.txt` and write the encrypted data to `data.txt.enc`. You
will be prompted for a password which is needed to decrypt the file again.

Decrypt:

```bash
[fe-open-01]$ openssl aes-256-cbc -d -a -in data.txt.enc -out data.txt.new
```

This will ask for the password used to encrypt the file. The decrypted contents
are written to `data.txt.new`.

{% note() %}
Note that there are more convenient and modern tools for file encryption
available, such as [age](https://github.com/FiloSottile/age).
{% end %}

# Prevent accidental changes to data

Put the data in a separate folder and run:

```bash
[fe-open-01]$ chmod -R a-w <folder name>
```

Now you can't change, add or remove files in that folder or any of its
subfolders.
