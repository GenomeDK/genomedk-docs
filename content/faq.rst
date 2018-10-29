FAQ
===

How do I change my password?
----------------------------

Run the :command:`change-password` command and follow the instructions. You
will need to enter your old password.

.. code-block:: shell

    $ change-password


I forgot my password
--------------------

Fill out the `request a new password`_ form.


How do I make the shell remember more commands?
-----------------------------------------------

Add ``export HISTSIZE=100000`` to your ``.bash_profile``.


Why are my jobs waiting for so long to start?
---------------------------------------------

* Check :command:`gnodes` and :command:`priority`.
* Check how many cores you are asking for.
* Check how much memory you are asing for.
* Check how much time you are asking for.


How do I open images/PDFs?
--------------------------

Use :command:`eog` for images and :command:`evince` for PDF.

For these to work you will need to SSH to the cluster with X forwarding
enabled.

.. todo:
    example + x forwarding


How can I avoid losing my session when I close my laptop?
---------------------------------------------------------

Use tmux/screen


I'm downloading a large file, but it keeps failing, what can I do?
------------------------------------------------------------------
Run in screen/tmux so you don't have to stay logged-in
Make wget auto-retry and continue from where it failed:

.. code-block:: console

    $ wget -c --timeout-120 --waitretry-60 --tries-10000 \
          --retry-connrefused https://someurl.com/data.tar.gz

When downloading large files you are encouraged to limit the progress output to
avoid stressing the system, *especially* when you're sending the progress
output to a file:

.. code-block:: console

    $ wget -c --timeout-120 --waitretry-60 --tries-10000 \
          --retry-connrefused --progress=mega:force \
          https://someurl.com/data.tar.gz


How do I prevent accidental changes to my important data?
---------------------------------------------------------

Put the data in a separate folder and do ``chmod -R a-w datafolder``.
Now you can't change, add or remove files in that folder hierarchy.


Why can't I connect?
--------------------

We only allow incoming connections from a whitelisted set of IPs, so if you get
a `connection refused` you should try sending us an email with the IP you are
connecting from. You can see what your IP is on http://myip.dk

We don't mind adding your home IP address, but beware that it might change
frequently.  If you have a university VPN that might be more stable.


I have a collaborator that would like to upload some data, how do we do that?
-----------------------------------------------------------------------------

We have a special upload user so just send us their email and we will set them
up. Once the data is uploaded we will move it to a folder you have access to.


I am an iPSYCH user, how do I export files?
-------------------------------------------

If you have many files you should pack them up in a tar/zip.
Use ``ipsych-export`` on the file to be exported and then send an email to
Anders Børglum and CC us so we can see when he approves it.


I am an iPSYCH user, why is NoMachine acting up?
------------------------------------------------
We have seen cases where the keyboard (or just some buttons) stop working and
some other mysterious bugs like this.

You should try closing NoMachine completely (not just the window with the
current session) and reconnecting - if that doesn't work the only thing we can
do is to kill your session so shoot us an email if you need that.

.. _request a new password: http://genome.au.dk/request-forms/request-new-password-forgot-password/
