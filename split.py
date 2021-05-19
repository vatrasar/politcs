import typing

from record import Record


def split_on_sport_levels(list_to_split:typing.List[Record]):
    sport_level_map_before={}
    sport_level_map_after={}
    for i in range(0,6):
        sport_level_map_before[i]=0
        sport_level_map_after[i]=0

    for person in list_to_split:
        sport_level_map_before[person.before_epidemic.sport_level]=sport_level_map_before[person.before_epidemic.sport_level]+1
        sport_level_map_after[person.after_epidemic.sport_level]=sport_level_map_after[person.after_epidemic.sport_level]+1



    return (sport_level_map_before,sport_level_map_after)

def split_on_friends_levels(list_to_split:typing.List[Record]):
    friends_level_map_before={}
    friends_level_map_after={}
    for i in range(0,6):
        friends_level_map_before[i]=0
        friends_level_map_after[i]=0

    for person in list_to_split:
        friends_level_map_before[person.before_epidemic.friends_level]=friends_level_map_before[person.before_epidemic.friends_level]+1
        friends_level_map_after[person.after_epidemic.friends_level]=friends_level_map_after[person.after_epidemic.friends_level]+1



    return (friends_level_map_before,friends_level_map_after)


def split_on_realtionship_status(list_to_split:typing.List[Record]):
    in_relationship_before=0
    in_relationship_after=0


    for person in list_to_split:
        if person.before_epidemic.is_in_realtionship:
            in_relationship_before=in_relationship_before+1
        if person.after_epidemic.is_in_realtionship:
            in_relationship_after = in_relationship_after+ 1


    return (in_relationship_before/float(len(list_to_split)),in_relationship_after/float(len(list_to_split)))


