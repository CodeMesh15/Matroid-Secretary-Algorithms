import random
from typing import List, Tuple

def classical_secretary(values: List[Tuple[int, float]]):
    # values: list of (element, weight)
    n = len(values)
    k = int(n / 3)  # sample phase
    best = max(w for _, w in values[:k])
    for e, w in values[k:]:
        if w > best:
            return e, w
    return max(values, key=lambda x: x[14])
