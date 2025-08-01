---
title: Installing and using software
weight: 40
---

For most use cases, we recommend that you install and use the
[Conda](https://conda.io/docs/) package manager to install software on GenomeDK.
Conda provides access to thousands of software packages and is easy to get
started with.

For more advanced use cases, or where there's a substantial need for
reproducibility, we recommend [Apptainer](https://apptainer.org/), which is also
supported on GenomeDK.

You can of course also compile software yourself, but you must provide all of the
necessary dependencies (compilers, libraries) for the build, e.g. using Conda.

# Software installation with Conda

Conda can install any kind of software. This means that your entire
setup can be installed through Conda (if there's packages for it all).
For example, you can create an environment with Rstudio, R, and ggplot2
with a single command.

Conda provides access to thousands of packages used in data science and
bioinformatics. These packages can be installed with a single command, so you
don't have to worry about compilers, dependencies, and where to put binaries.

## Installing Conda {#installing_conda}

Downloading and installing Conda is very simple, you just download and
run the installer:

```bash
[fe-open-01]$ wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O miniforge.sh
[fe-open-01]$ chmod +x miniforge.sh
[fe-open-01]$ bash miniforge.sh -b
[fe-open-01]$ ./miniforge3/bin/conda init bash
```

That's it! The last two step makes sure that Conda will be available
when you log in, so now is a good time to open a new connection and
check that Conda is available.

Now let's configure Conda to make it super useful.

## Configuring Conda

Conda can install packages from different *channels*. This is similar to
*repositories* in other package managers. Here we'll add a few channels
that are commonly used in bioinformatics:

```bash
[fe-open-01]$ conda config --append channels bioconda
[fe-open-01]$ conda config --append channels genomedk
[fe-open-01]$ conda config --set channel_priority strict
```

Conda creates a `base` environment which contains Conda itself. It's
tempting to install packages in `base`, but that might ruin your Conda
installation. You should *never* install anything in the base
environment.

To prevent that you accidentially install something in the `base`
environment, we'll configure Conda so that it doesn't activate it when
you log in:

```bash
[fe-open-01]$ conda config --set auto_activate_base false
```

Once you have done these steps, you should have a config file in your
home folder called `.condarc` that looks like this:

```bash
[fe-open-01]$ cat $HOME/.condarc
channels:
  - conda-forge
  - bioconda
  - genomedk
channel_priority: strict
auto_activate_base: false
```

## Finding Conda packages

You can easily search for Conda packages through the website
[anaconda.org](https://anaconda.org/) or using the
`conda search` command:

```bash
[fe-open-01]$ conda search samtools
```

Remember that the Conda package may not be called the exact official
name of the software. For example, the Conda package for the software
*biobambam2* is just called *biobambam*, so searching for *biobambam2*
would not return any results.

If you can't find a suitable Conda package, contact us and we will build a Conda
package for you (when possible). Sometimes building a Conda package is not
viable and in that case we will build a Singularity/Apptainer image instead.

## Installing Conda packages

Here is how the usage might look if we want to create a new environment
with the newest version of
[PySAM](http://pysam.readthedocs.io/en/stable/):

```bash
[fe-open-01]$ conda create -n amazing-project pysam
```

This gives us a clean environment with just the minimal number of
packages necessary to support PySAM. To use the software that was
installed in the environment, the environment needs to be activated
first:

```bash
[fe-open-01]$ conda activate amazing-project
(amazing-project) [fe-open-01]$ python -c 'import pysam; print(pysam.__version__)'
0.6.0
```

Notice that the prompt changed to show you that you're now in the
*amazing-project* environment.

You can install further packages in the environment with:

```bash
(amazing-project) [fe-open-01]$ conda install r-ggplot2
```

Since Conda knows about the entire environment you created, it can tell
you exactly which packages are used in the environment. This is very
useful for collaborating with others, since your collaborators can
create an exact copy of your environment with a single command.

To export your environment so that others can recreate it:

```bash
(amazing-project) [fe-open-01]$ conda env export > environment.yml
```

The `environment.yml` file contains an exact specification of your environment
and the packages installed. You can put this in your shared project folder.
Others will then be able to recreate your environment by running:

```bash
[fe-open-01]$ conda env create -f environment.yml
```

# Containers with Apptainer/Singularity

[Apptainer](https://apptainer.org/) is a container technology for HPC that used
to be called "Singularity". If you're familiar with Docker, Apptainer will seem
familiar and Apptainer can convert most Docker images to its own (SIF) format
and run them without issues.

## Finding Apptainer images

There's a multitude of repositories for Docker/Apptainer images:

* [Docker Hub](https://hub.docker.com/)
* [NVIDIA GPU Cloud](https://ngc.nvidia.com/catalog/containers)
* [Singularity Cloud Library](https://cloud.sylabs.io/library)
* [Quay.io](https://quay.io/)
* [BioContainers](https://biocontainers.pro/registry)

## Pull an image

Apptainer is already installed and configured on GenomeDK, and you should be
able to pull and run containers without any further setup.

```bash
[fe-open-01] apptainer pull docker://biocontainers/blast:2.2.31
```

This will pull the Docker image for BLAST and convert it to SIF, so it may take
a while. In this case, the image will be put in your current working directory as  `blast_2.2.31.sif`.

Be aware that you should pull and convert images *once* before submitting jobs.
That is, never put `apptainer pull` in a job script.

{% note() %}
The images are quite large, so consider putting them in a relevant project
folder.
{% end %}

## Run a container

You can now run a command inside the image:

```bash
[fe-open-01] apptainer run blast_2.2.31.sif blastp -version
blastp: 2.2.31+
Package: blast 2.2.31, build Apr 23 2016 15:49:47
```

You can of course do this in job scripts also.

Apptainer supports the use of GPUs in containers, for example:

```bash
[fe-open-01] apptainer pull docker://nvcr.io/nvidia/tensorflow:23.08-tf2-py3
```

Then, on a GPU node (either in an interactive or batch job):

```bash
[gn-1001] apptainer run --nv tensorflow_23.08-tf2-py3.sif python3 mnist_classify.py
```

Note the use of the `--nv` flag.

# Building software for CUDA

If you need to compile a piece of software that is supposed to use GPUs you most
likely have to do it in a job on one of the GPU nodes, since headers required
for compilation are only located there.

You can get a list of GPU nodes with:

```bash
[fe-open-01] sinfo -p gpu -N
NODELIST   NODES PARTITION STATE
gn-1001        1       gpu mix
gn-1002        1       gpu alloc
```

Headers and libraries for compilation are located in
`/usr/local/cuda/targets/x86_64-linux`.

Read more about how to submit jobs for the GPU nodes
[here](@/docs/interacting-with-the-queue.md#gpu_nodes).
