.. _getting_started:

How does the cluster work?
==========================

.. todo:

    Graphical overview

A cluster consists of a large number of interconnected machines. Each machine
is very much like your own desktop computer, except it's much more powerful
and is optimized for specific workloads. However, like your desktop computer,
each machine (often referred to as *node*) has a CPU, some memory, and a hard
disk. The nodes running your programs are usually called *compute nodes*.

To turn the separate nodes in to a cluster we need three more ingredients: a
network connecting the nodes, data storage, and a queue manager. In
section we'll discuss these components in a bit more detail, to give you an
understanding of how a cluster works and how to utilize it properly.

Components of the cluster
-------------------------

Our cluster is connected through a high-performance network which
allows all of the nodes to "talk" to each other. This allows programs running
on one node to communicate with programs running on another node.

The compute nodes allow us to compute things and the network allows us to
communicate between nodes. However, we also need access to data. This is the
task of the storage system. Since bioinformatics is extremely data intensive we
can't make do with a single hard disk as you would in your own computer.
Instead we buy hundreds of hard disks and use a file system that can manage
files across all of these disks and present the user with one, united file
structure, as most users expect. In our case, this storage system is known as
*fast storage* since the distributed nature of the system also makes it very,
very fast. Files that are not put on the fast storage system are instead placed
on a normal, slow shared file system.

With storage the system is now functional. However, any user would be able to
log in to any node and start running a program, which may consume the resources
of the entire node, potentially causing other peoples' programs to crash.
Similarly, one user would be able to start thousands of runs of a program on
different nodes, consuming the resources of the entire cluster for an unknown
duration of time. In short, it would be complete anarchy!

To solve this problem we need the final component of the cluster, the *queue
manager*. The queue manager is much like the queues in the supermarket. You
stand in the queue and wait until it's your turn to pay. On the cluster, you
submit *jobs* to the queue, and your jobs will then be run on some node chosen
by the queue manager, once resources are available. The queue manager also
allows you to specify certain requirements for your program to run. For
example, your program may need to run on a node with *a lot* of memory. If you
specify this when submitting your job, the queue manager will make sure to run
the job on a node with at least that amount of memory available. At GenomeDK
we use a queue manager called SLURM, so to run your programs on the cluster,
you'll be interacting a lot with SLURM.

Things to remember...
---------------------

This ends our tour of the cluster setup. Now, here's a few things that you
should keep in mind when using the cluster...

* The nodes in a cluster are set up so that they're all (more or less) identical.
  This means that software that is available on one node will also be available
  on all other nodes, that your user account exists on all nodes, and that you
  can access your files in the same way on all nodes. When the queue manager runs
  your job in a node, it more or less corresponds to you logging in to the node
  and running the program yourself.

* A cluster is accessed through a single node, often denoted the *frontend*. The
  frontend node is in many ways identical to all of the other nodes, but it is
  set up to allow access from the Internet. Your day-to-day interaction with the
  cluster thus goes through the frontend. However, you should *not* run any
  computation or memory intensive programs on the frontend. All users share the
  frontend's resources and thus it should mainly be used for basics things like
  looking around the file system, writing scripts, and submitting jobs.

In the next section you will learn how to connect to the cluster, which
essentially means getting access to the frontend node, so that you can start
submitting jobs.


Get access to the cluster
=========================

You can request access to the cluster by filling out one of these forms:

* `Normal users`_
* `iPSYCH users`_

Once you've been granted access, you'll receive an e-mail with your password.
You'll then be able to connect to the cluster.

.. _Normal users: https://genomedk.wufoo.com/forms/request-access-to-cluster/
.. _iPSYCH users: https://genomedk.wufoo.com/forms/request-access-to-cluster-ipsych-only/

Connecting to the cluster
-------------------------

SSH [Linux/macOS]
~~~~~~~~~~~~~~~~~

On Linux, open the terminal of your choice. On macOS, you may use
:program:Terminal.app: which can be found in the `Applications/Utilities`
folder. In both cases, you should now be able to log in to the frontend
by typing this command:

.. code-block:: console

    $ ssh USERNAME@login.genome.au.dk


MobaXterm [Windows]
~~~~~~~~~~~~~~~~~~~

On Windows, download and install the `MobaXterm`_ application following the
instructions on the website.

.. _MobaXterm: https://mobaxterm.mobatek.net/


Changing your password
======================

This is important! Since e-mail is not secure, someone may get access to the
password that we sent to you. Thus, you should change it immediately after
logging in. Run the command:

