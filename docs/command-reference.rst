=================
Command reference
=================

.. glossary::
    :sorted:

    space user
        Show compute and storage numbers for a single user across projects
        and home folders. Useful for keeping track of your own resource usage.

    space project <project name>
        Show compute and storage numbers for a given project. The resource
        usage of individual project members is shown. Useful for project owners
        that wish to identify which project members are using resources in the
        project.

    space overview
        Show compute and storage numbers for all projects owned by you.

    jobinfo <job id>
        Shows information for a job no matter which state the job is in. Be
        aware that for technical reasons :program:`jobinfo` may return some or
        all data from an old job that had the same job ID.

    finger <text>
        Search for a string in the database of users. Useful for finding a user
        based on real name or e-mail.

    gnodes [<username>]
        Show an overview of all available compute nodes on the cluster grouped
        by partition. Shows which nodes are available and which are occupied.

        If a username is given, the nodes running the user's jobs will be
        highlighted.

    gm-request-project -g <project name> -m <members>
        Request a new project folder with the given name and list of members.

    gm-add-user -g <project name> -u <username>
        Add a user to a project.

    gm-remove-user  -g <project name> -u <username>
        Remove a user from a project.

    gm-grant-admin-rights-to-user -g <project name> -u <username>
        Grant administrative rights to a user in a project.

    gm-revoke-admin-rights-from-user -g <project name> -u <username>
        Revoke a users' administrative rights to a project.

    gm-list-admins <project name>
        List all members of a project with administrative rights.

    gm-list-members <project name>
        List all members of a project.
