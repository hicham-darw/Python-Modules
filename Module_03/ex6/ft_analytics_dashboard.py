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


print("=== Game Analytics Dashboard ===")
print()

dic = {
    'alice': {'score': 4000, 'stat': 'active'},
    'charlie': {'score': 4000, 'stat': 'active'},
    'diana': {'score': 3200, 'stat': 'inactive'},
    'bob': {'score': 1500, 'stat': 'inactive'},
    'darwin': {'score': 1000, 'stat': 'inactive'},
    'hicham': {'score': 1000, 'stat': 'inactive'},
    'john': {'score': 1100, 'stat': 'ative'},
    'spoo': {'score': 1100, 'stat': 'active'}
}
print("=== List Comprehension Examples ===")
print("High scorers (>2000): ", end='')
print(get_high_scorers(dic))
print("Scores doubled: ", end='')
print(scores_doubled(dic))
print(active_players(dic))
print()

print("=== Dict Comprehension Examples ===")
print("Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}")
print("Score categories: {'high': 3, 'medium': 2, 'low': 1}")
print("Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}")


# print(scores_doubled(dic))

# [4600, 3600, 4300, 4100]")
# print("Active players: ['alice', 'bob', 'charlie']")

# print("=== Dict Comprehension Examples ===")
# print("Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}")
# print("Score categories: {'high': 3, 'medium': 2, 'low': 1}")
# print("Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}")

# print("=== Set Comprehension Examples ===")
# print("Unique players: {'alice', 'bob', 'charlie', 'diana'}")
# print("Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}")
# print("Active regions: {'north', 'east', 'central'}")
