from os import name, system
from time import sleep

from world import World, Place
from plant import PoplarTree, OakTree, PineTree
from conditions import Weather, Climate
from stats import StatisticReportGenerator


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
    w.generate_world(95)
    # w.add_plants([PoplarTree, OakTree, PineTree])
    for i in range(1, 6):
        w.places[i].plant = OakTree(w.places[i])
        w.places[i].is_free = False
        w.places[-i].plant = PineTree(w.places[-i])
        w.places[-i].is_free = False
    i = 500
    while i:
        if not w.get_all_plants():
            return 0
        clear()
        w.world_printer.print_forest(w)

        print("Turn number {}".format(i))
        print(StatisticReportGenerator(w).get_avg_parameters())
        print('sun={}, rain={}, wind={}'.format(
            w.climate.active_season.conditions['sun'],
            w.climate.active_season.conditions['rain'],
            w.climate.active_season.conditions['wind'],
        ))
        p1 = w.places[1]
        # if p1.plant is not None:
        #     print("heigh_p1="+str(p1.plant.height))
        #     print("leafs_p1="+str(p1.plant.leafs))

        w.next_turn()
        sleep(0.2)
        i -= 1


def get_climate():
    # Wearher(name, sun_max, sun_min, rain_max, rain_min, wind_max, wind_min)
    summer = Weather('summer', 35, 22, 5, 3, 20, 15)
    winter = Weather('winter', 10, 2, 10, 4, 20, 15)
    climate = Climate('middle_europe', summer, winter)
    return climate


if __name__ == "__main__":
    # test_main()
    main()
