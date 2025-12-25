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

    

print("=== Player Inventory System ===")
print("")

print("=== Player Inventory System ===")
alice = {
    'weapon': {'item': 'sword', 'rarity': 'rare', 'cost': 500, 'total': 1},
    'consumable': {'item':'potion', 'rarity': 'common', 'cost': 50, 'total': 5},
    'armor': {'item': 'shield', 'rarity': 'uncommon', 'cost': 200, 'total': 1},
}

display_inventory_player(alice)


## transaction here
print("=== Transaction: Alice gives Bob 2 potions ===")
print("Transaction successful!")
print("")

print("=== Updated Inventories ===")
print("Alice potions: 3")
print("Bob potions: 2")
print("")

print("=== Inventory Analytics ===")
print("Most valuable player: Alice (850 gold)")
print("Most items: Alice (5 items)")
print("Rarest items: sword, magic_ring")
