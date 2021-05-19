from enums.sex import Sex
import re

def get_sum_of_votes_from_map(my_map):
    sum=0
    for key in my_map.keys():
        sum=sum+my_map[key]
    return sum
def get_max_y(votes,is_chart_after):
    max=0
    for i in range(0,3):
       for key in votes[i][is_chart_after].keys():
           if votes[i][is_chart_after][key]>max:
               max=votes[i][is_chart_after][key]

    return max


def get_max_y_from_mean(votes):
    max=0
    for i in range(0,2):
       for mean_number in votes[i]:
           if mean_number>max:
               max=mean_number

    return max

def get_max_y_from_relation(votes):
    max = 0
    for i in range(0, 3):
        for k in range(0,2):
            if votes[i][k]>max:
                max=votes[i][k]

    return max


def get_sample_numbers(data):
    mans_list = filtr_records(data, sex=Sex.M)
    womens_list = filtr_records(data, sex=Sex.F)

    return (len(mans_list),len(womens_list),len(data))

def filtr_records(record_list:list,sex=Sex.ALL,type="....")->list:
    """
    :type str if you want for example all J types give ...J, if all NT type give .NT.
    :rtype: object
    """
    result=list(filter(lambda record:sex==Sex.ALL or record.sex==sex, record_list))

    result=list(filter(lambda record:re.match(type,record.type_name), result))


    return result

def get_mean_level(my_map):
    sum_befor_pandemic=0
    sum_present=0
    for key in my_map[0].keys():
        sum_befor_pandemic=my_map[0][key]*key+sum_befor_pandemic

    for key in my_map[1].keys():
        sum_present = my_map[1][key]*key + sum_present

    persons_sum=get_sum_of_votes_from_map(my_map[0])
    if persons_sum==0:
        return (0,0)
    return (float(sum_befor_pandemic)/persons_sum,float(sum_present)/persons_sum)



def convert_to_procent(in_map:map,number_of_voters):
    for key in in_map.keys():
        if number_of_voters==0:
            in_map[key] =0
        else:
            in_map[key]=round((in_map[key]/float(number_of_voters))*100)