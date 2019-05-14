==============
Advanced usage
==============

.. todo::

    Two-factor authentication
    =========================

    * FreeOTP (recommended)
    * NetIQ Advanced Authentication
    * Google Authenticator


Public-key authentication
=========================

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

On your own computer, open the terminal of your choice and type:

.. code-block:: console

    [local]$ ssh-keygen

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

    [local]$ ssh-copy-id -i PUBLIC-KEY-PATH login.genome.au.dk

Replace *PUBLIC-KEY-PATH* with the path to your public key. You will be asked
to enter your password for the cluster. You should now be able to log in to the
cluster without typing your password. Test this by runnning:

.. code-block:: console

    [local]$ ssh USERNAME@login.genome.au.dk

You should not be prompted for a password.

Now, set up public-key access to all compute nodes. On the frontend, run the
same :command:`ssh-keygen` command as before:

.. code-block:: console

    [fe1]$ ssh-keygen

Again, just press :kbd:`Enter` to use the default values (and do not type in a
password). Then run:

.. code-block:: console

    [fe1]$ cat ~/.ssh/id_rsa.pub >> authorized_keys

You will now be able to SSH between compute nodes without typing a password.

Encrypting sensitive data
=========================

If you need to transfer sensitive data (for example human genomes) out of the
cluster you must encrypt the data first. Encrypting the data makes it
impossible for strangers to look at it without decrypting it, which requires
a password chosen by you.

Encrypt:

.. code-block:: console

    [fe1]$ openssl aes-256-cbc -a -salt -in data.txt -out data.txt.enc

This will encrypt :file:`data.txt` and write the encrypted data to
:file:`data.txt.enc`. You will be prompted for a password which is needed to
decrypt the file again.

Decrypt:

.. code-block:: console

    [fe1]$ openssl aes-256-cbc -d -a -in data.txt.enc -out data.txt.new

This will ask for the password used to encrypt the file. The decrypted contents
are written to :file:`data.txt.new`.

Collaborating on data
=====================

Data sharing between users can only be accomplished through dedicated project
folders to which only certain users have access. To apply for a project folder,
fill out `this <https://genomedk.wufoo.com/forms/request-new-project-group>`_
form.

When your request has been accepted, you and the other project members will
have access to a shared folder in :file:`/project/PROJECT-NAME` where
*PROJECT-NAME* is the name requested for your project. All users can add, edit,
and delete files in the project folder unless restrictions have been set on
specific files/folders.


Backing up data
===============

We provide backup on good old-fashioned tape to all users. To back up a file,
it should be put in a directory called either :file:`BACKUP`, :file:`Backup` or
:file:`backup`. The directory can be located in any other directory.

Data is backed up approximately once per week.

.. warning::

    Do not back up temporary data files that can easily be reproduced.
    Computation is cheap, but backup is *very* expensive. The backup is meant
    for scripts/source code and important raw data.


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

    [fe1]$ firefox

Since macOS does not include an X server, you will need to download and install
XQuartz_ on your computer. When installed, reboot the computer. Now, you just
need to tell SSH that you wish to enable X-forwarding. To do this, add ``-X``
to the :program:`ssh` command when logging in to the cluster, for example:

.. code-block:: console

    [local]$ ssh -X USERNAME@login.genome.au.dk

You should then be able to open e.g. Firefox on the frontend:

.. code-block:: console

    [fe1]$ firefox

On Windows, we recommend that you use MobaXterm_ which has an integrated X
server.

.. _XQuartz: https://www.xquartz.org/
.. _MobaXterm: https://mobaxterm.mobatek.net/


VNC
-------------------------

If you want to use a full virtual desktop you can use a VNC program. There are
lots of options but we recommend TightVNC_ which works on both Linux, macOS,
and Windows. When downloading TightVNC we recommend to get "TightVNC Java
Viewer" from the download section. It downloads a ZIP archive which contains an
executable JAR file.

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
