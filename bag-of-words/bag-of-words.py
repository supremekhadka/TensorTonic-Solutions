import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """

    bow_vector = np.array([(tokens.count(word)) for word in vocab], dtype=int)

    return bow_vector