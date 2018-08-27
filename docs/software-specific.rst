Python
======

Jupyter Notebook/Lab
====================

Install the ``jupyter`` package in your environment.

One way to run a jupyter notebook on the cluster is to setup an SSH tunnel to
the Jupyter instance.

1. *Start an interactive job*. Login to the cluster and start an 
   interactive job where the notebook will run. You will below need the 
   computing node name and your user id (UID) at the cluster.

    .. code-block:: console

        [local ~]$ ssh <user>@login.genome.au.dk
        [me@genomedk ~]$ srun --pty bash
        [me@node ~]$ echo $UID

2. *Setup SSH tunnel.* Back on your local computer open a second terminal to 
   setup the port-forwarding from the computing node to your computer.

    .. code-block:: console

        [local ~]$ ssh -L<UID>:<node>:<UID> <user>@login.genome.au.dk

3. *Start the notebook*. Back on the computing node start a Jupyter notebook.
   For this you may have to first unset the environmental variable 
   XDG_RUNTIME_DIR (this could also be included in ~/.bashrc ).

    .. code-block:: console

        [me@node ~]$ unset XDG_RUNTIME_DIR
        [me@node ~]$ conda activate <jupyter-env>
        [me@node ~]$ jupyter-notebook --no-browser --port=$UID --ip=0.0.0.0
        ...

4. *Run the notebook*. Back on your local computer start a web browser and 
   paste the URL from above. But replace the part in parenthesis with 
   `localhost` to get: 
   
    .. code-block:: plain

        http://localhost:<UID>/?token=....

5. *Cleanup*. When finished, remember to log out from both sessions.



RStudio
=======


Perl
====


C/C++
=====

