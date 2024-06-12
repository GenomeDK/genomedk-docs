---
title: Interacting with the queue
weight: 40
---

Since GenomeDK is a shared system, all computations must be carried out
through a queue. Users submit jobs to the queue and the jobs then run
when it's their turn. To cater for different workloads, jobs can be
submitted to one or more *partitions*, which are essentially queues that
have been assigned certain restrictions such as the maximum running
time.

The queueing system used at GenomeDK is
[Slurm](https://slurm.schedmd.com/). Users that are familiar with Sun
Grid Engine (SGE) or Portable Batch System (PBS), will find Slurm very
familiar.

The queueing system allows us to either submit an *interactive* or
*batch* job. An interactive job effectively gives you a shell on a
compute node so that you can type commands and run programs that will
run on that node. This is great for experimenting and debugging
problems.

# Partitions and nodes

To get an overview of the available nodes:

```bash
[fe-open-01]$ gnodes
```

This will list each partition and all of the compute nodes assigned to
each partition. The header of each partitions lists the available
resources such as the number of cores per node, available memory per
node, and the maximum walltime (running time) a job in the partition can
have.

{% note() %}
There is a global seven day time limit. Submitting a job requesting more
than seven days will result in an error.
{% end %}

# Submitting jobs under a project

All projects are given an account that can be used to submit jobs
belonging to the project. The account name is the same as the project
name.

When submitting jobs, you should always specify which account should be
used:

- By default, you have a very small quota for running jobs **without
  specifying a project**. We allow this so that new users can
  familiarize themselves with GenomeDK and the queueing system without
  requesting or joining a project.

  However, when this small quota is used, you will no longer be able
  to submit jobs and `jobinfo` will show something like this (note the
  highlighted lines):

  ```txt
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
  ```

  To be able to submit jobs again, you must specify an account.

- Submitting jobs with the project account also has the benefit that
  jobs submitted with a project account get much higher priority than
  non-project jobs.

# Interactive jobs

To submit an interactive job:

```bash
[fe-open-01]$ srun --account <project name> --pty bash
srun: job 17129453 queued and waiting for resources
srun: job 17129453 has been allocated resources
[s03n73]$
```

This may take some time since you must wait until it's your turn in the
queue. Once it's your turn, you'll get a shell on the node that was
assigned to you. In this case, we were given the node *s03n73*.

You may also specify some requirements for the job, such as the amount
of memory that should be allocated:

```bash
[fe-open-01]$ srun --account <project name> --mem 16g --pty bash
```

When running a job you have access to the same filesystems as when
running on the frontend. Thus, you can access your home folder and
project folders with the same paths as on *fe-open-01*.

When you're done with your interactive session on the node, it can be
exited by running the `exit` command or pressing
`Control + D`.

```bash
[s03n73]$ exit
[fe-open-01]$
```

You'll now be back on the frontend.

# Batch jobs

While interactive jobs are useful, they require you to be logged in to
the node while your computations one the node are running. Exiting the
session will cancel your computations, which is not usually what you
want. Also, you may want to run many jobs on multiple nodes, and having
that many interactive sessions open quickly becomes unmanagable.

To solve this, we may submit a *batch* job instead. Batch jobs are
submitted to the queue like interactive jobs, but they don't give you a
shell to run commands. Instead, you must write a *job script* which
contains the commands that needs to be run.

The most minimal job script you can write looks like this:

```bash
#!/bin/bash
#SBATCH --account my_project

echo hello world
```

This specifies that you want to submit the job under the `my_project`
project folder. The rest of the script is a normal
[Bash](https://www.gnu.org/software/bash/manual/bash.html) script which
contains the commands that should be executed, when the job is started
by Slurm.

To specify which ressources are needed by the job:

```bash
#!/bin/bash
#SBATCH --account my_project
#SBATCH -c 8
#SBATCH --mem 16g

echo hello world
```

This specifies that you want eight cores and 16 GB of memory allocated
to the job.

Here's a more complicated job script:

```bash
#!/bin/bash
#SBATCH --account my_project
#SBATCH -c 8
#SBATCH --mem 16g
#SBATCH --partition gpu
#SBATCH --gres=gpu:1
#SBATCH --time 04:00:00

echo hello world
```

Unless you specify a partition other that short/normal, like *fat2* or
*express*, the partition parameter is largely ignored and your jobs are actually
submitted to both partitions. When they start, they are moved to a single
partition, in which they are started. This is done to avoid waiting in the
*short* queue if normal nodes are empty.

Long story short: don't worry, just submit the job asking for an appropriate
time limit and it will start in an appropriate place. Unless you want *fat2* or
*express*, you can forget about the partition parameter.

{% note() %}
A node can be shared by multiple users, so you should always take extra
care in requesting to correct amount of resources (nodes, cores and
memory). There is no reason to occupy an entire node if you are only
using a single core and a few gigabytes of memory. Always make sure to
utillize the resources on the requested nodes efficiently.
{% end %}

To submit a job for this script, save it to a file (e.g.
`example.sh`) and run:

```bash
[fe-open-01]$ sbatch example.sh
Submitted batch job 17129500
[fe-open-01]$
```

Contrary to `srun`, this command
returns immediately, giving us a job id to identify our job.

Most people find it annoying to write these job script for each step in
their workflow and instead use a workflow engine such as
[gwf](https://docs.gwf.app/en/latest/) (developed at GenomeDK) or
[snakemake](https://snakemake.readthedocs.io/) (quite popular in
bioinformatics). Such tools allow you to write entire pipelines
consisting of thousands of separate jobs and submit those jobs to Slurm
without writing job scripts manually.

# Checking job status

To check the status of a job:

```bash
[fe-open-01]$ jobinfo 17129500
```

To check the status of all of your submitted jobs:

```bash
[fe-open-01]$ squeue -u USERNAME
```

You can also omit the username flag to get an overview of all jobs that
have been submitted to the queue:

```bash
[fe-open-01]$ squeue
```

# Cancelling a job

Jobs can be cancelled using the `scancel` command:

```bash
[fe-open-01]$ scancel 17129500
```

# Checking job priorities

You may be wondering why one of your jobs are not starting. It may be
due to other jobs having a higher priority. To see the priority of all
jobs in the queue:

```bash
[fe-open-01]$ priority -a
```

# Constraining jobs to certain nodes

While the compute nodes are almost identical, there are small
differences such as CPU architecture. If your code depends on specific
CPU features you must restrict your jobs to compute nodes supporting
those features.

For example, our 4th generation nodes do not support AVX512
instructions. To restrict your job to only the 5th generation nodes that do
support it:

```bash
[fe-open-01]$ sbatch --constraint "gen5" ...
```

This also works for `srun`:

```bash
[fe-open-01]$ srun --constraint "gen5" ...
```

You can get a list of all of the features you can constrain by with the
`scontrol show node` command. For example, to get the features
associated with the `s21n21` node:

```bash
[fe-open-01]$ scontrol show node cn-1001
NodeName=cn-1001 Arch=x86_64 CoresPerSocket=96
   CPUAlloc=26 CPUEfctv=192 CPUTot=192 CPULoad=27.92
   AvailableFeatures=gen5,amd,avx512
   ActiveFeatures=gen5,amd,avx512
   Gres=(null)
   NodeAddr=cn-1001 NodeHostName=cn-1001 Version=23.11.2
   OS=Linux 4.18.0-477.27.2.el8_8.x86_64 #1 SMP Fri Sep 29 08:21:01 EDT 2023
   RealMemory=1547000 AllocMem=1433600 FreeMem=392897 Sockets=2 Boards=1
   State=MIXED ThreadsPerCore=1 TmpDisk=0 Weight=1 Owner=N/A MCS_label=default
   Partitions=normal
   BootTime=2023-12-08T16:08:20 SlurmdStartTime=2024-02-14T15:51:08
   LastBusyTime=2024-02-22T04:02:40 ResumeAfterTime=None
   CfgTRES=cpu=192,mem=1547000M,billing=192
   AllocTRES=cpu=26,mem=1400G
   CapWatts=n/a
   CurrentWatts=0 AveWatts=0
   ExtSensorsJoules=n/a ExtSensorsWatts=0 ExtSensorsTemp=n/a
```

Looking at the line that starts with `AvailableFeatures` we see that the
node has the *gen5*, *amd* and *avx512* features associated to it.
So in our earlier example we could have constrained on `avx512` instead of a
certain type of machine.

The [slurm
documentation](https://slurm.schedmd.com/sbatch.html#OPT_constraint) has
more info on how to ask for multiple features etc.

# Working on GPU nodes {#gpu_nodes}

There are currently two compute nodes on the cluster that are equipped
with GPU cards with two devices per node. There are currently no
frontends equipped with GPU devices.

If you need to compile a piece of software that is supposed to use GPU's
you most likely have to do it in a job on one of the compute nodes with
such devices, since headers required for compilation are only located
there.

Headers and libraries for compilation are located in
`/usr/local/cuda/targets/x86_64-linux`.

To to run a job on a node with a GPU device you need to submit it to the
*gpu* partition and specify how many GPU devices you are going to use,
for example to submit an interactive job that will use just one GPU:

```bash
[fe-open-01]$ srun --gres=gpu:1 -p gpu --pty /bin/bash
```
