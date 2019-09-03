import random
from typing import List
from mutator import PlantMutator


class Place:
    __slots__ = 'is_free', 'plant', 'world'

    def __init__(self, world):
        self.is_free = True
        self.plant = None
        self.world = world

    def delete_plant(self):
        self.plant = None
        self.is_free = True


class World:
    PLANT_DENSITY_MAP = (True, False)
    PLANT_MUTATOR = PlantMutator()

    def __new__(cls, climate):
        if not hasattr(cls, 'instance'):
            cls.instance = super(World, cls).__new__(cls)
        return cls.instance

    def __init__(self, climate):
        self.places = []
        self.world_printer = WorldPrinter()
        self.climate = climate

    def generate_world(self, size=30):
        for i in range(size):
            self.places.append(Place(self))

    def add_plants(self, plant_types: List):
        for place in self.places:

            if random.choice(self.PLANT_DENSITY_MAP):
                place.plant = random.choice(plant_types)(place)
                place.is_free = False

    def get_all_plants(self):
        plants = []
        for place in self.places:
            if not place.is_free:
                plants.append(place.plant)
        return plants

    def get_near_places(self, place, radius=1) -> List[Place]:
        near_places = []
        place_index = self.places.index(place)
        while radius:
            try:
                near_places.append(self.places[place_index + radius])
            except IndexError:
                pass
            if (place_index - radius) >= 0:
                near_places.append(self.places[place_index - radius])
            radius -= 1
        return near_places

    def next_turn(self):
        self.climate.next_season()
        for place in self.places:
            if not place.is_free:
                place.plant.grow()
                if not place.is_free:
                    place.plant.spread(self.get_near_places(place, place.plant.spread_radius), self.PLANT_MUTATOR)
                    if place.plant.age >= place.plant.die_age:
                        place.delete_plant()


class WorldPrinter:
    MAX_PRINT_HEIGHT = 15
    EMPTY_DELIMITER = ' '

    def _get_trees_level(self, world: World, level=0):
        pos = ''
        if world.places:
            for place in world.places:
                if place.is_free or place.plant.height <= level:
                    pos += '{} '.format(self.EMPTY_DELIMITER)
                else:
                    pos += '{} '.format(place.plant.sign)
        else:
            print("World haven't been generated yet.")
        return pos

    def _get_forest(self, world):
        forest = []
        for row in range(self.MAX_PRINT_HEIGHT):
            forest.append(self._get_trees_level(world, row))
        forest.reverse()
        return forest

    def print_forest(self, world):
        forest = self._get_forest(world)
        for level in forest:
            print(level)


class WorldException(Exception):
    pass
