Get started
=====================

Download
##############

``AggScatVIR`` has been managed on a GitHub repository. You can freely download the latest version of ``AggScatVIR`` by typing a standard GitHub command::

    git clone https://github.com/rtazaki1205/XXX.git (up be updated)


Structure of this package
##########################

The package consists of the following directories:
::

    aggscatvir
    ├── README.md
    ├── aggscatrt
    │    ├── single
    │    │   ├─── nochop
    │    │   ├─── chop5
    │    │   └─── chop10
    │    └── distave
    │        ├─── nochop
    │        ├─── chop5
    │        └─── chop10
    ├── manual
    └── python

The optical properties of various dust particles are located in the ``aggscatrt`` directory. This directory consists of two directories: ``single`` and ``distave``. The former and the latter contain the optical properties with/without a particle size distribution, respectively. The optical properties of various dust particles are located under the ``nochop`` directory. 

.. note::
   You will also find the directories named chop5 and chop10. These directories are intended for those who have run into issues due to a strong forward scattering in radiative transfer calculations (see also :ref:`radmctips`). Therefore, those who have other purposes may ignore these directories. 
 
If you go into the ``nochop`` directory, you will see a number of files named like::
    
    dustkapscatmat_XXX.inp

where ``XXX`` represents a dust model name. In this file, you will find all optical properties, such as opacity and scattering matrix elements, for a given dust model of XXX. The structure of this file is the same as the one used in RADMC-3D. See `the manual of RADMC-3D <https://www.ita.uni-heidelberg.de/~dullemond/software/radmc-3d/manual_radmc3d/inputoutputfiles.html#the-dustkapscatmat-inp-files>`_ for a detailed description.


In the ``python`` directory, you will find a simple notebook on the usage of python tools.
