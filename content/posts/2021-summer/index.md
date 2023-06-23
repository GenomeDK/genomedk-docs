---
title: Newsletter, summer 2021
date: 2021-07-08
---

Hello!

Summer is upon us and so it has become time for the 2021 summer
newsletter. There's plenty to cover this time as the past six months
have been both eventful and busy at GenomeDK.

We wish you all a great summer vacation!

Anders, Rasmus, and Dan

**The GenomeDK Team**

# The news

-   **Recent instability**

    As a lot of you have noticed, we have recently experienced stability
    issues. One of the servers hosting your home folders unexpectedly
    rebooted, which caused several issues when the server came back up
    again. Attempting to fix it, we updated the software on the server
    which required a few reboots, which prevented users on that server
    from logging in.

    The server is now stable again. During the next planned downtime, we
    will fully reinstall the server to ensure that no bad
    configuration/software is left there.

-   **We're shutting down /com/extra!**

    Yes, it's finally happening. After three years of recommending
    other means of installing and managing your software, we're
    shutting down /com/extra, our legacy software archive, on August
    16th! You've already received an e-mail about this, so this is just
    a gentle reminder to go back and re-read it, if you're still using
    /com/extra.

-   **Disk-based backup**

    The amount of data in backup has increased significantly over the
    past years, to the point where backup is a very significant post in
    our budget. Unfortunately, this leaves less money for buying new and
    replacing old equipment. To counter this, we are now working to
    replace our tape-based backup provided by AU IT, with a new
    disk-based backup solution. This will allow us to provide much more
    functionality to end-users and significantly reduce the cost of
    backup.

    We expect the new solution to go into production within the next
    three months. We will of course provide more information and updated
    documentation once it goes live!

-   **Terms of service**

    Over the past year, we have worked hard to formalize our information
    security framework at GenomeDK. As part of this work, we have
    developed a [terms](@/terms.md) document. We do
    this to provide more transparency about the services we provide,
    which should benefit you, the users.

    Note that by using the services provided by GenomeDK, you'll
    automatically be agreeing to the terms.

# Compute safely

We do what we can to protect you and your data at GenomeDK. There's a
few things that you can do to help us:

-   **Are you registered with a correct e-mail?**

    We use your e-mail to contact you about planned downtimes, outages,
    significant changes, password resets, this newsletter, and many
    other things. We also use it to notify you if your account is about
    to be deactivated. Please make sure that you're registered with a
    functioning e-mail that you check regularly!

    Run this:

    ```bash
    [fe1]$ finger $(whoami)
    ```

    to check what your e-mail address is currently. I you wish to change
    it, please get in touch via <support@genome.au.dk>.

-   **Check if your password has been compromised**

    If you reused your password for GenomeDK somewhere else, your
    password may have been leaked. A reliable source of password leaks
    is <https://haveibeenpwned.com>, which can tell you, based on your
    e-mail address, whether your password has been compromised.

    See [Changing your password](@/docs/getting-started.md#change_password) if
    you want to change your password.

# Other stuff

-   **Workshops**

    As the Danish society is slowly opening up again and most people
    have been vaccinated, we will again be doing physical workshops
    after the summer vacation. If your research group needs a workshop,
    get in touch!

-   **Learn using GPU's on HPC**

    Some of our colleagues from AU and SDU are doing a workshop on AI on
    HPC. If this has your interest, there's still open seats and it's
    entirely online:

    <https://www.gpuhackathons.org/event/interactive-hpc-dk-ai-science-gpu-bootcamp>

Thank you for reading!
