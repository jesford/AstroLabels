# AstroLabels
A set of common (for me) strings used to label astronomy plots. 

Typing out axes labels like 
```
plt.ylabel('$\Delta\Sigma_\mathrm{NFW}(R)\ [M_{\odot}\ \mathrm{pc}^{-2}]$')
```
gets old, so I'm starting a repository for keeping track of these strings. 

Example:
```python
import numpy as np
import matplotlib.pyplot as plt; plt.ion()
import seaborn; seaborn.set()

from astrolabels import AstroLabels
al = AstroLabels()

# hopefully your data doesn't look like this...
plt.plot(np.random.rand(10), np.random.rand(10), 'o')
plt.xlabel(al.r_mpc)
plt.ylabel(al.dsigma_off)
```
![sample plot](./images/sample_plot.png)

Feel free to add your own commonly used labels!
