import os
import typing

import numpy as np
from matplotlib import pyplot as plt

from enums.sex import Sex

from split import split_on_sport_levels, split_on_friends_levels, split_on_realtionship_status
from tools import filtr_records, get_sample_numbers, get_max_y_from_relation, get_sum_of_votes_from_map, \
    get_max_y_from_mean, get_max_y, get_mean_level, convert_to_procent


def get_standard_data_for_chart(persons_list,function_to_split,relationship=False):
    mans_list = filtr_records(persons_list, sex=Sex.M)
    womens_list = filtr_records(persons_list, sex=Sex.F)
    mans_map = function_to_split(mans_list)
    womans_map = function_to_split(womens_list)
    general_map=function_to_split(persons_list)

    if not(relationship):
        man_mean_level=get_mean_level(mans_map)
        womans_mean_level=get_mean_level(womans_map)
        general_mena_level=get_mean_level(general_map)
    else:
        return (mans_map, womans_map, general_map)

    return (mans_map,womans_map,general_map,man_mean_level,womans_mean_level,general_mena_level)


def produce_standard_charts(data,title,directory):


    if not os.path.exists("./results/"+directory):
            os.makedirs("./results/"+directory)#create directory if not exists

    sport_data_for_chart=get_standard_data_for_chart(data,split_on_sport_levels)
    plot_womans_mans_vefore_after_chart(sport_data_for_chart, title, directory,  "Sport.svg")

    friends_data_for_chart = get_standard_data_for_chart(data, split_on_friends_levels)
    plot_womans_mans_vefore_after_chart(friends_data_for_chart, title, directory,"Przyjaznie.svg")

    womans,mans,general=get_sample_numbers(data)
    raltionship_data = get_standard_data_for_chart(data, split_on_realtionship_status,True)

    plot_relationship_chart(raltionship_data, title, directory,"Zwiazki.svg",friends_data_for_chart,womans,mans,general)

#
def plot_relationship_chart(votes: typing.Tuple[typing.Dict], chart_title, directory, fileName,frends_votes,womans,mans,general):
    """
    votes is tuple. [0]=mans [1]=womans [2]=all
    :rtype:
    """
    is_chart_after = 0
    chart_title = "%s (M%d|F%d|C%d)" % (
    chart_title, womans,mans,general)


    max_y = get_max_y_from_relation(votes)
    x = np.arange(2)
    width = 0.2  # the width of the bars
    fig, ax = plt.subplots()
    rect_votes_groups = []
    sign = 1
    retio = 0.5
    votes_groups_names = ["mężczyźni", "kobiety", "wszyscy"]
    for index, votes_key_group in enumerate(votes_groups_names):
        rect_votes_group = ax.bar(x - sign * int(retio) * width, votes[index], width,
                                  label=votes_key_group)
        rect_votes_groups.append(rect_votes_group)
        retio = retio + 0.5
        sign = sign * (-1)
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("")
    ax.set_title(chart_title)
    ax.set_xticks(x)
    ax.set_xticklabels(["Przed pandemią", "Obecnie"], fontsize=8)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate("%.2f" % (height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=7)

    for rect_votes_group in rect_votes_groups:
        autolabel(rect_votes_group)
    fig.tight_layout()

    axes = plt.gca()
    axes.set_ylim([0, max_y + 0.5])
    plt.savefig("./results/" + directory + "/" + "Relacja" + fileName)
    plt.close()


def plot_womans_mans_vefore_after_chart(votes:typing.Tuple[typing.Dict], chart_title, directory, fileName):
    """
    votes is tuple. [0]=mans [1]=womans [2]=all
    :rtype:
    """
    is_chart_after=0
    #before

    plot_woman_man_mean_chart(chart_title, directory, fileName, votes)

    plot_woman_man_chart(chart_title, directory, fileName, 0, votes)
    plot_woman_man_chart(chart_title, directory, fileName, 1, votes)


def plot_woman_man_mean_chart(chart_title, directory, fileName, votes):
    chart_title = "%s (M%d|F%d|C%d)" % (
    chart_title, get_sum_of_votes_from_map(votes[0][0]), get_sum_of_votes_from_map(votes[1][0]), get_sum_of_votes_from_map(votes[2][0]))

    datas_before=[votes[3][0],votes[4][0],votes[5][0]]
    datas_after=[votes[3][1],votes[4][1],votes[5][1]]

    votes=list(zip(datas_before,datas_after))
    max_y=get_max_y_from_mean([datas_before,datas_after])
    x = np.arange(2)
    width = 0.2  # the width of the bars
    fig, ax = plt.subplots()
    rect_votes_groups = []
    sign = 1
    retio = 0.5
    votes_groups_names = ["mężczyźni", "kobiety", "wszyscy"]
    for index, votes_key_group in enumerate(votes_groups_names):
        rect_votes_group = ax.bar(x - sign * int(retio) * width, votes[index], width,
                                  label=votes_key_group)
        rect_votes_groups.append(rect_votes_group)
        retio = retio + 0.5
        sign = sign * (-1)
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("")
    ax.set_title(chart_title)
    ax.set_xticks(x)
    ax.set_xticklabels(["Przed pandemią","Obecnie"], fontsize=8)
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
    axes.set_ylim([0,max_y+3])
    plt.savefig("./results/" + directory + "/"+"Średnie" + fileName)
    plt.close()


def plot_woman_man_chart(chart_title, directory, fileName, is_chart_after, votes):
    chart_title = "%s (M%d|F%d|C%d)" % (
    chart_title, get_sum_of_votes_from_map(votes[0][is_chart_after]), get_sum_of_votes_from_map(votes[1][is_chart_after]), get_sum_of_votes_from_map(votes[2][is_chart_after]))

    convert_to_procent(votes[0][is_chart_after], get_sum_of_votes_from_map(votes[0][is_chart_after]))
    convert_to_procent(votes[1][is_chart_after], get_sum_of_votes_from_map(votes[1][is_chart_after]))
    convert_to_procent(votes[2][is_chart_after], get_sum_of_votes_from_map(votes[2][is_chart_after]))

    y_max=get_max_y(votes,is_chart_after)
    x = np.arange(len(votes[2][is_chart_after].keys()))
    width = 0.2  # the width of the bars
    fig, ax = plt.subplots()
    rect_votes_groups = []
    sign = 1
    retio = 0.5
    votes_groups_names = ["mężczyźni", "kobiety", "wszyscy"]
    for index, votes_key_group in enumerate(votes_groups_names):
        rect_votes_group = ax.bar(x - sign * int(retio) * width, votes[index][is_chart_after].values(), width,
                                  label=votes_key_group)
        rect_votes_groups.append(rect_votes_group)
        retio = retio + 0.5
        sign = sign * (-1)
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("%")
    ax.set_title(chart_title)
    ax.set_xticks(x)
    ax.set_xticklabels(votes[2][is_chart_after].keys(), fontsize=8)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=7)

    for rect_votes_group in rect_votes_groups:
        autolabel(rect_votes_group)
    fig.tight_layout()
    before_after="przedPandemia"
    if(is_chart_after==1):
        before_after = "obecnie"
    axes = plt.gca()
    axes.set_ylim([0,y_max+15])
    plt.savefig("./results/" + directory + "/"+before_after + fileName)
    plt.close()