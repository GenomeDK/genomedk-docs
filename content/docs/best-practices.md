---
title: Best practices
weight: 80
---

Using the same project structure for all of your projects provide a lot of
benefits. We recommend that you follow the structure shown below. It is flexible
enough to work for a wide variety of data analysis projects, but feel free to
adapt it to your needs.

```txt
myproject/
    data/
       README.txt
       ...
    steps/
       README.txt
       ...
    results/
       README.txt
       ...
    plots/
       README.txt
       ...
    scripts/
       README.txt
       ...
    docs/
       1-installing-dependencies.txt
       2-running-some-analysis.txt
       3-running-some-other-analysis.txt
       ...
    environment.yml
    NOTEBOOK.txt
    README.txt
    ...
```

Let's have a look at the goal of each folder:

**data**: This folder should contain your raw/original data files. You should consider
this directory read-only (even better: make it read-only). However, it is okay
to add new files to the folder, as long as you don't modify or delete other
files in the folder.

**steps**: This folder contains data files produced by various steps in your analysis. If
you're using a workflow tool like GWF, this directory is where you would put the
output of your targets. For large workflows it may be a good idea to make
subfolders for each step.

**results**: This folder contains the final data files (not plots) produced by your analysis.
Again, you may want to put these in subfolders for large workflows with many
result files.

**plots**: This directory contains scripts for generating plots from the result files and
the resulting plots in one or more formats. For example, you could have a script
called `plot_distribution_of_tumor_purities.py` which produces a plot called
`distribution_of_tumor_purities.pdf`.

**scripts**: This directory contains the scripts you wrote for your analysis,
e.g. those used by your workflow. Use file names that describe the purpose of
the scripts. At the top of each script, insert a comment that briefly describes
the input, output and purpose of the script. Again, a few sentences is better
than nothing and may often be enough.

**docs**: This folder is mainly for large projects where it may be nice to document each
analysis in its own file. If you use plain text files as shown above, remember
to give them numbers to make it easier for the reader to figure out where to
begin.

In addition to the folders described above, the project root should also contain
at least two files: a file documenting your project structure (this could just
contain a short introduction to the project and a link to this page) and a file
describing the software requirements for your project.

# Multi-user project

In the case of multi-user projects where many people collaborate on the same
data, the following structure may be used.

```txt
myproject/
    data/
        README.txt
        ...
    people/
        username1/
        username2/
        username3/
        ...
    results/
        README.txt
        ...
    README.txt
```

In this scenario the root folder contains a people folder which a subfolder for
each person working on the project. Each of these folders uses the same
directory structure as described for single-user projects. This means that each
user his/her own scripts, sandbox, docs, results, steps and data folders. The
user-specific data folder can contain data files that are not used by everyone
associated with the project, but it can also contain symbolic links to the root
data folder.

The root results folder is used to aggregate results from different users by
creating symbolic links to specific result files. For example, say that user A
produced a result `foo.txt` and user B wants to use this file. User B can then
create a symlink from `myproject/people/A/results/foo.txt` to
`/myproject/results/foo.txt`.

# Sanity check for repeatability

To check whether your project can easily be run by another person, package it
into a zip-file and send it to one of your colleagues. They should be able to
run your analysis with no help from you and by only reading the documentation in
your project.
