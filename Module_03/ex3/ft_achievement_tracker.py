def create_player_achievements(name, set):
    """
    this function print msg of creation with player name
    and return set
    """
    print(f"Player {name} achievements: {set}")
    return set


def achievement_analytics(player1, player2, player3):
    """
    this function take 3 set data structure of player achievements
    print more info about players and achievements of players
    return None
    """
    unique_achievements = player1 | player2 | player3
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print("")
    rare1 = player1.difference(player2, player3)
    rare2 = player2.difference(player1, player3)
    rare3 = player3.difference(player1, player2)
    result = rare1 | rare2 | rare3
    print("Common to all players: ", end="")
    print(f"{unique_achievements.intersection(player1, player2, player3)}")
    print(f"Rare achievements (1 player): {result}")
    print("")


def head_to_head(player1, player2):
    """
    this function compare between two sets
    alice and bob and gets common and unique achievements of both
    args:
        set1, set2
    return:
        None
    """
    print(f"Alice vs Bob common: {player1.intersection(player2)}")
    print(f"Alice unique: {player1.difference(player2)}")
    print(f"Bob unique: {player2.difference(player1)}")


print("=== Achievement Tracker System ===")
print("")
alice = create_player_achievements('alice',
                                   {'first_kill',
                                    'level_10',
                                    'treasure_hunter',
                                    'speed_demon'})
bob = create_player_achievements('bob',
                                 {'first_kill',
                                  'level_10',
                                  'boss_slayer',
                                  'collector'})
charlie = create_player_achievements('charlie',
                                     {'level_10',
                                      'treasure_hunter',
                                      'boss_slayer',
                                      'speed_demon',
                                      'perfectionist'})
print("")
print("=== Achievement Analytics ===")
achievement_analytics(alice, bob, charlie)

# head to head common and unique achievements of both
head_to_head(alice, bob)
