.. _faq:

FAQ
===

I forgot my password
--------------------

Fill out the `request a new password`_ form.


Why are my jobs waiting for so long to start?
---------------------------------------------

* Check :command:`gnodes` and :command:`priority`.
* Check how many cores you are asking for.
* Check how much memory you are asing for.
* Check how much time you are asking for.


Why is the partition I chose being ignored?
-------------------------------------------

Unless you specify a partition other that short/normal, like *fat2* or
*express*, the partition parameter is largely ignored and your jobs are
actually submitted to both partitions. When they start, they are moved to a
single partition, in which they are started. This is done to avoid waiting in
the *short* queue if normal nodes are empty.

Long story short: don't worry, just submit the job asking for an appropriate
time limit and it will start in an appropriate place. Unless you want *fat2* or
*express*, you can forget about the partition parameter.


How do I open images/PDFs?
--------------------------

Use :command:`eog` for images and :command:`evince` for PDF. For these to work
you will need to SSH to the cluster with :ref:`X-forwarding <xforwarding>`
enabled.


How can I avoid losing my session when I close my laptop?
---------------------------------------------------------

Use a terminal multiplexer like `tmux <https://github.com/tmux/tmux/wiki>`_
or `screen <https://www.gnu.org/software/screen/manual/screen.html>`_.


How do I prevent accidental changes to my important data?
---------------------------------------------------------

Put the data in a separate folder and run:

.. code-block: console

    [fe1]$ chmod -R a-w datafolder

Now you can't change, add or remove files in that folder hierarchy.


Why can't I connect?
--------------------

We only allow incoming connections from a whitelisted set of IPs, so if you get
a `connection refused` you should try sending us an email with the IP you are
connecting from. You can see what your IP is on http://myip.dk.

Contact us if you need your IP address to be whitelisted.


I have a collaborator that would like to upload some data, how do we do that?
-----------------------------------------------------------------------------

We have a special upload user so just send us their email and we will set them
up. Once the data is uploaded we will move it to a folder you have access to.


.. _ipsych-export:

I am an iPSYCH user, how do I export files?
-------------------------------------------

If you have many files you should pack them up in a tar/zip. Use
:program:`ipsych-export` on the file to be exported and then send an email to
Anders Børglum and CC us so we can see when he approves it.

.. _ipsych-import:

I am an iPSYCH user, how do I import files?
-------------------------------------------

Importing and exporting data is done through an intermediate server for
security reasons. Transferring data into the cluster isn't restricted, but we
still have to go through the intermediate step, so the first thing you do is
upload the data to ipsych.genome.au.dk with :program:`scp`.

.. code-block:: console

    [local]$ scp my-file me@ipsych.genome.au.dk:
    me@ipsych.genome.au.dk's password:
    my-file                                   100% 4387     4.3KB/s   00:00

Now we can import it into the actual cluster, by running the
:program:`ipsych-import` command from a session on ``fe2``.

.. code-block:: console

    [fe2]$ ipsych-import my-file my-file
    my-file                                   100% 4387     4.3KB/s   00:00

Now the file is available to your user from all machines, just like any other
file in your home directory.


I am an iPSYCH user, why is NoMachine acting up?
------------------------------------------------
We have seen cases where the keyboard (or just some buttons) stop working and
some other mysterious bugs like this.

You should try closing NoMachine completely (not just the window with the
current session) and reconnecting - if that doesn't work the only thing we can
do is to kill your session so shoot us an email if you need that.

.. _request a new password: http://genome.au.dk/request-forms/request-new-password-forgot-password/
