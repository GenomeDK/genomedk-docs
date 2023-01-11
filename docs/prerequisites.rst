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
