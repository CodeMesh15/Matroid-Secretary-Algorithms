from abc import ABC, abstractmethod
from typing import Iterable

class Matroid(ABC):
    def __init__(self, ground_set: Iterable[int]):
        self.E = list(ground_set)

    @abstractmethod
    def is_independent(self, subset: Iterable[int]) -> bool: ...
