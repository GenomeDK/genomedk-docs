:orphan:

========================
Working in a closed zone
========================

.. _zone_connect:

Connecting to a zone
====================

Step 1
------

Download and install the remote desktop client for your operating system on
your local machine.

* `Download client for Windows <https://www.nomachine.com/download/download&id=8>`_
* `Download client for macOS <https://www.nomachine.com/download/download&id=7>`_
* `Download client for Linux <https://www.nomachine.com/download/linux&id=1>`_

Step 2
------

Download and install FreeOTP, Google Authenticator or any similar app on your
phone. If you are at AU you probably already have Microsoft Authenticator
installed.

Step 3
------

Download the connection file for the zone you wish to connect to:

.. toctree::
    :maxdepth: 1

    ipsych
    brain

Step 4
------

Using the login information received in your mailbox. Login by entering your
username and password.

Assuming you entered correctly you will get access to the virtual desktop.

Open the the authenticator app on your phone and scan the :file:`QRCode.png`
located on your NoMachine desktop. From now on you will need to generate a
one-time password with the authenticator app every time you log in.

Step 5
------

Finally, read the documentation at http://genome.au.dk.


Using the data lock
===================

.. _gdk-export:

Exporting files
---------------

If you have many files you should pack them up in a tar/zip. Use
:program:`gdk-export` on the file to be exported and then send an email to
the zone owner and CC us so we can see when it is approved.

When the export has been approved you can download the file with:

.. code-block:: console

    [local]$ sftp -P 2022 <username>@185.45.23.195:test.fa .

Alternatively, use a graphical SFTP client such as WinSCP, FileZilla or
Cyberduck with host 185.45.23.195 and port 2022.


.. _gdk-import:

Importing files
---------------

Transferring data into a closed zone isn't restricted, but we still have to go
through an intermediate step for security reasons.

First, upload the file to the data lock:

.. code-block:: console

    [local]$ echo put test.fa . | sftp -b <username>@185.45.23.195

Alternatively, use a graphical SFTP client such as WinSCP, FileZilla or
Cyberduck with host 185.45.23.195 and port 2022.

You can now access the file from the inside at
:file:`/data-lock/public/<username>`. However, the file will be read-only. To
use the file, copy it to some other location, for example a relevant project
folder.

Cleanup
-------

Files in the public part of the data lock are automatically deleted after 60
days.
