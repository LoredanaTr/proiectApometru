from sistemApometru.citireABC import CitireABC


class CitireApaRece(CitireABC):
    def __int__(self, an, luna, index_apa_rece):
        super().__int__(an, luna)
        self.index_apa_rece = index_apa_rece

    def citire(self, valoare_index):
        self.index_apa_rece = valoare_index
        return f"Valoarea pentru apa rece este {self.index_apa_rece} "

    def get_index_apa_rece(self):
        return self.index_apa_rece