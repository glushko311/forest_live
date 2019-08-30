import abc
import random


class AbstractPlant(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def grow(self):
        pass

    @abc.abstractmethod
    def spread(self, places, mutator):
        pass


class Plant(AbstractPlant):
    __slots__ = 'leafs', 'roots', 'age', 'spread_start_age', 'grow_speed', 'die_age', 'place', 'sign', 'chanse_of_spread', 'variability', 'spread_radius'
    DIE_AGE_CONSTANT = 50
    MIN_GROW_SPEED = 1
    MAX_GROW_SPEED = 10
    SPREAD_RADIUS = 10

    def __init__(self, place, grow_speed=2, spread_start_age=5):
        self.leafs = 1
        self.roots = 1
        self.age = 0
        self.spread_start_age = spread_start_age  # 5
        self.grow_speed = grow_speed  # 2
        self.die_age = int(self.DIE_AGE_CONSTANT / grow_speed)
        self.place = place
        self.sign = "P"
        self.chanse_of_spread = 8
        self.variability = 0.1
        self.spread_radius = self.SPREAD_RADIUS

    def grow(self):
        self.age += 1
        self.leafs += self.grow_speed / 3
        self.roots += self.grow_speed / 3

    def spread(self, places, mutator):
        if self.age > self.spread_start_age:
            places = filter(lambda place: place.is_free, places)
            for place in places:
                if (random.randint(1, self.chanse_of_spread)) == 1:
                    place.is_free = False
                    place.plant = mutator.mutate(self, place)

    def __str__(self):
        return "Plant age={} leafs={} roots={}".format(self.age, self.leafs, self.roots)


class PoplarTree(Plant):
    __slots__ = 'plant_type'
    SPREAD_RADIUS = 1
    MIN_GROW_SPEED = 3
    MAX_GROW_SPEED = 5

    def __init__(self, place, spread_start_age=5, plant_type="poplar_tree"):
        super().__init__(place, spread_start_age)
        self.plant_type = plant_type
        self.grow_speed = 3
        self.spread_start_age = 3
        self.die_age = 20
        self.sign = "T"


class OakTree(Plant):
    __slots__ = 'plant_type'
    SPREAD_RADIUS = 3
    MIN_GROW_SPEED = 1
    MAX_GROW_SPEED = 3

    def __init__(self, place, spread_start_age=10, plant_type="oak_tree"):
        super().__init__(place, spread_start_age)
        self.plant_type = plant_type
        self.grow_speed = 1
        self.spread_start_age = 10
        self.die_age = 40
        self.sign = "O"


class PineTree(Plant):
    __slots__ = 'plant_type'
    SPREAD_RADIUS = 2
    MIN_GROW_SPEED = 2
    MAX_GROW_SPEED = 4

    def __init__(self, place, spread_start_age=5, plant_type="pine_tree"):
        super().__init__(place, spread_start_age)
        self.plant_type = plant_type
        self.grow_speed = 2
        self.spread_start_age = 5
        self.die_age = 20
        self.sign = "A"
