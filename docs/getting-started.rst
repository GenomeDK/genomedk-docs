.. _getting_started:

===============
Getting started
===============

.. note::

    If you don't know what a closed zone is, or you know that you're not
    running in one, skip all red boxes like the one below. Most users on
    GenomeDK are *not* in a closed zone.

.. admonition:: Closed zone...

    Running in a closed zone means running in a restricted environment.
    In some cases, this means that you must use special commands or
    follow special instructions for certain things. This will be noted in red
    boxes like this one throughout the documentation.

This page will tell you everything you need to know to get up and running on
GenomeDK. However, we assume that you have some experience with the command
line/terminal.

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

    [fe1]$ echo hello

Here, **fe1** is the name of the frontend node. If you need to run a command
on a compute node that you started an interactive job on (more about this
later), it will be shown like this:

.. code-block:: console

    [s03n11]$ echo hello

In this case the compute node is **s03n11**, but anything that has the format
**sXXnYY** is a compute node.

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

.. _request_access:

Get access to the cluster
=========================

.. admonition:: Closed zone...

    Fill out `this <https://genomedk.wufoo.com/forms/request-access-to-cluster-ipsych-only/>`_
    form instead.

Fill out the form for `normal users <https://genomedk.wufoo.com/forms/request-access-to-cluster/>`_.

Once you've been granted access, you'll receive an e-mail with your password.
You'll then be able to connect to the cluster.

.. _connecting_to_the_cluster:

Connecting to the cluster
=========================

.. admonition:: Closed zone...

    Follow the instructions `here <http://ipsych.genome.au.dk/>`_.

On Linux, open the terminal of your choice. On macOS, you may use
:program:`Terminal.app` which can be found in the
:file:`/Applications/Utilities` folder. In both cases, you should now be able
to log in to the frontend by typing this command:

.. code-block:: console

    [local]$ ssh USERNAME@login.genome.au.dk

On Windows, you have multiple options. On Windows 10, open
:program:`PowerShell`. You should then be able to type:

.. code-block:: console

    [local]$ ssh.exe USERNAME@login.genome.au.dk

Older versions of Windows do not include the :program:`ssh` command and thus
you will need to install an alternative yourself. We recommend MobaXterm_.

.. note::

    Access to GenomeDK is restricted to the internal network at Aarhus University.
    However, if you need access from abroad or for some other reason can not
    connect connect from AU, feel free to :ref:`contact us <contact>` to get
    whitelisted.

.. _MobaXterm: https://mobaxterm.mobatek.net/


Changing your password
======================

This is important! Since e-mail is not secure, someone may get access to the
password that we sent to you. Thus, you should change it immediately after
logging in. Run the command:

.. code-block:: console

    [fe1]$ change-password

It will ask you for your current password, then ask what your new password
should be. Finally, it will ask you to confirm your new password by typing it
again.

.. warning::

    Do not use :program:`passwd`, :program:`yppasswd` or
    :program:`ipsych-passwd` to change your password. These commands won't
    work in all cases or at all.

.. _mounting:

Accessing your files locally
============================

You can access your files on GenomeDK locally by a process called *mounting*.
Mounting the GenomeDK filesystem locally makes it possible to access and edit
your files as if they were located in a folder on your own harddrive.

Unfortunately, mounting over SSH does not work on Windows. If you're on Windows
you can use MobaXterm_ or one of the alternatives listed in
:ref:`copying_data`.

* On distros with the :program:`apt` package manager (Ubuntu, Mint etc.):

  .. code-block:: console

      [local]$ apt-get install sshfs

* On distros with the :program:`yum` package manager (Fedora, CentOS etc.):

  .. code-block:: console

      [local]$ yum install sshfs

* On macOS, download and install the *SSHFS* and *FUSE for macOS* packages
  from the `OSX FUSE`_ website.

Create a directory where the filesystem will be mounted:

.. code-block:: console

    [local]$ mkdir ~/GenomeDK

Now mount the filesystem by running this command:

.. code-block:: console

    [local]$ sshfs USERNAME@login.genome.au.dk:/home/USERNAME ~/GenomeDK \
        -o idmap=none -o uid=$(id -u),gid=$(id -g) \
        -o allow_other -o umask=077 -o follow_symlinks

