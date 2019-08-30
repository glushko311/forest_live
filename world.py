import random
from typing import List
from .plant import Plant
from .mutator import PlantMutator

class Place:
    __slots__ = 'is_free', 'sun', 'water', 'plant'

    def __init__(self, sun, water):
        self.is_free = True
        self.sun = sun
        self.water = water
        self.plant = None

    def delete_plant(self):
        self.plant = None
        self.is_free = True


class World:
    PLANT_DENSITY_MAP = (True, False)
    PLANT_MUTATOR = PlantMutator()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(World, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.places = []
        self.world_printer = WorldPrinter()

    def generate_world(self, size=30, min_sun=20, max_sun=50, min_water=20, max_water=50):
        delta_sun = max_sun - min_sun
        if delta_sun <= 0:
            raise WorldException("Not correct min or max sun")
        delta_water = max_water - min_water
        if delta_water <= 0:
            raise WorldException("Not correct min or max water")
        delta_sun_per_position = delta_sun / size
        delta_water_per_position = delta_water / size
        for i in range(size):
            self.places.append(Place(int(i * delta_sun_per_position), int(i * delta_water_per_position)))

    def add_plants(self, plant_types: List[Plant]):
        for place in self.places:

            if random.choice(self.PLANT_DENSITY_MAP):
                place.plant = random.choice(plant_types)(place)
                # place.plant = PoplarTree(place)
                place.is_free = False

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
        for place in self.places:
            if not place.is_free:
                place.plant.grow()
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
                if place.is_free or place.plant.leafs <= level:
                    pos += '  {}  '.format(self.EMPTY_DELIMITER)
                else:
                    pos += '  {}  '.format(place.plant.sign)
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
