import random
import itertools


class Weather:
    def __init__(self, season_name, max_sun, min_sun, max_rain, min_rain, max_wind, min_wind):
        self.sun = (min_sun, max_sun)
        self.rain = (min_rain, max_rain)
        self.wind = (min_wind, max_wind)
        self.season_name = season_name
        self.conditions = self.get_concreate_weather()

    def get_concreate_weather(self):
        conditions = {
            'sun': random.randint(*self.sun),
            'rain': random.randint(*self.rain),
            'wind': random.randint(*self.wind),
                      }
        return conditions


class Climate:
    def __init__(self, climate_name, *args):
        self.seasons = itertools.cycle([*args])
        self.climate_name = climate_name
        self.active_season = next(self.seasons)

    def next_season(self):
        self.active_season = next(self.seasons)
        return self.active_season

# add to pytest
# if __name__ == "__main__":
#     summer = Weather('summer', 35, 22, 4, 2, 5, 1)
#     winter = Weather('winter', 10, 2, 10, 6, 8, 4)
#     climate = Climate(summer, winter)
#     print(climate.next_season().season_name)
#     print(climate.next_season().season_name)
#     print(climate.next_season().season_name)
#     print(climate.next_season().season_name)
#     print(climate.next_season().season_name)



