.. _getting_started:

===============
Getting started
===============

.. note::

    If you don't know what a closed zone is, or you know that you're not
    running in one, skip all red boxes like the one below. Most users on
    GenomeDK are *not* in a closed zone.

.. admonition:: Closed zone...

    Running in a closed zone means running in a restricted environment.
    In some cases, this means that you must use special commands or
    follow special instructions for certain things. This will be noted in red
    boxes like this one throughout the documentation.

This page will tell you everything you need to know to get up and running on
GenomeDK. However, we assume that you have some experience with the command
line/terminal.

.. _request_access:

Get access to the cluster
=========================

You should check out our :ref:`terms`.

To request a user, fill out the `user request form <https://console.genome.au.dk/user-requests/create/>`_.

Once you've been granted access, you'll receive an e-mail. You'll then be able
to connect to the cluster.

Cite us!
========

We provide GenomeDK as a resource to research. If you publish results from
computations performed on GenomeDK, it is important that you acknowledge/cite
GenomeDK in your publications. We recommend phrasing it like this:

  *Some/all of the computing for this project was performed on the GenomeDK
  cluster. We would like to thank GenomeDK and Aarhus University for providing
  computational resources and support that contributed to these research
  results.*

.. _connecting_to_the_cluster:

Connecting to the cluster
=========================

GenomeDK is divided into multiple *zones*. Most users belong to the open zone.
If you're in doubt about which zone you belong to, check your account
confirmation e-mail. If it doesn't mention a specific zone, you belong to the
open zone. If still in doubt, please contact support.

Connecting to the open zone
---------------------------

On Linux, open the terminal of your choice. On macOS, you may use
:program:`Terminal.app` which can be found in the
:file:`/Applications/Utilities` folder. In both cases, you should now be able
to log in to the frontend by typing this command:

.. code-block:: console

    [local]$ ssh USERNAME@login.genome.au.dk

On Windows, you have multiple options. On Windows 10, open
:program:`PowerShell`. You should then be able to type:

.. code-block:: console

    [local]$ ssh.exe USERNAME@login.genome.au.dk

Older versions of Windows do not include the :program:`ssh` command and thus
you will need to install an alternative yourself. We recommend MobaXterm_.

.. note::

    Access to GenomeDK is restricted to the internal network at Aarhus
    University. However, if you need access from abroad or for some other reason
    can not connect connect from AU, feel free to :ref:`contact us <contact>` to
    have your IP whitelisted. You can see what your IP is at
    https://console.genome.au.dk/ip.

.. _zone_connect:

Connecting to a closed zone
---------------------------

#. Download and install the remote desktop client for your operating system on
   your local machine.

   * `Download client for Windows <https://www.nomachine.com/download/download&id=8>`_
   * `Download client for macOS <https://www.nomachine.com/download/download&id=7>`_
   * `Download client for Linux <https://www.nomachine.com/download/linux&id=1>`_

#. Download and install FreeOTP, Google Authenticator or any similar app on your
   phone. If you are at AU you probably already have Microsoft Authenticator
   installed.

#. Download the connection file for the zone you wish to connect to:

    .. toctree::
        :maxdepth: 1

        ../zones/ipsych
        ../zones/brain

#. Using the login information received in your mailbox. Login by entering your
   username and password.

   Assuming you entered correctly you will get access to the virtual desktop.

   Open the the authenticator app on your phone and scan the :file:`QRCode.png`
   located on your NoMachine desktop. From now on you will need to generate a
   one-time password with the authenticator app every time you log in.

.. _MobaXterm: https://mobaxterm.mobatek.net/

.. _change_password:

Changing your password
======================

This is important! Since e-mail is not secure, someone may get access to the
password that we sent to you. Thus, you should change it immediately after
logging in. Run the command:

.. code-block:: console

    [fe-open-01]$ gdk-auth-change-password

It will ask you for your current password, then ask what your new password
should be. Finally, it will ask you to confirm your new password by typing it
again.

.. warning::

    Do not use :program:`passwd`, :program:`yppasswd` or
    :program:`ipsych-passwd` to change your password. These commands won't
    work in all cases or at all.


I forgot my password
====================

Send an e-mail to support to request a password reset.


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

    [local]$ ssh-copy-id -i PUBLIC-KEY-PATH USERNAME@login.genome.au.dk

Replace *PUBLIC-KEY-PATH* with the path to your public key and *USERNAME* with
your cluster username. You will be asked to enter your password for the cluster.
You should now be able to log in to the cluster without typing your password.
Test this by runnning:

.. code-block:: console

    [local]$ ssh USERNAME@login.genome.au.dk

You should not be prompted for a password.

Now, set up public-key access to all compute nodes. On the frontend, run the
same :command:`ssh-keygen` command as before:

.. code-block:: console

    [fe-open-01]$ ssh-keygen

Again, just press :kbd:`Enter` to use the default values (and do not type in a
password). Then run:

.. code-block:: console

    [fe-open-01]$ cat ~/.ssh/id_rsa.pub >> authorized_keys

You will now be able to SSH between compute nodes without typing a password.


Using a terminal multiplexer
============================

Using a terminal multiplexer allows you to keep your session open, even when
you disconnect from the cluster. You can even reconnect from a different
computer and get your session back.

We recommend that you use either :command:`tmux` or :command:`screen`.

* `tmux <https://github.com/tmux/tmux/wiki>`_
* `screen <https://www.gnu.org/software/screen/manual/screen.html>`_.
