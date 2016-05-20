import numpy.testing as nt
# assert_equal, assert_allclose, assert_raises

from ..astrolabels import AstroLabels
al = AstroLabels()


def test_dsigma():
    nt.assert_equal(al.dsigma,
                    "$\Delta$$\Sigma(R)$ $[M_{\odot}\ \mathrm{pc}^{-2}]$")


def test_rmpc():
    nt.assert_equal(al.r_mpc, "$R$ $[\mathrm{Mpc}]$")


def test_sigmaoff():
    nt.assert_equal(al.sigma_off,
                    "$\Sigma^\mathrm{off}(R)$ $[M_{\odot}\ \mathrm{pc}^{-2}]$")
