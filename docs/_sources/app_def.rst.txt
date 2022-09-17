.. _definition:

Appendix A: Definitions
===========================

.. _radiusdef:

Radius definitions
####################

Because of its complex shapes, there are several ways to define the size of an aggregate. We will use two definitions: (i) the volume-equivalent radius :math:`a_\mathrm{V}` and (ii) the characteristic radius :math:`a_\mathrm{c}`. The former and latter definitions are, so-to-speak measuring the mass and the apparent size of an aggregate, respectively.

The volume-equivalent radius is the radius of a sphere formed by squashing an aggregate into a spherical shape. Since the volume of the dust particle is the same before and after the squashing process, we have

.. math::
   \frac{4}{3}\pi a_\mathrm{V}^3=N \frac{4}{3}\pi a_\mathrm{mon}^3,

where :math:`a_\mathrm{mon}` is the radius of a monomer and :math:`N` is the number of monomers. We have also assumed all monomers in the aggregate are idential and spherical. From this, we obtain 

.. math::
   a_\mathrm{V}=a_\mathrm{mon}N^{1/3},


The volume-equivalent radius may be regarded as a measure of the aggregate volume (or its mass). It is obvious however that an actual aggregate has a size much larger than the volume-equivalent radius, particularly when the porosity is high. Thus, we introduce the second definition for the aggregate radius: the characteristic radius :math:`a_\mathrm{c}` (Mukai et al. 1992, Kozasa et al. 1992):

.. math::
   a_\mathrm{c} = \sqrt{\frac{5}{3}}a_\mathrm{g},

where :math:`a_\mathrm{g}` is the radius of gyration defined by

.. math::
    a_\mathrm{g} = \sqrt{\sum_{i=1}^{N} \frac{ \\|\vec{r_i}-\vec{r_M}\\|^2 }{N}}

.. _strucdef:

Porosity and fractal dimension
################################

By using the above two radius definitions, we define the porosity of an aggregate by

.. math::
   \mathcal{P} = 1 - \left(\frac{a_\mathrm{V}}{a_\mathrm{c}}\right)^3

Since both :math:`a_\mathrm{c}` and :math:`a_\mathrm{V}` are proportional to the monomoer radius, the porosity is independent of the monomer radius.

It is also useful to intorudce the fractal dimension :math:`D_\mathrm{f}` defined as follows:

.. math::
   N = k_\mathrm{f}\left(\frac{a_\mathrm{g}}{a_\mathrm{mon}}\right)^{D_\mathrm{f}},

where :math:`k_\mathrm{f}` is the fractal prefactor. 
The fractal dimension describes how the number of monomers, let say, the volume of an aggregate, goes up if we increase the radius of gyration of an aggregate. 

For example, if :math:`D_\mathrm{f}=3`, the volume increases with the radius cubed, which is similar to the case of a single spherical particle. A fractal dimension may take a value lower than 3. For example, if all monomers are lined up to form a straight chain aggregate. In this case, the total volume is proportaional to the radius, and hence :math:`D_\mathrm{f}=1`. Therefore, the fractal dimension will take a value :math:`1\le D_\mathrm{f}\le 3`, and the lower this value is, the more open the aggregate structure becomes.

The  fractal prefactor :math:`k_\mathrm{f}` may be regarded as related to a packing fraction in :math:`D_\mathrm{f}` dimensional space. Its meaning becomes clear if we consider the case of :math:`D_\mathrm{f}=3`. In this case, the above fractal scaling law gives 

.. math::
   \left(\frac{a_\mathrm{V}}{a_\mathrm{c}}\right)^3=\left(\frac{3}{5}\right)^{3/2}k_\mathrm{f}\approx0.465 k_\mathrm{f} ~~(D_\mathrm{f}=3)


By substituting this expression into the definition of the porosity, we obtain

.. math::
   \mathcal{P}=1-0.465 k_\mathrm{f}~~(D_\mathrm{f}=3)

Therefore, the fractal prefactor is related to the porosity of an aggregate. 

Optical properties
################################

The definition of the optical properties written in a file ``dustkapscatmat_XXX.inp`` follows the definitions of the ones used in RADMC-3D. See `the manual of RADMC-3D <https://www.ita.uni-heidelberg.de/~dullemond/software/radmc-3d/manual_radmc3d/dustradtrans.html#polarization-stokes-vectors-and-full-phase-functions>`_ for a detailed description.


