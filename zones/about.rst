.. _about_zones:

======================
What is a closed zone?
======================

The GenomeDK cluster is divided into zones. The open zone resembles traditional
high-performance computing systems where data can be moved freely in and out of
the system.

For projects with additional security or legal requirements, GenomeDK provides
*closed zones*. A closed zone is an additional layer of security on top of our
existing security solutions.

A closed zone provides:

Isolated networking
    Users and compute nodes that are not part of the closed zone cannot access
    or even see nodes that are in the closed zone.
Data access limitations
    Users in the zone cannot directly move data in or out of GenomeDK. Instead,
    data must be imported and exported. Exporting requires approval from the
    owner of the closed zone. All exports are logged.
Access through a virtual desktop
    Users must access the cluster through a special virtual desktop which
    disallows copy-paste. This means that users cannot leak data by copy-
    pasting it out of the closed zone.
No node sharing
    In the open zone, jobs from multiple users can run on the same compute
    node. In a closed zone, only jobs started by users in the same zone can
    share a compute node.
Limited or no Internet connectivity
    The owner of the zone can choose how "open" the zone should be. For example,
    connections to specific websites can be allowed, or Internet connectivity
    can be cut completely.
User management
    The owner of a zone controls who is given access to the zone.

A closed zone is not tied to a single project -- one or more project folders
belong to the zone, so users in a zone can still organize and share their data
via project folders inside the zone.

Users will need a separate account/user for each closed zone they need access
to.

If you think that you need a closed zone for your projects, feel free to get in
touch.
