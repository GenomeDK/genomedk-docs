Get ready
=========

The first thing we will do is to make sure that we can connect to the cluster.

* jail users must follow the instructions at http://ipsych.genome.au.dk
* Windows users will want to get Putty (and WinSCP for transferring files)
* Linux and macOS users need no additional software

To connect you run the following command from a terminal or by putting the same
address in to Putty.

.. code-block:: console

    [me@local ~]$ ssh me@login.genome.au.dk
    [me@genomedk ~]$

Creating a script
=================

Now we will create a simple text file on our local machine, with the following
content:

.. code-block:: sh

    #!/bin/bash
    source /com/extra/bwa/0.7.5a/load.sh
    reference_prefix="/data/refseq/iGenome/Homo_sapiens/UCSC/hg19/Sequence/BWAIndex/genome.fa"
    bwa mem $reference_prefix test-reads.fq > test-reads.sam

The script loads a pre-installed piece of software - in this case bwa - from a
local software repository. It is important that you load the software in your
script -- loading it in your session and starting a script will only work if
you remember to load the software every time you submit the job.

Too see what else is available you can use the command ``sw-list``.

Copying a file to the cluster
=============================

.. note:: ipsych.genome.au.dk users must follow the guide in Ipsych Usage.

To get this script from your local machine to the cluster you can use the scp
command on linux/mac and the WinSCP program on windows. This uses the same
protocol as ssh so you connect to the same address with the same credentials.

.. code-block:: console

    [me@local ~]$ scp scriptfile me@login.genome.au.dk:faststorage/scriptfile
    me@login.genome.au.dks password:
    scriptfile                                     100%  242     0.2KB/s   00:00
    [me@local ~]$

Downloading data from the internet
==================================

Now you might have noticed that the script mentions a test-reads.fq which we
haven't made. This is a file that is publicly available via http. You can use
the wget or curl commands to download it.

The cluster is behind a firewall. To download through the firewall you have to
configure a proxy, by setting the environment variables ``http_proxy`` and
``ftp_proxy``.

This will enable the proxy for this session, if you want it to be enabled every
session you can add the same export commands to the ``.bash_profile`` file in
your home folder.

.. code-block:: console

    [me@genomedk ~]$ wget http://cs.au.dk/~aeh/genomedk_tut/test-reads.fq
    --2015-01-14 10:37:14--  http://cs.au.dk/~aeh/genomedk_tut/test-reads.fq
    Resolving in... 10.20.0.50
    Connecting to in|10.20.0.50|:3128... connected.
    Proxy request sent, awaiting response... 200 OK
    Length: 380 [text/plain]
    Saving to: “test-reads.fq”
    100%[==============================================>] 380         --.-K/s   in 0s

    2015-01-14 10:37:14 (44.4 MB/s) - “test-reads.fq” saved [380/380]
    [me@genomedk ~]$ mv test-reads.fq faststorage/
    [me@genomedk ~]$ cd faststorage/
    [me@genomedk faststorage]$

.. note::

    If the first command does not work for you, it may be because your user
    was created a long time ago

We move the script and the datafile into the faststorage folder, as this
storage is more suited for datafiles.

The cluster has two storage systems. One is a standard shared NFS system, where
your homedir is located. This is good for smaller files and less often used
files. The other storage, is a much faster system, with much more available
space. The disadvantage is that the performance of small files is not as good
as on NFS and there is no client side caching so certain usage patterns are not
very fast. To access the faster storage you use the faststorage folders. You
have a personal one in your homedir and every project dir also has one.

As a rule of thumb all non-tiny data files should be on faststorage.

If you need backups you can create a folder called BACKUP and everything under
that folder will have backups. Try to avoid putting larger derived files under
backup - you can always derive them again, if you make sure to backup your
pipeline, which was used to generate the files.

Submitting a job
================

Now to actually run our script we need to submit it to the queue of jobs. This
is done by executing srun scriptfile which will wait until the job is done,
showing you the output from the job as it executes.

