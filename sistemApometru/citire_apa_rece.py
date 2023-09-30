from sistemApometru.citireABC import CitireABC


class CitireApaRece(CitireABC):
    def __int__(self, an, luna, index_apa_rece):
        super().__int__(an, luna)
        self.index_apa_rece = index_apa_rece


    def citire(self):
        pass
