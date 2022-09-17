Application for RADMC-3D
==========================

One key application of ``AggScatVIR`` is observational modeling of (un)polarized scattered light from protoplanetary disks and debris disks. Our database has been designed so that users can easily carry out radiative transfer simulations with `RADMC-3D <https://www.ita.uni-heidelberg.de/~dullemond/software/radmc-3d/>`_, which is a publicly available radiative transfer simulation code. Since our dust data files (``dustkapscatmat_XXX.inp``) have a data structure directly readable by RADMC-3D v2.0, one can run RADMC-3D without additional data processing. You need to pick up one of our dust models and put it into a directory that RADMC-3D will be running. You are ready to run RADMC-3D as long as the other necessary input files have been properly prepared (see below).

Step-by-step guide to run RADMC-3D with AggScatVIR
###################################################

Here is a step-by-step guide to run RADMC-3D with ``AggScatVIR``.

First, please make sure that RADMC-3D has been installed in your working environment. If not, please follow the instructions in `the manual of RADMC-3D <https://www.ita.uni-heidelberg.de/~dullemond/software/radmc-3d/>`_ to install it on your system.

Suppose you've already installed RADMC-3D, then please go into a directory that you want to let RADMC-3D run. In other words, it is the directory where other necessary input files for RADMC-3D are located. Next, you need to choose one of our dust model files (``dustkapscatmat_XXX.inp``) and put it into your working directory.

You will also need to modify (or prepare) two other input files of RADMC-3D (``radmc3d.inp`` and ``dustopac.inp``) so that the code can recognize our dust file. In ``radmc3d.inp``, please make sure that the full polarization treatment is on. This can be done by inserting the following line in the file::

    scattering_mode_max = 5
 
In ``dustopac.inp``, please ensure that the ``inputstype`` and ``file_name_extension`` options are properly given. For example, this file can be like this::


    iformat  
    nspec
    -----------------------------
    inputstyle                       <=== Put 10 to use full scattering matrix elements
    iquantum                         
    file_name_extension              <=== Put XXX in dustkapscatmat_XXX.inp

where ``XXX`` should be read as your desired dust model name. 

Now it is ready. If you would like to make a scattered light image at a wavelength of 1.6 microns, you type::

    radmc3d image (... some other options...) lambda 1.6 stokes

The final option ``stokes`` is necessary if you would like to obtain an image with the full Stokes parameters.

.. _radmctips:

Tips for radiative transfer simulations
########################################

.. warning:: **Thermal Monte Carlo runs**: If you try to run ``mctherm`` in RADMC-3D using a dust file in this package, you will see warnings regading the wavelength coverage. This is because our database only covers visible and near-IR wavelengths, and this is too narrow to determine radiation equilibrium temperature of a dust particle. *Therefore, the package is more suited for monochromatic radiative transfer simulations.* 

.. seealso:: **Chopping forward scattering**: Dust particles much larger than the wavelength may exhibit a strong forward scattering, which may cause some issures in your simulations. One approximate  way to mitigate this issue is to chop the forward scattering peak off. For this purpose, ``AggScatVIR`` offers the dustkapscatmat_XXX.inp file with two different chopping angles: 5 and 10 degrees. If you encounter the issue, please consider using those files instead of those from the ``nochop`` directory.