.. code-block:: console

    [me@genomedk faststorage]$ srun --mem-per-cpu=4G --partition=express scriptfile
    srun: job 2396710 queued and waiting for resources
    srun: job 2396710 has been allocated resources
    [M::main_mem] read 2 sequences (102 bp)...
    [main] Version: 0.7.5a-r405
    [main] CMD: bwa mem /data/refseq/iGenome/Homo_sapiens/UCSC/hg19/Sequence/BWAIndex/genome.fa test-reads.fq
    [main] Real time: 6.297 sec; CPU: 2.907 sec
    [me@genomedk faststorage]$

The script should finish quickly with no errors. If you look at the srun
command you can see that we asked for the express partition. This is a couple
of machines used for test jobs that will always have a time limit of at most 1
hour. That also means there should rarely, if ever, be any wait time. We also
ask for 4GB of memory to work with.

Let's try with a slightly larger input file. Modify the script to look like
this:

.. code-block:: sh

    #!/bin/bash
    #SBATCH --partition normal
    #SBATCH --mem-per-cpu 8G
    #SBATCH -c 4
    source /com/extra/bwa/0.7.5a/load.sh
    reference_prefix="/data/refseq/iGenome/Homo_sapiens/UCSC/hg19/Sequence/BWAIndex/genome.fa"
    input_file="/faststorage/data/genomedk-tutorial/testfile-105M.fq"
    bwa mem $reference_prefix $input_file > test-reads-105M-A.sam &
    bwa mem $reference_prefix $input_file > test-reads-105M-B.sam &
    bwa mem $reference_prefix $input_file > test-reads-105M-C.sam &
    bwa mem $reference_prefix $input_file > test-reads-105M-D.sam &
    wait

Now we specify the extra parameters in the file itself, which will only work
with the sbatch command that we will see in a minute. Instead of the express
partition we now ask for the normal partition where the main bulk of the jobs
are run and the default time limit is 48 hours. We also ask for more memory and
4 cores.

As an example, we simply run the same bwa command four times in parallel
(indicated by the ``&`` and ``wait``). If we ran multiple commands without
asking for extra cores they would share a single cpu, getting only 25% of the
time each.

If there are a lot of jobs in the queue already or if the job takes longer than
a few minutes to run you probably don't want to block your terminal while you
wait. Instead you can submit it with sbatch scriptfile which will return
immediately and give you a job number that can be used to check on the  job
later.

.. code-block:: console

    [me@genomedk faststorage]$ sbatch scriptfile
    Submitted batch job 2396712
    [me@genomedk faststorage]$ squeue -j 2396712
	     JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
	   2396712    normal scriptfi       me PD       0:00      1 (None)
    [me@genomedk faststorage]$ squeue -u me
	     JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
	   2396712    normal scriptfi       me PD       0:00      1 (None)

An alternative approach (and often preferred method), would have been to create
four different scripts, each using just one core, and submitted them all at the
same time with sbatch.

The larger test files are still pretty small so it doesn't take more than a few
minutes to finish once the job gets through the queue. Once the job is finished
we can get some information about it with the jobinfo command. It will look
something like this:

.. code-block:: console

    [me@genomedk faststorage]$ jobinfo 2396712
    Name                : scriptfile
    User                : me
    Partition           : normal
    Nodes               : s01n23
    Cores               : 4
    State               : COMPLETED
    Submit              : 2015-01-14T11:23:53
    Start               : 2015-01-14T11:23:53
    End                 : 2015-01-14T11:33:42
    Reserved walltime   : 2-00:00:00
    Used walltime       :   00:09:49
    Used CPU time       :   00:35:33
    % User (Computation): 36.74%
    % System (I/O)      : 63.26%
    Mem reserved        : 8G/core
    Max Mem used        : 20.71G (s01n23)
    Max Disk Write      : 1.12G (s01n23)
    Max Disk Read       : 21.75G (s01n23)

This shows when the job was started/finished, what was requested and so on.

The most important information is the maximum memory usage and used walltime.
In this case we can see that we actually used 5.2GB per core (20.71GB for four
cores), and not the 8GB that we asked for. If we were running a similar script
on many different input files asking for 8GB would be an okay safety margin,
while asking for 32GB is a waste of resources. The default 48 hour time limit
is too large, as our jobs only take a few minutes to run. The more accurately
everyone specifies their jobs the smoother the whole queue system is going to
run.
