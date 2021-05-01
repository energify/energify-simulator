
import numpy as np
import random

a = [0,1,2,3]
random.shuffle(a)
print(a)

'''shape = 15
scale = 2

s = np.random.exponential(shape,100)
print(sorted(s))
print(np.mean(s))

import matplotlib.pyplot as plt
import scipy.special as sps  
count, bins, ignored = plt.hist(s, 50, density=True)
y = bins**(shape-1)*(np.exp(-bins/scale) /  
                     (sps.gamma(shape)*scale**shape))
plt.plot(bins, y, linewidth=2, color='r')  
plt.show()'''


