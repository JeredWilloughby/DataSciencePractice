#This program show how to display a heat plot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


s =pd.Series([0.0,0.1,0.2,0.3,0.4],
             ['V','W','X','Y', 'g'])
heatmap_data=pd.DataFrame({'A': s+0.0,
                            'B': s+0.1,
                            'C': s+0.2,
                            'D': s+0.3,
                            'E': s+0.4,
                            'F': s+0.5,
                            'G': s+0.6
                            })

plt.imshow(heatmap_data, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(heatmap_data.columns)), heatmap_data.columns)
plt.yticks(range(len(heatmap_data)), heatmap_data.index)
