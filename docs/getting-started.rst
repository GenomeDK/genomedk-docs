How does the cluster work?
==========================

* Graphical overview
* Queuing system, partitions
* Different types of storage

Get access to the cluster
=========================

* Creating an account
* Connecting to the closer 
* Two-factor authentication
* Public key setup

Copying data
============

* From your own machine
    * scp
    * mount on linux/osx
    * winscp on windows
    * mobaxterm on windows
    * filezilla sftp on all platforms
    * CyberDuck on OS X
    * rsync on OS X / Linux
* From the Internet
    * wget

Using graphical interfaces
==========================

X or vnc yadda yadda

**X-forwarding**

You can use X-forwarding to tunnel individual graphical programs to your local
desktop. This works well for many programs, but programs that do fancy graphics
or anything animated might not work well.

TODO: Add -X on linux
TODO: Install and use XQuartz on OS X
TODO (maybe): Xming + putty X-forwarding on windows?
TODO: MobaXterm also allows X-forwarding

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

TODO: What to put into TightVNC

To connect to the running VNC server the ssh tunnel through the login node has to established. In case of TightVNC tunneling option is included in the software it-self and following settings should be sufficient:

.. image:: images/TightVNC.png
    :align: center

TODO: Screenshot of TightVNC settings

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

