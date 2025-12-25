def display_inventory_player(alice):
    inv_value = 0
    item_count = 0
    for key, value in alice.items():
        print(f"{value['item']} ({key}, {value['rarity']}): {value['total']}x @ {value['cost']} gold each = {value['total'] * value['cost']} gold")
        inv_value += value['cost'] * value['total']
        item_count += value['total']
    print("")
    print(f"Inventory value: {inv_value} gold")
    print(f"Item count: {item_count} items")
    print("Categories: ", end="")
    for key, value in alice.items():
        print(f"{key}({value['total']})", end="")
        if (key != 'armor'):
            print(', ', end="")
    print("")
    print("")


def transaction_potions(player1, player2, potions):
    if potions < 0:
        return
    for key, value in player1.items():
        if (key == 'consumable'):
            total_item = value['total']
            if (total_item < potions):
                print("Transaction rejected!")
                return
            value['total'] -= potions
    for key, value in player2.items():
        if (key == 'consumable'):
            value['total'] += potions
            print("Transaction successful!")
            print("")
            print("=== Updated Inventories ===")
            print(f"Alice potions: {alice['consumable']['total']}")
            print(f"Bob potions: {bob['consumable']['total']}")
            print("")
            return


def inventory_analytics(player):
    total = 0
    for key, value in alice.items():
        total += (value['cost'] * value['total'])
    print(f"Most valuable player: Alice ({total} gold)")
    total = 0
    for key, value in alice.items():
        total += value['total']
    print(f"Most items: Alice ({total} items)")


def get_rarest_item(player, rare_list):
    for key, value in player.items():
        if value['rarity'] == 'rare':
            rare_list.append(value['item'])
    return rare_list


alice = {
    'weapon': {'item': 'sword',
               'rarity': 'rare',
               'cost': 500,
               'total': 1
               },
    'consumable': {'item': 'potion',
                   'rarity': 'common',
                   'cost': 50,
                   'total': 5
                   },
    'armor': {'item': 'shield',
              'rarity': 'uncommon',
              'cost': 200,
              'total': 1
              },
}

bob = {
    'weapon': {'item': 'magic_ring',
               'rarity': 'rare',
               'cost': 1000,
               'total': 1
               },
    'consumable': {'item': 'potion',
                   'rarity': 'common',
                   'cost': 50,
                   'total': 0
                   },
    'armor': {'item': 'shield',
              'rarity': 'uncommon',
              'cost': 200,
              'total': 1}
}

print("=== Player Inventory System ===")
print("")

# inventory of alice
print("=== Alice's Inventory ===")
display_inventory_player(alice)

# transaction here alice and bob
print("=== Transaction: Alice gives Bob 2 potions ===")
transaction_potions(alice, bob, 2)

print("=== Inventory Analytics ===")
inventory_analytics(alice)

# displaye rarest item
rare_list = []
rare_list = get_rarest_item(alice, rare_list)
rare_list = get_rarest_item(bob, rare_list)
print("Rarest items: ", end="")
i = 0
while (i < len(rare_list)):
    if (i == len(rare_list) - 1):
        print(f"{rare_list[i]}")
    else:
        print(f"{rare_list[i]}, ", end="")
    i += 1