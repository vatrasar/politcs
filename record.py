from enum import Enum

from enums.fractions import Fraction
from enums.priority_party_feature import Priority_party_feature
from enums.sex import Sex


class Record():
    def __init__(self,fractions,sex,priority_party_feature,main_party,type_name,vote_value=1):
        self.main_party=main_party
        self.sex=Sex.get_sex(sex)
        self.priority_party_feature=Priority_party_feature.get_party_feature(priority_party_feature)
        self.fraction=self.get_fraction(fractions)
        self.vote_value=vote_value
        #letters in type name
        self.type_name=type_name

    def get_fraction(self,fractions):
        for fraction in fractions:
            if not(isinstance(fraction,float)):
                return Fraction.get_fraction_from_name(fraction)

        return ""