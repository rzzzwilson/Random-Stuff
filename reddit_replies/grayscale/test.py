#!/bin/env python
# -*- coding: utf-8 -*-

"""
How to make a custom colourmap.

From: reddit.com/r/learnpython/comments/6srxq8/grayscale_plot/
"""

import sys
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# define our custom colourmap
lower_rgb = 118/256.        # because colours must be in the range [0, 1]
upper_rgb = 148/256.
colours = [(lower_rgb, lower_rgb, lower_rgb), (upper_rgb, upper_rgb, upper_rgb)]
cm = LinearSegmentedColormap.from_list('test_cmap', colours, N=32)

# generate float random data in range [0, 1000]
np.random.seed(0)
grid = np.random.rand(200, 200) * 1000

# plot data, show colour bar, save image
plt.imshow(grid, cmap=cm)
plt.colorbar()
plt.show()
