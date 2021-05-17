import math
from enum import Enum


class Sex(Enum):
    M=0
    F=1
    NO_INFO=2
    ALL=3

    @staticmethod
    def get_sex(sex):
        if(isinstance(sex,float)):
            return Sex.NO_INFO
        if("Mężczyzna"==sex):
            return  Sex.M
        elif "Kobieta"==sex:
            return Sex.F