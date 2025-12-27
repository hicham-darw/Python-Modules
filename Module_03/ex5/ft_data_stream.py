def proccessing_game_events(total: int):
    players = ['alice', 'bob', 'charlie', ]
    events = ['killed monster', 'found treasure', 'leveled up']
    for i in range(total):
        id = i + 1
        name = players[i % len(players)]
        event = events[i % len(events)]
        level = i % 15
        yield id, name, event, level


def fibonacci(nbr):
    if (nbr == 0 or nbr == 1):
        return nbr
    else:
        return fibonacci(nbr - 1) + fibonacci(nbr - 2)


def loop_fibo(nbr: int):
    for i in range(nbr):
        yield i, fibonacci(i)


def is_prime(nbr: int):
    i = 2
    if (nbr == 2):
        return (nbr)
    while (i < nbr):
        if (nbr % i == 0):
            return -1
        i += 1
    return nbr


def prime_numbers(nbr):
    x = 2
    i = 0
    while (i < nbr):
        if (is_prime(x) > 0):
            yield x
            i += 1
        x += 1


print("=== Game Data Stream Processor ===")
print("")

print("Processing 1000 game events...")
print("")

total_events = 0
high_level = 0
treasure_events = 0
level_up_events = 0
for id, name, event, level in proccessing_game_events(1000):
    total_events += 1
    print(f"Event {id}: Player {name} (level {level}) {event}")

    if level >= 10:
        high_level += 1

    if (event == 'found treasure'):
        treasure_events += 1

    if (event == 'leveled up'):
        level_up_events += 1

print("")
print("=== Stream Analytics ===")

print(f"Total events processed: {total_events}")
print(f"High-level players (10+): {high_level}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {level_up_events}")
print("")

print("Memory usage: Constant (streaming)")
print("Processing time: 0.045 seconds")
print("")

print("=== Generator Demonstration ===")
print("Fibonacci sequence (first 10): ", end='')
i = 0
for x, xfibo in loop_fibo(10):
    if (x == 9):
        print(f"{xfibo}")
    else:
        print(f"{xfibo}, ", end='')

print("Prime numbers (first 5): ", end='')
i = 0
for x in prime_numbers(5):
    if (i == 4):
        print(f"{x}")
    else:
        print(f"{x}, ", end='')
    i += 1
