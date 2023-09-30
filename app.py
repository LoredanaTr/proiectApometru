from sistemApometru.afisare import Afisare
from sistemApometru.citire_apa_rece import CitireApaRece
from sistemApometru.citire_apa_calda import CitireApaCalda


an_curent = None
luna_curenta = None

def configurare_luna_an():
    global an_curent, luna_curenta
    an = input("Introduceti anul curent: ")
    luna = input("Introduceti luna curenta: ")
    an_curent = an
    luna_curenta = luna
    return an, luna



def run_app():

    global an_curent, luna_curenta

    an_curent, luna_curenta = configurare_luna_an() #setam luna si anul ptr care introducem date

    contor_apa_rece = CitireApaRece(an_curent, luna_curenta)
    contor_apa_calda = CitireApaCalda(an_curent, luna_curenta)

    while True:  # afisare meniu
        print("   Meniu:")
        print("1. Adaugă citire apa calda ")
        print("2. Adaugă citire apa rece ")
        print("3. Afișare consum ")
        print("4. Reconfigurare luna si an")
        print("5. Iesire")

        # utilizatorul alege o optiune
        optiune = input("Alege o opțiune: ")

        if optiune == "1":  # adaugam o citire noua
            apa_calda = int(input("Introduceți valoarea contorului de apă caldă: "))
            contor_apa_calda.citire(apa_calda)
            print(f"Pentru anul {an_curent} si luna {luna_curenta}: ")
            print(f"Valoarea indexului pentru contorul de apa calda este {contor_apa_calda.index_apa_calda}") #la fel se face si ptr apa rece

        elif optiune == "2":  #adaugam o citire noua ptr apa  rece
            apa_rece = int(input("Introduceți valoarea contorului de apă rece: "))
            contor_apa_rece.citire(apa_rece)
            print(f"Pentru anul {an_curent} si luna {luna_curenta}: ")
            print(f"Valoarea indexului pentru contorul de apa rece este {contor_apa_rece.index_apa_rece}")  # la fel se face si ptr apa rece



        elif optiune == "3":  # afisam consumul
            afisare_date = Afisare()
            afisare_date.afisare_consum()

        elif optiune == "4":  #reconfigurare an si luna curenta
            an_curent, luna_curenta = configurare_luna_an()

        elif optiune == "5":  # ieșim din aplicație
            print("La revedere!")
            break

        else:
            print("Opțiune invalidă. Vă rugăm să selectați o opțiune validă.")

if __name__ == '__main__':
   run_app()




