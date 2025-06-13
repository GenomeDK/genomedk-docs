---
title: Accessing data from Denmark Statistics
---

# Introduction and limitations

The DST zone on GenomeDK is closed zone with additional restrictions due to
requirements from DST:

* The zone can only be accessed through DST's DDV (Danmarks Datavindue). This
  means that you will be connecting to GenomeDK through two virtual desktops
  (one from DDV and then one from GenomeDK, inside the first one). It also
  means that there's no copy-paste available between your computer and the
  virtual desktop.
* There is no Internet connectivity whatsoever (i.e., it's not possible to
  install software with Conda or pull a GitHub repository).
* DST controls which users must access a projects. This means that a project
  owner is not able to add users to a project themselves.
* Data that should leave the zone must be uploaded to DST and it will go
  through the usual DST verification process.
* You must request one user per DST project.

Another very substantial limitation is that your own data is not allowed to
be copied directly into your project folder in the DST zone. Thus, you
cannot join your DST data set with other datasets.

# Working in the DST zone

To get started, you must request a user in the DST zone.

As usual, to start a project on GenomeDK you will use the `gdk-project-request`
command to request a project folder:

```bash
$ gdk-project-request my-project
```

When the project folder has been approved and created, it must be linked to the
DST project ID that DST has given you. DST will also have given you a
secret/access identifier, that couples you to the DST project ID. To link your
project folder to a DST project, run:

```bash
$ gdk-dst-project-link my-project 1234567 verysecretsecret
The project folder 'my-project' is now linked to DST project '1234567'.
```

Note that only the project owner can link a project folder to a DST project.
Linking the project is a one-time thing. You will not have to do this again.

Other persons that need to access the project folder must also request a
user for the DST zone. When created, they can "join" your linked project
folder using:

```bash
$ gdk-dst-project-join my-project othersecret
You have now been added to the project! Remember to log out and log in again.
```

Where `othersecret` is the secret the person received from DST. This
authenticates the user's access to the project.

When a project is linked and you're a member of the project, you can list
the DST data files that are available for your project:

```bash
$ gdk-dst-delivery-list
delivery id  file id
423874924    abc
```

This will list a delivery ID and file ID that you can use to retrieve the
file:

```bash
$ gdk-dst-delivery-retrieve 423874924 abc
```

If the file is large, this may take a while. The retrieved file will be
put in a read-only directory under your project folder called "dst".

When you need to get data out, it must go through DST's verification
process. So first you will have to upload the file to your working area
at DST:

```bash
$ gdk-dst-file-upload myresult.tar.gz
```

After this, the process is the same as for a normal DST project.
