=============
System status
=============

On-going
--------

.. eventlist::
    :status: ongoing

Upcoming
--------

.. eventlist::
    :status: upcoming

Recent
------

.. eventlist::
    :status: recent
    :reverse:


.. event:: Updating drivers and firmware
    :uid: downtime-210311
    :start: 2021-03-11 08:00 +0200
    :end: 2021-03-11 16:00 +0200
    :tags: drivers firmware

    During this downtime we will update firmware and drivers, as well as BeeGFS,
    which serves /faststorage. This will improve overall stability of the systems.

    At the start of the maintenance we will close all open connections and shut off
    access to the cluster for all users.

    Queued jobs overlapping the maintenance window will not start. Running jobs
    will be re-queued at the start of the maintenance.


.. event:: NFS storage maintenance
    :uid: downtime-20201110
    :start: 2020-11-10 14:00 +0200
    :end: 2020-11-11 10:00 +0200
    :actualend: 2020-11-11 10:00 +0200
    :tags: storage nfs management

    The cluster will be unavailable for all users in this timespan. During the
    downtime we will decomission our old NFS storage servers. After this
    maintenance, all users will be on new storage servers.

    Additionally, we will move critical services to a new management node.


.. comment::

    .. event:: Dead file server
        :uid: dead-file-server-20200624
        :start: 2020-08-06 09:00 +0200
        :end: 2020-08-12 12:00 +0200
        :tags: unexpected outage

        A storage server (s96n01) unexpectedly died yesterday.

        This means that faststorage is completely unavailable. To prevent any
        further problems and confusion, all users have been disconnected from
        the cluster.

        We have contacted the manufacturer. You will be notificed as soon as
        the issue is resolved.

.. event:: Major power outage
    :uid: power-outage-20200624
    :start: 2020-06-24 11:23 +0200
    :end: 2020-06-25 15:30 +0200
    :tags: unexpected outage

    Today at approx. 11.23 we experienced a major power outage. The outage
    affected a large area around Ny Munkegade/Langelandsgade. While the first
    line of emergency power kicked, the second line did not. This caused the
    entire cluster to shut down.

    The power resumed at approx. 12.30 and the cluster slowly booted up again.
    At 13.00 all compute nodes and frontends were up and running.
    Unfortunately, faststorage did not come back up as expected. One of the
    JBODs (a drawer full of hard drives) was completely dead. This causes the
    entire faststorage to become unavailable.

    We have reported the issue to the manufacturer and expect it to be resolved
    during tomorrow. We do not expect any data loss.

    **UPDATE:** We have now recovered fully from the power outage yesterday.
    Some compute nodes will remain unavailable.

    All users should now be able to access the cluster and access all
    filesystems (home folder and faststorage). If you experience any issues,
    please let us know.

.. event:: General maintenance
    :uid: downtime-20200617
    :start: 2020-06-17 23:59 +0200
    :end: 2020-06-18 22:00 +0200
    :actualend: 2020-06-18 16:45 +0200
    :tags: storage upgrades

    The cluster will be unavailable for all users in this timespan.

    During the downtime we will upgrade several systems including the
    faststorage filesystem.

    At the start of the maintenance we will close all open connections and shut
    off access to the cluster for all users.

    Queued jobs overlapping the maintenance window will not start. Running jobs
    will be re-queued at the start of the maintenance.

    We apologize for any inconvenience this may cause.

    Extended due to database issues.

.. event:: nfs storage maintenance
    :uid: downtime-20200104
    :start: 2020-02-01 08:00 +0200
    :end: 2020-02-01 16:00 +0200
    :actualend: 2020-02-01 14:28 +0200
    :tags: storage nfs

    the cluster will be unavailable for all users in this timespan. during the
    downtime we will apply system updates across the cluster and perform nfs
    storage maintenance as we are working towards decommissioning our old nfs
    storage servers and introducing new servers. over time, this will result
    in a more stable and responsive environment for all genomedk users.

.. event:: nfs storage maintenance
    :uid: downtime-20191207
    :start: 2019-12-07 08:00 +0200
    :end: 2019-12-07 16:00 +0200
    :actualend: 2019-12-07 10:30 +0200
    :tags: storage nfs

    the cluster will be unavailable for all users in this timespan. during the
    downtime we will apply system updates across the cluster and perform nfs
    storage maintenance as we are working towards decommissioning our old nfs
    storage servers and introducing new servers. over time, this will result
    in a more stable and responsive environment for all genomedk users.

