:orphan:

.. _newsletter-2022-winter:

=======================
Newsletter, winter 2022
=======================

Hello!

First of all, happy New Year! We hope that you've enjoyed the holidays.

In 2021 you all submitted 19 mio. jobs and used 21 mio. billing hours worth of
compute. More than 200 projects were created and we welcomed 200 new users!

Anders, Rasmus, and Dan

**The GenomeDK Team**


News
====

Disk-based backup
-----------------

We have now switched completely to our own disk-based backup solution! This
means that we can now much more quickly recover files from backup. In the future
we will also provide a more flexible way of specifying which files should be
backed up.

We're on Twitter
----------------

We're now on social media as `@GenomeDK_AU <https://twitter.com/GenomeDK_AU>`_ -
on Twitter. Follow us for casual status updates and other HPC-related content.
Let us know if you have content ideas!

ISO 27001-compliance
--------------------

GenomeDK is a ISO 27001-compliant HPC facility, which means that we have a
formal information security management system (ISMS) in place to guide our
information security choices and implementation. This summer we completed our
first external audit and received an excellent report.

Unstable faststorage
--------------------

During the past six months many of you have experienced unstable access to
faststorage due to a range of (mostly) software-related issues in the filesystem
software (BeeGFS) that is responsible for faststorage. We have previously
described the actions we have taken to resolve these issues in detail. Since
then we have introduced additional automation to self-heal faststorage and are
working with the company behind BeeGFS to address any remaining issues.


Upcoming
========

New hardware
------------

Due to supply issues and significant price jumps in 2021, we did not purchase
any new hardware. In the coming year we'll be acquiring new hardware for both
compute and storage, which should result in shorter waiting times when
submitting jobs and a more stable faststorage.

Hardware retirement
-------------------

We'll retire the s04 nodes during 2022 as they reach end-of-life.


Tips and tricks
===============

When adding new R packages to Rstudio in a conda Rstudio/R environment you 
should always check if the package is available in conda before trying to 
install it via the R console.

This ensures that the package and dependencies are compatible with the R version
that comes with the conda provided Rstudio/R installation. 

An example could be the rather popular Tidyverse collection of R packages, which
by its nature has several layers of dependent packages, which usually fail
installing via the R console.

To check if the Tidyverse is available via conda first activate your R/Rstudio
environment and then run:

.. code-block:: console

   conda search r-tidyverse

(Tip: All R packages in conda are prefixed with "r-")

To install the latest compatible version of Tidyverse run:

.. code-block:: console

   conda install r-tidyverse

The Tidyverse package should now be installed and available for use with R.

---

Thank you for reading!
