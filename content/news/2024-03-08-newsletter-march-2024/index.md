---
title: Newsletter, March 2024
extra:
    published: false
---

We're now well into 2024 and it's time for the 10th edition of the newsletter.
2023 was probably one of the most transformative and busy years in the history
of GenomeDK. In this newsletter we'll touch on some of the big events. We'll
also provide you with some tips for keeping track of your usage of GenomeDK.

<!-- more -->

Last year we welcomed 230 new users and handed out 147 official GenomeDK mugs!
We also grew from 10028 TB to 15433 TB of data on `/faststorage`.

# What just happened?

A lot of things happened in the server room last year:

* We retired our old faststorage system and replaced it with a new, faster
  system with a capacity of 23 PB. This required installing three tonnes of
  equipment and migrating 12 PB of data behind the scenes, with minimal
  downtime.
* We retired and physically removed tonnes of retired hardware from the server room,
  preparing GenomeDK for future expansions.
* We installed new servers for the critical infrastructure that makes GenomeDK
  tick. This included moving all critical services to two new servers, as well
  as migrating all home folders to a new file server. We also improved and
  simplified our core network infrastructure.
* We had piping work done so that we now have access to water for water-cooling
  equipment, which leads us to...
* We purchased and installed, with the help of [Danoffice and
  Lenovo](https://www.danofficeit.com/stories/water-cooling/), 60 new compute
  nodes with a total of 11520 cores and 90 TB of memory. These babies are
  water-cooled and sit in a single rack.

On top of that, we recently moved all frontends to newer, bigger, faster
machines for improved user experience and reliability.

Here's a few pictures, in chronological order, from the year that passed for your enjoyment!

{{ gallery() }}

*Credit for pictures 3-6 goes to Nils Krogh.*

Outside of the server room, we also saw big changes and improvements:

* All servers were migrated from CentOS 7 to AlmaLinux 8, providing users with a
  much more up-to-date base system.
* We introduced TOTP-based two-factor authentication for all users, replacing our
  old whitelist-based setup.
* We improved our information with regards to resource usage for project owners.
  All project owners now receive a monthly e-mail with usage numbers for each of
  their projects. Projects owners will also automatically receive an e-mail if
  one of their projects are highly active.
* We successfully completed our yearly ISAE 3000 audit and ISO 27001
  verification audit.
* Our steering committee conducted a workshop to discuss the future strategic
  objectives for GenomeDK. This resulted in a document which describes the
  high-level strategic, as well as information security, objectives for the
  organization.
* We re-designed our website for a more modern and consistent look, and
  launched our news section (that you're looking at right now).
* We advertised two new system administrator positions!

In January 2023, we also had a great trip to [Happy Tammsvik](http://happytammsvik.se),
Stockholm, Sweden, together with [MOMA](https://www.moma.dk), where we presented
GenomeDK and how we provide infrastructure for MOMA's clinical diagnostics at the
13th NACG workshop.

# Tips and tricks

## Running on the frontend

We're seeing an increased tendency for users to run computations on the frontend.
Computations running on the frontend are killed without warning. When you test
your code on the frontend, please ensure that:

* it is only using a single core,
* you kill it after at most 10 minutes.

File downloads are exempted from these rules. It's perfectly fine to download files
on the frontend. In fact, you should never submit a job for downloading data.

## Keep track of your usage

Project owners now receive monthly e-mails with up-to-date usage of each of
their projects, but it is also possible to retrieve detailed usage data for
projects using the `gdk-project-usage` command. This command also provides usage
data over time.

## Use SPRING compression for FASTQ files

If you store FASTQ files on GenomeDK, we strongly encourage you to consider
[SPRING compressing](https://pubmed.ncbi.nlm.nih.gov/30535063/) the files to
save space. This is especially relevant if the files are also marked for backup.
