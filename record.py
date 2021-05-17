from enum import Enum

from enums.fractions import Fraction
from enums.priority_party_feature import Priority_party_feature
from enums.sex import Sex


class Record():
    def __init__(self,sex,type_name:str,sport_level_before, friends_level_before,is_in_realtionship_before,sport_level_after, friends_level_after,is_in_realtionship_after):
        self.sex = Sex.get_sex(sex)
        self.type_name = type_name.upper()
        self.before_epidemic=PersonDataFromOneYear(sport_level_before, friends_level_before,is_in_realtionship_before)
        self.after_epidemic=PersonDataFromOneYear(sport_level_after, friends_level_after,is_in_realtionship_after)


class PersonDataFromOneYear():

    def __init__(self,sport_level, friends_level,is_in_realtionship):


        self.sport_level_before=int(sport_level)
        if(friends_level=="Więcej niż 5"):
            self.friends_level = 5
        else:
            self.friends_level=int(friends_level)
        if(is_in_realtionship=="Nie"):
            self.is_in_realtionship=False
        else:
            self.is_in_realtionship = True



