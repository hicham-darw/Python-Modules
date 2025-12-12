days = 0

inp = 0

def ft_count_harvest_recursive():
    global inp
    global days

    if (inp == 0):
        days = int(input("Days until harvest: "))
        inp += 1
    if (days < int(inp)):
        print("Harvest time!")
        return ;
    print("Day", inp);
    n = int(inp)
    inp += 1;
    ft_count_harvest_recursive()
