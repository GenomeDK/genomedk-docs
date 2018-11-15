===============================
Software-specific documentation
===============================

Python
======

Different Python versions can be installed through the Conda package manager.
For example, for a project that needs Python 2.7, create an environment like
this:

.. code-block:: console

    $ conda activate
    $ conda create -n myproject python=2.7
    $ conda activate myproject
    $ python --version

If you need Python 3.6 for another project, just create another environment
for that project:

.. code-block:: console

    $ conda deactivate # exit the myproject environment
    $ conda create -n mynewproject python=3.6
    $ conda activate mynewproject
    $ python --version

Jupyter Notebook/Lab
====================

Install the ``jupyter`` package in your environment.

One way to run a Jupyter Notebook on the cluster is to setup an SSH tunnel to
the Jupyter instance.

*Start an interactive job*. Login to the cluster and start an interactive job
where the notebook will run.

.. code-block:: console

    [local ~]$ ssh <user>@login.genome.au.dk
    [me@genomedk ~]$ srun --pty bash

*Setup SSH tunnel.* Back on your local computer open a second terminal to setup
the port-forwarding from the computing node to your computer.

.. code-block:: console

    [local ~]$ ssh -L$UID:$HOSTNAME:$UID USER@login.genome.au.dk

You will need to replace *USER* with your username on the cluster.

*Start the notebook*. Back on the computing node start a Jupyter notebook.
For this you may have to first unset the environmental variable
:envvar:`XDG_RUNTIME_DIR` (this could also be included in
:file:`~/.bashrc`).

.. code-block:: console

    [me@node ~]$ unset XDG_RUNTIME_DIR
    [me@node ~]$ conda activate <jupyter-env>
    [me@node ~]$ jupyter-notebook --no-browser --port=$UID --ip=0.0.0.0

*Run the notebook*. Back on your local computer start a web browser and
paste the URL from above. But replace the part in parenthesis with
*localhost* to get:

.. code-block:: plain

    http://localhost:<UID>/?token=....

*Cleanup*. When finished, remember to log out from both sessions.

RStudio
=======

RStudio is available on the cluster as a graphical application, which can
be run on both compute nodes and the frontend node. Bare in mind, the
frontend node must *not* be used for computation or analysis. RStudio needs
:ref:`X-forwarding <xforwarding>` to be enabled.

When logged in, you must either activate the environment where RStudio is
installed or install it into an environment yourself
(see :ref:`installing_and_using_software`):

.. code-block:: console

    [fe1]$ conda install -n my-project rstudio r
    [fe1]$ conda activate my-project
    (my-project) [fe1]$ rstudio

To run an analysis or computations in RStudio you will need to run RStudio in
an interactive job on a compute node.

.. code-block:: console

   [fe1]$ srun --mem=4g -c 1 --time=10:0:0 --pty bash
   srun: job 3597082 queued and waiting for resources
   srun: job 3597082 has been allocated resources
   [s03n11]$ conda activate my-project
   (my-project) [s03n11]$ rstudio

RStudio is automatically terminated if it allocates more than the reserved 4GB,
the 10 hours expires or the connection is lost. So remember to save your work!

Perl
====

.. warning::

    As of June 26, 2018 the old Perl module collection present in
    :file:`/com/extra/perl-cpan` will not work and support for it has been
    dropped.

.. note::

    Perl and Perl modules can be installed through Conda, which is also the
    recommended method. The method described here should only be used in cases
    where no Conda package exists for the module or it has been decided that
    Conda should not be used at all.

    See :ref:`installing_and_using_software` for help with Conda.

For installation of Perl modules from CPAN a simple command line tool can be
installed, and just one command will install it for you.

To start just run:

.. code-block:: console

    [fe1]$ cpan App::cpanminus

:file:`CPAN.pm` requires configuration, but most of it can be done
automatically. If you answer *no* below, you will enter an interactive dialog
for each configuration option instead.

.. code-block:: plain

    Would you like to configure as much as possible automatically? [yes]
    and just answer 'yes'

    <install_help>

    Warning: You do not have write permission for Perl library directories.

    To install modules, you need to configure a local Perl library directory or
    escalate your privileges.  CPAN can help you by bootstrapping the local::lib
    module or by configuring itself to use 'sudo' (if available).  You may also
    resolve this problem manually if you need to customize your setup.

    What approach do you want?  (Choose 'local::lib', 'sudo' or 'manual')
    here you want local::lib

    Autoconfigured everything but 'urllist'.

    Now you need to choose your CPAN mirror sites.  You can let me
    pick mirrors for you, you can select them from a list or you
    can enter them by hand.

    Would you like me to automatically choose some CPAN mirror
    sites for you? (This means connecting to the Internet) [yes]

For this, just answer *yes*. Then a lot of output follows, what is actually
important is:

.. code-block:: none

    local::lib is installed. You must now add the following environment variables
    to your shell configuration files (or registry, if you are on Windows) and
    then restart your command line shell and CPAN before installing modules:

    PATH="/home/xjk/perl5/bin${PATH:+:${PATH}}"; export PATH;
    PERL5LIB="/home/xjk/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"; export PERL5LIB;
    PERL_LOCAL_LIB_ROOT="/home/xjk/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"; export PERL_LOCAL_LIB_ROOT;
    PERL_MB_OPT="--install_base \"/home/xjk/perl5\""; export PERL_MB_OPT;
    PERL_MM_OPT="INSTALL_BASE=/home/xjk/perl5"; export PERL_MM_OPT;

You need to put these lines into you :file:`~/.bashrc` file.

After all that you need to start a new session, and you can install new modules
with :program:`cpanm` command, for example:

.. code-block:: console

    [fe1]$ cpanm DBD::mysql
    --> Working on DBD::mysql
    Fetching http://www.cpan.org/authors/id/C/CA/CAPTTOFU/DBD-mysql-4.046.tar.gz ... OK
    Configuring DBD-mysql-4.046 ... OK
    ==> Found dependencies: Test::Deep
    --> Working on Test::Deep
    Fetching http://www.cpan.org/authors/id/R/RJ/RJBS/Test-Deep-1.128.tar.gz ... OK
    Configuring Test-Deep-1.128 ... OK
    ==> Found dependencies: Test::Tester
    --> Working on Test::Tester
    Fetching http://www.cpan.org/authors/id/E/EX/EXODIST/Test-Simple-1.302136.tar.gz ... OK
    Configuring Test-Simple-1.302136 ... OK
    Building and testing Test-Simple-1.302136 ... OK
    Successfully installed Test-Simple-1.302136
    Building and testing Test-Deep-1.128 ... OK
    Successfully installed Test-Deep-1.128
    Building and testing DBD-mysql-4.046 ... OK
    Successfully installed DBD-mysql-4.046
    3 distributions installed
    [fe1]$ perldoc -l DBD::mysql
    /home/xjk/perl5/lib/perl5/x86_64-linux-thread-multi/DBD/mysql.pm
