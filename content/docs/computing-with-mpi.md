---
title: Computing with MPI
weight: 49
extra:
  menu_category: compute
---

[MPI](https://www.open-mpi.org/) is a technology used by some applications to
perform coordinated, parallel, single and multi-node computations. Such
applications are written to use MPI to communicate between compute nodes,
enabling applications to scale to thousands of cores.

# Obtaining MPI-enabled software

A lot of software has MPI-enabled builds, but defaults to builds that are not
MPI-enabled. You must therefore ensure that you install the MPI-enabled version.

If using Conda, you must look up the name of the MPI-enabled build and install
that specific build. For example, to install the MPI-enabled build of the 
popular [GROMACS](https://www.gromacs.org/) software package, you must run:

```bash
$ conda install 'gromacs=*=mpi_openmpi*'
```

The [typical resources](@/docs/installing-software.md#conda_find) for finding
Conda packages can help in finding the right package build to install.

If you compile software from the source code, you can use Conda to install the
necessary compiler and libraries. See the [software development](#mpi-develop)
section for more details. Well-written software, [like
GROMACS](https://manual.gromacs.org/current/install-guide/index.html#quick-and-dirty-cluster-installation), will
have clear documentation for building it with MPI-support.

# Submitting MPI programs to the queue

Submitting jobs with MPI programs is slightly more involved and you have many
more options for allocating resources. The most common cases are covered in this
section. For more involved setups, consult the 
[sbatch documentation](https://slurm.schedmd.com/sbatch.html) and the 
documentation of the application you are running.

## Interactive

You can allocate resources and run your program interactively. You should only
use this for development and testing:

```bash
$ salloc --nodes 2 --account <project-name>
$ mpiexec ./myprog
```

Here, `salloc` allocates two nodes. Unlike `srun`, it doesn't redirect you to
any of the allocated nodes. Instead, every command you run after this will be
executed on all of the allocated nodes and the results printed directly to your
terminal.

## Single-node

For a single-node setup, you can force the queuing system to put all tasks on
one node with `--nodes=1`:

```bash
#!/bin/bash
#SBATCH --job-name mpi-single-node
#SBATCH --account myproject
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1 # this is the default
#SBATCH --mem-per-cpu=8g

mpirun ./myprog
```

## Multi-node

For a multi-node computation, specify the number of nodes with `--nodes`, as 
well as the number of tasks

```bash
#!/bin/bash
#SBATCH --job-name mpi-multi-node
#SBATCH --account myproject
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1 # this is the default
#SBATCH --mem-per-cpu=4g

mpirun ./myprog
```

Depending on the program you are running, you may want to use multiple cores per
task (`--cpus-per-task`), spawn more tasks (`--ntasks`), or ask for a specific
number of nodes (`--nodes`).

# Developing MPI-enabled software {#mpi-develop}

You can install OpenMPI with Infiniband-support via Conda with:

```bash
$ conda install openmpi gcc
```

The OpenMPI package brings `mpicc` which can be used to compile MPI programs:

```bash
$ mpicc myprog.c -o myprog
```

This will set all of the necessary compiler and linker flags.

# Advice on scaling and performance

Modern compute nodes are *big* and thus many MPI workloads can be run in a 
single-node setup, thus reducing communication overhead. You should always 
benchmark your application to verify that a multi-node setups indeed provides 
a useful speed-up.

Additionally, it is important to benchmark how the application scales as you
increase the number of tasks and/or cores used, to ensure that resources are 
used optimally.
