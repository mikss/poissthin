# PYTHON 2

import numpy as np
import matplotlib.pyplot as plt, mpld3
import genPRM
from mpld3 import plugins

# TODO: https://mpld3.github.io/examples/drag_points.html
# TODO: http://stackoverflow.com/questions/26532327/retrieve-data-from-dynamic-mpld3-plot-in-python
# TODO: http://stackoverflow.com/questions/24498322/get-point-information-after-dragging

box_time = 40
box_thin = 1
inten_time = 1
inten_thin = 0.65

# simulate
poiss = genPRM.sim(box_time, inten_time)
[prm_in, prm_out] = genPRM.thin(poiss, box_thin, inten_thin)

fig = plt.figure()

# plot 2D
plt.subplot(211)
if prm_in: plt.scatter(*zip(*prm_in), s=40, color='#1199EE', alpha=0.5, edgecolor = 'k')
if prm_out: plt.scatter(*zip(*prm_out), s=40, color='0.5', alpha=0.25, edgecolor='k')
plt.xlabel('time')
plt.ylabel('thinning dimension')
plt.axis([0, box_time, 0, box_thin])
plt.plot([0,box_time],[inten_thin,inten_thin], alpha=0.5, linewidth=2, color='0.5', linestyle=':')
# plt.axhspan(inten_thin, box_thin, color='0.95', alpha=0.75, lw=0)

# plot 1D: prep
prm = prm_in + prm_out
prm.sort(key = lambda tup: tup[0])
d1_times = [0] + list(zip(*prm)[0])
d1_heights = range(len(d1_times))
prm_in.sort(key = lambda tup: tup[0])
d1_times_thinned = [0] + list(zip(*prm_in)[0])
d1_heights_thinned = range(len(d1_times_thinned))

# plot 1D: work around lack of steps in mpld3
plt.subplot(212)
dup_times = [val for val in d1_times for _ in (0,1)]
dup_times = dup_times[1:] + [dup_times[-1], box_time]
dup_heights = [val for val in d1_heights for _ in (0,1)]
dup_heights += [dup_heights[-1]]
dup_times_thinned = [val for val in d1_times_thinned for _ in (0,1)]
dup_times_thinned = dup_times_thinned[1:] + [dup_times_thinned[-1], box_time]
dup_heights_thinned = [val for val in d1_heights_thinned for _ in (0,1)]
dup_heights_thinned += [dup_heights_thinned[-1]]

# plot 1D: actual plotting
plt.plot(dup_times,dup_heights,linewidth=1.5, color='0.5', alpha=0.3)
plt.plot(dup_times_thinned,dup_heights_thinned,linewidth=1.5,color='#1199EE',alpha=0.6)
plt.xlabel('time')
plt.ylabel('number of jumps')
plt.axis([0, box_time, 0, box_time * inten_time * 1.5])

# plot LLN limit
plt.plot([0, box_time],[0, box_time * inten_time], color= '0.5', alpha=0.5, linestyle='--')
plt.plot([0, box_time],[0, box_time * inten_time * inten_thin], color='#1199EE', alpha=0.5, linestyle='--')

#mpld3.show(fig)
mpld3.save_html(fig,'poisstest.html')
