.. _best_practices:

Structure and document your projects
====================================

Using the same project structure for all of your projects provide a lot of
benefits. We recommend that you follow the structure shown below. It is
flexible enough to work for a wide variety of data analysis projects, but
feel free to adapt it to your needs.

.. code-block:: text

    myproject/
        data/
           README.txt
           ...
        steps/
           README.txt
           ...
        results/
           README.txt
           ...
        plots/
           README.txt
           ...
        scripts/
           README.txt
           ...
        docs/
           1-installing-dependencies.txt
           2-running-some-analysis.txt
           3-running-some-other-analysis.txt
           ...
        environment.yml
        NOTEBOOK.txt
        README.txt
        ...

This may seem like a large structure for a simple project, but remember that
you can always scale down this structure. E.g. for small projects you may drop
the ``docs`` folder and simply document how to run your analyses in
``myproject/README.txt``. Each folder contains a ``README.txt`` file which
documents the purpose and contents of the folder. You don't have to write a
lot, just what's necessary to understand your project and its different parts.

.. warning::

    If you consider modifying the basic project structure, make sure that you
    thought about what it means for the reproducibility of your project! Consider
    whether it is necessary to change the structure or if you're just being lazy.

Let's have a look at the goal of each folder:

data
    This folder should contain your raw/original data files. You should
    consider this directory read-only (even better: make it read-only).
    However, it is okay to add new files to the folder, as long as you
    don't modify or delete other files in the folder.

steps
    This folder contains data files produced by various steps in your
    analysis. If you're using a workflow tool like GWF, this directory is where
    you would put the output of your targets. For large workflows it may be a
    good idea to make subfolders for each step.

results
    This folder contains the final data files (not plots) produced by
    your analysis. Again, you may want to put these in subfolders for large
    workflows with many result files.

plots
    This directory contains scripts for generating plots from the result
    files and the resulting plots in one or more formats. For example, you could
    have a script called ``plot_distribution_of_tumor_purities.py`` which produces
    a plot called ``distribution_of_tumor_purities.pdf``.

scripts
    This directory contains the scripts you wrote for your analysis,
    e.g. those used by your workflow. Use file names that describe the purpose
    of the scripts. At the top of each script, insert a comment that briefly
    describes the input, output and purpose of the script. Again, a few
    sentences is better than nothing and may often be enough.

docs
    This folder is mainly for large projects where it may be nice to
    document each analysis in its own file. If you use plain text files as shown
    above, remember to give them numbers to make it easier for the reader to
    figure out where to begin.

In addition to the folders described above, the project root should also
contain at least two files: a file documenting your project structure
(this could just contain a short introduction to the project and a link
to this page) and a file describing your environment.

Multi-user project
==================

In the case of multi-user projects where many people collaborate on the same
data, the following structure may be used.

.. code-block:: text

    myproject/
        data/
            README.txt
            ...
        people/
            username1/
            username2/
            username3/
            ...
        results/
            README.txt
            ...
        README.txt

In this scenario the root folder contains a people folder which a subfolder
for each person working on the project. Each of these folders uses the same
directory structure as described for single-user projects. This means that
each user his/her own scripts, sandbox, docs, results, steps and data folders.
The user-specific data folder can contain data files that are not used by
everyone associated with the project, but it can also contain symbolic links
to the root data folder.

The root results folder is used to aggregate results from different users by
creating symbolic links to specific result files. For example, say that user
A produced a result :file:`foo.txt` and user B wants to use this file. User B can
then create a symlink from :file:`myproject/people/A/results/foo.txt` to
:file:`/myproject/results/foo.txt`.

Use project-specific environments
=================================

An environment is a isolated collection of programs and libraries. You can
have multiple environments (e.g. one for each project) and these environments
can have different software and even different versions of the same software
installed simultaneously. To use an environment you must *activate* it. This
will load all of the software available in the environment into your shell so
that it is available as any other program installed on the machine.

First, download and install the Anaconda distribution according to the
instructions for your platform. Instructions can be found here along with
detailed documentation on how to use the :command:`conda` command. Then
run:

.. code-block:: console

    $ conda activate
    $ conda create -n myproject python=3.5

If the first command doesn't work, you're running an old version of Anaconda.
Please download and install a newer version.

This will create an environment called *myproject* with Python 3.5 installed.
To enter the environment, use this command:

.. code-block:: console

    $ source activate myproject

Now check that the environment has been activated correctly by starting Python:

.. code-block:: console

    $ python
    Python 3.5.1 |Continuum Analytics, Inc.| (default, Dec 7 2015, 11:24:55)
    [GCC 4.2.1 (Apple Inc. build 5577)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ImportError: No module named 'numpy'

As you can see running the python command now opens Python 3.5.1 and we can
also see that the Python installation was provided by Continuum, the company
providing Anaconda. However, if we try to import e.g. numpy we get an error
because this package has not been installed in the environment. Let's try to
install it. Press :kbd:`Control-d` to close the Python interpreter and then
run this command:

.. code-block:: console

    $ conda install numpy

This will install the latest version of the numpy package into the current
environment (you may have to say yes to installing the packages). Now try to
open Python again and import numpy. It should work this time.

The conda install command lets you choose exactly which version of the package
to install. When we created the ``myproject`` environment which chose to
specifically install Python version 3.5 using the ``=`` character. This syntax
also works for conda install, e.g. ``conda install numpy=1.9.1``.

When you are done working with your project, or you want to switch to another
environment for working with another project, run the command:

.. code-block:: console

    $ source deactivate

That's fine, but we still need a way to export an environment and its packages
to other people. We can do this with:

You may think that Anaconda only works for Python and Python packages, however,
Anaconda actually works for any program that is available as an Anaconda package
(which may Python, R or any other language, including binaries). Packages are
provided through channels. While the official Anaconda channel contains thousands
of popular packages, other channels provide even more packages. One such channel
is the R channel which provides access to the R programming language and many
popular libraries used with R. To get access to the R channel run:

.. code-block:: console

    $ conda config --add channels r

Another great channel is the Bioconda channel which provides access to
hundreds of packages related to bioinformatics such as BWA, samtools, BLAST
etc.:

.. code-block:: console

    $ conda config --add channels bioconda

However, all of this hardly improves reproducibility. However, Anaconda allows
you to specify an environment (a list of channels and packages with specific
versions) in an environment file. Create a file called :file:`environment.yml`
in the project folder and put this in the file:

.. code-block:: yaml

    name: myproject
    channels:
      - r
      - bioconda
    dependencies:
      - python=3.4
      - numpy=1.9.2
      - r-essentials=1.4
      - bwa=0.7.15

Now, for the sake of clarity, let's remove our existing myproject environment.

.. code-block:: console

    $ conda env remove -n myproject

We can now create the exact environment specified in environment.yml by simply running:

.. code-block:: console

    $ conda env create

As you work you may need to change your environment, e.g. update a package to a
more recent version, add or remove a package. To do this, just modify the
environment.yml file and then run:

.. code-block:: console

    $ conda env update --prune

Sanity check for repeatability
==============================

To check whether your project can easily be run by another person, package it
into a zip-file and send it to one of your colleagues. They should be able to
run your analysis with no help from you and by only reading the documentation
in your project (and maybe this document).
