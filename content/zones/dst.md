---
title: Accessing data from Denmark Statistics
---

# Introduction and limitations

The DST zone on GenomeDK is a closed zone configured to comply with DST requirements. This means:

* The zone can only be accessed through DST's remote desktop. This
  means that you will be connecting to GenomeDK through two virtual desktops
  (one from DDV and then one from GenomeDK, inside the first one). It also means
  that there's no copy-paste available between your computer and the virtual
  desktop.
* There is no Internet connectivity (i.e., it's not possible to install software
  with Conda or pull a GitHub repository).
* DST controls which users must access a projects. This means that a project
  owner is not able to add users to a project themselves.
* Data that should leave the zone must be uploaded to DST and it will go through
  the usual DST verification process.
* You must request one user per DST project.

Be aware that your own data is not allowed to be copied directly into your
project folder in the DST zone. Thus, you cannot join your DST data set with
other datasets.

# Requesting a user

To get started, you must request a user in the DST zone.

Go to the [user request
form](https://console.genome.au.dk/user-requests/create/) and pick the "DST"
zone. Then fill out and submit the form. Remember to note your DST project ID in
the "Reason" field. You'll receive an e-mail when your account has been approved
and created.

Users are project-specific, so you must request a user for each project you wish to access.

# Logging in

To log in, you must use your DST credentials to access
[remote.dst.dk](https://remote.dst.dk), a remote desktop solution provided by
DST. Please contact DST support if you have any doubts or issues accessing the
remote desktop.

Once logged in, open a browser (Microsoft Edge or Google Chrome) and enter the address XXXYYYZZZ. This will take you to GenomeDK's remote desktop
solution where you can log in with your GenomeDK credentials (username and
password from when you requested your user).

# Initial project setup

When your project/data is ready, DST will supply the following information to you:

* A project ID that uniquely identifies the project.
* An "access identifier", a secret string that you must use to identify yourself on GenomeDK.

With this information in hand, you're ready to set up your project on GenomeDK.

The following only needs to be done once, by one user, for each project.

To start a project on GenomeDK you will use the `gdk-project-request`
command to request a project folder:

```bash
[fe-dst-01]$ gdk-project-request my-project
```

When the project folder has been approved and created, it must be linked to the
DST project ID that DST has given you. To link your project folder to a DST project, run:

```bash
[fe-dst-01]$ gdk-dst-project-link my-project 1234567 verysecretsecret
The project folder 'my-project' is now linked to DST project '1234567'.
```

Note that only the project owner can link a project folder to a DST project.

# Joining a project

If you need to access a project folder that has been linked to a DST project, you must also request a user for the DST zone (see the first section).

When created, you can "join" a linked project folder using:

```bash
[fe-dst-01]$ gdk-dst-project-join my-project othersecret
You have now been added to the project! Remember to log out and log in again.
```

Where `othersecret` is the access identifier you received from DST.

# Retrieving data deliveries

When a project is linked, members of the project can list the DST data files
(deliveries) that are available for your project:

```bash
[fe-dst-01]$ gdk-dst-delivery-list
delivery id  file id
423874924    abc
```

This will list a delivery ID and file ID that you can use to retrieve the file:

```bash
[fe-dst-01]$ gdk-dst-delivery-retrieve 423874924 abc
```

The retrieved file will be put in a read-only directory under your project
folder called "dst".

When you need to get data out, it must go through DST's usual verification
process. So first you will have to upload the file to your working area at DST:

```bash
[fe-dst-01]$ gdk-dst-file-upload myresult.tar.gz
```

After this, the process is the same as for a normal DST project.

# Frequently asked questions

## When can I request a user on GenomeDK?

You can request a user on GenomeDK as soon as you've received a DST project ID.

## When can I request a project folder on GenomeDK?

You can request a project folder as soon as your user has been created. However, the project folder can only be linked to your DST project once you've received both a DST project ID and access identifier, and when GenomeDK has been informed about the creation of your project.

## How do I export data from the DST zone?

???

## Do I need a data processing agreement with you?

No. In GDPR-terms, GenomeDK is a sub-processor to DST, and that processing is
regulated by a data processing agreement between DST and GenomeDK.

You will have to sign a data processing agreement with DST, where you are the
data controller and DST is the data processor.
