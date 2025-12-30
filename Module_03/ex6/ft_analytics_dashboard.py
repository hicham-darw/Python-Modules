# lists ----------------------
def get_high_scorers(dic):
    """
    this function take a dictionary and get high scores
    greather than 2000 in list
    args:
        dictionary:
    return:
        list []
    """
    return [k for k, v in dic.items() if v['score'] > 2000]


def scores_doubled(dic):
    """
    this function get doubled scores
    args:
        dictionary
    returns:
        list []
    """
    lst = [value['score'] for value in dic.values()]
    return [score for score in set(lst) if lst.count(score) > 1]


def active_players(dic):
    """
        this function display active players
        args:
            dictionary
        returns:
            list []
    """
    return [k for k, v in dic.items() if v['stat'] == 'active']


# dictionaries -----------------------
def player_scores(dic):
    """
    this function return scores players key , value (name: score)
        args:
            dict
        returns:
            dict
    """
    return {k: v['score'] for k, v in dic.items()}


def score_categories(dic):
    """
    this function return a dictionary has 3 keys
    high: ?, medium: ?, low: ?
    values
        total players high scores
        total players medium scores
        total players low score
    args:
        dict
    returns:
        dict
    """
    res_dic = {}
    max_score = 0
    min_score = 0
    mid_score = 0
    for key, value in dic.items():
        if (value['score'] > 3000):
            max_score += 1
        elif (value['score'] < 1100):
            min_score += 1
        else:
            mid_score += 1
    res_dic['high'] = max_score
    res_dic['medium'] = mid_score
    res_dic['low'] = min_score
    return res_dic


def achievement_counts(dic):
    """
    this function return total achievements of players
    args:
        dict
    returns:
        dict key, value (name, total_achievements)
    """
    res_dic = {k: len(v['achievements']) for k, v in dic.items()
               if v['achievements'] is not None}
    return res_dic


# sets -----------------------------------
def get_unique_players(dic):
    """
    this function return unique players in data set
    args:
        dict
    returns:
        set
    """
    res_set = {k for k, v in dic.items() if v['unique_player'] == 1}
    return res_set


def get_unique_achievements(dic):
    """
    this function returns unique achievements in set data structure
    Args:
        dict
    returns:
        set
    """
    res_set = set()
    achievs = [
        'level_10',
        'leveled_up',
        'boss_slayer',
        'missionary',
        'first kill',
        'master',
        'hackerman',
        'hunter']
    i = 0
    while (i < len(achievs)):
        counter = 0
        for d in dic.values():
            if (d['achievements'] is not None):
                for x in d['achievements']:
                    if (x == achievs[i]):
                        counter += 1
        if (counter == 1):
            res_set.add(achievs[i])
        i += 1
    return res_set


def get_active_regions(dic):
    """
    this function return active regions
    args:
        dict
    returns:
        set (active regions)
    """
    return {v['region'] for v in dic.values() if v['stat'] == 'active'}


# combined analysis
def total_players(dic):
    """
    this function return total players
    Args:
        dict
    returns:
        int total_players
    """
    t_player = 0
    for key in dic.keys():
        t_player += 1
    return t_player


def total_unique_achievements(dic):
    """
    this function total unique achievements
    args:
        dict
    returns:
        set (unique achievements)
    """
    s = set()
    for value in dic.values():
        if (value['achievements'] is not None):
            for d in value['achievements']:
                if (d not in s):
                    s.add(d)
    return len(s)


def get_average_score(dic):
    """
    this function return average of score players
    args:
        dict
    returns:
        int, float average
    """
    total_score = 0
    div = 0
    for value in dic.values():
        total_score += value['score']
        div += 1
    return (total_score / div)


def top_performer_player(dic):
    """
    this function returns performer player by score and achievements
    args:
        dict
    returns:
        str (xxxx points, xx achievements)
    """
    top = 0
    name = ""
    points = 0
    achievements = 0
    for key, value in dic.items():
        if value['achievements'] is not None:
            if (value['score'] > top):
                achievements = len(value['achievements'])
                name = key
                points = value['score']
    return f"{name} ({points} points, {achievements} achievements)"


dic = {
    'alice': {
        'unique_player': 1,
        'score': 4000,
        'stat': 'active',
        'region': 'north',
        'achievements': [
            'first kill',
            'level_10',
            'boss_slayer',
            'master',
            'hunter']
        },
    'diana': {
        'unique_player': 1,
        'score': 3200,
        'stat': 'inactive',
        'region': 'west',
        'achievements': None
        },
    'bob': {
        'unique_player': 1,
        'score': 1800,
        'stat': 'inactive',
        'region': 'west',
        'achievements': ['leveled_up', 'master',  'hunter']
        },
    'charlie': {
        'unique_player': 1,
        'score': 4000,
        'stat': 'active',
        'region': 'central',
        'achievements': [
            'level_10',
            'boss_slayer',
            'master',
            'hunter',
            'first kill',
            'missionary',
            'hackerman']
        },
    'darwin': {
        'unique_player': 0,
        'score': 1000,
        'stat': 'inactive',
        'region': 'west',
        'achievements': None
        }
}


print("=== Game Analytics Dashboard ===")
print()
# list Comprehension Examples -------
print("=== List Comprehension Examples ===")
print("High scorers (>2000): ", end='')
print(get_high_scorers(dic))
print("Scores doubled: ", end='')
print(scores_doubled(dic))
print("Active players: ", end='')
print(active_players(dic))
print()
# dict Comrehensions examples
print("=== Dict Comprehension Examples ===")
print("Player scores: ", end='')
print(player_scores(dic))
print("Score categories: ", end='')
print(score_categories(dic))
print("achievement counts: ", end='')
print(achievement_counts(dic))
print()
# set Comprehensions examples
print("=== Set Comprehension Examples ===")
print("Unique players: ", end='')
print(get_unique_players(dic))
print("Unique achievements: ", end='')
print(get_unique_achievements(dic))
print("Active regions: ", end='')
print(get_active_regions(dic))
print()
# combined analysis
print("=== Combined Analysis ===")
print("total players: ", end='')
print(total_players(dic))
print("Total unique achievements: ", end='')
print(total_unique_achievements(dic))
print("Average score: ", end='')
print(get_average_score(dic))
print("Top performer: ", end='')
print(top_performer_player(dic))
