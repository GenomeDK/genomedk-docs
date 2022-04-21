.. _installing_and_using_software:

=============================
Installing and using software
=============================

We recommend that you install and use the `Conda`_ package manager to install
software on GenomeDK. However, we used to have another mechanism for installing
software that has now been deprecated. If you used this mechanism before,
please read through the next section for instructions on how to transition
safely to Conda. If you're a new user you may skip the next section and jump
directly to :ref:`installing_conda`.

**Why Conda?** The clever thing about Conda is that it allows you to use
separate environments for separate projects. If you have a project where you've
installed a bunch packages for Python or R there is no reason for those to
accidentally seep in to your next project. If you want to try different
versions of some package you can just create separate environments for them
instead of installing and uninstalling multiple times. With separate
environments you force yourself to make the dependencies for each project
explicit which in turn makes it easier for collaborators to run your code and
improves reproducibility.

Conda also provides access to thousands of packages used in data science and
bioinformatics. These packages can be installed with a single command, so you
don't have to worry about compilers, dependencies, and where to put binaries.

.. _installing_conda:

Installing the Conda package manager
====================================

Downloading and installing Conda is very simple, you just download and run the
installer:

.. code-block:: console

   [fe-open-01]$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
   [fe-open-01]$ chmod +x miniconda.sh
   [fe-open-01]$ bash miniconda.sh -b
   [fe-open-01]$ ./miniconda3/bin/conda init bash

That's it! The last two step makes sure that Conda will be available when you
log in, so now is a good time to open a new connection and check that Conda is
available.

Now let's configure Conda to make it super useful.

Configuring Conda
=================

Conda can install packages from different *channels*. This is similar to
*repositories* in other package managers. Here we'll add a few channels that
are commonly used in bioinformatics:

.. code-block:: console

    [fe-open-01]$ conda config --add channels defaults
    [fe-open-01]$ conda config --add channels bioconda
    [fe-open-01]$ conda config --add channels conda-forge
    [fe-open-01]$ conda config --add channels genomedk

Conda creates a ``base`` environment which contains Conda itself. It's tempting
to install packages in ``base``, but that might ruin your Conda installation.
You should *never* install anything in the base environment.

To prevent that you accidentially install something in the ``base``
environment, we'll configure Conda so that it doesn't activate it when you log
in:

.. code-block:: console

    [fe-open-01]$ conda config --set auto_activate_base false

Searching for packages
======================

You can easily search for Conda packages through the website anaconda.org_ or
using the :command:`conda search` command:

.. code-block:: console

    [fe-open-01]$ conda search rstudio

Remember that the Conda package may not be called the exact official name of
the software. For example, the Conda package for the software *biobambam2* is
just called *biobambam*, so searching for *biobambam2* would not return any
results.

Using environments
==================

When you just installed Conda, it comes with a single environment known as the
*base* environment. To activate the base environment, just type:

.. code-block:: console

    [fe-open-01]$ conda activate
    (base) [fe-open-01]$

You now have access to the software installed in the base environment.

Here is how the usage might look if we want to create a new environment with
the newest version of `PySAM`_:

.. literalinclude:: examples/conda-create-env
    :language: console

This gives us a clean environment with just the minimal number of packages
necessary to support PySAM. To use the software that was installed in the
environment, the environment needs to be activated first:

.. code-block:: console

    [fe-open-01]$ conda activate amazing-project
    (amazing-project) [fe-open-01]$ python -c 'import pysam; print(pysam.__version__)'
    0.6.0

Notice that the prompt changed to show you that you're now in the
*amazing-project* environment.

