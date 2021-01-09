# responseSpect
acceleration,velocity and displacement response spectra calculation

The followings are the basic example of using responseSpect.

```python   
from responseSpect import responseSpectMain
import numpy as np
dt=0.02 #time interval (s)
acc=np.loadtxt("acc.txt") #one column acceleration time history (g)
beta=0.05 #damping ratio
T=[1,2,3,4,5] # periods list
sa,sv,sd=responseSpectMain.SaSvSd(acc,dt,T,beta)   
```
