import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    e = np.unique(y)
    sum = 0
    for i in e:
        p = y.count(i) / len(y)
        if p == 0:
            sum += 0
        else:
            sum += p * np.log2(p)
    
    entropy = -sum
    
    return float(entropy)