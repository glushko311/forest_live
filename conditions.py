import random
import itertools


class Weather:
    def __init__(self, season_name, max_sun, min_sun, max_rain, min_rain, max_wind, min_wind):
        self.sun = max_sun, min_sun
        self.rain = max_rain, min_rain
        self.wind = max_wind, min_wind
        self.season_name = season_name

    def get_concreate_weather(self):
        conditions = {
            'sun': random.randint(self.sun),
            'rain': random.randint(self.rain),
            'wind': random.randint(self.wind),
                      }
        return conditions


class Climate:
    def __init__(self, climate_name, *args):
        self.seasons = itertools.cycle([*args])
        self.climate_name = climate_name

    def next_season(self):
        return next(self.seasons)


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



