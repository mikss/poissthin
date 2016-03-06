# genPRM.py: Python2

import numpy as np

# simulate Poisson Random Measure (PRM)
def sim(box_time, inten_time):
    rate = box_time * inten_time
    N = np.random.poisson(rate)
    poiss = np.random.uniform(0,box_time,N)
    return(poiss)

# adds a control dimension to PRM and then thins
def thin(poiss, box_thin, inten_thin):
    control = np.random.uniform(0,box_thin,len(poiss)) # valid because homogeneous intensity
    prm = zip(poiss, control)
    prm_in = [ele for ele in prm if ele[1] <= inten_thin]
    prm_out = [ele for ele in prm if ele[1] > inten_thin]
    return [prm_in, prm_out]
