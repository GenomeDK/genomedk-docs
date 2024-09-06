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

Conda can be quite slow, especially when installing packages with many
dependencies. To speed up Conda, you can install a faster dependency solver:

```bash
[fe-open-01]$ conda install -n base --yes conda-libmamba-solver
[fe-open-01]$ conda config --set solver libmamba
```

The `libmamba` solver is still experimental, but in our experience it's a lot
faster and better than the default solver.

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

Since Conda knows about the entire environment you created, it can tell
you exactly which packages are used in the environment. This is very
useful for collaborating with others, since your collaborators can
create an exact copy of your environment with a single command.

To export your environment so that others can recreate it:

```bash
(amazing-project) [fe-open-01]$ conda env export > environment.yml
```

The `environment.yml` file contains an
exact specification of your environment and the packages installed. You
can put this in your shared project folder. Others will then be able to
recreate your environment by running:

```bash
[fe-open-01]$ conda env create -f environment.yml
```

You can read more about [using environments for projects](/docs/best-practices/).

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

# Using graphical interfaces

There's two options for using programs with a graphical user interface
on GenomeDK.

## X-forwarding {#xforwarding}

You can use X-forwarding to tunnel individual graphical programs to your
local desktop. This works well for many programs, but programs that do
fancy graphics or anything animated might not work well.

On Linux you simply need to tell SSH that you wish to enable
X-forwarding. To do this, add `-X` to the `ssh` command when logging in to the cluster, for example:

```bash
[local]$ ssh -X USERNAME@login.genome.au.dk
```

You should then be able to open e.g. Firefox on the frontend:

```bash
[fe-open-01]$ firefox
```

Since macOS does not include an X server, you will need to download and
install [XQuartz](https://www.xquartz.org/) on your computer. When
installed, reboot the computer. Now, you just need to tell SSH that you
wish to enable X-forwarding. To do this, add `-X` to the
`ssh` command when logging in to the
cluster, for example:

```bash
[local]$ ssh -X USERNAME@login.genome.au.dk
```

You should then be able to open e.g. Firefox on the frontend:

```bash
[fe-open-01]$ firefox
```

On Windows, we recommend that you use
[MobaXterm](https://mobaxterm.mobatek.net/) which has an integrated X
server.

## VNC

{% note() %}
We're working on a better solution for virtual desktops on
GenomeDK. These instructions only work if you run Linux or macOS on your own
computer.
{% end %}

If you want to use a full virtual desktop you can use a VNC client. Any VNC
client will do. [Remote Ripple](https://remoteripple.com/) works on many
different platforms and is free.

First, ensure that your VNC client of choice is installed on your computer.

Next, log on to GenomeDK and start a *VNC server*:

```bash
[fe-open-01]$ vncserver
WARNING: vncserver has been replaced by a systemd unit and is now considered deprecated and removed in upstream.
Please read /usr/share/doc/tigervnc/HOWTO.md for more information.

New 'fe-open-02:1 (das)' desktop is fe-open-02:1

Starting applications specified in /home/das/.vnc/xstartup
Log file is /home/das/.vnc/fe-open-02:1.log
```

(You can ignore the warning).

If this is the first time, you will be asked to specify a password for accessing
the desktop. Enter a password of your choice.

The display id (`:1` in the example output above) is needed when you want to
connect to the desktop with your VNC client.

You must compute 5900 + the display id, which is the port number you will use to
connect to the remote desktop. So in this example, the port number is 5901.

On your own computer, start an SSH tunnel to the VNC server:

```bash
[local]$ ssh -N -L 5901:localhost:5901 <username>@login.genome.au.dk
```

Now open your VNC client and connect to host `localhost` and the port number you
calculated. You will be asked for the password you specified earlier.

# Using a terminal multiplexer

Using a terminal multiplexer allows you to keep your session open, even
when you disconnect from the cluster. You can even reconnect from a
different computer and get your session back.

We recommend that you use either `tmux` or `screen`.

-   [tmux](https://github.com/tmux/tmux/wiki)
-   [screen](https://www.gnu.org/software/screen/manual/screen.html).