Where *USERNAME* should be replaced with your GenomeDK username. You should
now be able to access your files on GenomeDK by going to the ``~/GenomeDK``
directory on your computer.

To unmount the directory, run:

.. code-block:: console

    [local]$ umount ~/GenomeDK

.. _OSX FUSE: https://osxfuse.github.io/


.. _copying_data:

Copying data
============

.. admonition:: Closed zone...

    To copy data from the cluster, see :ref:`gdk-export`
    To copy data to the cluster, see :ref:`gdk-import`

From your own machine to/from the cluster
-----------------------------------------

If you :ref:`mounted <mounting>` GenomeDK on your computer, you can copy files
to and from the cluster by simple drag-and-drop. Otherwise you can use one of
the solutions listed here or one of these alternatives:

* Filezilla_ [Linux/macOS/Windows]
* Cyberduck_ [macOS]
* MobaXterm_ [Windows]
* WinSCP_ [Windows]

You may also use the command line.

To copy a single file from your computer to the cluster:

.. code-block:: console

    [local]$ scp myfile.txt login.genome.au.dk:path/to/destination/

On Windows, replace ``scp`` with ``scp.exe``.

To copy a single file from the cluster to your computer:

.. code-block:: console

    [local]$ scp login.genome.au.dk:/path/to/file .

If you want to copy an entire folder to/from the cluster you will want to use
:program:`rsync` instead. To copy a folder from your computer to the cluster:

.. code-block:: console

    [local]$ rsync -e ssh -avz /path/to/data user@login.genome.au.dk:data

Windows doesn't have :program:`rsync` installed, so you must resort to one of
the options listed above.

If you want to upload a folder, but also delete files that you deleted in the
source folder from the destination:

.. code-block:: console

    [local]$ rsync -e ssh -avz --delete /path/to/data user@login.genome.au.dk:data

If you want to download data from the cluster:

.. code-block:: console

    [local]$ rsync -e ssh -avz --delete /location/data user@login.genome.au.dk:data

You may want to add the ``--progress`` flag to all of these commands if you're
downloading/uploading large amounts of data.

.. _Filezilla: https://filezilla-project.org/
.. _Cyberduck: https://cyberduck.io/
.. _WinSCP: https://winscp.net/eng/index.php


From the Internet to the cluster
--------------------------------

You can use :program:`wget` to download data from the Internet to the cluster:

.. code-block:: console

    [fe1]$ wget -c --timeout=120 --waitretry=60 \
        --tries=10000 --retry-connrefused URL

Remember to replace ``URL`` with the thing you want to download.

When downloading large files you are encouraged to limit the progress output to
avoid stressing the system, *especially* when you're sending the progress
output to a file:

.. code-block:: console

    [fe1]$ wget -c --progress=giga:force --timeout=120 --waitretry=60 \
        --tries=10000 --retry-connrefused URL


Where to put your data
======================

On your laptop, all files reside on your local hard disk. However, on GenomeDK
that is not the case. To achieve high performance and accommodate the huge
amounts of data located on the cluster, data is saved on network file systems.

Each of these file systems have their own advantages and disadvantages. Thus,
you need to put your data on the right file system to utilize the cluster
optimally.

/home/<username>
    Your home folder is on a file system called NFS. This file system handles
    many small files well, but not big files. It's also rather slow to access
    this file system from many compute nodes at the same time and your home
    folder is limited to 100 GB.

    We do *not* recommend storing raw data files, temporary files or results on
    this file system. However, it's fine for small documents like notes,
    programs and your Conda installation.

/faststorage/home/<username>
    For big files we provide access to a fast, parallel file system called
    BeeGFS. We call this file system *faststorage*. This file system is ideal
    for large data files and intermediate data generated by your jobs. However,
    it will be much slower for small files. All users have their own home
    folder located at :file:`/faststorage/home/<username>`. There is no limit
    on the amount of data that can be stored in this folder, but the data can
    only be accessed by your user.

/faststorage/project/<project name>
    All projects get their own folder on fast storage. All files related to the
    project should be placed in this folder. Project folders have no quota and
    can be accessed by all members of the project.

