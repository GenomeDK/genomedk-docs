---
title: Documentation
sort_by: weight
insert_anchor_links: right
template: doc.html
page_template: doc.html
---

It's time to get your feet wet and learn how to use GenomeDK! The
documentation is organized such that it can be used in two ways:

-   You can read it from beginning to end like a *book* to familiarize
    yourself with GenomeDK and learn how to do basic things like
    submitting a job and working with projects.
-   You can use it as a *reference* to look up the solution for specific
    questions you may have, such as what is the command for requesting a
    new project folder? Or, how do I get passwordless authentication
    working?

If you're new to GenomeDK you will most likely want to read the
documentation *as a book*. As you become more experienced you will more
often use it as a *reference*.

Before you start reading the documentation and using GenomeDK, there's
a few things that you should know.

# Conventions

You will be jumping a lot between different computers. This includes
your own computer, the frontend node, and various compute nodes.

Commands that need to be run on your own computer will look like this:

```bash
[local]$ echo hello
```

Note that the prompt says **local** in square brackets. When you need to
run a command on the frontend node, the prompt will instead say:

```bash
[fe-open-01]$ echo hello
```

Here, **fe-open-01** is the name of the frontend node. If you need to
run a command on a compute node that you started an interactive job on
(more about this later), it will be shown like this:

```bash
[cn-1004]$ echo hello
```

In this case the compute node is **cn-1004**.

# Learning to use the shell

When interacting with GenomeDK you will be using a *shell* on a
Linux/UNIX system. If you are not familiar with these concepts we
recommend the [Shell
novice](https://swcarpentry.github.io/shell-novice/) tutorial from
Software Carpentry.

If you are affiliated with Aarhus University or the Central Denmark
Region (RM), there's also excellent local training and consultancy
initiatives available at:

* [Bioinformatics Core Facility](https://biomed.au.dk/bioinformatics-core-facility) - provides basic (bioinformatics) data analysis training and consultancy services.
* [Accessible Bioinformatics Café](https://abc.au.dk/) - regular, informal cafés covering basic Linux, programming, and data analysis.

If your research group, company or department needs training for
GenomeDK specifically, we also [offer workshops based on your needs](@/help.md).
