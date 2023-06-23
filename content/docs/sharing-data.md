---
title: Sharing data
weight: 70
---

Data shares allow you to easily share data with collaborators or services that
do not have access to GenomeDK.

{% warning() %}
Data shares, of course, do not work in closed zones.
{% end %}

# Creating a share

Creating a share is easy, just run:

```bash
[fe-open-01]$ gdk-share-create
wiKdTt3oFek      /faststorage/share/wiKdTt3oFek.tmp
```

The command outputs two things: an identifier, which uniquely identifies
your share, and a path on the filesystem. You can now copy the data that
you wish to share to the outputted path. For example:

```bash
[fe-open-01]$ cp mydata.tar.gz /faststorage/share/wiKdTt3oFek.tmp/
```

In this example we copy the file `mydata.tar.gz` to the share.

You can inspect the share with `ls`.

```bash
[fe-open-01]$ ls -l /faststorage/share/wiKdTt3oFek.tmp
total 42
-rw-rw-r-- 1 das das 42 2022-05-17 10:21 mydata.tar.gz
```

When you have copied all of the files you wish to share to the share
folder, it's time to publish it.

# Publishing a share

To make the data available outside of GenomeDK, you must publish your
share.

```bash
[fe-open-01]$ gdk-share-publish <share id>
```

Continuing the example above, we would run:

```bash
[fe-open-01]$ gdk-share-publish wiKdTt3oFek
https://share.genome.au.dk/JTTwInSMXqU
```

Note that publishing the share may take a while, especially if you share
many small files. When the share has been published, you receive a link
to the share. Any person with the link can access the share. In this
case we got the link:

> <https://share.genome.au.dk/JTTwInSMXqU>

(The link won't work as the share has been deleted).

The link will be available for 60 days after which the share will be
deleted. If you need the share to be available for longer you must
contact support.

# Downloading files from a share

You can download files with any client that supports HTTPS, which means
that any normal Internet browser will work. If you shared many or very
large files, or a browser is not available, e.g. if your collaborator is
downloading files from your share to another HPC system, it is easier to
use `wget`:

```bash
$ wget --mirror --no-parent --no-host-directories https://share.genome.au.dk/JTTwInSMXqU
```

This will download all files in the share.

# Listing shares

You can get a list of your shares:

```bash
[fe-open-01]$ gdk-share-list
id              url                                         path                                state           expires
wiKdTt3oFek     https://share.genome.au.dk/JTTwInSMXqU      -                                   published       2022-07-16
```

Since we already published our share, the folder on GenomeDK is no
longer available.

# Deleting a share

If you no longer need a share you can either wait for it to expire or
delete it manually. You can delete a share with this command:

```bash
[fe-open-01]$ gdk-share-delete wiKdTt3oFek
Removed wiKdTt3oFek
```

This may take a while if the share contained many or large files.
