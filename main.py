from os import name, system
from time import sleep

from plants.world import World, Place
from plants.plant import PoplarTree, OakTree, PineTree


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    w = World()
    w.generate_world(10)
    w.add_plants([PoplarTree, OakTree, PineTree])
    # w.places[4].plant = PoplarTree(w.places[4])
    # w.places[4].is_free = False
    i = 200
    while i:
        clear()
        w.world_printer.print_forest(w)

        print("Turn number {}".format(i))
        w.next_turn()
        sleep(0.3)
        i -= 1


if __name__ == "__main__":
    # test_main()
    main()
