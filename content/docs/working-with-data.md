---
title: Working with data
weight: 60
---

On your laptop, all files reside on your local hard disk. However, on GenomeDK
that is not the case. To achieve high performance and accommodate the huge
amounts of data located on the cluster, data is saved on network file systems.

# Where to put your data {#data_locations}

Each of these file systems have their own advantages and disadvantages. Thus,
you need to put your data on the right file system to utilize the cluster
optimally.

## /home/\<username\>

Your home folder is on a file system called NFS. This file system handles many
small files well, but not big files. It's also rather slow to access this file
system from many compute nodes at the same time and your home folder is limited
to 100 GB.

We do *not* recommend storing raw data files, temporary files or results on this
file system. However, it's fine for small documents like notes, programs and
your Conda installation.

This location IS NOT eligible for backup. Instead we perform regular snapshots
(see the section on [snapshots](#snapshots)).

## /faststorage/project/\<project name\>

All projects get their own folder on fast storage. All files related to the
project should be placed in this folder. Project folders have no quota and can
be accessed by all members of the project.

This location IS eligible for backup.

## /faststorage/home/\<username\>

Users created before June 23, 2022 have a home folder located on faststorage at
`/faststorage/home/<username>`. More recent users do not have this directory and
are instead encouraged to use project folders to organize their data.

There is no limit on the amount of data that can be stored in this folder, but
the data can only be accessed by your user.

This location IS eligible for backup.

## /scratch/$SLURM_JOB_ID, $TMPDIR, $TMP

All jobs get access shared, local disk. Files written to this space are only
available on the given node (that is, you can not access files written here from
other nodes).

This folder is deleted when the job finishes! Any files written here, that you
wish to keep, should be moved to *faststorage* as the last step in your job
script.

Use this for (1) temporary files that are not needed later, or (2) for output
files that are written in small chunks.

This location is NOT eligible for backup.

# Backing up data {#backup}

We provide backup on to disk on a remote site to all users. To back up a file,
it should be put in a directory called either `BACKUP`, `Backup` or `backup`.
The directory can be located in any other directory, but only some locations are
eligible for backup.

Data is backed up once per week and snapshots are kept for 14 days.

{% warning() %} Do not back up temporary data files that can easily be
reproduced. Computation is cheap, but backup is expensive. The backup is meant
for scripts/source code and important raw data. {% end %}

# Snapshots {#snapshots}

All home folders are automatically snapshotted. As a user you do not have to do
anything to enable this.

Snapshots do not provide the same data safety as a backup since the data is not
stored at an offsite location. Instead, a snapshot of the data is taken on a
regular basis and stored on the local server. This means that if you e.g.
deleted a file by mistake, the file can be recovered from a previous snapshot.

Snapshots are currently taken with the following intervals and retention times:

-   15 minutes, last 4 are kept
-   1 hour, last 24 are kept
-   24 hours, last 31 are kept
-   Weekly, last 8 are kept
-   Monthly, last 12 are kept

# Accessing your files locally {#mounting}

You can access your files on GenomeDK locally by a process called *mounting*.
Mounting the GenomeDK filesystem locally makes it possible to access and edit
your files as if they were located in a folder on your own harddrive.

Unfortunately, mounting over SSH does not work on Windows. If you're on Windows
you can use [MobaXterm](https://mobaxterm.mobatek.net/) or one of the
alternatives listed in [Copying data](#copying_data).

- On distros with the `apt` package manager (Ubuntu, Mint etc.):

  ```bash
  [local]$ apt-get install sshfs
  ```

- On distros with the `yum` package manager (Fedora, CentOS etc.):

  ```bash
  [local]$ yum install sshfs
  ```

- On macOS, download and install the *SSHFS* and *FUSE for macOS* packages from
  the [OSX FUSE](https://osxfuse.github.io/) website.

Create a directory where the filesystem will be mounted:

```bash
[local]$ mkdir ~/GenomeDK
```

Now mount the filesystem by running this command:

```bash
[local]$ sshfs USERNAME@login.genome.au.dk:/home/USERNAME ~/GenomeDK
    -o idmap=none -o uid=$(id -u),gid=$(id -g)
    -o umask=077 -o follow_symlinks
```

Where *USERNAME* should be replaced with your GenomeDK username. You should now
be able to access your files on GenomeDK by going to the `~/GenomeDK` directory
on your computer.

To unmount the directory, run:

```bash
[local]$ umount ~/GenomeDK
```

# Copying data {#copying_data}

Users in the open zone can freely transfer files to and from GenomeDK. However,
users in a closed zone must use the **data lock** to import and export data. See
[Using the data lock](#using_the_data_lock).

## From your own machine to/from the cluster

If you [mounted](#mounting) GenomeDK on your computer, you can copy files to and
from the cluster by simple drag-and-drop. Otherwise you can use one of the
solutions listed here or one of these alternatives:

- [Filezilla](https://filezilla-project.org/) [Linux/macOS/Windows]
- [Cyberduck](https://cyberduck.io/) [macOS]
- [MobaXterm](https://mobaxterm.mobatek.net/) [Windows]
- [WinSCP](https://winscp.net/eng/index.php) [Windows]

You may also use the command line.

To copy a single file from your computer to the cluster:

```bash
[local]$ scp myfile.txt login.genome.au.dk:path/to/destination/
```

On Windows, replace `scp` with `scp.exe`.

To copy a single file from the cluster to your computer:

```bash
[local]$ scp login.genome.au.dk:/path/to/file .
```

If you want to copy an entire folder to/from the cluster you will want to use
`rsync` instead. To copy a folder from your computer to the cluster:

```bash
[local]$ rsync -e ssh -avz /path/to/data user@login.genome.au.dk:data
```

Windows doesn't have `rsync` installed, so you must resort to one of the options
listed above.

If you want to upload a folder, but also delete files that you deleted in the
source folder from the destination:

```bash
[local]$ rsync -e ssh -avz --delete /path/to/data user@login.genome.au.dk:data
```

If you want to download data from the cluster:

```bash
[local]$ rsync -e ssh -avz --delete /location/data user@login.genome.au.dk:data
```

You may want to add the `--progress` flag to all of these commands if you're
downloading/uploading large amounts of data.

## From the Internet to the cluster

You can use `wget` to download data from the Internet to the cluster:

```bash
[fe-open-01]$ wget -c --timeout=120 --waitretry=60
    --tries=10000 --retry-connrefused URL
```

Remember to replace `URL` with the thing you want to download.

When downloading large files you are encouraged to limit the progress output to
avoid stressing the system, *especially* when you're sending the progress output
to a file:

```bash
[fe-open-01]$ wget -c --progress=dot:giga --timeout=120 --waitretry=60
    --tries=10000 --retry-connrefused URL
```

# Using the data lock {#using_the_data_lock}

## Exporting files {#gdk-export}

If you have many files you should pack them up in a tar/zip. Run `gdk-export` on
the file to be exported.

When the export has been approved you can download the file with:

```bash
[local]$ sftp <username>@185.45.23.195:test.fa .
```

Alternatively, use a graphical SFTP client such as WinSCP, FileZilla or
Cyberduck with host 185.45.23.195 and port 22.

## Listing pending exports

You can list your pending (unapproved) exports with `gdk-export-list`.

## Deleting pending exports

You can delete a pending export with `gdk-export-delete <filename>`.

## Importing files {#gdk-import}

Transferring data into a closed zone isn't restricted, but we still have to go
through an intermediate step for security reasons.

First, upload the file to the data lock:

```bash
[local]$ echo put test.fa . | sftp <username>@185.45.23.195
```

Alternatively, use a graphical SFTP client such as WinSCP, FileZilla or
Cyberduck with host 185.45.23.195 and port 22.

You can now access the file from the inside at `/data-lock/public/<username>`.
However, the file will be read-only. To use the file, copy it to some other
location, for example a relevant project folder.

## Cleanup

Files in the public part of the data lock are automatically deleted after 60
days.

# Editing files

If you [mounted](#mounting) GenomeDK on your computer, you can edit files
directly by just opening them with your prefered text editor on your computer.
Otherwise you can use one of the solutions listed here.

## Nano, vim, emacs

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

Likewise, [vim](https://www.vim.org/) and
[emacs](https://www.gnu.org/software/emacs/index.html) are already installed on
the cluster. Documentation for each editor can be found on their respective
websites.

## Gedit with X-forwarding

If you want a graphical user interface and a more familiar editing experience,
you may use the `Gedit` editor with
[X-forwarding](/docs/installing-software/#xforwarding). Make sure that you are
connected to the cluster with X-forwarding enabled. Then run:

```bash
[fe-open-01]$ gedit
```

This will open the `Gedit` editor in a new window. Since the editor runs on the
frontend, you have access to all of your files on the cluster.

# Encrypting sensitive data

If you need to transfer sensitive data (for example human genomes) out of the
cluster you may want to encrypt the data first. Encrypting the data makes it
impossible for strangers to look at it without decrypting it, which requires a
password chosen by you.

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

# Prevent accidental changes to data

Put the data in a separate folder and run:

```bash
[fe-open-01]$ chmod -R a-w <folder name>
```

Now you can't change, add or remove files in that folder or any of its
subfolders.
