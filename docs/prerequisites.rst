=============
Prerequisites
=============

Before you start reading the documentation and using GenomeDK, there's a few
things that you should know.

Conventions
===========

You will be jumping a lot between different computers. This includes your own
computer, the frontend node, and various compute nodes.

Commands that need to be run on your own computer will look like this:

.. code-block:: console

    [local]$ echo hello

Note that the prompt says **local** in square brackets. When you need to run a
command on the frontend node, the prompt will instead say:

.. code-block:: console

    [fe-open-01]$ echo hello

Here, **fe-open-01** is the name of the frontend node. If you need to run a command
on a compute node that you started an interactive job on (more about this
later), it will be shown like this:

.. code-block:: console

    [s03n11]$ echo hello

In this case the compute node is **s03n11**, but anything that has the format
**sXXnYY** is a compute node.

Learning to use the shell
=========================

When interacting with the cluster you will be using a *shell* on a Linux/UNIX
system. If you are not familiar with these concepts we recommend the
`Shell novice <https://swcarpentry.github.io/shell-novice/>`_ tutorial from
Software Carpentry.

What is a closed zone?
======================

The GenomeDK cluster is divided into zones. There is one *open* zone and
multiple *closed* zones. Most users only need to use the open zone.

.. warning::

    If you are not part of a project that requires a closed zone, you are in our
    default, open zone and you can ignore this section completely.

For projects with additional security requirements, GenomeDK provides *closed
zones*. A closed zone is an additional layer of security on top of our
existing security solutions. Closed zones were previously called *jails*.

A closed zone provides:

Isolated networking
    Users and compute nodes that are not part of the closed zone cannot access
    or even see nodes that are in the closed zone.
Data access limitations
    Users in the zone cannot directly move data in or out of GenomeDK. Instead,
    data must be imported and exported. Exporting requires approval from the
    owner of the closed zone. All exports are logged.
Access through a virtual desktop
    Users must access the cluster through a special virtual desktop which
    disallows copy-paste. This means that users cannot leak data by copy-
    pasting it out of the closed zone.
No node sharing
    In the open zone, jobs from multiple users can run on the same compute
    node. In a closed zone, only jobs started by users in the same zone can
    share a compute node.

A closed zone is not tied to a single project. Users will need a separate
account/user for each closed zone they need access to. If you think that you
need a closed zone for your projects, feel free to get in touch.
