import pandas as pd

from enums.fractions import Fraction
from enums.main_party import Main_party
from enums.priority_party_feature import Priority_party_feature
from enums.sex import Sex
from record import Record
import re
import matplotlib.pyplot as plt
import typing
import os
# results_data=pd.read_csv("data.csv")
# test=results_data.iloc[0]
# print(results_data.iloc[0][1])
import numpy as np

def load_data(filename_with_extension)->list:
    df_data = pd.read_csv(filename_with_extension)
    record_list=[]

    for index,record in df_data.iterrows():
        my_record=Record(record[8],record[7],record[5],record[1],record[3],record[6],record[2],record[4])
        record_list.append(my_record)

    return record_list


def filtr_records(record_list:list,sex=Sex.ALL,type="....",priority_party_feature=Priority_party_feature.ALL, main_party=Main_party.ALL)->list:
    """
    :type str if you want for example all J types give ...J, if all NT type give .NT.
    :rtype: object
    """
    result=list(filter(lambda record:sex==Sex.ALL or record.sex==sex, record_list))

    result=list(filter(lambda record:re.match(type,record.type_name), result))
    result = list(filter(lambda record: priority_party_feature == Priority_party_feature.ALL or record.priority_party_feature == priority_party_feature,result))
    result = list(filter(lambda record: main_party == Main_party.ALL or record.main_party == main_party,result))

    return result

def split_on_partys(data):
    partys_map={}
    for party in Main_party:
        if party!=Main_party.ALL:
            partys_map[party]=[]
    for record in data:
        partys_map[record.main_party].append(record)
    return partys_map

def split_on_fractions(data,fractions):
    fraction_map={}
    for fraction in fractions:
        fraction_map[fraction]=[]
    for record in data:
        fraction_map[record.fraction].append(record)
    return fraction_map

def get_votes_in_procent_for_each_party(data_map:map,sum_of_votes):
    result_map={}

    for entry in zip(data_map.keys(),data_map.values()):
        if sum_of_votes!=0:
            result_map[entry[0]]=round((float(get_sum_of_votes(entry[1]))/sum_of_votes)*100)
        else:
            result_map[entry[0]] = int(0)
    return result_map

def get_sum_of_votes(data):
    sum=0
    for record in data:
        sum=sum+record.vote_value
    return sum
def get_womans_weight(data):
    mans_list = filtr_records(data, sex=Sex.M)
    womens_list = filtr_records(data, sex=Sex.F)
    return float(len(mans_list))/len(womens_list)

def set_weight(data, weight):
    for record in data:
        record.vote_value=weight

def split_on_ideas(data):
    ideas_map={}
    for party in Priority_party_feature.get_priority_feature_list():
        ideas_map[party]=[]
    for record in data:
        ideas_map[record.priority_party_feature].append(record)
    return ideas_map


def produce_standard_charts(data,title,woman_weight,directory):

    standard_charts_for_partys(data, title, woman_weight,directory)





def standard_charts_for_partys(data, title, woman_weight,directory):


    if not os.path.exists("./results/"+directory):
        os.makedirs("./results/"+directory)#create directory if not exists


    mans_list = filtr_records(data, sex=Sex.M)
    womens_list = filtr_records(data, sex=Sex.F)
    # all
    all_fractions_map = split_on_partys(data)
    all_votes_in_procent_for_each_fraction = get_votes_in_procent_for_each_party(all_fractions_map, get_sum_of_votes(data))

    # with weight
    set_weight(womens_list, weight=woman_weight)
    weight_fractions_map = split_on_partys(data)
    weight_votes_in_procent_for_each_fractions = get_votes_in_procent_for_each_party(weight_fractions_map,
                                                                                 get_sum_of_votes(data))
    set_weight(womens_list, weight=1)
    # mans
    mans_fractions_map = split_on_partys(mans_list)
    mans_votes_in_procent_for_each_fraction = get_votes_in_procent_for_each_party(mans_fractions_map,
                                                                               get_sum_of_votes(mans_list))
    # womans
    womens_fractions_map = split_on_partys(womens_list)
    womens_votes_in_procent_for_each_fraction = get_votes_in_procent_for_each_party(womens_fractions_map,
                                                                                 get_sum_of_votes(womens_list))
    plot_the_chart(
        {"mężczyźni": mans_votes_in_procent_for_each_fraction, "kobiety": womens_votes_in_procent_for_each_fraction,
         "suma bez wag": all_votes_in_procent_for_each_fraction, "suma z wagami": weight_votes_in_procent_for_each_fractions},
        Main_party.get_main_party_names(), title+": partie",len(mans_list),len(womens_list),directory,directory+"_partie.svg")

    #standard charts for fractions

    ##LR
    zl_fractions = Fraction.get_ZL_fractions()
    make_chart_for_fraction(data, title, woman_weight,zl_fractions,Main_party.LR,directory)

    ##konfa
    konf_fractions = Fraction.get_konf_fractions()
    make_chart_for_fraction(data, title, woman_weight, konf_fractions, Main_party.KONF,directory)

    # standard charts for values
    ##all
    all_ideas_map = split_on_ideas(data)
    all_votes_in_procent_for_each_idea=get_votes_in_procent_for_each_party(all_ideas_map,get_sum_of_votes(data))

    ## with weight
    set_weight(womens_list, weight=woman_weight)
    weight_ideas_map = split_on_ideas(data)
    weight_votes_in_procent_for_each_ideas = get_votes_in_procent_for_each_party(weight_ideas_map,
                                                                               get_sum_of_votes(data))
    set_weight(womens_list, weight=1)

    ## mans
    mans_ideas_map = split_on_ideas(mans_list)
    mans_votes_in_procent_for_each_ideas = get_votes_in_procent_for_each_party(mans_ideas_map,
                                                                                  get_sum_of_votes(mans_list))
    ## womans
    womens_ideas_map = split_on_ideas(womens_list)
    womens_votes_in_procent_for_each_ideas= get_votes_in_procent_for_each_party(womens_ideas_map,
                                                                                    get_sum_of_votes(womens_list))
    plot_the_chart(
        {"mężczyźni": mans_votes_in_procent_for_each_ideas, "kobiety": womens_votes_in_procent_for_each_ideas,
         "suma bez wag": all_votes_in_procent_for_each_idea,
         "suma z wagami": weight_votes_in_procent_for_each_ideas},
        Priority_party_feature.get_priority_feature_names_list(), title+": wartości", len(mans_list), len(womens_list),directory,directory+"_wartosci.svg")


