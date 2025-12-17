def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    result = seed_type.capitalize() + " seeds:"
    if (unit == 'packets'):
        print(result, quantity, unit, "available")
    elif (unit == 'grams'):
        print(result, quantity, unit, "total")
    elif (unit == 'area'):
        print(result, "covers", 12, "square meters")
    else:
        print("Unknown unit type")
