import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    dot = np.dot(a, b)
    
    norm_a = np.sqrt(np.square(a).sum())
    norm_b = np.sqrt(np.square(b).sum())

    if norm_a == 0 or norm_b == 0:
      return 0
    
    return dot / (norm_a * norm_b)

  