from os import name, system
from time import sleep

from world import World, Place
from plant import PoplarTree, OakTree, PineTree
from conditions import Weather, Climate


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    c = get_climate()
    w = World(c)
    w.generate_world(10)
    w.add_plants([PoplarTree, OakTree, PineTree])
    i = 200
    while i:
        clear()
        w.world_printer.print_forest(w)

        print("Turn number {}".format(i))
        w.next_turn()
        sleep(0.3)
        i -= 1


def get_climate():
    summer = Weather('summer', 35, 22, 4, 2, 5, 1)
    winter = Weather('winter', 10, 2, 10, 6, 8, 4)
    climate = Climate('middle_europe', summer, winter)
    return climate


if __name__ == "__main__":
    # test_main()
    main()
