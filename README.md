# genomedk-docs

User documentation for the GenomeDK cluster.

To get started (requires a working installation of conda):

    $ git clone git@github.com:birc-aeh/genomedk-docs.git
    $ cd genomedk-docs/
    $ conda activate
    $ conda env create -f environment.yml -n gdk-docs
    $ conda activate gdk-docs
    $ cd docs

You can now build the documentation:

    $ make html

To see the documentation in your browser, open the file 
`_build/html/index.html`.
