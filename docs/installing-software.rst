.. _installing_and_using_software:

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

For old users only...
---------------------

Previously, GenomeDK has made software available for users through a special
mechanism called :file:`/com/extra` which allowed users to load specific
software packages. However, there are several problems with the approach taken
here. If you are already using software from :file:`/com/extra`, note that this
may not be supported in the future and that no new software will be made
available through this mechanism.

Also, note that software installed through the old mechanism may interfere with
your environments. If you wish to use Conda we therefore encourage you to edit
your :file:`.bashrc` and :file:`.bash_profile` files and remove all lines which
loads software from :file:`/com/extra`.

Additionally, you should ensure that none of the above files reference any
system Python installation or related modules. It's also a good idea to remove
any reference to :file:`/com/extra/stable`.

.. _installing_conda:

Installing the Conda package manager
------------------------------------

Downloading and installing Conda is very simple, you just download and run the
installer:

.. code-block:: console

   [fe1]$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
   [fe1]$ chmod +x Miniconda3-latest-Linux-x86_64.sh
   [fe1]$ ./Miniconda3-latest-Linux-x86_64.sh -b
   [fe1]$ conda init

That's it! The last step makes sure that Conda will be available when you log
in, so now is a good time to open a new connection and check that Conda is
available.

Now let's configure Conda to make it super useful.

Configuring Conda
-----------------

Conda can install packages from different *channels*. This is similar to
*repositories* in other package managers. Here we'll add a few channels that
are commonly used in bioinformatics:

.. code-block:: console

    [fe1]$ conda config --add channels defaults
    [fe1]$ conda config --add channels bioconda
    [fe1]$ conda config --add channels conda-forge
    [fe1]$ conda config --add channels genomedk

Finally, to make Conda more predictable, we use *strict* channel priority:

.. code-block:: console

    [fe1]$ conda config --set channel_priority strict

Searching for packages
----------------------

You can easily search for Conda packages through the website anaconda.org_ or
using the :command:`conda search` command:

.. code-block:: console

    [fe1]$ conda search rstudio

Remember that the Conda package may not be called the exact official name of
the software. For example, the Conda package for the software *biobambam2* is
just called *biobambam*, so searching for *biobambam2* would not return any
results.

Using environments
------------------

When you just installed Conda, it comes with a single environment known as the
*base* environment. To activate the base environment, just type:

.. code-block:: console

    [fe1]$ conda activate
    (base) [fe1]$

You now have access to the software installed in the base environment.

Here is how the usage might look if we want to create a new environment with
the newest version of `PySAM`_:

.. literalinclude:: examples/conda-create-env
    :language: console

This gives us a clean environment with just the minimal number of packages
necessary to support PySAM. To use the software that was installed in the
environment, the environment needs to be activated first:

.. code-block:: console

    [fe1]$ conda activate amazing-project
    (amazing-project) [fe1]$ python -c 'import pysam; print(pysam.__version__)'
    0.6.0

Notice that the prompt changed to show you that you're now in the
*amazing-project* environment.

Conda can install any kind of software. This means that your entire setup can
be installed through Conda (if there's packages for it all). For example,
you can create an environment with Rstudio, R, and ggplot2 with a single
command.

Command reference
-----------------

To install software in the currenctly activated environment:

.. code-block:: console

    (amazing-project) [fe1]$ conda install PACKAGE-NAME

To remove a software package from the currently activated environment:

.. code-block:: console

    (amazing-project) [fe1]$ conda remove PACKAGE-NAME

To update a software package in the currently activated environment:

.. code-block:: console

    (amazing-project) [fe1]$ conda update PACKAGE-NAME

Since Conda knows about the entire environment you created, it can tell you
exactly which packages are used in the environment. This is very useful for
collaborating with others, since your collaborators can create an exact copy
of your environment with a single command.

To export your environment so that others can recreate it:

.. code-block:: console

    (amazing-project) [fe1]$ conda env export > environment.yml

The :file:`environment.yml` file contains an exact specification of your
environment and the packages installed. You can put this in your shared project
folder. Others will then be able to recreate your environment by running:

.. code-block:: console

    [fe1]$ conda env create -f environment.yml

You can read more about using environments for projects
:ref:`here <project_specific_environments>`. There's also also a `cheat sheet`_
with Conda commands available.

I don't think I can use Conda because...
----------------------------------------

A Conda package is not available
    In this case you can contact us and we will build a Conda package for you
    (when possible). Sometimes building a Conda package is not viable and in
    that case we will build a :ref:`Singularity <singularity>` image instead.

I'm part of a project that dictates the software I should use
    In this case the project should and probably will supply you for either a
    set of Conda packages or :ref:`Singularity <singularity>` images. In some
    cases you will only be given


.. _PySAM: http://pysam.readthedocs.io/en/stable/
.. _anaconda.org: https://anaconda.org/
.. _Conda: https://conda.io/docs/
.. _Anaconda: https://www.anaconda.com/download/
.. _cheat sheet: http://know.continuum.io/rs/387-XNW-688/images/conda-cheatsheet.pdf
