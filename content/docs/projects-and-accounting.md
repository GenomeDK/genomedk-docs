---
title: Projects and accounting
weight: 30
---

A project folder is a workspace with access control and usage management tools.
You can request project folders as you need them and manage access to project
folders with the tools covered in this section. A project folder is how multiple
users on GenomeDK can collaborate.

Project folders do not have any resource limits, but we send notifications to the
project owner if resource usage in the project has increased significantly, as
well as monthly usage summaries.

# Listing projects {#collaborating}

You can list all of the projects you're a member of:

```bash
[fe-open-01]$ gdk-project-list
```

You can also list all projects owned by you:

```bash
[fe-open-01]$ gdk-project-list -f owner
```

Or just list all projects:

```bash
[fe-open-01]$ gdk-project-list -f all
```

# Requesting a project

Data sharing between users can only be accomplished through dedicated project
folders to which only certain users have access.

Run the following command to request a new project folder:

```bash
[fe-open-01]$ gdk-project-request -g <project name>
```

where **project name** is the desired name of the new project.

{% warning() %} When you request a project you're officially the project owner.
This means that you're responsible for the resources used by the project. Thus,
you should familiarize yourself with the tools provided for monitoring the
resources used by you and your projects (described later). {% end %}

When your request has been accepted, you will receive an e-mail with further
instructions.

# Managing a project

Project owners and project members with administrative rights can manage their
own projects.

Add a user to a project:

```bash
[fe-open-01]$ gdk-project-add-user -g <project name> -u <username>
```

Remove a user from a project:

```bash
[fe-open-01]$ gdk-project-remove-user  -g <project name> -u <username>
```

Grant administrative rights to a user in a project:

```bash
[fe-open-01]$ gdk-project-promote-user -g <project name> -u <username>
```

Revoke a users' administrative rights to a project:

```bash
[fe-open-01]$ gdk-project-demote-user -g <project name> -u <username>
```

Obtain a list of events for one of your projects. This will list membership
changes, backup runs, and other events related to the project:

```bash
[fe-open-01]$ gdk-project-events <project name>
```

List various information about the project, e.g. who the current project owner
is, when the project was created, etc. Also provides an overview of the total
number of billing hours used by the given project, as well as the current
storage and backup usage:

```bash
[fe-open-01]$ gdk-project-show <project name>
```

Provides a detailed listing of the resources used by all projects owned by you:

```bash
[fe-open-01]$ gdk-project-usage
```

To get help for any of the commands, run the command with `-h`, for example:

```bash
[fe-open-01]$ gdk-project-usage -h
```

{% note() %}
Don't know the username of one of your collaborators? You can use
the `finger` command to get information about any user on GenomeDK:

```bash
[fe-open-01]$ finger <name, username or mail>
```

For example, to find all users with "anders" in their name:

```bash
[fe-open-01]$ finger anders
aeh             Anders Egerup Halager <aeh@birc.au.dk>
anders          Anders Boerglum <anders@biomed.au.dk>
...
```

{% end %}

# Data access in project folders

All members can add, edit, and delete files in the project folder unless
restrictions have been set on specific files/subfolders. If you have data that
you want to keep private to your user, but that belongs to in the project folder
anyway, you can set permissions so that only you can read, write, and execute
the file with this command:

```bash
[fe-open-01]$ chmod go-rwx <files>
```

The `chmod` command changes file permissions. The first parameter specifies that
groups (g) and others (o) should have their read (r), write (w), and execute (x)
permissions removed (-). This means that it's only the owner of the file who can
now access it.

If you want to change file permissions on all files in a folder, use:

```bash
[fe-open-01]$ chmod -R go-rwx <folder>
```

The `-R` means "do recursively". So it will find all files in that folder and updates
the file permissions.


**Note**, that you cannot change file permissions for a specific user to access
that data, you can only change "groups" (`g`) and "others" (`o`).

You can read more about `chmod` [here](https://en.wikipedia.org/wiki/Chmod).
