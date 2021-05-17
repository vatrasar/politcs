from enum import Enum


class Fraction(Enum):
    KORWIN="Korwin"
    RN="RN"
    SP=2
    POR=3
    RAZEM="Razem"
    SLD="SLD"
    NO_PREFERENCES="Bez preferencji"
    KORONA="Korona"
    NO_FRACTIONS=8
    WIOSNA="Wiosna"
    PIS=10
    ALL=11

    @staticmethod
    def get_fraction_names():
        fraction_names_list=[]
        for party in Fraction:
            if party!=Fraction.ALL:
                fraction_names_list.append(party)

        return fraction_names_list

    @staticmethod
    def get_ZL_fractions():
        fraction_names_list = [Fraction.RAZEM,Fraction.WIOSNA,Fraction.SLD,Fraction.NO_PREFERENCES]
        # for party in Fraction:
        #     if party != Fraction.ALL:
        #         fraction_names_list.append(party)

        return fraction_names_list

    @staticmethod
    def get_konf_fractions():
        fraction_names_list = [Fraction.KORONA, Fraction.KORWIN, Fraction.RN, Fraction.NO_PREFERENCES]
        # for party in Fraction:
        #     if party != Fraction.ALL:
        #         fraction_names_list.append(party)

        return fraction_names_list

    @staticmethod
    def get_fractions_names(fractions):
        fractions_names_list=[]
        for fraction in fractions:
            fractions_names_list.append(fraction.value)
        return fractions_names_list

    @staticmethod
    def get_fraction_from_name(name):
        if(name=="Korwin"):
            return Fraction.KORWIN
        elif name=="Korona":
            return Fraction.KORONA
        elif name=="Ruch narodowy":
            return Fraction.RN
        elif name=="Bez preferencji":
            return Fraction.NO_PREFERENCES
        elif name=="Razem":
            return Fraction.RAZEM
        elif name=="Wiosna":
            return Fraction.WIOSNA
        elif name=="SLD":
            return Fraction.SLD
        elif name=="Solidarna Polska":
            return Fraction.SP
        elif name=="Porozumienie":
            return Fraction.POR
        elif name=="PIS":
            return Fraction.PIS
        else:
            return Fraction.NO_FRACTIONS
