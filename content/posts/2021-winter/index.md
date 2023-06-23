---
title: Newsletter, winter 2020
date: 2021-01-05
---

Hello!

Welcome back from a well-deserved Christmas vacation.

This time we will cover a few important changes to the queueing system
that will be introduced over the coming months. We also look back at
some of the work that has been done to reorganize our storage. And then
we are now a DeiC national HPC facility! Read more below.

Enjoy!

*The GenomeDK Team*

# Upcoming changes

In the coming weeks we will introduce a few changes to the queueing
system (Slurm):

## Time limit of 7 days for all jobs

In the future we will not allow jobs with a walltime (time limit) of
more than 7 days. Jobs longer than this are bad for several reasons:

1.  Long-running will most likely overlap with a planned downtime, which
    makes proper maintenace of GenomeDK harder.
2.  A job running for a month is likely to fail, either because the
    compute node fails or becomes another job running on the same node
    interferes in a bad way.
3.  When we see long running jobs they are usually inefficient, with bad
    I/O patterns causing excessive running time.
4.  The job could easily have been split into several jobs which
    increases resilience to failures and minimizes total running time of
    the computation.

If you are sure that your job requires more than 7 days of running time,
you can request an increase by writing to our support mail.

## All usage must be associated with a project

As GenomeDK has grown it has become harder to assign resource usage to
its rightful owner(s), which causes difficulties when reporting and
billing resource usage. For projects, the project owner is responsible
for the resources used by all members of the project. However, the
accounting only works if users remember to specify that account when
submitting jobs:

```bash
$ sbatch --account <project name> test.sh
```

Or in a *gwf* workflow:

```python
gwf = Workflow(defaults={"account": "<project name>"})
```

If users omit this, the usage will be assigned directly to their
account.

To avoid this problem, we will only allow a very small amount of
resources to be used *without specifying an account* when submitting
jobs. When these resources are used, jobs won't run and `jobinfo` will
show something like this (note the highlighted lines):

```
Name                : bash
User                : das
Account             : --
  Note: You haven't specified a project. You have a limited number of billing hours!
Partition           : short,normal
Nodes               : None assigned
Cores               : 1
GPUs                : 0
State               : PENDING (AssocMaxWallDurationPerJobLimit)
...
```

To be able to submit jobs again, supply the proper project/account as
shown above.

## A few updates

-   **We're a DeiC national HPC facility!**

    GenomeDK has become part of the DeiC national HPC initiative. We
    have already welcomed the first users that got access to GenomeDK
    through the program. For our existing users, our new title means
    that we will receive extra funding which allows us to expand and
    renew GenomeDK at a faster rate over the coming years.

-   **Storage changes**

    In the last newsletter we mentioned that home folders would move to
    newer file servers and that all projects would be moved to
    `/faststorage/project`.

    The move has now been finalized. The result should be more reliable
    and (in some cases) speedy interactions with the filesystem,
    especially when navigating and traversing home folders.

    In total, we moved hundreds of terabytes of data with a single
    downtime.

-   **Home folder quotas**

    Since 2019, new users have been assigned a 100 GB quota on their
    home folders. All home folders now have quotas.

    Old users (pre-2019), that have more than 100 GB used in their home
    folder, have been assigned a quota equal to their current usage (at
    the time of the move) plus 25 GB.

-   **Backup and snapshots**

    As part of the restructuring of our storage systems, home folders
    are **no longer** backed up. Instead, we take snapshots of them so
    that we, for example, can restore files that were accidentially
    deleted.

    The documentation has been updated with details on backup and
    snapshots. Read more in [Working with data](@/docs/working-with-data.md).

-   **Workshops**

    Due to COVID-19 there will be no workshops before restrictions have
    been lifted.

Thank you for reading!
