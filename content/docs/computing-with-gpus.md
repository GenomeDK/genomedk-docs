---
title: Computing with GPUs
weight: 48
extra:
  menu_category: compute
---

Graphical processing units (GPUs) are accelerators that may be used to speed up
certain operations. GPUs are especially good at linear algebra type computations
such as matrix multiplication.

Software must be written specifically to take advantage of one or more GPUs. You
should only allocate GPUs for software that you know can take advantage of the
GPU.

# Types of GPUs {#gpu_nodes}

We currently provide access to two types of GPUs:
	
|                     | Nvidia H200 SXM 141GB  | Nvidia L40S 48GB |
|---------------------|------------------------|------------------|
| Partition           | `gpu-h200`             | `gpu-l40s`       |
| Nodes/GPUs          | 2 nodes x 4 GPUs       | 2 nodes x 8 GPUs |
| Architecture        | Hopper                 | Ada Lovelace     |
| VRAM                | 141 GB                 | 48 GB            |
| Memory Bandwidth    | 4800 GB/s              | 864 GB/s         |
| TDP                 | 700 W                  | 350 W            |
| FP64 Performance    | 34.0 TFLOPS            | 1.4 TFLOPS       |
| FP32 Performance    | 67.0 TFLOPS            | 91.6 TFLOPS      |
| FP16 Performance    | 989.5 TFLOPS           | 733.0 TFLOPS     |
| BF16 Performance    | 989.5 TFLOPS           | 733.0 TFLOPS     |
| FP8 Performance     | 1979.0 TFLOPS          | 733.0 TFLOPS     |
| INT8 Performance    | 1979.0 TOPS            | 733.0 TOPS       |

You can read more about the exact machine specifications 
[here](@/docs/hardware.md) and see pricing for the different GPU types
[here](@/pricing.md). GPUs are also 
[subject to resource limits](@/docs/partitions-and-resource-limits.md).

Which one to use very much depends on the software you're using and the 
computation you are running. In general, the L40S is good for inference and 
small simulations, while the H200 is good for model training and large 
simulations due to the larger amount of memory, but you should always benchmark 
your specific application to find the most appropriate fit.

{% warning() %}
Be aware that GPUs are much, much more expensive than CPUs! For example, one 
hour on an Nvidia L40S is 50x the cost of one hour on a CPU-core. You should
always consider whether the speed-up gained from the GPU is worth the cost.
{% end %}

# Requesting GPUs

To to run a job on a node with a GPU device you need to submit it to the right
partition *and* specify how many GPU devices you are going to use.

For example, to submit an interactive job with one Nvidia L40S GPU allocated:

```bash
[fe-open-01]$ srun --gpus 1 -p gpu-l40s --pty bash
```

Or to submit an interactive job with two Nvidia H200 GPUs allocated:

```bash
[fe-open-01]$ srun --gpus 2 -p gpu-h200 --pty bash
```

{% note() %}
Note that the software you're using must support using multiple GPUs,
otherwise allocating more GPUs will not make a difference.
{% end %}

If you really don't care which type of GPU you get, you can specify both
partitions:

```bash
[fe-open-01]$ srun --gpus 2 -p gpu,gpu-h200 --pty bash
```

In a batch script it looks like this. Here we ask for four Nvidia L40S GPUs:

```bash
#!/bin/bash
#SBATCH --account my_project
#SBATCH -c 8
#SBATCH --mem 16g
#SBATCH --partition gpu
#SBATCH --gpus 4
#SBATCH --time 04:00:00

echo hello world
```

# Monitoring GPU utilization

{% warning() %}
GPU jobs that, after running for two hours, have an average GPU utilization of
less than 75% are automatically cancelled!
{% end %}

GPU-time is exceedingly expensive, so you should make sure that you are 
utilizing the GPU well. You can see the average GPU utilization for your job 
using `jobinfo`:

```bash
[fe-open-01]$ jobinfo <job id>
...
GPUs                : 4
...
GPU utilization     : 3.68 GPUs (92%)
```

In this, four GPUs were requested for the job and it used on average 3.68 GPUs,
which becomes a utilization of 92%. You may use `jobinfo` to check the
utilization *as the job runs*.

Alternatively, you can connect to the running job and use the `nvidia-smi` 
command to get GPU and memory utilization:

```bash
[fe-open-01]$ srun --jobid <job id> --overlap --pty bash
[gn-1001]$ nvidia-smi
```
