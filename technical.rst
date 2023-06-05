:orphan:

.. _technical:

=========
Technical
=========

.. table:: Overview of available compute nodes
    :align: left

    +---------------+--------+-------------------------------------------------------+
    | Nodes / cores | Prefix | Description                                           |
    +===============+========+=======================================================+
    | 52 / 3228     | s21,   | -  2x AMD/"EPYC Rome" 7452 CPUs @                     |
    |               | s22    |    2.35 GHz, 32 cores/CPU                             |
    |               |        | -  512 GB memory                                      |
    |               |        | -  Infiniband EDR                                     |
    +---------------+--------+-------------------------------------------------------+
    | 30 / 1080     | s05    | -  2x Intel/"Skylake" Gold 6140                       |
    |               |        |    CPU @ 2.30GHz, 18 cores/CPU                        |
    |               |        | -  384 GB memory                                      |
    |               |        | -  Infiniband FDR                                     |
    +---------------+--------+-------------------------------------------------------+
    | 2 / 72        | s10    | -  2x Intel/"Skylake" Gold 6140                       |
    |               |        |    CPU @ 2.30GHz, 18 cores/CPU                        |
    |               |        | -  384 GB memory                                      |
    |               |        | -  Infiniband FDR                                     |
    |               |        | -  Two Nvidia V100 16Gb GPU devices                   |
    +---------------+--------+-------------------------------------------------------+

Storage
=======

Data may be located either on our NFS servers or on fast storage, our 23 PB
BeeGFS distributed file system (fast storage).

Home folders are located on NFS. Project folders are located on fast storage.
Fast storage is reserved for large data files involved in I/O intensive
computations.

NFS can deliver read/write performance of up to 700MB/s, while fast storage
can reach an aggregated read/write performance of more than 45 GB/s.

Backup
======

Backup is made to an offsite disk based solution on a weekly basis. Read more
here: :ref:`Working with Data <working_with_data>`.

Power
=====

Storage and switches are protected by 3x40 kVA UPS.
Diesel generator provides long term power backup for storage and switches.

In case of power failure, only frontend and compute nodes will be without
power.
