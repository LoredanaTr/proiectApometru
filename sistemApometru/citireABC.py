from abc import ABC, abstractmethod


class CitireABC(ABC):
    def __init__(self, an, luna):
        self.an = an
        self.luna = luna

    @abstractmethod
    def citire(self, valoare_index):
        pass

