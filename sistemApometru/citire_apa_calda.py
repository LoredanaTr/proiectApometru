from sistemApometru.citireABC import CitireABC


class CitireApaCalda(CitireABC):
    def __int__(self, an, luna, index_apa_calda):
        super().__int__(an, luna)
        self.index_apa_calda = index_apa_calda

    def citire(self, valoare_index):
        self.index_apa_calda = valoare_index
        return f"Valoarea pentru apa calda este {self.index_apa_calda} " #sa fac acelasi lucru ptr apa rece la linia 4

    def get_index_apa_calda(self):
        return self.index_apa_calda