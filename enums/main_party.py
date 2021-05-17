from enum import Enum

class Main_party(Enum):
    ZP="ZP"
    KONF="KONF"
    KO="KO"
    LR="LR"
    PSL="PSL"
    PL2050="PL2050"
    OTHER="Inna"
    ALL="all"

    @staticmethod
    def get_main_party_names():
        partys_names_list=[]
        for party in Main_party:
            if party!=Main_party.ALL:
                partys_names_list.append(party.value)

        return partys_names_list

    @staticmethod
    def get_main_party(main_party):

        if ("Zjednoczona prawica" == main_party):
            return Main_party.ZP
        elif "Lewica Razem" == main_party:
            return Main_party.LR
        elif "Koalicja Obywatelska" == main_party:
            return Main_party.KO
        elif "Konfederacja" == main_party:
            return Main_party.KONF
        elif "Polska 2050" == main_party:
            return Main_party.PL2050
        elif "PSL" == main_party:
            return Main_party.PSL
        elif "Inna" == main_party:
            return Main_party.OTHER