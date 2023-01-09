
.. _projects:

=======================
Projects and accounting
=======================

.. _collaborating:

Listing projects
================

You can list all of the projects you're a member of with:

.. code-block:: console

    [fe-open-01]$ gdk-project-list

You can also list all projects owned by you:

.. code-block:: console

    [fe-open-01]$ gdk-project-list -f owner

Or just list all projects:

.. code-block:: console

    [fe-open-01]$ gdk-project-list -f all

Requesting a project
====================

Data sharing between users can only be accomplished through dedicated project
folders to which only certain users have access.

Run the following command to request a new project folder:

.. code-block:: console

    [fe-open-01]$ gdk-project-request -g <project name>

where **project name** is the desired name of the new project.

.. warning::

    When you request a project you're officially the project owner. This means
    that you're responsible for the ressources used by the project.
    Thus, you should familiarize yourself with the tools provided for
    monitoring the resources used by you and your projects (described later).

When your request has been accepted, you will receive an e-mail with
further instructions.

Managing a project
==================

Project owners and project members with administrative rights can manage their
own projects through the following commands:

:command:`gdk-project-add-user -g <project name> -u <username>`
    Add a user to a project.
:command:`gdk-project-remove-user  -g <project name> -u <username>`
    Remove a user from a project.
:command:`gdk-project-promote-user -g <project name> -u <username>`
    Grant administrative rights to a user in a project.
:command:`gdk-project-demote-user -g <project name> -u <username>`
    Revoke a users' administrative rights to a project.
:command:`gdk-project-show <project name>`
    List various information about the project, e.g. who the current project
    owner is, when the project was created, etc. Also provides an overview of
    the total number of billing hours used by the given project, as well as the
    current storage and backup usage.
:command:`gdk-project-usage`
    Provides a detailed listing of the ressources used by all projects owned by
    you.

To get help for any of the commands, run the command without any parameters.

.. note::

    Don't know the username of one of your collaborators? You can use the
    :command:`finger` command to get information about any user on GenomeDK:

    .. code-block:: console

        [fe-open-01]$ finger <name, username or mail>

    For example, to find all users with "anders" in their name:

    .. code-block:: console

        [fe-open-01]$ finger anders
        aeh             Anders Egerup Halager <aeh@birc.au.dk>
        anders          Anders Boerglum <anders@biomed.au.dk>
        ...

Data access in project folders
==============================

All members can add, edit, and delete files in the project folder unless
restrictions have been set on specific files/subfolders. If you have data that
you want to keep private to your user, but that belongs to in the project
folder anyway, you can set permissions so that only you can read, write, and
execute the file with this command:

.. code-block:: console

    [fe-open-01]$ chmod go-rwx <files>

The :command:`chmod` command changes file permissions. The first parameter
specifies that groups (g) and others (o) should have their read (r), write (w),
and execute (x) permissions removed (-). This means that it's only the owner of
the file who can now access it.

You can read more about :command:`chmod`
`here <https://en.wikipedia.org/wiki/Chmod>`_.