.. warning::

    The 100GB limit was introduced in 2019 for new users. Old users are
    encouraged to keep their home folders under 100 GB since this allows us to
    move them to much faster storage servers. If your home folder is less than
    100 GB and you want to be moved to the fast storage servers, get in touch.

Editing files
=============

If you :ref:`mounted <mounting>` GenomeDK on your computer, you can edit files
directly by just opening them with your prefered text editor on your computer.
Otherwise you can use one of the solutions listed here.

Nano, vim, emacs
----------------

With editors like :program:`nano`, :program:`vim` and :program:`emacs` you can
edit files directly on the cluster. The editor itself also runs on the cluster
and thus your editor settings etc. are conserved, even if you log in from
another computer. Also, these editors don't require a graphical user interface,
so you don't need X-forwarding or VNC.

The :program:`nano` editor is by far the simplest editor of three, but also the
least powerful. However, it's just fine for quickly editing scripts or looking
at output files. The documentation for :program:`nano` can be reached by
running the command:

.. code-block:: console

    [fe1]$ man nano

You can open :program:`nano` by running:

.. code-block:: console

    [fe1]$ nano name-of-file.txt

Likewise, `vim`_ and `emacs`_ are already installed on the cluster.
Documentation for each editor can be found on their respective websites.

.. _vim: https://www.vim.org/
.. _emacs: https://www.gnu.org/software/emacs/index.html


Gedit with X-forwarding
-----------------------

If you want a graphical user interface and a more familiar editing experience,
you may use the :program:`Gedit` editor with :ref:`X-forwarding <xforwarding>`.
Make sure that you are connected to the cluster with X-forwarding enabled. Then
run:

.. code-block:: console

    [fe1]$ gedit

This will open the :program:`Gedit` editor in a new window. Since the editor
runs on the frontend, you have access to all of your files on the cluster.

Interacting with the queue
==========================

Since GenomeDK is a shared system, all computations must be carried out through
a queue. Users submit jobs to the queue and the jobs then run when it's their
turn. To cater for different workloads, jobs can be submitted to one or more
*partitions*, which are essentially queues that have been assigned certain
restrictions such as the maximum running time.

The queueing system used at GenomeDK is Slurm_. Users that are familiar with
Sun Grid Engine (SGE) or Portable Batch System (PBS), will find Slurm very
familiar.

.. note::

    A node can be shared by multiple users, so you should always take extra
    care in requesting to correct amount of resources (nodes, cores and
    memory). There is no reason to occupy an entire node if you are only using
    a single core and a few gigabytes of memory. Always make sure to utillize
    the resources on the requested nodes efficiently.

To get an overview of the available partitions:

.. code-block:: console

    [fe1]$ gnodes

This will list each partition and all of the compute nodes assigned to each
partition. The header of each partitions lists the available resources such as
the number of cores per node, available memory per node, and the maximum
walltime (running time) a job in the partition can have.

The queueing system allows us to either submit an *interactive* or *batch* job.
An interactive job effectively gives you a shell on a compute node so that you
can type commands and run programs that will run on that node. This is great
for experimenting and debugging problems.

Interactive jobs
----------------

To submit an interactive job:

.. code-block:: console

    [fe1]$ srun --pty /bin/bash
    srun: job 17129453 queued and waiting for resources
    srun: job 17129453 has been allocated resources
    [s03n73]$

This may take some time since you must wait until it's your turn in the queue.
Once it's your turn, you'll get a shell on the node that was assigned to you.
In this case, we were given the node *s03n73*.

You may also specify some requirements for the job, such as the amount of
memory that should be allocated:

.. code-block:: console

    [fe1]$ srun --mem=16g --pty /bin/bash

When running a job you have access to the same filesystems as when running on
the frontend. Thus, you can access your home folder and project folders with
the same paths as on *fe1*.

When you're done with your interactive session on the node, it can be exited
by running the ``exit`` command or pressing :kbd:`Control + D`.

.. code-block:: console

        [s03n73]$ exit
        [fe1]$

You'll now be back on the frontend.

Batch jobs
----------

While interactive jobs are useful, they require you to be logged in to the node
while your computations one the node are running. Exiting the session will
cancel your computations, which is not usually what you want. Also, you may
want to run many jobs on multiple nodes, and having that many interactive
sessions open quickly becomes unmanagable.

