import abc
import copy
import random

from plant import Plant


class AbstractMutator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def mutate(self, entity, place):
        pass


class PlantMutator(AbstractMutator):
    """
    Pattern prototype
    """
    def mutate(self, entity: Plant, place):
        new_plant = copy.copy(entity)
        new_plant.age = 1
        new_plant.leafs = 1
        new_plant.roots = 1
        new_plant.grow_speed += (-1) ** (random.randint(1, 2)) * entity.grow_speed * entity.variability
        new_plant.die_age += (-1) ** (random.randint(1, 2)) * entity.die_age * entity.variability
        new_plant.place = place
        return new_plant