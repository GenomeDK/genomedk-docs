---
title: Hardware and infrastructure
weight: 100
---

This page contains details about the hardware and infrastructure that is available on GenomeDK.

# Compute

* cn-\[1001-1060\] (60 nodes, 11520 cores)
    * 2x AMD/"EPYC Genoa" 9654 CPUs @ 3.7 GHz, 96 cores/CPU
    * 1.5 TB memory
    * Infiniband HDR
* gn-\[1001-1002] (2 nodes, 128 cores, 16 GPUs)
    * 2x AMD EPYC 9354 CPU @ 3.40GHz, 32 cores/CPU
    * 768 GB memory
    * Infiniband EDR
    * 8x Nvidia L40S 48GB GPU

# Storage

Home folders are located on NFS. 

Project folders are located on our BeeGFS-based storage system which can reach an aggregated read/write performance of more than 100 GB/s.

# Backup

Backup is made to an off-site disk based solution on a weekly basis.

# Power

Storage and switches are protected by 2x100 kVA UPS. Diesel generator
provides long-term power backup for storage and switches.

In case of power failure, only frontends and compute nodes will be
without power.
