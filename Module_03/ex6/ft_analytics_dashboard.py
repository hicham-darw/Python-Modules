# lists ----------------------
def get_high_scorers(dic):
    res = []
    for key, value in dic.items():
        if value['score'] > 2000:
            res.append(key)
    return res


def scores_doubled(dic):
    lst = []
    doubled = []
    for key, value in dic.items():
        if value['score'] in lst:
            doubled.append(value['score'])
        else:
            lst.append(value['score'])
    return doubled


def active_players(dic):
    lst = []
    for key, value in dic.items():
        if (value['stat'] == 'active'):
            lst.append(key)
    return (lst)


# dictionaries -----------------------
def player_scores(dic):
    res_dic = {}
    for key, value in dic.items():
        res_dic[key] = value['score']
    return res_dic


def score_categories(dic):
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
    res_dic = {}
    for key, value in dic.items():
        if (value['achievements'] is not None):
            res_dic[key] = len(value['achievements'])
    return res_dic


# sets -----------------------------------
def get_unique_players(dic):
    res_set = set()
    for key, value in dic.items():
        if (value['unique_player'] == 1):
            res_set.add(key)
    return (res_set)


def get_unique_achievements(dic):
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
    s = set()
    for value in dic.values():
        if value['stat'] == 'active':
            if (value['region'] not in s):
                s.add(value['region'])
    return s


# combined analysis
def total_players(dic):
    t_player = 0
    for key in dic.keys():
        t_player += 1
    return t_player


def total_unique_achievements(dic):
    s = set()
    for value in dic.values():
        if (value['achievements'] is not None):
            for d in value['achievements']:
                if (d not in s):
                    s.add(d)
    return (len(s))


def get_average_score(dic):
    total_score = 0
    div = 0
    for value in dic.values():
        total_score += value['score']
        div += 1
    return (total_score / div)


def top_performer_player(dic):
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
        },
    'hicham': {
        'unique_player': 0,
        'score': 1000,
        'stat': 'inactive',
        'region': 'north',
        'achievements': None
        },
    'john': {
        'unique_player': 0,
        'score': 1100,
        'stat': 'ative',
        'region': 'central',
        'achievements': None
        },
    'spoo': {
        'unique_player': 0,
        'score': 1100,
        'stat': 'active',
        'region': 'east',
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
