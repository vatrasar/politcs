import pandas as pd

from comparation_charts import produce_comparation_charts
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

from standard_charts import produce_standard_charts, plot_womans_mans_vefore_after_chart, get_standard_data_for_chart
from tools import get_sum_of_votes_from_map, get_sample_numbers, filtr_records


def load_data(filename_with_extension)->list:
    df_data = pd.read_csv(filename_with_extension)
    record_list=[]

    for index,record in df_data.iterrows():
        my_record=Record(record[8],record[7],record[5],record[1],record[3],record[6],record[2],record[4])
        record_list.append(my_record)

    return record_list








#


def produce_for_each_demension(data):
    letters_pairs=[["E","I"],["N","S"],["T","F"],["J","P"]]
    list_of_demensions=[]
    for pair_index,letter_pair in enumerate(letters_pairs):
        for letter in letter_pair:
            type_name=list("....")
            type_name[pair_index]=letter
            type_name="".join(type_name)
            type_votes = filtr_records(data, type=type_name)
            type_name=type_name.replace(".","x")
            list_of_demensions.append(type_votes)
            produce_standard_charts(type_votes, "wyniki "+type_name, type_name)
            
    produce_comparation_charts(list_of_demensions)
    # type_votes = filtr_records(data, type=".NF.")
    # produce_standard_charts(type_votes, "wyniki " + "XNFX", womans_weight, "XNFX")


def produce_for_each_type(data, womans_weight):
    types=["INTJ","INTP","INFP","INFJ","ISFJ","ISFP","ISTP","ISTJ","ENTJ","ENTP","ENFP","ENFJ","ESFJ","ESFP","ESTP","ESTJ"]
    for type_name in types:


        type_votes = filtr_records(data, type=type_name)

        produce_standard_charts(type_votes, "wyniki "+type_name, womans_weight, type_name)



if __name__ == '__main__':

    resuts=load_data("data2.csv")
    # resuts=filtr_records(resuts,Sex.M,"...J","")

    produce_standard_charts(resuts,"wyniki ogólne","ogolne")
    produce_for_each_demension(resuts,)
    produce_standard_charts(filtr_records(resuts, type="INFJ"), "wyniki " + "INFJ", "INFJ")
    # produce_for_each_demension(resuts,womans_weight)
    # produce_for_each_type(resuts,womans_weight)



