---
title: Newsletter, winter 2022
date: 2022-01-18
---

Hello!

First of all, happy New Year! We hope that you've enjoyed the holidays.

In 2021 you all submitted 19 mio. jobs and used 21 mio. billing hours
worth of compute. During the year, storage usage grew from 7.5 PB to 9.6
PB, and peaked at 10 PB.

Last, but not least, welcome to the 200 users that joined us during
2021!

Anders, Rasmus, and Dan

**The GenomeDK Team**

# Updates

## New office location

Our office has moved to the newly renovated buildings in the University
City. You can now find us in building 1872, room 359.

## Disk-based backup

We have now switched completely to our own disk-based backup solution!
This means that we can now much more quickly recover files from backup.
In the future we will also provide a more flexible way of specifying
which files should be backed up.

## We're on Twitter

We're now on social media as
[\@GenomeDK_AU](https://twitter.com/GenomeDK_AU) -on Twitter. Follow us
for casual status updates and other HPC-related content. Get in touch if
you have ideas for users, projects or research we should feature.

## ISO 27001-compliance

GenomeDK is a ISO 27001-compliant HPC facility. This means that we have
a formal information security management system (ISMS) in place to guide
our information security choices and implementation, and that you can
safely store your sensitive data on GenomeDK.

## Unstable faststorage

During the past six months many of you have experienced unstable access
to faststorage due to a range of (mostly) software-related issues in the
filesystem software (BeeGFS) that is responsible for faststorage. We
have previously described the actions we have taken to resolve these
issues in detail. Since then we have introduced additional automation to
self-heal faststorage and are working with the company behind BeeGFS to
address any remaining issues.

## More detailed usage statistics

The `space` command has been updated and now provides a monthly overview of
billing hours used by users, projects, and all projects owned by you. To see a
report for your user specifically:

```bash
[local]$ space user
```

Or for a specific project:

```bash
[local]$ space project --project <name>
```

Or get an overview for all projects owned by you:

```bash
[local]$ space overview
```

# Upcoming

## New hardware

Due to supply issues and significant price jumps in 2021, we did not
purchase any new hardware. In the coming year we'll be acquiring new
hardware for both compute and storage, which should result in shorter
waiting times when submitting jobs and a more stable faststorage.

## Hardware retirement

We'll retire the s04 nodes during 2022 as they reach end-of-life.

# Tips and tricks

## Always use Conda, when using Conda

**Short version:** Always do `conda install` to install packages, no
matter what language the package is for. Not doing so can cause
hard-to-debug issues and broken Conda environments.

**Long version:** When adding new R packages to Rstudio, you should
always install it via Conda. For example, to install the Tidyverse
package, do this:

```bash
[local]$ conda install r-tidyverse
```

Instead of doing this in the Rstudio console:

``` r
install.packages("tidyverse")
```

The same applies for Python packages. For example, to install SciPy, do
this:

```bash
[local]$ conda install scipy
```

Instead of this:

```bash
[local]$ pip install scipy
```

---

Thank you for reading!
