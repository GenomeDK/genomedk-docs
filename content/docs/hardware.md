---
title: Hardware and infrastructure
weight: 32
extra:
  menu_category: basics
---

This page contains details about the hardware and infrastructure that is 
available on GenomeDK.

# Compute (CPU)

* cn-\[1001-1060\] (60 nodes, 11520 cores)
  * 2x AMD/"EPYC Genoa" 9654 CPUs @ 3.7 GHz, 96 cores/CPU
  * 1.5 TB memory
  * Infiniband HDR (200G)
  * 6.4 TB NVME scratch
* cn-\[1060-1110\] (50 nodes, 9600 cores)
  * 2x AMD/"EPYC Genoa" 9655 CPUs @ 3.7 GHz, 96 cores/CPU
  * 768 GB memory
  * Infiniband NDR (400G)
  * 6.4 TB NVME scratch

# Compute (GPU)

* gn-\[1001-1002\] (2 nodes, 128 cores, 16 GPUs)
  * 2x AMD EPYC 9354 CPU @ 3.40GHz, 32 cores/CPU
  * 768 GB memory
  * Infiniband EDR (100G)
  * 8x Nvidia L40S 48GB GPU
  * 7.7 TB NVME scratch
* gn-\[1003-1004\] (2 nodes, 256 cores, 8 GPUs)
  * 2x AMD EPYC 9575F CPU @ 3.30 GHz, 64 cores/CPU
  * 768 GB memory
  * 4x Nvidia H200 141GB GPU
  * Infiniband NDR (400G)
  * 6.4 TB NVME scratch

# Storage

Home folders are located on NFS. 

Project folders are located on our BeeGFS-based storage system which can reach 
an aggregated read/write performance of more than 150 GB/s.

# Backup

Backup is made to an off-site disk based solution on a weekly basis.

# Power

Storage and switches are protected by 2x100 kVA UPS. Diesel generator
provides long-term power backup for storage and switches.

In case of power failure, only frontends and compute nodes will be
without power.
