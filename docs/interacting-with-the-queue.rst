==========================
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

The queueing system allows us to either submit an *interactive* or *batch* job.
An interactive job effectively gives you a shell on a compute node so that you
can type commands and run programs that will run on that node. This is great
for experimenting and debugging problems.

Partitions and nodes
--------------------

To get an overview of the available nodes:

.. code-block:: console

    [fe-open-01]$ gnodes

This will list each partition and all of the compute nodes assigned to each
partition. The header of each partitions lists the available resources such as
the number of cores per node, available memory per node, and the maximum
walltime (running time) a job in the partition can have.

Submitting jobs under a project
-------------------------------

All projects are given an account that can be used to submit jobs belonging to
the project. The account name is the same as the project name.

When submitting jobs, you should always specify which account should be used:

* By default, you have a very small quota for running jobs **without specifying a
  project**. We allow this so that new users can familiarize themselves with
  GenomeDK and the queueing system without requesting or joining a project.

  However, when this small quota is used, you will no longer be able to submit
  jobs and ``jobinfo`` will show something like this (note the highlighted lines):

  .. code-block:: console
      :emphasize-lines: 3,4,9

      Name                : bash
      User                : das
      Account             : --
          Note: You haven't specified a project. You have a limited number of billing hours!
      Partition           : short,normal
      Nodes               : None assigned
      Cores               : 1
      GPUs                : 0
      State               : PENDING (AssocMaxWallDurationPerJobLimit)
      ...

  To be able to submit jobs again, you must specify an account.

* Submitting jobs with the project account also has the benefit that jobs
  submitted with a project account get much higher priority than non-project
  jobs.

Interactive jobs
----------------

To submit an interactive job:

.. code-block:: console

    [fe-open-01]$ srun --account <project name> --pty bash
    srun: job 17129453 queued and waiting for resources
    srun: job 17129453 has been allocated resources
    [s03n73]$

This may take some time since you must wait until it's your turn in the queue.
Once it's your turn, you'll get a shell on the node that was assigned to you.
In this case, we were given the node *s03n73*.

You may also specify some requirements for the job, such as the amount of
memory that should be allocated:

.. code-block:: console

    [fe-open-01]$ srun --account <project name> --mem 16g --pty bash

When running a job you have access to the same filesystems as when running on
the frontend. Thus, you can access your home folder and project folders with
the same paths as on *fe-open-01*.

When you're done with your interactive session on the node, it can be exited
by running the ``exit`` command or pressing :kbd:`Control + D`.

.. code-block:: console

        [s03n73]$ exit
        [fe-open-01]$

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

The most minimal job script you can write looks like this:

.. code-block:: shell

    #!/bin/bash
    #SBATCH --account my_project

    echo hello world

This specifies that you want to submit the job under the ``my_project`` project
folder. The rest of the script is a normal Bash_ script which contains the
commands that should be executed, when the job is started by Slurm.

To specify which ressources are needed by the job:

.. code-block:: shell

    #!/bin/bash
    #SBATCH --account my_project
    #SBATCH -c 8
    #SBATCH --mem 16g

    echo hello world

This specifies that you want eight cores and 16 GB of memory allocated to the
job.

.. note::

    A node can be shared by multiple users, so you should always take extra
    care in requesting to correct amount of resources (nodes, cores and
    memory). There is no reason to occupy an entire node if you are only using
    a single core and a few gigabytes of memory. Always make sure to utillize
    the resources on the requested nodes efficiently.

To submit a job for this script, save it to a file (e.g. :file:`example.sh`)
and run:

.. code-block:: console

    [fe-open-01]$ sbatch example.sh
    Submitted batch job 17129500
    [fe-open-01]$

Contrary to :command:`srun`, this command returns immediately, giving us a job
id to identify our job.

Most people find it annoying to write these job script for each step in their
workflow and instead use a workflow engine such as gwf_ (developed at
GenomeDK) or snakemake_ (quite popular in bioinformatics). Such tools allow you
to write entire pipelines consisting of thousands of separate jobs and submit
those jobs to Slurm without writing job scripts manually.

Flags for ressource allocation
------------------------------

The below table contains the most commonly used flags for ``srun``/``sbatch``.

