import numpy as np

def entropy(p: np.ndarray) -> float:
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))