Conda can install any kind of software. This means that your entire setup can
be installed through Conda (if there's packages for it all). For example,
you can create an environment with Rstudio, R, and ggplot2 with a single
command.

Command reference
=================

To install software in the currenctly activated environment:

.. code-block:: console

    (amazing-project) [fe-open-01]$ conda install PACKAGE-NAME

To remove a software package from the currently activated environment:

.. code-block:: console

    (amazing-project) [fe-open-01]$ conda remove PACKAGE-NAME

To update a software package in the currently activated environment:

.. code-block:: console

    (amazing-project) [fe-open-01]$ conda update PACKAGE-NAME

Since Conda knows about the entire environment you created, it can tell you
exactly which packages are used in the environment. This is very useful for
collaborating with others, since your collaborators can create an exact copy
of your environment with a single command.

To export your environment so that others can recreate it:

.. code-block:: console

    (amazing-project) [fe-open-01]$ conda env export > environment.yml

The :file:`environment.yml` file contains an exact specification of your
environment and the packages installed. You can put this in your shared project
folder. Others will then be able to recreate your environment by running:

.. code-block:: console

    [fe-open-01]$ conda env create -f environment.yml

You can read more about using environments for projects
:ref:`here <project_specific_environments>`. There's also also a `cheat sheet`_
with Conda commands available.

I don't think I can use Conda because...
========================================

A Conda package is not available
    In this case you can contact us and we will build a Conda package for you
    (when possible). Sometimes building a Conda package is not viable and in
    that case we will build a :ref:`Singularity <singularity>` image instead.

I'm part of a project that dictates the software I should use
    In this case the project should and probably will supply you for either a
    set of Conda packages or :ref:`Singularity <singularity>` images. If not,
    most or all of the software will probably be available through Conda
    anyway, so you can still set up an environment with the software.


.. _PySAM: http://pysam.readthedocs.io/en/stable/
.. _anaconda.org: https://anaconda.org/
.. _Conda: https://conda.io/docs/
.. _Anaconda: https://www.anaconda.com/download/
.. _cheat sheet: http://know.continuum.io/rs/387-XNW-688/images/conda-cheatsheet.pdf

Mamba - a Conda alternative
===========================

Conda can take an extremely long time solve dependencies and sometimes Conda
may never finish solving dependencies - this is where Mamba - the drop-in 
replacement for Conda comes in.

From the `Mamba`_ project description:

  Mamba is a reimplementation of the conda package manager in C++.
  
  - parallel downloading of repository data and package files using
    multi-threading
  - libsolv for much faster dependency solving, a state of the art library 
    used in the RPM package manager of Red Hat, Fedora and OpenSUSE
  - core parts of mamba are implemented in C++ for maximum efficiency

It can be installed via Conda:

.. code-block:: console

   [fe-open-01]$ conda install mamba -n base -c conda-forge


.. _Mamba: https://github.com/mamba-org/mamba

Using graphical interfaces
==========================

There's two options for using programs with a graphical user interface on
GenomeDK.

.. _xforwarding:

X-forwarding
------------

You can use X-forwarding to tunnel individual graphical programs to your local
desktop. This works well for many programs, but programs that do fancy graphics
or anything animated might not work well.

On Linux you simply need to tell SSH that you wish to enable X-forwarding. To
do this, add ``-X`` to the :program:`ssh` command when logging in to the
cluster, for example:

.. code-block:: console

    [local]$ ssh -X USERNAME@login.genome.au.dk

You should then be able to open e.g. Firefox on the frontend:

.. code-block:: console

    [fe-open-01]$ firefox

Since macOS does not include an X server, you will need to download and install
XQuartz_ on your computer. When installed, reboot the computer. Now, you just
need to tell SSH that you wish to enable X-forwarding. To do this, add ``-X``
to the :program:`ssh` command when logging in to the cluster, for example:

.. code-block:: console

    [local]$ ssh -X USERNAME@login.genome.au.dk

You should then be able to open e.g. Firefox on the frontend:

.. code-block:: console

    [fe-open-01]$ firefox

On Windows, we recommend that you use MobaXterm_ which has an integrated X
server.

.. _XQuartz: https://www.xquartz.org/
.. _MobaXterm: https://mobaxterm.mobatek.net/


VNC
---

If you want to use a full virtual desktop you can use a VNC program. There are
lots of options but we recommend TightVNC_ 2.x which works on both Linux,
macOS, and Windows. When downloading TightVNC we recommend to get "TightVNC
Java Viewer". It downloads a ZIP archive which contains an executable JAR file.

To use VNC you first need to login to the frontend and start a *VNC server*.
Starting the server is done with the ``vncserver`` command and looks like this:

.. code-block:: console
    :emphasize-lines: 8

    [fe-open-01]$ vncserver

    You will require a password to access your desktops.

    Password:
    Verify:

    New 'fe-open-01.genomedk.net:3 (user)' desktop is fe-open-01.genomedk.net:3

    Creating default startup script /home/user/.vnc/xstartup
    Starting applications specified in /home/user/.vnc/xstartup
    Log file is /home/user/.vnc/fe-open-01.genomedk.net:3.log

The display id (``:3`` in this example) is needed when you want to connect
the VNC client.

To connect to the running VNC server the SSH tunnel through the login node has
to be established. In case of TightVNC, the tunneling option is included in the
software itself and following settings should be sufficient:

.. image:: tightvnc.png
    :align: center

Note the "Port" field! The number specified must be 5900 plus the display ID,
which in this example was :3. Thus, the port number becomes 5903.

.. _TightVNC: https://www.tightvnc.com/download.php
.. _MobaXterm: https://mobaxterm.mobatek.net/
