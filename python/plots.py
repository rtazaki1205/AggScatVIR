import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

class plots:
    """
    A class to set some axes.

    Methods
    --------
    set_lmd_vs_opc:
        set axis for a plot for the opacity againt wavelength.
    set_lmd_vs_albedo:
        set axis for a plot for the albedo, pmax, asymmetry parameter  against wavelength.
    set_ang_vs_phase:
        set axis for a plot for the phase function against scattering angle.
    set_lmd_vs_opc: 
        set axis for a plot for the degree of polarization against scattering angle.
    """

    def set_lmd_vs_opc(self):
        """
        set axis for a plot for the opacity againt wavelength.
        """
        self.set_ylim(1.e2,2.e5)
        self.set_xscale('log')
        self.set_yscale('log')
        self.set_xlim(0.5,4)
        self.set_xticks([0.5,1,2,4])
        self.set_xlabel('Wavelength $(\mu\mathrm{m})$', fontsize=20)
        self.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        self.get_xaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())
 
    def set_lmd_vs_albedo(self):
        """
        set axis for a plot for the albedo, pmax, asymmetry parameter  against wavelength.
        """
        self.set_ylim(0,1)
        self.set_xscale('log')
        self.set_xlim(0.5,4)
        self.set_xticks([0.5,1,2,4])
        self.set_xlabel('Wavelength $(\mu\mathrm{m})$', fontsize=20)
        self.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        self.get_xaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())

    def set_ang_vs_phase(self):
        """
        set axis for a plot for the phase function against scattering angle.
        """
        self.set_yscale('log')
        self.set_xlim(0,180)
        self.set_xlabel('Scattering angle (degrees)',fontsize=20)
        self.xaxis.set_major_locator(MultipleLocator(30))
        self.xaxis.set_minor_locator(MultipleLocator(10))

    def set_ang_vs_pol(self):
        """
        set axis for a plot for the degree of polarization against scattering angle.
        """
        self.set_xlim(0,180)
        self.set_xlabel('Scattering angle (degrees)',fontsize=20)
        self.xaxis.set_major_locator(MultipleLocator(30))
        self.xaxis.set_minor_locator(MultipleLocator(10))
