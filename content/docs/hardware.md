---
title: Hardware
weight: 100
---

This page contains details about the hardware and infrastructure that is available on GenomeDK.

# Inventory

* s21, s22 (52 nodes, 3228 cores)
    * 2x AMD/"EPYC Rome" 7452 CPUs @ 2.35 GHz, 32 cores/CPU
    * 512 GB memory
    * Infiniband EDR
* s05 (30 nodes, 1080 cores)
    * 2x Intel/"Skylake" Gold 6140 CPU @ 2.30GHz, 18 cores/CPU
    * 384 GB memory
    * Infiniband FDR
* s10 (2 nodes, 72 cores)
    * 2x Intel/"Skylake" Gold 6140 CPU @ 2.30GHz, 18 cores/CPU
    * 384 GB memory
    * Infiniband FDR
    * 2x Nvidia V100 16Gb GPU

# Storage

Data may be located either on our NFS servers or on fast storage, our 23
PB BeeGFS distributed file system (fast storage).

Home folders are located on NFS. Project folders are located on fast
storage. Fast storage is reserved for large data files involved in I/O
intensive computations.

NFS can deliver read/write performance of up to 700MB/s, while fast
storage can reach an aggregated read/write performance of more than 45
GB/s.

# Backup

Backup is made to an off-site disk based solution on a weekly basis.

# Power

Storage and switches are protected by 2x100 kVA UPS. Diesel generator
provides long term power backup for storage and switches.

In case of power failure, only frontend and compute nodes will be
without power.
