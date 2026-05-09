import pandas as pd
import yaml
import itertools
import sys

def load_season_calendar(file_path):
    df = pd.read_csv(file_path, delimiter=",")
    return dict(zip(df[df.columns[1]], df[df.columns[0]]))

def load_raster(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        raw_raster = yaml.safe_load(file)

    raster = {}
    for number, match_days in raw_raster.items():
        match_day_set = set(map(int, match_days.split(",")))
        raster[int(number)] = match_day_set  

    return raster

def validate_data(season_calendar, raster, team_name):
    num_match_days_calendar = len(season_calendar)
    num_match_days_raster = len(set(itertools.chain.from_iterable(raster.values())))

    if num_match_days_calendar != num_match_days_raster:
        print(f"\n🚨 Fehler für {team_name}: Anzahl der Spieltage stimmt nicht überein!")
        print(f"  → Saisonkalender: {num_match_days_calendar} Spieltage, Raster: {num_match_days_raster} Spieltage.")
        sys.exit(1)

def find_combinations(season_calendar1, raster1, season_calendar2, raster2, results=3, fixed_number1=None, fixed_number2=None, mode="best"):
    possible_numbers1 = {fixed_number1} if fixed_number1 else set(raster1.keys())
    possible_numbers2 = {fixed_number2} if fixed_number2 else set(raster2.keys())

    combinations = []

    for number1, number2 in itertools.product(possible_numbers1, possible_numbers2):
        shared_home_games = 0
        common_weekends = []

        for match_day, weekend in season_calendar1.items():
            if match_day in raster1.get(number1, set()):
                for match_day2, weekend2 in season_calendar2.items():
                    if weekend == weekend2 and match_day2 in raster2.get(number2, set()):
                        shared_home_games += 1
                        common_weekends.append(weekend)

        combinations.append(((number1, number2), shared_home_games, common_weekends))

    reverse_sort = (mode == "best")
    combinations.sort(key=lambda x: x[1], reverse=reverse_sort)
    return combinations[:results]