import numpy as np
from collections import Counter

def calculate_entropy(series):
    counts = Counter(series)
    total = sum(counts.values())
    probabilities = [count / total for count in counts.values()]
    entropy = -sum(p * np.log2(p) for p in probabilities if p > 0)
    return entropy
