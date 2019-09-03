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
    __slots__ = 'leafs', 'height', 'age', 'spread_start_age', 'grow_speed', 'die_age', 'place', 'sign', 'chanse_of_spread', 'variability', 'spread_radius'
    DIE_AGE_CONSTANT = 50
    MIN_GROW_SPEED = 1
    MAX_GROW_SPEED = 10
    SPREAD_RADIUS = 10
    GROW_MATRIX = {
            (0, 0, 0): (0.3, 0.2),
            (2, 0, 0): (-0.5, 0),
            (1, 0, 0): (-0.2, 0),
            (0, 2, 0): (-0.3, -0.3),
            (0, 1, 0): (-0.2, 0),
            (1, 1, 0): (-0.5, 0),
            (2, 1, 0): (-0.6, 0),
            (2, 2, 0): (-0.6, -0.3),
            (0, 0, 1): (0.4, 0.1),
            (0, 0, 2): (0.5, 0),
            (1, 0, 1): (0, 0.2),
            (0, 1, 1): (0, 0),
            (1, 1, 1): (0, 0),
            (1, 2, 1): (-0.2, -0.2),
            (2, 1, 1): (-0.4, 0),
            (1, 0, 2): (0, 0.4),
            (2, 0, 1): (0, 0.2),
            (2, 0, 1): (0, 0.2),
            (2, 0, 2): (0, 0.4),
            (0, 2, 2): (0, 0),
            (0, 1, 2): (0.1, 0.1),
            (0, 2, 1): (0, 0),
        }

    def __init__(self, place, grow_speed=2, spread_start_age=5):
        self.leafs = 1
        self.height = 1
        self.age = 0
        self.spread_start_age = spread_start_age  # 5
        self.grow_speed = grow_speed  # 2
        self.die_age = int(self.DIE_AGE_CONSTANT / grow_speed)
        self.place = place
        self.sign = "P"
        self.chanse_of_spread = 8
        self.variability = 0.2
        self.spread_radius = self.SPREAD_RADIUS

    def grow(self):
        # key (water_cond_coef, wind_cond_coef, sun_cond_coef)
        # value (grow_leafs_speed, grow_height_speed)
        self.age += 1

        conditions = self.place.world.climate.active_season.conditions
        water_cond_coef = self._determine_water_conditions(conditions)
        wind_cond_coef = self._determine_wind_conditions(conditions)
        sun_cond_coef = 1
        key = (water_cond_coef, wind_cond_coef, sun_cond_coef)
        # value (grow_leafs_speed, grow_height_speed)
        if sum(key) >= 5:
            self.place.is_free = True
            self.place.delete_plant()
        else:
            grow_coeff_tuple = self.GROW_MATRIX[key]
            self.leafs += self.grow_speed * grow_coeff_tuple[0]
            self.height += self.grow_speed / 5

        # water_need = self.leafs * self.grow_speed
        # sun_need = self.leafs / self.height
        # if water_need > (conditions['rain'])*2:
        #     self.place.is_free = True
        #     self.place.delete_plant()
        # elif water_need > (conditions['rain']):
        #     self.leafs -= self.grow_speed / 3
        # else:
        #     self.leafs += self.grow_speed / 3
        #     self.height += self.grow_speed / 5

    def _determine_water_conditions(self, conditions):
        water_need = self.leafs * self.grow_speed
        water = conditions['rain']
        if water_need > water*2:
            return 5  # die plant code
        elif water_need > water*1.5:
            return 2  # uncomfortable conditions 2
        elif water_need > (conditions['rain']):
            return 1  # uncomfortable conditions 1
        else:
            return 0  # comfortable conditions

    def _determine_wind_conditions(self, conditions):
        # TODO  constant 50 is strenth(maybee roots) need to implement its for plants
        critical_wind = 50 / (self.leafs * self.height)
        wind = conditions['wind']
        if wind > critical_wind*2:
            return 5
        elif wind > critical_wind*1.5:
            return 2
        elif wind > critical_wind:
            return 1
        else:
            return 0

    def spread(self, places, mutator):
        if self.age > self.spread_start_age:
            places = filter(lambda place: place.is_free, places)
            for place in places:
                if (random.randint(1, self.chanse_of_spread)) == 1:
                    place.is_free = False
                    place.plant = mutator.mutate(self, place)

    def __str__(self):
        return "Plant age={} leafs={}".format(self.age, self.leafs)


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
    MAX_GROW_SPEED = 2

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
        self.spread_start_age = 2
        self.die_age = 50
        self.sign = "A"
