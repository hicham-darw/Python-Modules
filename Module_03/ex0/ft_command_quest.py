import sys


def command_quest(argv):
    """
    function take arguments from user and display it to stdout
    """
    print("=== Command Quest ===")
    if len(argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {argv[0]}")
        print(f"Total arguments: {len(argv)}")
        print("")
    elif len(sys.argv) > 1:
        print(f"Program name: {argv[0]}")
        print(f"Arguments received: {len(argv) - 1}")
        i = 1
        while (i < len(argv)):
            print(f"Argument {i}: {argv[i]}")
            i += 1
        print(f"Total arguments: {len(argv)}")
        print("")


command_quest(sys.argv)
