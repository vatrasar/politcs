def get_comparation_data_for_chart(data, split_on_sport_levels):
    pass


def produce_comparation_charts(list_of_demensions,title,directory):
    if not os.path.exists("./results/" + directory):
        os.makedirs("./results/" + directory)  # create directory if not exists

    sport_data_for_chart = get_comparation_data_for_chart(data, split_on_sport_levels)
    plot_womans_mans_vefore_after_chart(sport_data_for_chart, title, directory, "Sport.svg")

    friends_data_for_chart = get_standard_data_for_chart(data, split_on_friends_levels)
    plot_womans_mans_vefore_after_chart(friends_data_for_chart, title, directory, "Przyjaznie.svg")

    womans, mans, general = get_sample_numbers(data)
    raltionship_data = get_standard_data_for_chart(data, split_on_realtionship_status, True)

    plot_relationship_chart(raltionship_data, title, directory, "Zwiazki.svg", friends_data_for_chart, womans, mans,
                            general)
