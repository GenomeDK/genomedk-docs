---
title: Software-specific documentation
weight: 90
---

# GATK

GATK 4 can be installed through Conda with:

```bash
$ conda install -c bioconda gatk4
```

GATK 3 cannot be installed this easily due to licensing restrictions. Instead,
you must download a licensed copy of GATK from
<https://software.broadinstitute.org/gatk/download/archive>, for example:

```bash
[fe-open-01]$ conda activate myproject
(myproject) [fe-open-01]$ conda install -c bioconda gatk
(myproject) [fe-open-01]$ wget https://storage.googleapis.com/gatk-software/package-archive/gatk/GenomeAnalysisTK-3.8-1-0-gf15c1c3ef.tar.bz2
(myproject) [fe-open-01]$ gatk3-register GenomeAnalysisTK-3.8-1-0-gf15c1c3ef.tar.bz2
```

You can now call GATK with the `gatk3` command:

```bash
(myproject) [fe-open-01]$ gatk3 --help
```

# Matlab

Matlab can be installed easily in user-space, but you must bring your own license.

First, [download your desired version](https://se.mathworks.com/downloads/) for Linux and put it in your home folder.

Unzip the file in a new folder, e.g.:

```bash
$ unzip matlab_R2023a_glnxa64.zip -d matlab_R2023_glnxa64
```

Go to the folder and execute the install script. This will make a Matlab window pop up.

```bash
$ ./install -agreeToLicense yes -destinationFolder /home/<username>/matlab/glnxa64 -outputFile matlab-install.log
```

Specify the installation folder as `/home/<username>/matlab/glnxa64`.

You then need to activate your license.

Go to folder `/home/<username>/matlab/glnxa64/bin` and execute the activation file:

```bash
$ ./activate_matlab.sh
```

Activating the license requires a [graphical environment](@/docs/using-graphical-interfaces.md).

Matlab is now installed. To use it in a batch script, you must ensure that the `matlab` executable is in your `$PATH`. You can do this in your batch script/workflow file or put it in your `.bashrc`:

```bash
export PATH=/home/<username>/matlab/glnxa64/bin/:$PATH
```

You can then run a Matlab script like this:

```bash
$ matlab -nodisplay -nosplash -r "<filename>; exit;"
```

where `<filename>` is the name of your script, without the `.m` extension.

# Jupyter Notebook/Lab

Install the `jupyter` package in your environment.

One way to run a Jupyter Notebook on the cluster is to setup an SSH tunnel to
the Jupyter instance.

*Start an interactive job*. Login to the cluster and start an interactive job
where the notebook will run.

```bash
[local ~]$ ssh <user>@login.genome.au.dk
[me@genomedk ~]$ srun --pty bash
srun: job 3597082 queued and waiting for resources
srun: job 3597082 has been allocated resources
[me@node ~]$
```

*Setup SSH tunnel.* Back on your local computer open a second terminal to setup
the port-forwarding from the computing node to your computer.

```bash
[local ~]$ ssh -L<UID>:<compute node>:<UID> <user>@login.genome.au.dk
```

You will need to replace `<UID>` with your user ID on the cluster, `<compute
node>` with the name of the compute node you have your job on, and `<user>` with
your username on the cluster. You can easily get those values by running
following commands on your compute node inside the interactive job you started
in the previous step.

```bash
[me@node ~]$ echo $UID
1234
[me@node ~]$ hostname -s
node
[me@node ~]$ echo $USER
me
```

Resulting in a command that would look like this:

```bash
[local ~]$ ssh -L1234:node:1234 me@login.genome.au.dk
```

*Start the notebook*. Back on the computing node start a Jupyter notebook. For
this you may have to first unset the environmental variable `XDG_RUNTIME_DIR`
(this could also be included in `~/.bashrc`).

```bash
[me@node ~]$ unset XDG_RUNTIME_DIR
[me@node ~]$ conda activate <jupyter-env>
[me@node ~]$ jupyter-notebook --no-browser --port=$UID --ip=0.0.0.0
```

*Run the notebook*. Back on your local computer start a web browser and paste
the URL from above. But replace the part in parenthesis with *localhost* to get:

```txt
http://localhost:<UID>/?token=....
```

*Cleanup*. When finished, remember to log out from both sessions.

# RStudio

We recommend using the [GenomeDK Desktop](https://desktop.genome.au.dk) to obtain
a graphical remote desktop on GenomeDK. Click "Start a new desktop" and choose
an instance that fits the resources you need, as well as a project folder to
associate the usage with.

When your desktop starts, you can now install Rstudio by opening the "Terminal"
application and running:

```bash
[cn-1001]$ conda install -n my-project rstudio-desktop
[cn-1001]$ conda activate my-project
(my-project) [cn-1001]$ rstudio
```

If you already installed RStudio, you can skip the installation step.

# TeXLive/LaTeX

TeXLive is available on GenomeDK in the form of TinyTeX, which is a stripped
down version of TeXLive. See [TinyTex](https://yihui.org/tinytex/) for more
details.

The Conda provided package is for CLI or script usage, the R integration has not
been tested and should probably be done using the guide described on the TinyTeX
home page.

To install TinyTeX with Conda in a new environment:

```bash
[fe-open-01]$ conda create <name of project> -c genomedk tinytex
```

or if you have an existing environment where you want TinyTeX installed:

```bash
[fe-open-01]$ conda activate <existing project>
[fe-open-01]$ conda install -c genomedk tinytex
```

Compiling documents is done using the normal TexLive commands, i.e.:

```bash
[fe-open-01]$ pdflatex test.tex
```

To install LaTeX packages from CTAN:

```bash
[fe-open-01]$ tlmgr install <package>
```

Search for packages using tlmgr:

```bash
[fe-open-01]$ tlmgr search <package>
```
