import numpy as np
import matplotlib.pyplot as plt; plt.ion()
import matplotlib
import seaborn; seaborn.set()

from astrolabels import AstroLabels
al = AstroLabels()

matplotlib.rcParams["axes.labelsize"] = 20
matplotlib.rcParams["legend.fontsize"] = 20

# hopefully your data doesn't look like this...
plt.figure(figsize=(5, 5))
plt.plot(np.random.rand(10), np.random.rand(10), 'o')
plt.xlabel(al.r_mpc)
plt.ylabel(al.dsigma_off)
plt.tight_layout()
plt.savefig('sample_plot.png')
