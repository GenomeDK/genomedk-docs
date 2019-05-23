
.. _how_does_the_cluster_work:

==================
What is a cluster?
==================

A cluster consists of a large number of interconnected machines.

Each machine is very much like your own desktop computer, except it’s much more
powerful. Like your desktop computer, each machine (often referred to as
*node*) has a CPU, some memory, and a hard disk. The nodes running your
programs are usually called *compute nodes*.

To turn the nodes in to a cluster we need three more ingredients: a network,
data storage, and a queue manager. In section we’ll discuss these components in
a bit more detail to give you an understanding of how a cluster works.

Network
=======

Nodes in the cluster connect to a high-performance network. The network allows
programs running on different nodes to "talk" to each other. It also lets you
log in to a node from any other node (with some restrictions).

Storage
=======

Bioinformatics is data intensive so we can’t make do with a single hard disk as
you would in your own computer. Instead we buy hundreds of hard disks and use a
file system that can manage files across these disks. The file system presents
the user with a unified file system.

We call our distributed file system *fast storage* because it's blazingly fast.
It's up to you to your files on fast storage or on the slower shared file
system.

With storage the cluster is now functional. But, any user would be able to log
in to any node and run a program, which may consume the resources of the entire
node. This could cause other users' programs on the same node to crash.
Likewise, one user can start thousands of runs of a program on different nodes,
consuming the resources of the entire cluster for an unknown duration of time.
In short, it would be complete anarchy!

To solve this problem we need a *queue manager*.

Queue manager
=============

The queue manager is much like the queues in the supermarket. You stand in the
queue and wait until it’s your turn to pay. On the cluster, you submit *jobs*
to the queue and your jobs will run on some node chosen by the queue manager,
once resources are available.

The queue manager also allows you to specify certain requirements for your
program to run. For example, your program may need to run on a node with *a
lot* of memory. If you specify this when submitting your job, the queue manager
will make sure to run the job on a node with at least that amount of memory
available.

At GenomeDK we use a queue manager called Slurm, so to run your programs on the
cluster, you’ll be interacting a lot with Slurm.

Things to remember...
=====================

This ends our tour of the cluster setup. Now, here's a few things that you
should keep in mind when using the cluster...

* The nodes in a cluster are set up so that they’re all (more or less)
  identical. Software that is available on one node will also be available on
  all other nodes and you can access your files in the same way on all nodes.
  When the queue manager runs your job on a node, it more or less corresponds
  to you logging in to the node and running the program yourself.

* You access the cluster through a single node, often denoted the *frontend*.
  The frontend node is identical to the other nodes, but it is set up to allow
  access from the Internet. Your day-to-day interaction with the cluster goes
  through the frontend. But, you should not run any computation or memory
  intensive programs on the frontend. All users share the frontend's resources
  and you should only use it for basics things like looking around the file
  system, writing scripts, and submitting jobs.

In the next section you will learn how to connect to the cluster so that you
can start submitting jobs.
