.. _technical:

=========
Technical
=========

.. table:: Overview of available nodes
    :align: left

    +---------------+-------------------------------------------------------+
    | Nodes / cores | Description                                           |
    +===============+=======================================================+
    | 95 / 1520     |                                                       |
    |               |                                                       |
    |               | -  Two Intel/"Sandy Bridge"                           |
    |               |    E5-2670 CPUs @ 2.67 GHz, 8                         |
    |               |    cores/CPU                                          |
    |               | -  64 GB memory                                       |
    |               | -  10 GigE                                            |
    |               |                                                       |
    |               |                                                       |
    +---------------+-------------------------------------------------------+
    | 56 / 896      |                                                       |
    |               |                                                       |
    |               | -  Two Intel/"Sandy Bridge"                           |
    |               |    E5-2670 CPUs @ 2.67 GHz, 8                         |
    |               |    cores/CPU                                          |
    |               | -  128 GB of memory                                   |
    |               | -  Infiniband 4X QDR                                  |
    |               |                                                       |
    |               |                                                       |
    +---------------+-------------------------------------------------------+
    | 38 / 912      |                                                       |
    |               |                                                       |
    |               | -  Two Intel/"Haswell" E5-2680v3                      |
    |               |    CPUs @ 2.5 Ghz, 12 cores/CPU                       |
    |               | -  256 GB of memory                                   |
    |               | -  Infiniband FDR                                     |
    |               |                                                       |
    |               |                                                       |
    +---------------+-------------------------------------------------------+
    | 30 / 1080     | -  Two Intel/"Skylake" Gold 6140                      |
    |               |    CPU @ 2.30GHz, 18 cores/CPU                        |
    |               | -  384 GB of memory                                   |
    |               | -  Infiniband FDR                                     |
    +---------------+-------------------------------------------------------+
    | 2 / 72        | -  Two Intel/"Skylake" Gold 6140                      |
    |               |    CPU @ 2.30GHz, 18 cores/CPU                        |
    |               | -  384 GB of memory                                   |
    |               | -  Infiniband FDR                                     |
    |               | -  Two Nvidia V100 16Gb GPU devices                   |
    +---------------+-------------------------------------------------------+
    | 1 / 32        |                                                       |
    |               |                                                       |
    |               | -  Four AMD/Opteron 6212 CPUs @                       |
    |               |    2.67 GHz, 8 cores/CPU                              |
    |               | -  512 GB memory                                      |
    |               | -  10 GigE and 1 GigE NIC's.                          |
    |               |                                                       |
    |               |                                                       |
    +---------------+-------------------------------------------------------+
    | 3 / 72        |                                                       |
    |               |                                                       |
    |               | -  Four Intel/"Westmere" E7-4807                      |
    |               |    CPUs @ 1.87 Ghz, 6 cores/CPU                       |
    |               | -  1024 GB memory                                     |
    |               | -  10 GigE and 1GigE NIC's.                           |
    |               |                                                       |
    |               |                                                       |
    +---------------+-------------------------------------------------------+

Storage
=======

The total storage space available is 12 PB.

Data may be located either on our NFS servers or on fast storage, our
11.5 PB BeeGFS distributed file system (fast storage).

Home folders are located on NFS storage by default. Project folders are located
on fast storage. Fast storage is reserved for large data files involved in
I/O intensive computations.

NFS can deliver read/write performance of up to 700MB/s, while fast storage
can reach an aggregated read/write performance of more than 35GB/s.

Backup
======

Backup is made to AU ITs IBM-TSM disk and tape archive.

Power
=====

Storage and switches are protected by 3x40 kVA UPS
Diesel generator provides long term power backup for storage and switches.

In case of power failure, only frontend and compute nodes will be without
power.
