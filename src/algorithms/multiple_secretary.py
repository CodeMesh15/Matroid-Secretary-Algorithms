from typing import List, Tuple, Iterable, Set
import random

def threshold_multi(values: List[Tuple[int, float]], k: int):
    n = len(values)
    t = int(n / 3)
    sample = sorted((w for _, w in values[:t]), reverse=True)
    tau = sample[min(k-1, len(sample)-1)] if sample else float("inf")
    chosen: Set[int] = set()
    for e, w in values[t:]:
        if w >= tau and len(chosen) < k:
            chosen.add(e)
    return chosen