def make_chart_for_fraction(data, title, woman_weight,zl_fractions,party,directory):

    zl_voters = filtr_records(data, main_party=party)
    mans_list = filtr_records(zl_voters, sex=Sex.M)
    womens_list = filtr_records(zl_voters, sex=Sex.F)
    # all
    all_fractions_map = split_on_fractions(zl_voters, zl_fractions)
    all_votes_in_procent_for_each_fraction = get_votes_in_procent_for_each_party(all_fractions_map,
                                                                                 get_sum_of_votes(zl_voters))
    # with weight
    set_weight(womens_list, weight=woman_weight)
    weight_fractions_map = split_on_fractions(zl_voters, zl_fractions)
    weight_votes_in_procent_for_each_fractions = get_votes_in_procent_for_each_party(weight_fractions_map,
                                                                                     get_sum_of_votes(zl_voters))
    set_weight(womens_list, weight=1)
    # mans
    mans_fractions_map = split_on_fractions(mans_list, zl_fractions)
    mans_votes_in_procent_for_each_fraction = get_votes_in_procent_for_each_party(mans_fractions_map,
                                                                                  get_sum_of_votes(mans_list))
    # womans
    womens_fractions_map = split_on_fractions(womens_list, zl_fractions)
    womens_votes_in_procent_for_each_fraction = get_votes_in_procent_for_each_party(womens_fractions_map,
                                                                                    get_sum_of_votes(womens_list))
    plot_the_chart(
        {"mężczyźni": mans_votes_in_procent_for_each_fraction, "kobiety": womens_votes_in_procent_for_each_fraction,
         "suma bez wag": all_votes_in_procent_for_each_fraction,
         "suma z wagami": weight_votes_in_procent_for_each_fractions},
        Fraction.get_fractions_names(zl_fractions), title+": frakcje "+party.value,len(mans_list),len(womens_list),directory,directory+"Frakcje_%s.svg"%(party.value))


def plot_the_chart(votes_map:typing.Dict,labels,chart_title,mans_number,womans_number,directory,fileName):
    """
    votes: list of dictionarys. each dictionary for one bar for example [mans,womans,general pop]
    where man={party:procentageResult}
    :rtype:
    """



    legend_elements_list=votes_map.keys()

    chart_title="%s (M%d|F%d)"%(chart_title,mans_number,womans_number)

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots()

    rect_votes_groups=[]
    sign=1
    retio=0.5
    for votes_key_group in votes_map.keys():
        rect_votes_group=ax.bar(x - sign*int(retio)*width, votes_map[votes_key_group].values(), width, label=votes_key_group)
        rect_votes_groups.append(rect_votes_group)
        retio=retio+0.5
        sign=sign*(-1)




    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("%")
    ax.set_title(chart_title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels,fontsize=8)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',fontsize=7)

    for rect_votes_group in rect_votes_groups:
        autolabel(rect_votes_group)


    fig.tight_layout()

    plt.savefig("./results/"+directory+"/"+fileName)
    plt.close()

def produce_for_each_demension(data,womans_weight):
    letters_pairs=[["E","I"],["N","S"],["T","F"],["J","P"]]
    for pair_index,letter_pair in enumerate(letters_pairs):
        for letter in letter_pair:
            type_name=list("....")
            type_name[pair_index]=letter
            type_name="".join(type_name)
            type_votes = filtr_records(data, type=type_name)
            type_name=type_name.replace(".","x")
            produce_standard_charts(type_votes, "wyniki "+type_name, womans_weight, type_name)
    type_votes = filtr_records(data, type=".NF.")
    produce_standard_charts(type_votes, "wyniki " + "XNFX", womans_weight, "XNFX")


def produce_for_each_type(data, womans_weight):
    types=["INTJ","INTP","INFP","INFJ","ISFJ","ISFP","ISTP","ISTJ","ENTJ","ENTP","ENFP","ENFJ","ESFJ","ESFP","ESTP","ESTJ"]
    for type_name in types:


        type_votes = filtr_records(data, type=type_name)

        produce_standard_charts(type_votes, "wyniki "+type_name, womans_weight, type_name)



if __name__ == '__main__':

    resuts=load_data("data2.csv")
    # resuts=filtr_records(resuts,Sex.M,"...J","")
    womans_weight=get_womans_weight(resuts)
    produce_standard_charts(resuts,"wyniki ogólne", womans_weight,"ogolne")
    produce_for_each_demension(resuts,womans_weight)
    produce_for_each_type(resuts,womans_weight)



