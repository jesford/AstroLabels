# AstroLabels
A set of common (for me) strings used to label astronomy plots. 

Typing out axes labels like 
```
plt.ylabel('$\Delta\Sigma^\mathrm{off}(R)\ [M_{\odot}\ \mathrm{pc}^{-2}]$')
```
gets old, so I'm starting a repository for keeping track of these strings. 

You can install with `$ pip install AstroLabels`

Here's an example:
```python
import numpy as np
import matplotlib.pyplot as plt
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
