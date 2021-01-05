
=======================
Projects and accounting
=======================

.. _collaborating:

Requesting a project
====================

Data sharing between users can only be accomplished through dedicated project
folders to which only certain users have access.

Run the following command to request a new project folder:

.. code-block:: console

    [fe1]$ gm-request-project -g <project name>

where **project name** is the desired name of the new project.

.. warning::

    When you request a project you're officially the project owner. This means
    that you're responsible for the compute and storage used by the project.
    Thus, you should familiarize yourself with the tools provided for
    monitoring the resources used by you and your projects (described later).

When your request has been accepted, you  will have access to a shared folder
in :file:`/faststorage/project/<project name>` where *project name* is the name
requested for your project.

Managing a project
==================

Project owners and project members with administrative rights can manage their
own projects through the following commands:

:command:`gm-add-user -g <project name> -u <username>`
    Add a user to a project.
:command:`gm-remove-user  -g <project name> -u <username>`
    Remove a user from a project.
:command:`gm-grant-admin-rights-to-user -g <project name> -u <username>`
    Grant administrative rights to a user in a project.
:command:`gm-revoke-admin-rights-from-user -g <project name> -u <username>`
    Revoke a users' administrative rights to a project.
:command:`gm-list-admins <project name>`
    List all members of a project with administrative rights.
:command:`gm-list-members <project name>`
    List all members of a project.

To get help for any of the commands, run the command without any parameters.

.. note::

    Don't know the username of one of your collaborators? You can use the
    :command:`finger` command to get information about any user on GenomeDK:

    .. code-block:: console

        [fe1]$ finger <name, username or mail>

    For example, to find all users with "anders" in their name:

    .. code-block:: console

        [fe1]$ finger anders
        aeh             Anders Egerup Halager <aeh@birc.au.dk>
        anders          Anders Boerglum <anders@biomed.au.dk>
        ...


.. _jobs_with_project:

Submitting jobs under a project
===============================

All projects are given an account that can be used to submit jobs belonging to
the project. The account name is the same as the project name.

Submitting jobs with the project account has the benefit that jobs submitted
with a project account get much higher priority than non-project jobs.

To submit a job with an account:

.. code-block:: console

    [fe1]$ sbatch --account <project name> ...

Or in *gwf*:

.. code-block:: python

  gwf = Workflow(defaults={"account": "<project name>"})


Keeping track of resource usage
===============================

To help you keep up to date on how much compute and storage is used by you and
your projects, you can use the :command:`space` command.

:command:`space user`
    Provides an overview of your own resource usage, that is, the storage used
    by files owned by you, as well as the billing hours you have used across
    all projects.
:command:`space overview`
    Provides you with an overview of the compute usage over time, as well as
    storage usage accounting, of all of the projects you own.
:command:`space project <project name>`
    Shows detailed compute and storage accounting for a specific project.
    For example, you can see how much compute and storage is used by each
    member of the project. All members of the project can run this command.


Data access in project folders
==============================

All members can add, edit, and delete files in the project folder unless
restrictions have been set on specific files/subfolders. If you have data that
you want to keep private to your user, but that belongs to in the project
folder anyway, you can set permissions so that only you can read, write, and
execute the file with this command:

.. code-block:: console

    [fe1]$ chmod go-rwx <files>

The :command:`chmod` command changes file permissions. The first parameter
specifies that groups (g) and others (o) should have their read (r), write (w),
and execute (x) permissions removed (-). This means that it's only the owner of
the file who can now access it.

You can read more about :command:`chmod`
`here <https://en.wikipedia.org/wiki/Chmod>`_.
