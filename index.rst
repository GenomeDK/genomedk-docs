====================
Welcome to GenomeDK!
====================

.. eventlist::
    :status: ongoing
    :quiet:

.. container:: lead

  GenomeDK is a national high-performance computing facility for bioinformatics
  and life sciences managed by the Joint AU/RM Genome Data Center, located at
  Aarhus University, Denmark.

---

We know that you're busy so here are some shortcuts:

* :ref:`Request an account <request_access>`
* :ref:`Get started <connecting_to_the_cluster>` using the cluster
* :ref:`Contact us <contact>` if you need help

Give me the numbers
===================

GenomeDK comprises 185 nodes (6568 cores) connected with Infiniband. Each
node has from 16 to 64 cores and either 128 GB, 256 GB, 384 GB or 512 GB
of RAM for a total of 56 TB of memory.

The cluster has been designed specifically for bioinformatic workloads and has
a storage capacity of 12 PB. Do you want to know :ref:`more <technical>`?

Where do I start?
=================

If you're new to GenomeDK, please read through the :ref:`documentation <docs>`.
This will help do common things like handling data, submitting jobs and
installing software, as well as how to request an account.

Once you're comfortable with performing routine tasks on the cluster, read
the :ref:`Best practices <best_practices>`, which contains suggestions and
patterns for organizing your projects and keeping your research reproducible.

Who can get an account?
=======================

We are open to account requests from people associated with a university
or small and medium-sized enterprises (SMEs).

What does it cost?
==================

In 2020, the prices are:

* 0.12 DKK/billing hour
* 250 DKK/TB/year
* 700 DKK/TB/year in backup*

One billing hour corresponds to one CPU core for one hour or 8 GB memory for
one hour, whichever is highest.

Prices are updated yearly and are subject to change. Do not hesitate to contact
us if you have any questions.

\* For example, if you store 1 TB of data in backup for a year you will be
billed 250 + 700 DKK. 250 DKK for the on-disk copy and 700 DKK for the two
off-site backup copies.

How do I pay?
=============

Costs are associated with *project folders*. The owner of a project folder is
responsible for the costs associated with the project. The project owner will
be charged yearly based on actual usage.

If the project owner is associated with either:

* Faculty of Health, Aarhus University,
* Faculty of Natural Sciences, Aarhus University,
* Central Region Denmark (Region Midt),

then the usage is paid internally and the project owner will not receive a bill
directly from GenomeDK.


.. toctree::
  :maxdepth: 1
  :hidden:
  :caption: Main

  governance
  publications
  technical
  system-status

.. toctree::
  :maxdepth: 3
  :hidden:
  :caption: Help

  support
  training
  docs/index
