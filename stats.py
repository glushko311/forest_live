class StatisticReportGenerator:

    def __init__(self, world):
        self._world = world

    def get_avg_parameters(self):
        plants = self._world.get_all_plants()
        avg_leafs = 0
        avg_height = 0
        avg_age = 0
        for plant in plants:
            avg_leafs += plant.leafs
            avg_height += plant.height
            avg_age += plant.age
        count_plants = len(plants)
        stat_dict = {}
        if count_plants:
            stat_dict = {
                'avg_leafs': avg_leafs / count_plants,
                'avg_height': avg_height / count_plants,
                'avg_age': avg_age / count_plants
            }
        return stat_dict
