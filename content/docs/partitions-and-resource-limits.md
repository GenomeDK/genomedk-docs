---
title: Partitions and resource limits
weight: 43
extra:
  menu_category: compute
---

Since GenomeDK is a shared system, all computations must be carried out
through a queue. Users submit jobs to the queue and the jobs then run
when it's their turn.

The queuing system is configured into partitions with different characteristics
and there are limits on resource usage to ensure fair access to the resources.

# Partitions and nodes

To get an overview of the available nodes:

```bash
[fe-open-01]$ gnodes
```

This will list each partition and all of the compute nodes assigned to
each partition. The header of each partitions lists the available
resources such as the number of cores per node, available memory per
node, and the maximum walltime (running time) a job in the partition can
have.

# Resource limits {#resource_limits}

All users/jobs are subject to the following limits:

* A user can at most use 3600 cores at once.
* A user can at most use 12 GPUs at once.
* GPU jobs that, after running for two hours, have an average GPU utilization of
  less than 75% are automatically cancelled!
* A job can at most declare 1000 dependencies. Exceeding the limit results in 
  an error when the job is submitted.
* A job can at most request a time limit of 7 days. Exceeding the limit results 
  in an error when the job is submitted.
* A job array can at most have a length of 150000. Exceeding the limit results 
  in an error when the job is submitted.

The limits are subject to change at any time.