To solve this, we may submit a *batch* job instead. Batch jobs are submitted to
the queue like interactive jobs, but they don't give you a shell to run
commands. Instead, you must write a *job script* which contains the commands
that needs to be run.

A job script looks like this:

.. code-block:: shell

    #!/bin/bash
    #SBATCH --partition normal
    #SBATCH --mem-per-cpu 4G
    #SBATCH -c 1

    echo hello world > result.txt

The job script specifies which resources are needed as well as the commands to
be run. Line 2 specifies that this job should be submitted to the *normal*
partition. Line 3 specifies that we want 4G of memory per allocated core, and
line 4 specifies that we want a single core to run on. See the table below for
an overview of commonly used resource flags:

.. csv-table:: Resource flags
    :header: "Short flag", "Long flag", "Description"
    :align: left
    :widths: 10, 40, 50

    "``-A``", "``--account``", "Account to submit the job under. See :ref:`jobs_with_project`."
    "``-p``", "``--partition``", "One or more comma-separated partitions that the job may run on. Jobs submitted to the *gpu* partition should also use the *--gres* flag."
    "", "``--mem-per-cpu``", "Memory allocated per allocated CPU core."
    "``-c``", "``--cpus-per-task``", "Number of cores allocated for the job. All cores will be on the same node."
    "``-n``", "``--ntasks``", "Number of cores allocated for the job. Cores may be allocated on different nodes."
    "``-N``", "``--nodes``", "Number of nodes allocated for the job. Can be combined with ``-n`` and ``-c``."
    "``-t``", "``--time``", "Maximum time the job will be allowed to run."
    "", "``--gres=gpu:<number of gpu's>``", "Number of GPU cards to be used in case the job is being submitted to the *gpu* partition. If not defined the job will not have access to GPU cards, even if it is running on a proper node."

The rest of the script is a normal Bash_ script which contains the commands
that should be executed, when the job is started by Slurm.

To submit a job for this script, save it to a file (e.g. :file:`example.sh`)
and run:

.. code-block:: console

    [fe1]$ sbatch example.sh
    Submitted batch job 17129500
    [fe1]$

Contrary to :command:`srun`, this command returns immediately, giving us a job
id to identify our job.

.. _gpu_nodes:

Working on GPU nodes
--------------------

There are currently two compute nodes on the cluster that are equipped with GPU
cards with two devices per node. There are currently no frontends equipped with
GPU devices.

If you need to compile a piece of software that is supposed to use GPU’s you
most likely have to do it in a job on one of the compute nodes with such
devices, since headers required for compilation are only located there.

Headers and libraries for compilation are located in
:file:`/usr/local/cuda/targets/x86_64-linux`.

To to run a job on a node with a GPU device you need to submit it to the *gpu*
partition and specify how many GPU devices you are going to use, for example to
submit an interactive job that will use just one GPU:

.. code-block:: console

    [fe1]$ srun --gres=gpu:1 -p gpu --pty /bin/bash


Checking job status
-------------------

To check the status of a job:

.. code-block:: console

    [fe1]$ jobinfo 17129500

To check the status of all of your submitted jobs:

.. code-block:: console

    [fe1]$ squeue -u USERNAME

You can also omit the username flag to get an overview of all jobs that have
been submitted to the queue:

.. code-block:: console

    [fe1]$ squeue

Cancelling a job
----------------

Jobs can be cancelled using the :program:`scancel` command:

.. code-block:: console

    [fe1]$ scancel 17129500

Checking job priorities
-----------------------

You may be wondering why one of your jobs are not starting. It may be due to
other jobs having a higher priority. To see the priority of all jobs in the
queue:

.. code-block:: console

    [fe1]$ priority -a


Extra credit
------------

Most people find it annoying to write these job script for each step in their
workflows and instead use a workflow engine such as gwf_ (developed at
GenomeDK) or snakemake_ (quite popular in bioinformatics). Such tools allow you
to write entire pipelines consisting of thousands of separate jobs and submit
those jobs to Slurm without writing job scripts.

.. _Slurm: https://slurm.schedmd.com/
.. _Bash: https://www.gnu.org/software/bash/manual/bash.html
.. _gwf: https://docs.gwf.app/en/latest/
.. _snakemake: https://snakemake.readthedocs.io/
