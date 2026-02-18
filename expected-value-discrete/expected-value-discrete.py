import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x)
    p = np.array(p)
    
    if np.sum(p) < 1 - 10e-6:
        raise ValueError("Probabilities do not sum to 1!")
        return

    return float(np.sum(x*p))