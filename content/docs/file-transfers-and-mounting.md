---
title: File transfers and mounting
weight: 37
---

This section covers ways to access your data on GenomeDK, as well as various ways to transfer data to/from GenomeDK.

If you are in a closed zone, you must use the data lock to import and export data. This is also covered in this section.

# Accessing your files locally (mounting) {#mounting}

You can access your files on GenomeDK locally by a process called *mounting*.
Mounting the GenomeDK filesystem locally makes it possible to access and edit
your files as if they were located in a folder on your own harddrive.

Unfortunately, mounting over SSH does not work on Windows. If you're on Windows
you can use [MobaXterm](https://mobaxterm.mobatek.net/) or one of the
alternatives listed [here](#copying_data).

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

You can now copy files to and from the cluster by simple drag-and-drop.

# Transferring data {#copying_data}

Users in the open zone can freely transfer files to and from GenomeDK. However,
users in a closed zone must use the **data lock** to import and export data. See
[Using the data lock](#using_the_data_lock).

{% note() %}
When downloading files to GenomeDK, always run the download on the frontend. You
should never submit a download as a job.
{% end %}

## From your own machine to/from the cluster (SFTP)

You can transfer data to/from GenomeDK using any SFTP-compatible client, for example:

- [Filezilla](https://filezilla-project.org/) [Linux/macOS/Windows]
- [Cyberduck](https://cyberduck.io/) [macOS]
- [MobaXterm](https://mobaxterm.mobatek.net/) [Windows]
- [WinSCP](https://winscp.net/eng/index.php) [Windows]

In any case, you must connect to host `login.genome.au.dk` and port 22.

## From your own machine to/from the cluster (scp/rsync)

You can also use `scp` and `rsync` to transfer data.

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

## From the Internet to the cluster (HTTP/HTTPS)

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

## To/from the Internet to the cluster (FTP)

To transfer data using the [(S)FTP
protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol), you may use
`lftp`, which is pre-installed on GenomeDK.

Start an interactive session from the frontend:

```bash
[fe-open-01]$ lftp ftp://<remote username>@<remote host>
```

You will be asked to enter your password for the remote user.

Once connected, you can run the following commands:

| Command                 | Description                                       |
| ----------------------- | ------------------------------------------------- |
| `ls`                    | List files in current directory on the FTP server |
| `cd <dir>`              | Change directory on the FTP server                |
| `lcd <dir>`             | Change local directory                            |
| `get <file>`            | Download a single file                            |
| `put <file>`            | Upload a single file                              |
| `mget <files>`          | Download multiple files (supports wildcards)      |
| `mput <files>`          | Upload multiple files (supports wildcards)        |
| `mirror <src> <dst>`    | Recursively download a directory                  |
| `mirror -R <src> <dst>` | Recursively upload a directory                    |
| `bye`                   | Exit the session                                  |

To upload a file from GenomeDK to the remote host:

```bash
lftp> put mydata.fastq
```

To download multiple files from the remote host to GenomeDK:

```bash
lftp> mget *.fastq
```

If you're uploading or downloading very large files, it may speed up things if
you use parallel transfers:

```bash
lftp> pput -n 4 bigfile.fastq
lftp> pget -n 4 bigfile.fastq
```

Usually, 4-8 parallel transfers is enough to provide a dramatic speed-up.
Increasing the number of transfers too much will cause the transfer to
become slower. Never run more than 16 parallel transfers.

To synchronize a directory on GenomeDK to the remote:

```bash
lftp> mirror -R /faststorage/project/myproject/data/foo .
```

If a transfer is interrupted, lftp can continue where it left off. Use the `-c`
(continue) option with the `get`, `put`, or `mirror` commands. For example:

```bash
lftp> mirror -c -R /faststorage/project/myproject/data/foo .
```

When you're done transferring files, you can exit the session with:

```bash
lftp> bye
```

# Using the data lock {#using_the_data_lock}

The data lock is used in closed zones, where data cannot be transferred out of GenomeDK directly via the methods described above. Instead, files must be exported and the zone owner must then approve the export. When approved, you can then access the exported files over SFTP.

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
