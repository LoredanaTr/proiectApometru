from sistemApometru.citire_apa_calda import CitireApaCalda
from sistemApometru.citire_apa_rece import CitireApaRece


class Afisare: #funcția principală pentru interacțiunea cu utilizatorul
    def __init__(self):
        self.citiri = []

    def afisare_consum(self):
        consum_apa_rece = 0
        consum_apa_calda = 0

        for citire in self.citiri:
            if isinstance(citire, CitireApaCalda):
                consum_apa_calda += citire.get_index_apa_calda()  #pe obiectul creat citire, creat cu clasa citire apa calda(14)
            elif isinstance(citire, CitireApaRece):
                consum_apa_rece += citire.get_index_apa_rece()
        print(f" Apa rece: consumul este {consum_apa_rece} ")
        print(f" Apa calda: consumul este {consum_apa_calda}")
