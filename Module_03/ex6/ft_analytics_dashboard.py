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


print("=== Game Analytics Dashboard ===")
print()

dic = {
    'alice': {
        'unique_player': 1,
        'score': 4000,
        'stat': 'active',
        'achievements': ['first_kill', 'level_10', 'boss_slayer', 'master',  'hunter']
        },
    'diana': {
        'unique_player': 1,
        'score': 3200,
        'stat': 'inactive',
        'achievements': None
        },
    'bob': {
        'unique_player': 1,
        'score': 1800,
        'stat': 'inactive',
        'achievements': ['level_10', 'master',  'hunter']
        },
    'charlie': {
        'unique_player': 1,
        'score': 4000,
        'stat': 'active',
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
        'achievements': None
        },
    'hicham': {
        'unique_player': 0,
        'score': 1000,
        'stat': 'inactive',
        'achievements': None
        },
    'john': {
        'unique_player': 0,
        'score': 1100,
        'stat': 'ative',
        'achievements': None
        },
    'spoo': {
        'unique_player': 0,
        'score': 1100,
        'stat': 'active',
        'achievements': None
        }
}
print("=== List Comprehension Examples ===")
print("High scorers (>2000): ", end='')
print(get_high_scorers(dic))
print("Scores doubled: ", end='')
print(scores_doubled(dic))
print("Active players: ", end='')
print(active_players(dic))
print()

print("=== Dict Comprehension Examples ===")
print("Player scores: ", end='')
print(player_scores(dic))
print("Score categories: ", end='')
print(score_categories(dic))
print("achievement counts: ", end='')
print(achievement_counts(dic))
print()

print("=== Set Comprehension Examples ===")
print("Unique players: ", end='')


def get_unique_players(dic):
    res_set = set()
    for key, value in dic.items():
        if (value['unique_player'] == 1):
            res_set.add(key)
    return (res_set)


print(get_unique_players(dic))
# print(" {'alice', 'bob', 'charlie', 'diana'}")
# print("Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}")
# print("Active regions: {'north', 'east', 'central'}")
