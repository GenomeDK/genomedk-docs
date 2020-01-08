.. _newsletter-2020-winter:

=======================
Newsletter, winter 2020
=======================

Hello!

We're back from winter vacation and it's time for a new GenomeDK newsletter.

Enjoy!

*The GenomeDK Team*

A few updates
-------------

* **More compute coming in 2020**

  In 2019 we said goodbye to our s01 and s02 nodes. These were the original
  nodes from the purchase that kickstarted GenomeDK in 2012. The nodes were
  out of warranty and started to cause issues since they were connected to the
  cluster through a different network than the remaining nodes, which caused a
  bottleneck that affected all users.

  Taking these nodes off the grid has caused a small queue to build up since we
  now have fewer compute nodes available. However, we're currently in the final
  stages of submitting a tender for new compute nodes. Hopefully this will
  result in a significant increase of our compute power in 2020.

* **Workshops**

  We cover topics like general cluster usage, *gwf* workflows, software
  management with Conda, and how to organize your projects. If your
  group/center/institute would like a workshop, don't hesitate to contact us.
  You can read more `here <https://genome.au.dk/support/#workshops>`_.

  We also hosted a very popular official workshop in December. Next time we'll
  make sure to book a larger room and get more cake!

* **Stay up to date on your compute and storage usage**

  The ``space`` command has been updated. It now has different views for users,
  projects, and project owners. Additionally, compute usage over time is now
  also reported. You can read more about the space commands
  `here <https://genome.au.dk/docs/working-with-data/#how-much-space-am-i-using>`_
  and `here <https://genome.au.dk/docs/working-with-data/#being-a-project-owner>`_.

* **New storage has been completely attached**

  Since the last newsletter the new expansion for faststorage has been
  completed. This included moving several petabytes of project data from old to
  new storage and then reattaching the old storage. This process was completely
  transparent to users.

* **Old project folders are being moved to faststorage**

  Old projects were created on our NFS filesystem. NFS is not suitable for the
  kind of data that projects usually contain, so we're now in the process of
  moving those old projects to fast storage. To do this we need regular
  downtimes that have been (and still will be) announced on the
  `status page <https://genome.au.dk/system-status/>`_.

User story
----------

**Lucie was one of the most active users on GenomeDK in 2019. We asked her to
say a bit about what she's been doing.**

I am Lucie Bergeron and I am currently enrolled as a PhD Fellow at Copenhagen
University under the supervision of Guojie Zhang (http://zhanggjlab.org/en/).

I started my project on germline mutation rate in vertebrates 2 years ago, yes,
it goes beyond mammals! During the first year of my PhD I collected trio
samples (parents and offspring) for 75 species of vertebrates including 44
mammals, 17 birds, 8 fishes and 6 reptiles.

We sequenced each individual at 60X coverage and then we will map the reads and
call variants. Finally, by comparing the genome of the parents to the one of
their offspring, we can find the number of germline mutation that occurs in one
generation. For most species, I have 1 or 2 trios but for few I have more than
5 trios. Especially, I’ve got a big pedigree of rhesus macaque (Macaca mulatta)
with 19 trios.

With this dataset I developed my pipeline and got some interesting results that
we could compare to humans and apes mutational processes.

My project is in collaboration with Søren Besenbacher and Mikkel H. Schierup
from Aarhus University who introduced me to GenomeDK! Since then I am using it
extensively to analyze all my genomes.

**Thanks to Lucie for sharing her story with us!**

---

Thank you for reading!
