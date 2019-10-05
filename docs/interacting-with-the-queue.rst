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