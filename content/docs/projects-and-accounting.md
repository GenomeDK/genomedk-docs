---
title: Projects and accounting
weight: 30
---

A project folder is a workspace with access control and usage management tools.
You can request project folders as you need them and manage access to project
folders with the tools covered in this section. A project folder is how multiple
users on GenomeDK can collaborate.

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

Do not request a lot of small projects that are related, for example with different 
analyses of the same data. Instead, make one larger or more comprehensive one. 

- No-go examples: Three projects `bulkRNA_mouse`, `bulkRNA_human`, `bulkRNA_apes`
  with the same or similar users in that project, and where each data came from
  the same research study.
- Good example: One project `bulkRNA`, that has subfolders `mouse`, `human`, `apes`.

Why structure it this way? Because for legal reasons, projects cannot be deleted,
so all these small projects will start accumulating and filling out the 
`faststorage/project/` with these small project names.

# Managing a project

Project owners and project members with administrative rights can manage their
own projects.

You can list various information about the project, e.g. who the current project
owner is, when the project was created, etc. Also provides an overview of the
total number of billing hours used by the given project, as well as the current
storage and backup usage:

```bash
[fe-open-01]$ gdk-project-show <project name>
```

Obtain a list of events for one of your projects. This will list membership
changes, backup runs, and other events related to the project:

```bash
[fe-open-01]$ gdk-project-events <project name>
```

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

# Resource monitoring

Project folders do not have any resource limits by default. However, project
owners can monitor the resource usage of their projects with:

```bash
[fe-open-01]$ gdk-project-usage [-o <username>] [-p <project name>] [-y <year>] [-u] [--csv]
```

For example, to get a usage report for all of your own projects for the current
year, just run:


```bash
[fe-open-01]$ gdk-project-usage
```

You can expand limit to a specific project with:

```bash
[fe-open-01]$ gdk-project-usage -p MyProject
```

Sometimes you want to see which user is causing an increase in usage. To usage
per user:

```bash
[fe-open-01]$ gdk-project-usage -p MyProject -u
```

Or show usage for a specific year:

```bash
[fe-open-01]$ gdk-project-usage -p MyProject -y 2024
```

In addition to this, project owners receive:

* a monthly e-mail with a usage summary for all of their projects,
* a high-activity warning e-mail if the project consumes grows quickly in 
  resource usage.

# Resource quotas

As a project owner you can set quotas on resources with:

```bash
[fe-open-01]$ gdk-project-set-quota -p <project name> -h <max billing hours> -s <max storage> -b <max backup>
```

The arguments are described in detail in the command help (`gdk-project-set-quota -h`).

You can see quotas set on a project, if any, with:

```bash
gdk-project-show <project name>
```

When quotas are set, the project owner will receive a warning by e-mail when
the usage exceeds 90% of the specified quota.

It's important to understand that **quotas are not strict**:

* A project may exceed its billing hour quota somewhat, as the quota is checked 
  on an hourly basis. If the quota is reached, all running jobs will be 
  cancelled and new jobs will not be able to start until the quota has been
  increased.
* Storage and backup usage is measured on a weekly basis and thus projects may
  exceed the specified quota substantially. Even though the quota is exceeded,
  data may still be written to and read from the project folder. It's up to the
  project owner to either increase the quota or delete data to obey the quota.

{% note() %}
Once set, a quota cannot be decreased, only increased.
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

You can read more about `chmod` [here](https://en.wikipedia.org/wiki/Chmod).
