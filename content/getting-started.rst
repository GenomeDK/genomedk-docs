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



MobaXterm [Windows]
~~~~~~~~~~~~~~~~~~~



Changing your password
----------------------

This is important! Since e-mail is not secure, someone may get access to the
password that we sent to you. Thus, you should change it immediately after
logging in. Run the command::

.. code-block:: bash

    $ change-password

It will ask you for your current password, then ask what your new password
should be. Finally, it will ask you to confirm your new password by typing it
again.


Two-factor authentication
-------------------------

* FreeOTP (recommended)
* NetIQ Advanced Authentication
* Google Authenticator


Public-key setup
----------------

* ssh-keygen [Linux/macOS]
* PuttyGen [Windows]


Copying data
============

Encrypting sensitive data
-------------------------

If you need to transfer sensitive data (for example human genomes) out of the
cluster you must encrypt the data first. Encrypting the data makes it
impossible for strangers to look at it without decrypting it, which requires
a password chosen by you.

Encrypt:

.. code-block:: bash

    $ openssl aes-256-cbc -a -salt -in data.txt -out data.txt.enc

This will encrypt ``data.txt`` and write the encrypted data to
``data.txt.enc``. You will be prompted for a password which is needed to
decrypt the file again.

Decrypt:

.. code-block:: bash

    $ openssl aes-256-cbc -d -a -in data.txt.enc -out data.txt.new

This will ask for the password used to encrypt the file. The decrypted contents
are written to ``data.txt.new``.


From your own machine to/from the cluster
-----------------------------------------

* Filezilla [Linux/macOS/Windows]
* scp [Linux/macOS]
* SSH mount [Linux/macOS]
* rsync [Linux/macOS]
* CyberDuck [macOS]
* WinSCP [Windows]
* MobaXterm [Windows]


From the Internet to the cluster
--------------------------------

* wget

.. todo::

    Use the --progress=giga:force flag to avoid excessive output while
    downloading big files.


Using graphical interfaces
==========================

X or vnc yadda yadda

**X-forwarding**

You can use X-forwarding to tunnel individual graphical programs to your local
desktop. This works well for many programs, but programs that do fancy graphics
or anything animated might not work well.

.. todo::
    Add -X on linux
    Install and use XQuartz on OS X
    MobaXterm also allows X-forwarding
    Maybe Xming + putty X-forwarding on windows?



**VNC**

If you want to use a full virtual desktop you can use a VNC program. There are
lots of options but we recommend TightVNC_.  It is a Java program that will
work on Linux, Windows and OS X.

To use VNC you first need to login to the frontend and start a *VNC server*.
Starting the server is done with the ``vncserver`` command and looks like this:

.. code-block:: console

    $ vncserver
    [user@fe1 ~]$ vncserver

    You will require a password to access your desktops.

    Password:
    Verify:

    New 'fe1.genomedk.net:3 (user)' desktop is fe1.genomedk.net:3

    Creating default startup script /home/user/.vnc/xstartup
    Starting applications specified in /home/user/.vnc/xstartup
    Log file is /home/user/.vnc/fe1.genomedk.net:3.log

    [aeh@fe1 ~]$ vncserver -list

    TigerVNC server sessions:

    X DISPLAY # PROCESS ID
    :3      27049a

The display id (``:3`` in this example) is needed when you want to connect
the VNC client.

.. todo::
    What to put into TightVNC

To connect to the running VNC server the ssh tunnel through the login node has
to established. In case of TightVNC tunneling option is included in the
software it-self and following settings should be sufficient:

.. image:: images/tightvnc.png
    :align: center

.. todo::
    Screenshot of TightVNC settings

Editing files
=============

* Using nano to edit files directly on the cluster
* Other text editors that people might want to use (vim, emacs)
* Using X forwarding and gedit
* Editing files through a mount

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