.. csv-table:: Resource flags
    :header: "Short flag", "Long flag", "Description"
    :align: left
    :widths: 10, 30, 60

    "``-A``", "``--account``", "Account to submit the job under. Always specify this."
    "``-p``", "``--partition``", "One or more comma-separated partitions that the job may run on [#f1]_. Jobs submitted to the *gpu* partition should also use the *--gres* flag [#f2]_."
    "", "``--mem``", "Total memory that should be allocated for the job, e.g. `16g`."
    "``-c``", "``--cpus-per-task``", "Number of cores allocated for the job. All cores will be on the same node."
    "``-N``", "``--nodes``", "Number of nodes allocated for the job."
    "``-t``", "``--time``", "Maximum time the job will be allowed to run."
    "``-C``", "``--constraint``", "Constrain nodes to be allocated."
    "", "``--gres=gpu:<number of gpu's>``", "Number of GPU cards to be used in case the job is being submitted to the *gpu* partition. If not defined the job will not have access to GPU cards, even if it is running on a proper node."

.. [#f1] Unless you specify a partition other that short/normal, like *fat2* or
   *express*, the partition parameter is largely ignored and your jobs are
   actually submitted to both partitions. When they start, they are moved to a
   single partition, in which they are started. This is done to avoid waiting in
   the *short* queue if normal nodes are empty.

   Long story short: don't worry, just submit the job asking for an appropriate
   time limit and it will start in an appropriate place. Unless you want *fat2* or
   *express*, you can forget about the partition parameter.

.. [#f2] See :ref:`gpu_nodes` for more.

Checking job status
-------------------

To check the status of a job:

.. code-block:: console

    [fe-open-01]$ jobinfo 17129500

To check the status of all of your submitted jobs:

.. code-block:: console

    [fe-open-01]$ squeue -u USERNAME

You can also omit the username flag to get an overview of all jobs that have
been submitted to the queue:

.. code-block:: console

    [fe-open-01]$ squeue

Cancelling a job
----------------

Jobs can be cancelled using the :program:`scancel` command:

.. code-block:: console

    [fe-open-01]$ scancel 17129500

Checking job priorities
-----------------------

You may be wondering why one of your jobs are not starting. It may be due to
other jobs having a higher priority. To see the priority of all jobs in the
queue:

.. code-block:: console

    [fe-open-01]$ priority -a

Constraining jobs to certain nodes
----------------------------------

While the compute nodes are almost identical, there are small differences
such as CPU architecture. If your code depends on specific CPU features you
must restrict your jobs to compute nodes supporting those features.

For example, our 4th generation nodes do not support AVX512 instructions. To
restrict your job to only the s05 (gen3) nodes that do support it:

.. code-block:: console

    [fe-open-01]$ sbatch --constraint "gen3" ...

This also works for ``srun``:

.. code-block:: console

    [fe-open-01]$ srun --constraint "gen3" ...

You can get a list of all of the features you can constrain by with the
``scontrol show node`` command. For example, to get the features associated
with the ``s21n21`` node:

.. code-block:: console
    :emphasize-lines: 4

    [fe-open-01]$ scontrol show node s21n21
    NodeName=s21n21 CoresPerSocket=32
        CPUAlloc=0 CPUTot=64 CPULoad=N/A
        AvailableFeatures=gen4,s21,512g
        ActiveFeatures=gen4,s21,512g
        Gres=(null)
        NodeAddr=s21n21 NodeHostName=s21n21
        RealMemory=515538 AllocMem=0 FreeMem=N/A Sockets=2 Boards=1
        State=AVAILABLE ThreadsPerCore=1 TmpDisk=0 Weight=1 Owner=N/A MCS_label=N/A
        Partitions=short
        BootTime=None SlurmdStartTime=None
        LastBusyTime=2022-05-02T13:01:48
        CfgTRES=cpu=64,mem=515538M,billing=64
        AllocTRES=
        CapWatts=n/a
        CurrentWatts=0 AveWatts=0
        ExtSensorsJoules=n/s ExtSensorsWatts=0 ExtSensorsTemp=n/s

Looking at the line that starts with ``AvailableFeatures`` we see that the node
has the *gen4* and *s21* features associated to it.

The `slurm documentation`_ has more info on how to ask for
multiple features etc.

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

    [fe-open-01]$ srun --gres=gpu:1 -p gpu --pty /bin/bash


.. _Slurm: https://slurm.schedmd.com/
.. _slurm documentation: https://slurm.schedmd.com/sbatch.html#OPT_constraint
.. _Bash: https://www.gnu.org/software/bash/manual/bash.html
.. _gwf: https://docs.gwf.app/en/latest/
.. _snakemake: https://snakemake.readthedocs.io/
