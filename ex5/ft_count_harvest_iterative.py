def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 1;
    n = range(1, days + 1, 1)
    for i in n:
        print("Day ", i)
    print("Harvest time!")