.. code-block:: console

    $ change-password

It will ask you for your current password, then ask what your new password
should be. Finally, it will ask you to confirm your new password by typing it
again.


Two-factor authentication
=========================

* FreeOTP (recommended)
* NetIQ Advanced Authentication
* Google Authenticator


Public-key authentication setup
===============================

A public-key setup is a way to be able to access one computer from another
computer securely, but without typing a password every time you want to log in.
This is practical if you often log in to the frontend of the cluster. However,
we can also use a public-key setup to allow you to access any compute node on
the cluster from the frontend without typing your password every time. This is
especially handy when you're debugging a problem on the compute nodes.

.. todo::

    Note that for security reasons we require that you either (1) log in with
    a password and two-factor authentication (2) log in with public-key
    authentication

Here, we will first set up a public key for accessing the frontend. Then, we'll
set up a key for accessing compute nodes from the frontend.

ssh-keygen [Linux/macOS]
------------------------

On your own computer, open the terminal of your choice and type:

.. code-block:: console

    $ ssh-keygen

You'll be asked several questions. The defaults are just fine, so just press
the :kbd:`Enter` for all of them. Make sure to leave the passphrase empty!

The output should look similar to this:

.. code-block:: console
    :emphasize-lines: 6

    Generating public/private rsa key pair.
    Enter file in which to save the key (/Users/das/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /Users/das/.ssh/id_rsa.
    Your public key has been saved in /Users/das/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:XxSd35yPd1bUoIJQDBCAvxDu+pB25ipYpcmp+VEh5JE das@jorn
    The key's randomart image is:
    +---[RSA 2048]----+
    | .+oooo+.   ...o.|
    |ooE.   ...   oo o|
    |.oo .   . . o  +o|
    |......     o   .=|
    |.o *.   S   .  .o|
    | oB.     . .  . =|
    |==.o      .    o.|
    |B.+.             |
    |.++.             |
    +----[SHA256]-----+

Note the path of the public key (on the highlighted line). To copy the public
key to the cluster, run:

.. code-block:: console

    $ ssh-copy-id -i PUBLIC-KEY-PATH login.genome.au.dk

Replace `PUBLIC-KEY-PATH` with the path to your public key. You will be asked
to enter your password for the cluster. You should now be able to log in to the
cluster without typing your password. Test this by runnning:

.. code-block:: console

    $ ssh USERNAME@login.genome.au.dk

You should not be prompted for a password.

Now, set up public-key access to all compute nodes. On the frontend, run the
same :command:`ssh-keygen` command as before:

.. code-block:: console

    $ ssh-keygen

Again, just press :kbd:`Enter` to use the default values (and do not type in a
password). Then run:

.. code-block:: console

    $ cat ~/.ssh/id_rsa.pub >> authorized_keys

You will now be able to SSH between compute nodes without typing a password.

PuttyGen [Windows]
------------------


.. _mounting:

Accessing your files locally
============================

You can access your files on GenomeDK locally by a process called *mounting*.
Mounting the GenomeDK filesystem locally makes it possible to access and edit
your files as if they were located in a folder on your own harddrive.

sshfs [Linux/macOS]
-------------------

On Linux, install the :program:`sshfs` program through your package manager.

On distros with the :program:`apt` package manager (Ubuntu, Mint etc.):

.. code-block:: console

    $ apt-get install sshfs

On distros with the :program:`yum` package manager (Fedora, CentOS etc.):

.. code-block:: console

    $ yum install sshfs

On macOS, download and install the *SSHFS* and *FUSE for macOS* packages
from the `OSX FUSE`_ website.

Create a directory where the filesystem will be mounted:

.. code-block:: console

    $ mkdir ~/GenomeDK

Now mount the filesystem by running this command:

.. code-block:: console

    $ sshfs USERNAME@login.genome.au.dk:/home/USERNAME ~/GenomeDK \
        -o idmap=none -o uid=$(id -u),gid=$(id -g) \
        -o allow_other -o umask=077 -o follow_symlinks

   Where *USERNAME* should be replaced with your GenomeDK username. You should
   now be able to access your files on GenomeDK by going to the ``~/GenomeDK``
   directory on your computer.

To unmount the directory, run:

.. code-block:: console

    $ umount ~/GenomeDK

.. _OSX FUSE: https://osxfuse.github.io/

Win-SSHFS [Windows]
-------------------


Encrypting sensitive data
=========================

If you need to transfer sensitive data (for example human genomes) out of the
cluster you must encrypt the data first. Encrypting the data makes it
impossible for strangers to look at it without decrypting it, which requires
a password chosen by you.

Encrypt:

.. code-block:: console

    $ openssl aes-256-cbc -a -salt -in data.txt -out data.txt.enc

This will encrypt ``data.txt`` and write the encrypted data to
``data.txt.enc``. You will be prompted for a password which is needed to
decrypt the file again.

Decrypt:

.. code-block:: console

    $ openssl aes-256-cbc -d -a -in data.txt.enc -out data.txt.new

This will ask for the password used to encrypt the file. The decrypted contents
are written to ``data.txt.new``.


Copying data
============

From your own machine to/from the cluster
-----------------------------------------

If you :ref:`mounted <mounting>` GenomeDK on your computer, you can copy files to
and from the cluster by simple drag-and-drop. Otherwise you can use one of the
solutions listed here.


Filezilla [Linux/macOS/Windows]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

scp [Linux/macOS]
~~~~~~~~~~~~~~~~~

rsync [Linux/macOS]
~~~~~~~~~~~~~~~~~~~

CyberDuck [macOS]
~~~~~~~~~~~~~~~~~

WinSCP [Windows]
~~~~~~~~~~~~~~~~

MobaXterm [Windows]
~~~~~~~~~~~~~~~~~~~


From the Internet to the cluster
--------------------------------

* wget

.. todo::

    Use the --progress=giga:force flag to avoid excessive output while
    downloading big files.


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

Xorg [Linux]
~~~~~~~~~~~~

Since most Linux distributions already include an X server, you simply need to
tell SSH that you wish to enable X-forwaring. To do this, add ``-X`` to the
:program:`ssh` command when logging in to the cluster, for example:

.. code-block:: console

    $ ssh -X USERNAME@login.genome.au.dk

You should then be able to open e.g. Firefox on the frontend:

.. code-block:: console

    [fe1]$ firefox

XQuartz [macOS]
~~~~~~~~~~~~~~~

Since macOS does not include an X server, you will need to download and install
XQuartz_ on your computer. When installed, reboot the computer. Now, you just
need to tell SSh that you wish to enable X-forwarding. To do this, add ``-X``
to the :program:`ssh` command when logging in to the cluster, for example:

.. code-block:: console

    $ ssh -X USERNAME@login.genome.au.dk

You should then be able to open e.g. Firefox on the frontend:

.. code-block:: console

    [fe1]$ firefox

.. _XQuartz: https://www.xquartz.org/

MobaXterm [Windows]
~~~~~~~~~~~~~~~~~~~



VNC
---

If you want to use a full virtual desktop you can use a VNC program. There are
lots of options but we recommend TightVNC_ which works on both Linux, macOS,
and Windows.

To use VNC you first need to login to the frontend and start a *VNC server*.
Starting the server is done with the ``vncserver`` command and looks like this:

.. code-block:: console
    :emphasize-lines: 8

    [fe1]$ vncserver

    You will require a password to access your desktops.

    Password:
    Verify:

    New 'fe1.genomedk.net:3 (user)' desktop is fe1.genomedk.net:3

    Creating default startup script /home/user/.vnc/xstartup
    Starting applications specified in /home/user/.vnc/xstartup
    Log file is /home/user/.vnc/fe1.genomedk.net:3.log

The display id (``:3`` in this example) is needed when you want to connect
the VNC client.

To connect to the running VNC server the SSH tunnel through the login node has
to be established. In case of TightVNC, the tunneling option is included in the
software itself and following settings should be sufficient:

.. image:: images/tightvnc.png
    :align: center

Note the "Port" field! The number specified must be 5900 plus the display ID,
which in this example was :3. Thus, the port number becomes 5903.

.. _TightVNC: https://www.tightvnc.com/

Editing files
=============

If you :ref:`mounted <mounting>` GenomeDK on your computer, you can edit files
directly by just opening them with your prefered text editor on your computer.
Otherwise you can use one of the solutions listed here.

Nano, vim, emacs
----------------

With editors like :program:`nano`, :program:`vim` and :program:`emacs` you can
edit files directly on the cluster. The editor itself also runs on the cluster
and thus your editor settings etc. are conserved, even if you log in from
another computer. Also, these editors don't require a graphical user interface,
so you don't need X-forwarding or VNC.

The :program:`nano` editor is by far the simplest editor of three, but also the
least powerful. However, it's just fine for quickly editing scripts or looking
at output files. The documentation for :program:`nano` can be reached by
running the command:

.. code-block:: console

    [fe1]$ man nano

You can open :program:`nano` by running:

.. code-block:: console

    [fe1]$ nano name-of-file.txt

Likewise, `vim`_ and `emacs`_ are already installed on the cluster.
Documentation for each editor can be found on their respective websites.

.. _vim: https://www.vim.org/
.. _emacs: https://www.gnu.org/software/emacs/index.html


Gedit with X-forwaring
----------------------

If you want a graphical user interface and a more familiar editing experience,
you may use the :program:`Gedit` editor with :ref:`X-forwarding <xforwarding>`.
Make sure that you are connected to the cluster with X-forwarding enabled. Then
run:

.. code-block:: console

    [fe1]$ gedit

This will open the :program:`Gedit` editor in a new window. Since the editor
runs on the frontend, you have access to all of your files on the cluster.

Interacting with the queue
==========================

* What is an interactive job?
* Using srun
* Now we're on a different node, fs is the same, but env may not be

* What is a batch job?
* Writing a job script
* Annoying to write job script manually, so most people use *gwf* instead.

Installing and using software
=============================

.. warning::

    Previously, GenomeDK has made software available for users through a
    special mechanism called :file:`/com/extra` which allowed users to load
    specific software packages. However, there are several problems with the
    approach taken here. If you are already using software from `/com/extra`,
    note that this may not be supported in the future and that no new software
    will be made available through this mechanism.

    Also, note that software installed through the old mechanism may interfere
    with your environments. If you wish to use Conda we therefore encourage you
    to edit your :file:`.bashrc` file and remove all lines which loads software
    from :file:`/com/extra`.

We recommend that you install and use the `Conda`_ package manager to install
software on GenomeDK.

Downloading and installing Conda is very simple, you just download and run the
installer:

.. code-block:: console

   [fe1]$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
   [fe1]$ chmod +x Miniconda3-latest-Linux-x86_64.sh
   [fe1]$ ./Miniconda3-latest-Linux-x86_64.sh

You can use follow the installers suggestions about where to install and
the let it add conda to your :file:`.bashrc`.

Now that we have conda available we also need a few settings. The first
is necessary and tells conda to trust our proxy server, the rest adds
some recommended "channels" which will make a whole bunch of useful
packages available to install.

.. code-block:: console

    [fe1]$ conda activate
    [fe1]$ conda config --add channels defaults
    [fe1]$ conda config --add channels conda-forge
    [fe1]$ conda config --add channels bioconda

The clever thing about conda is that it allows you to use separate
environments for separate projects. If you have a project where you've
installed a bunch packages into your Python or R there is no reason for
those to accidentally seep in to your next project. If you want to try
different versions of some package you can just create separate
environments for them instead of installing and uninstalling multiple
times. With separate environments you force yourself to make the
dependencies for each project explicit which in turn makes it easier for
collaborators to run your code and improves reproducibility.

Here is how the usage might look if we want to create a new environment
with the newest version of `pysam`_:

.. literalinclude:: examples/conda-create-env
    :language: console

This gives us a clean environment with just the minimal number of packages
necessary to support pysam. To use the software that was installed in the
environment, the environment needs to be activated first:

.. code-block:: console

    [fe1]$ conda activate amazing-project
    (amazing-project) [fe1]$ python -c 'import pysam; print(pysam.__version__)'
    0.6.0

Notice that the prompt changed to show you, that you're now in the
*amazing-project* environment.

Conda can install any kind of software. This means that your entire setup can
be installed through Conda (if there's packages for it all). For example,
you can create an environment with Rstudio, R, and ggplot2 with a single
command. You can search for packages `here <anacondaorg>`_.

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
:ref:`here <project_specific_environments>`.

.. _pysam: http://pysam.readthedocs.io/en/stable/
.. _anacondaorg: https://anaconda.org/
.. _Conda: https://conda.io/docs/
.. _Anaconda: https://www.anaconda.com/download/

.. todo::

    For existing users:

    * Migrating from old setup to conda environments
    * Remove all uses of /com/extra (.bashrc, .bash_profile)
    * Check PATH in general
    * DISCLAIMER: DO NOT USE /com/extra


    * Should Conda be installed by default?
    * What is an environment?
    * Why are environments useful?
    * Creating environments
    * Changing between environments
    * Installing software in an environment
    * Sharing an environment
