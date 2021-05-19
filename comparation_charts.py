import os
import typing

import numpy as np
from matplotlib import pyplot as plt

from enums.sex import Sex
from split import split_on_sport_levels, split_on_friends_levels, split_on_realtionship_status
from standard_charts import get_standard_data_for_chart
from tools import filtr_records, get_mean_level, get_sample_numbers


def get_comparation_data_for_chart(persons_list, function_to_split,relationship):
    mans_list = filtr_records(persons_list, sex=Sex.M)
    womens_list = filtr_records(persons_list, sex=Sex.F)
    mans_map = function_to_split(mans_list)
    womans_map = function_to_split(womens_list)
    general_map = function_to_split(persons_list)

    if not (relationship):
        man_mean_level = get_mean_level(mans_map)
        womans_mean_level = get_mean_level(womans_map)
        general_mena_level = get_mean_level(general_map)
    else:
        return (mans_map, womans_map, general_map)

    return (mans_map, womans_map, general_map, man_mean_level, womans_mean_level, general_mena_level)


def plot_comparation_charts(demension_data_map:typing.Dict, chart_title, directory):
    if not os.path.exists("./results/"+directory):
            os.makedirs("./results/"+directory)#create directory if not exists

    for key in demension_data_map.keys():
        plot_comparation_chart(demension_data_map[key],chart_title+": "+key, directory,key)


def plot_div_charts(demension_data_map:typing.Dict, chart_title, directory):
    if not os.path.exists("./results/"+directory):
            os.makedirs("./results/"+directory)#create directory if not exists

    for key in demension_data_map.keys():
        plot_div_chart(demension_data_map[key],key, directory,key)


def plot_div_chart(demension_data_map:typing.Dict, chart_title, directory,chart_type):
    chart_title = "zmiana %% między czasmi przed pandemią i po:%s" % (chart_title)
    max_y=0
    min_y=0
    for key in demension_data_map.keys():
        if demension_data_map[key]>max_y:
            max_y=demension_data_map[key]
        if demension_data_map[key] < min_y:
            min_y=demension_data_map[key]

    x = np.arange(len(demension_data_map.keys()))
    width = 0.4  # the width of the bars
    fig, ax = plt.subplots()
    rect_votes_groups = []
    sign = 1
    retio = 0.5






    rect_votes_group = ax.bar(x - sign * int(retio) * width, demension_data_map.values(), width,
                          label="")
    rect_votes_groups.append(rect_votes_group)

    retio = retio + 0.5
    sign = sign * (-1)
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("%")
    ax.set_title(chart_title)
    ax.set_xticks(x)
    ax.set_xticklabels(demension_data_map.keys(), fontsize=8)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:

            height = rect.get_height()
            cof=0
            if(height<0):
                cof=(min_y/100.0)*5
            ax.annotate("%.2f"%(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height+cof),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=7)

    for rect_votes_group in rect_votes_groups:
        autolabel(rect_votes_group)
    fig.tight_layout()


    axes = plt.gca()
    axes.set_ylim([min_y-(float(-min_y)/100)*20,max_y+(float(max_y)/100)*50])


    plt.savefig("./results/" + directory + "/"+chart_type+".svg")
    plt.close()



def plot_comparation_chart(demension_data_map:typing.Dict, chart_title, directory,chart_type):
    chart_title = "%s" % (chart_title)
    max_y=0
    y_label={"sport": "Średni poziom sportu", "relacja":"% osób w związku","przyjaźń":"Średni poziom przyjaźni"}
    for i in range(0,2):
        for key in demension_data_map.keys():
            if demension_data_map[key][i]>max_y:
                max_y=demension_data_map[key][i]

    x = np.arange(len(demension_data_map.keys()))
    width = 0.4  # the width of the bars
    fig, ax = plt.subplots()
    rect_votes_groups = []
    sign = 1
    retio = 0.5
    reslut_values_list=[[],[]]

    for pair in demension_data_map.values():
        reslut_values_list[0].append(pair[0])
        reslut_values_list[1].append(pair[1])


    for i in range(0,2):
        if i==0:
            label="przed pandemią"
        else:
            label="obecnie"
        rect_votes_group = ax.bar(x - sign * int(retio) * width, reslut_values_list[i], width,
                              label=label)
        rect_votes_groups.append(rect_votes_group)
        retio = retio + 0.5
        sign = sign * (-1)
    retio = retio + 0.5
    sign = sign * (-1)
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(y_label[chart_type])
    ax.set_title(chart_title)
    ax.set_xticks(x)
    ax.set_xticklabels(demension_data_map.keys(), fontsize=8)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate("%.2f"%(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=7)

    for rect_votes_group in rect_votes_groups:
        autolabel(rect_votes_group)
    fig.tight_layout()


    axes = plt.gca()
    axes.set_ylim([0,max_y+(float(max_y)/100)*50])


    plt.savefig("./results/" + directory + "/"+chart_type+".svg")
    plt.close()


def div_between_before_pandemic_and_present(demension_data_map):
    for dyscypline in demension_data_map.keys():
        for key in demension_data_map[dyscypline].keys():
            data=demension_data_map[dyscypline][key]
            demension_data_map[dyscypline][key]=(float(data[1]-data[0])/data[0])*100
    return demension_data_map


def produce_comparation_charts(map_of_demensions:typing.Dict,title,directory):
    if not os.path.exists("./results/" + directory):
        os.makedirs("./results/" + directory)  # create directory if not exists

    demension_data_map={"sport":{},"przyjaźń":{},"relacja":{}}
    for demension_names in map_of_demensions.keys():
        data=map_of_demensions[demension_names]
        sport_data_for_chart = get_standard_data_for_chart(data, split_on_sport_levels)
        friends_data_for_chart = get_standard_data_for_chart(data, split_on_friends_levels)
        womans, mans, general = get_sample_numbers(data)
        raltionship_data = get_standard_data_for_chart(data, split_on_realtionship_status, True)

        demension_data_map["sport"][demension_names]=sport_data_for_chart[5]
        demension_data_map["przyjaźń"][demension_names] =  friends_data_for_chart[5]
        demension_data_map["relacja"][demension_names] =  raltionship_data[2]


    plot_comparation_charts(demension_data_map,"porównanie wymiarów","wymiary/porownanie")
    demension_data_map=div_between_before_pandemic_and_present(demension_data_map)
    plot_div_charts(demension_data_map,title,"wymiary/RoznicaPrzedIPo")
    # plot_womans_mans_vefore_after_chart(sport_data_for_chart, title, directory, "Sport.svg")
    #
    # friends_data_for_chart = get_standard_data_for_chart(data, split_on_friends_levels)
    # plot_womans_mans_vefore_after_chart(friends_data_for_chart, title, directory, "Przyjaznie.svg")
    #
    #
    #
    # plot_relationship_chart(raltionship_data, title, directory, "Zwiazki.svg", friends_data_for_chart, womans, mans,
    #                         general)
