import numpy as np
from plots import *
from agginfo import *

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

class dustmodel:
    """
    A class to read a `dustkapscatmat_XXX.inp` file and store the information.

    Parameters
    ----------
    partype : str
        | Dust particle type.
        | **Available input values**:
        | ``'FA11'``, ``'FA13'``, ``'FA15'``, ``'FA19'``, ``'CAHP'``, ``'CAMP'``, ``'CALP'``, ``'grs'``
    size : str
        | Dust particle size.
        | **Available input values**:
        | **For aggregates**: the number of monomers.
        |   *Example*: ``size='4096'`` if you want an aggregate consisting of 4096 monomers.  
        | **For irregular grains**: the volume-equivalent radius in units of microns
        |   (the dicimal dot should be replaced by the underscore).
        |   *Example*: ``size='1_6000'`` if you want an irregular grain with the volume-eq. radius of 1.6 microns.
        |
        | You can also use ``agginfo.get_sizelist`` to obtain a list of available size values.
    comp : str
        | Dust composition.
        | **Available input values**: ``'org'``, ``'amc'``
    amon : str (optional)
        | Monomer radius (necessary if you call aggregate files).
        | **Available input values**:
        | ``'100nm'``, (``'150nm'``), ``'200nm'``, (``'300nm'``), ``'400nm'``
        | *Note*: 150nm and 300nm are only available for fractal aggregates.
    dist : bool (optional)
        With size distribution.
    chop : str (optional)
        | Forward scattering chop.
        | **Available input values**: ``'nochop'``, ``'chop5'``, ``'chop10'``

    Attributes
    ----------
    model : bool
        dust model name 
    path  : str
        a relative path to the file
    dist  : bool
        with size distribution 
    aggop : bool
        if particle type is aggregates
    nlam  : int
        Number of wavelength grids
    nang  : int
        Number of scattering angle grids.
    lmd   : float[nlam]
        Wavelength (microns)
    scatang : float[nang]
        Scattering angles (degrees)
    kabs,ksca,asym : float[nlam]
        Absorption and scattering opacities (cm^2/g) and the asymmetry parameter
    albedo  : float[nlam]
        Single scattering albedo (=ksca/(kabs+ksca))
    pmax    : float[nlam]
        Maximum degree of linear polariation
    z11,z12,z22,z33,z34,z44: float[nlmd,nang]
        Scattering matrix elements

    rhomat : float
        Material density (g/cc)
    avmin, avmax  : float (*only when* ``dist=True``)
        Volume-equivalent of the minimum and maximum aggregates in the size distribution
    av     : float (*only when* ``dist=False``)
        Volume-equivalent radius (micron) 
    pow    : float (*only when* ``dist=True``)
        Power-law index of size distribution: n(a)da propto a^{-p}da
    amon   : float (*only when* ``partype!='grs'``)
        Monomer radius (microns)
        Number of monomers of the minimum aggregate in the size distribution
    npmin, npmax  : float (*only when* ``partype!='grs'`` *and* ``dist=True``)
        Number of monomers of the minimum and maximum aggregates in the size distribution (if dist=True)
    acmin, acmax  : float (*only when* ``partype!='grs'`` *and* ``dist=True``)
        Characteristic radius of the minimum and maximum aggregates in the size distribution
    pormin,pormax : float (*only when* ``partype!='grs'`` *and* ``dist=True``)
        Porosity of the minimum and maximum aggregates in the size distribution
    np     : float (*only when* ``partype!='grs'`` *and* ``dist=False``)
        Number of monomers
    ac     : float (*only when* ``partype!='grs'`` *and* ``dist=False``)
        Characteristic radius (micron)
    por    : float (*only when* ``partype!='grs'`` *and* ``dist=False``)
        Porosity of the aggregate

    Methods
    -------
    showmodel:
        Print info about dust propertie.
    dustspec:
        Show summary plots of the optical property.
    """

    def __init__(self,partype,size,comp,amon=None,dist=True,chop='nochop'):
        """
        Constructs all the necessary attributes for the dustmodel object.
        """

        self.dist=dist

        # generate file name
        if chop not in ['nochop', 'chop5', 'chop10']:
            print('error: incorrect chop option')
            print('input value = ',chop)
            print('available options are' ,['nochop', 'chop5', 'chop10'])
            exit()
        
        # check partype
        if partype not in ['grs','CALP','CAMP','CAHP','FA19','FA15','FA13','FA11']:
            print('error: incorrect particle type')
            print('input value = ',partype)
            print('available options are ',['grs','CALP','CAMP','CAHP','FA19','FA15','FA13','FA11'])
            exit()

        # if grs, reset monomer radius option
        if partype == 'grs':
            amon=None

        # get a list of particle size
        nl=get_sizelist(partype,amon)
        
        # check consistency between monomer radius and number of monomers
        if size not in nl:
            print('Incorrect particle size')
            print('input particle type =',partype)
            if partype != 'grs':
                print('input monomer radius =',amon)
            if not nl:
                print('--> this monomer radius is not available')
            else:
                print('available size option is ',nl)
            exit()

        # set modelname and filename
        if partype=='grs':
            self.aggop=False
            if dist:
                filename='../aggscatrt/distave/'
                if chop=='nochop':
                    modelname=partype+'_rvmax'+size+'um_'+comp+'.inp'
                elif chop=='chop5':
                    modelname=partype+'_rvmax'+size+'um_'+comp+'_chop5.inp'
                elif chop=='chop10':
                    modelname=partype+'_rvmax'+size+'um_'+comp+'_chop10.inp'
            else:
                filename='../aggscatrt/single/'
                if chop=='nochop':
                    modelname=partype+'_rv'+size+'um_'+comp+'.inp'
                elif chop=='chop5':
                    modelname=partype+'_rv'+size+'um_'+comp+'_chop5.inp'
                elif chop=='chop10':
                    modelname=partype+'_rv'+size+'um_'+comp+'_chop10.inp'

        elif partype=='CALP' or partype =='CAMP' or partype=='CAHP' or \
            partype=='FA19' or partype=='FA15' or partype=='FA13' or \
            partype=='FA11':

            self.aggop=True
            if dist:
                filename='../aggscatrt/distave/'
                if chop=='nochop':
                    modelname=partype+'_Nmax'+size+'_'+amon+'_'+comp+'.inp'
                elif chop=='chop5':
                    modelname=partype+'_Nmax'+size+'_'+amon+'_'+comp+'_chop5.inp'
                elif chop=='chop10':
                    modelname=partype+'_Nmax'+size+'_'+amon+'_'+comp+'_chop10.inp'
            else:
                filename='../aggscatrt/single/'
                if chop=='nochop':
                    modelname=partype+'_'+size+'_'+amon+'_'+comp+'.inp'
                elif chop=='chop5':
                    modelname=partype+'_'+size+'_'+amon+'_'+comp+'_chop5.inp'
                elif chop=='chop10':
                    modelname=partype+'_'+size+'_'+amon+'_'+comp+'_chop10.inp'
        else:
            print('error: filename generation was not done correctly.')
            print('strange!')
            exit()

        filename=filename+chop+'/dustkapscatmat_'+modelname
        
        #
        self.model=modelname
        self.path=filename
        # start reading dustkapscatmat.inp
        header=''
        with open(filename,'r') as f:
            dum=f.readline()
            while (dum.strip()[0]=='#'):
                if self.aggop:
                    if self.dist:
                        if 'material density' in dum:
                            self.rhomat=float(dum.split()[-1])
                        if 'Monomer radius' in dum:
                            self.amon=float(dum.split()[-1])
                        if 'Minimum number of monomers' in dum:
                            self.npmin=float(dum.split()[-1]) 
                        if 'Maximum number of monomers' in dum:
                            self.npmax=float(dum.split()[-1]) 
                        if 'Minimum volume-equivalent radius' in dum:
                            self.avmin=float(dum.split()[-1])
                        if 'Maximum volume-equivalent radius' in dum:
                            self.avmax=float(dum.split()[-1])
                        if 'Power-law index' in dum:
                            self.pow=float(dum.split()[-1])                   
                    else:
                        if 'material density' in dum:
                            self.rhomat=float(dum.split()[-1])
                        if 'Monomer radius' in dum:
                            self.amon=float(dum.split()[-1])
                        if 'Number of monomers' in dum:
                            self.np=float(dum.split()[-1]) 
                else:
                    if self.dist:
                        if 'material density' in dum:
                            self.rhomat=float(dum.split()[-1])
                        if 'Minimum volume-equivalent radius' in dum:
                            self.avmin=float(dum.split()[-1])
                        if 'Maximum volume-equivalent radius' in dum:
                            self.avmax=float(dum.split()[-1])
                        if 'Power-law index' in dum:
                            self.pow=float(dum.split()[-1])
                    else:
                        if 'material density' in dum:
                            self.rhomat=float(dum.split()[-1])


                header = header + dum
                dum = f.readline()

            self.header=header
            self.iformat=int(dum)
            self.nlmd=int(f.readline())
            self.nang=int(f.readline())
            
            # preparing arrays
            self.lmd=np.zeros(self.nlmd)
            self.kabs=np.zeros(self.nlmd)
            self.ksca=np.zeros(self.nlmd)
            self.asym=np.zeros(self.nlmd)
            self.pmax=np.zeros(self.nlmd)
            self.albedo=np.zeros(self.nlmd)

            self.scatang=np.zeros(self.nang)
            self.z11=np.zeros([self.nlmd,self.nang])
            self.z12=np.zeros([self.nlmd,self.nang])
            self.z22=np.zeros([self.nlmd,self.nang])
            self.z33=np.zeros([self.nlmd,self.nang])
            self.z34=np.zeros([self.nlmd,self.nang])
            self.z44=np.zeros([self.nlmd,self.nang])

            dum=f.readline() # skip empty line
            for iwl in range(self.nlmd):
                dum=f.readline().split()
                self.lmd[iwl]=float(dum[0])
                self.kabs[iwl]=float(dum[1])
                self.ksca[iwl]=float(dum[2])
                self.asym[iwl]=float(dum[3])
                self.albedo[iwl]=self.ksca[iwl]/(self.kabs[iwl]+self.ksca[iwl])

            dum=f.readline() # skip empty line
            for iang in range(self.nang):
                dum=f.readline()
                self.scatang[iang]=float(dum)

            dum=f.readline() # skip empty line
            for iwl in range(self.nlmd):
                for iang in range(self.nang):
                    dum=f.readline().split()
                    self.z11[iwl,iang]=float(dum[0])
                    self.z12[iwl,iang]=float(dum[1])
                    self.z22[iwl,iang]=float(dum[2])
                    self.z33[iwl,iang]=float(dum[3])
                    self.z34[iwl,iang]=float(dum[4])
                    self.z44[iwl,iang]=float(dum[5])
                self.pmax[iwl]=max(-self.z12[iwl,:]/self.z11[iwl,:])

        # get radius, porosity of aggregates
        if self.aggop:
            if self.dist:
                self.acmin,self.pormin = get_radius_and_porosity(partype,amon,str(int(self.npmin)))
                self.acmax,self.pormax = get_radius_and_porosity(partype,amon,str(int(self.npmax)))
            else:
                self.av  = self.amon * self.np**(1.0/3.0)
                self.ac,self.por = get_radius_and_porosity(partype,amon,str(int(self.np)))

    def dustspec(self):
        """Print info about dust properties
        """
        if self.aggop:
            if self.dist:
                print('=============== Dust Parameters ===============')
                print('Model name = %-s'%self.model)
                print('Monomer radius           (um) = %-8.5f'%self.amon)
                print('Material density       (g/cc) = %-7.4f'%self.rhomat)
                print('-----Minimum aggregate in the distribution-----')
                print('Number of monomers            = %-5i'%self.npmin)
                print('Volume-eq radius         (um) = %-8.5e'%self.avmin)
                print('Characteristic radius    (um) = %-8.5e'%self.acmin)
                print('Porosity                  (%%) = %-7.2f'%self.pormin)
                print('-----Maximum aggregate in the distribution-----')
                print('Number of monomers            = %-5i'%self.npmax)
                print('Volume-eq radius         (um) = %-8.5e'%self.avmax)
                print('Characteristic radius    (um) = %-8.5e'%self.acmax)
                print('Porosity                  (%%) = %-7.2f'%self.pormax)
                print('-----------------------------------------------')
                print('Power-law index of size dist. = %-8.5e'%self.pow)
            else:
                print('=============== Dust Parameters ===============')
                print('Model name = %-s'%self.model)
                print('Monomer radius           (um) = %-8.5f'%self.amon)
                print('Material density       (g/cc) = %-7.4f'%self.rhomat)
                print('Number of monomers            = %-5i'%self.np)
                print('Volume equivalent radius (um) = %-8.5e'%self.av)
                print('Characteristic radius    (um) = %-7.4f'%self.ac)
                print('Porosity                  (%%) = %-7.2f'%self.por)
        else:
            if self.dist:
                print('=============== Dust Parameters ===============')
                print('Model name = %-s'%self.model)
                print('Material density       (g/cc) = %-7.4f'%self.rhomat)
                print('Minimium volume-eq radius (um)= %-8.5e'%self.avmin)
                print('Maximum volume-eq radius (um) = %-8.5e'%self.avmax)
                print('Power-law index of size dist. = %-8.5e'%self.pow)
            else:
                print('=============== Dust Parameters ===============')
                print('Model name = %-s'%self.model)
                print('Material density       (g/cc) = %-7.4f'%self.rhomat)


    def showmodel(self):
        """Show summary plots of the optical property
        """

        #fig,axes = plt.subplots(2,2,figsize=(15,12),gridspec_kw={'hspace': 0.0, 'wspace': 0.2, 'width_ratios': [1,1]})
        fig,axes = plt.subplots(2,2,figsize=(15,12),gridspec_kw={'hspace':0.4})

        axes[0,0].set_title('Opacity',fontsize=20)
        axes[1,0].set_title('Albedo, Max pol, asymmetry parameter',fontsize=20)
        axes[0,1].set_title('Phase function',fontsize=20)
        axes[1,1].set_title('Degree of polarization $-Z_\mathrm{12}/Z_\mathrm{11}$',fontsize=20)
        
        plots.set_lmd_vs_opc(axes[0,0])
        axes[0,0].plot(self.lmd,self.ksca,linewidth=3,c='black',linestyle='--',label='$\kappa_\mathrm{sca}$')
        axes[0,0].plot(self.lmd,self.kabs,linewidth=3,c='black',linestyle='-',label='$\kappa_\mathrm{abs}$')
        
        plots.set_lmd_vs_albedo(axes[1,0])
        axes[1,0].plot(self.lmd,self.ksca/(self.kabs+self.ksca),linewidth=3,c='black',linestyle='-',label='$\omega$')
        axes[1,0].plot(self.lmd,self.pmax,linewidth=3,c='black',linestyle='--',label='$P_\mathrm{max}$')
        axes[1,0].plot(self.lmd,self.asym,linewidth=3,c='black',linestyle=':',label='$g$')

        plots.set_ang_vs_phase(axes[0,1])
        plots.set_ang_vs_pol(axes[1,1])
        for iwl in range(self.nlmd):
            axes[0,1].plot(self.scatang[:],self.z11[iwl,:]/self.ksca[iwl],label='$\lambda=$'+str(self.lmd[iwl])+' $\mu\mathrm{m}$')
            axes[1,1].plot(self.scatang[:],-self.z12[iwl,:]/self.z11[iwl,:],label='$\lambda=$'+str(self.lmd[iwl])+' $\mu\mathrm{m}$')

        axes[0,0].legend(fontsize=16)
        axes[1,0].legend(fontsize=16)
        axes[0,1].legend(fontsize=16)
        axes[1,1].legend(fontsize=16)


if __name__ == '__main__':

    aggregate='FA11'
    monosize='100nm'
    a=dustmodel(partype=aggregate,size='128',amon=monosize,comp='org',dist=False,chop='chop10')
    a.dustspec()
