class AstroLabels(object):
    """Formatted strings for labeling astronomy plots."""
    def __init__(self):
        # units
        self.mpc = " $[\mathrm{Mpc}]$"
        self.msun_pc2 = " $[M_{\odot}\ \mathrm{pc}^{-2}]$"

        # quantities
        self.sgma = "$\Sigma(R)$"
        self.sgma_off = "$\Sigma^\mathrm{off}(R)$"
        self.delta = "$\Delta$"

        # dimensionful quantities
        self.r_mpc = "$R$" + self.mpc
        self.sigma = self.sgma + self.msun_pc2
        self.sigma_off = self.sgma_off + self.msun_pc2
        self.dsigma = self.delta + self.sigma
        self.dsigma_off = self.delta + self.sigma_off