.. event:: Storage node failure
    :uid: storage-failure-20191202
    :start: 2019-12-02 18:45 +0200
    :end:   2019-12-02 23:55 +0200
    :tags: storage failure

    Approximately at 18:45 one of the storage nodes for faststorage experianced a
    hardware failure which resulted in I/O errors when trying to access faststorage. The queue
    was paused almost immidately. It was quickly discovered that failure cannot be handled
    remotely. At 21:32 our representative was at the site and at 22:15 the failure
    was preliminarly resolved. After further stability testing at 23:55 the cluster
    resumed normal operations. No data was lost.

.. event:: NFS storage maintenance
    :uid: downtime-20191102
    :start: 2019-11-02 08:00 +0200
    :end: 2019-11-02 16:00 +0200
    :actualend: 2019-11-02 14:15 +0200
    :tags: storage nfs

    the cluster will be unavailable for all users in this timespan. during the
    downtime we will apply system updates across the cluster and perform nfs
    storage maintenance as we are working towards decommissioning our old nfs
    storage servers and introducing new servers. over time, this will result
    in a more stable and responsive environment for all genomedk users.

.. event:: NFS storage maintenance
    :uid: downtime-20191005
    :start: 2019-10-05 08:00 +0200
    :end: 2019-10-05 16:00 +0200
    :actualend: 2019-10-05 10:29 +0200
    :tags: storage nfs

    The cluster will be unavailable for all users in this timespan. During the
    downtime we will perform NFS storage maintenance as we are working towards
    decommissioning our old NFS storage servers and introducing new servers.
    Over time, this will result in a more stable and responsive environment for
    all GenomeDK users.

.. event:: NFS storage maintenance
    :uid: downtime-20190907
    :start: 2019-09-07 08:00 +0200
    :end: 2019-09-07 16:00 +0200
    :actualend: 2019-09-07 12:49 +0200
    :tags: storage nfs

    The cluster will be unavailable for all users in this timespan. During the
    downtime we will perform NFS storage maintenance as we are working towards
    decommissioning our old NFS storage servers and introducing new servers.
    Over time, this will result in a more stable and responsive environment for
    all GenomeDK users.

.. event:: Faststorage hardware upgrade
    :uid: faststorage-upgrade-20190805
    :start: 2019-08-06 00:00 +0200
    :end: 2019-08-06 16:00 +0200
    :tags: storage hardware

    The cluster will be unavailable for all users in this time span. During the
    downtime we will be applying hardware expansion to our storage. Because the
    expansion involves key infrastructure upgrades, the downtime is needed.


.. event:: Faststorage outage
    :uid: faststorage-outage-20190726
    :start: 2019-07-26 01:12 +0200
    :end: 2019-07-26 06:05 +0200
    :actualend: 2019-07-26 06:05 +0200
    :tags: outage

    Due to unexpected software crash faststorage was unavailable. The problem has been resolved
    and everything should be back up and operational now.


.. event:: Fire detector and cooling maintenance
    :uid: fire-detector-and-cooling-maintenance-20190522
    :start: 2019-06-12 08:00 +0200
    :end: 2019-06-12 12:00 +0200
    :actualend: 2019-06-12 10:00 +0200
    :tags: building

    This maintenance does not involve the cluster itself. No changes or
    upgrades will be performed.

    Due to maintenance of the fire detector and cooling system in the server
    room we need to lower the power output to a minimum. The cluster will not
    be available in any way during this maintenance.


.. event:: Building maintenance
    :uid: building-maintenance-20190507
    :start: 2019-05-07 08:00 +0200
    :end: 2019-05-07 12:00 +0200
    :actualend: 2019-05-07 13:44 +0200
    :tags: building

    Due to critical building maintenance on 7th of May 8:00-12:00 we have to
    lower the power output to the minimum. Therefore, the downtime procedure
    will be followed. We hope to limit the scope of this downtime to just
    compute nodes, and keep the rest of the cluster fully operational.


.. event:: NFS storage maintenance
    :uid: nfs-storage-maintenance-20190501
    :start: 2019-05-03 08:00 +0200
    :end: 2019-05-03 16:00 +0200
    :actualend: 2019-05-03 11:30 +0200
    :tags: storage nfs

    The cluster will be unavailable for all users in this timespan. During the
    downtime we will perform NFS storage maintenance as we are working towards
    decommissioning our old NFS storage servers and introducing new servers.
    Over time, this will result in a more stable and responsive environment for
    all GenomeDK users.
