from enum import Enum


class Priority_party_feature(Enum):
    ECONOMY="Ekonomia"
    BELIEVES="Światopogląd"
    SOCIAL="Socjalne"
    PANDEMIC="Pandemia"
    FOREIGN_POLICY="Polityka.Z"
    LEADER="Lider"
    OTHER="Inne"
    ALL="all"



    @staticmethod
    def get_priority_feature_list():
        feature_list = []
        for feature in Priority_party_feature:
            if feature!=Priority_party_feature.ALL:
                feature_list.append(feature)
        return feature_list

    @staticmethod
    def get_priority_feature_names_list():
        feature_list = []
        for feature in Priority_party_feature:
            if feature != Priority_party_feature.ALL:
                feature_list.append(feature.value)
        return feature_list

    @staticmethod
    def get_party_feature(party_feature):

        if ("Sprawy światopoglądowe(aborcja, dyskryminacja, religia w szkołach)" == party_feature):
            return Priority_party_feature.BELIEVES
        elif "Gospodarka(podatki, regulacje dla firm, prawa pracownicze)" == party_feature:
            return Priority_party_feature.ECONOMY
        elif "Sympatia do liderów partyjnych" == party_feature:
            return Priority_party_feature.LEADER
        elif "Polityka socjalna(wsparcie dla najbiedniejszych, polityka prorodzinna)" == party_feature:
            return Priority_party_feature.SOCIAL
        elif "Polityka zagraniczna(integracja z UE, sojusz z USA, niezależność)" == party_feature:
            return Priority_party_feature.FOREIGN_POLICY
        elif "Inne" == party_feature:
            return Priority_party_feature.OTHER
        elif "Stosunek do pandemii (lockdowny, przymus noszenia masek)" == party_feature:
            return Priority_party_feature.PANDEMIC