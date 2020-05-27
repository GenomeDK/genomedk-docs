.. _technical:

=========
Technical
=========

.. table:: Overview of available compute nodes
    :align: left

    +---------------+-------------------------------------------------------+
    | Nodes / cores | Description                                           |
    +===============+=======================================================+
    | 50 / 3200     | -  2x AMD/"EPYC Rome" 7452 CPUs @                     |
    |               |    2.35 GHz, 32 cores/CPU                             |
    |               | -  512 GB memory                                      |
    |               | -  Infiniband EDR                                     |
    +---------------+-------------------------------------------------------+
    | 40 / 640      | -  2x Intel/"Sandy Bridge"                            |
    |               |    E5-2670 CPUs @ 2.67 GHz, 8 cores/CPU               |
    |               | -  128 GB memory                                      |
    |               | -  10 GigE                                            |
    +---------------+-------------------------------------------------------+
    | 56 / 896      | -  2x Intel/"Sandy Bridge"                            |
    |               |    E5-2670 CPUs @ 2.67 GHz, 8                         |
    |               |    cores/CPU                                          |
    |               | -  128 GB memory                                      |
    |               | -  Infiniband 4X QDR                                  |
    +---------------+-------------------------------------------------------+
    | 32 / 816      | -  2x Intel/"Haswell" E5-2680v3                       |
    |               |    CPUs @ 2.5 Ghz, 12 cores/CPU                       |
    |               | -  256 GB memory                                      |
    |               | -  Infiniband FDR                                     |
    +---------------+-------------------------------------------------------+
    | 30 / 1080     | -  2x Intel/"Skylake" Gold 6140                       |
    |               |    CPU @ 2.30GHz, 18 cores/CPU                        |
    |               | -  384 GB memory                                      |
    |               | -  Infiniband FDR                                     |
    +---------------+-------------------------------------------------------+
    | 2 / 72        | -  2x Intel/"Skylake" Gold 6140                       |
    |               |    CPU @ 2.30GHz, 18 cores/CPU                        |
    |               | -  384 GB memory                                      |
    |               | -  Infiniband FDR                                     |
    |               | -  Two Nvidia V100 16Gb GPU devices                   |
    +---------------+-------------------------------------------------------+
    | 3 / 72        | -  4x Intel/"Westmere" E7-4807                        |
    |               |    CPUs @ 1.87 Ghz, 6 cores/CPU                       |
    |               | -  1024 GB memory                                     |
    |               | -  Infiniband 4X QDR                                  |
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

Storage and switches are protected by 3x40 kVA UPS.
Diesel generator provides long term power backup for storage and switches.

In case of power failure, only frontend and compute nodes will be without
power.
