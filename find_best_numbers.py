import argparse
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

def find_best_combinations(season_calendar1, raster1, season_calendar2, raster2, results=3, fixed_number1=None, fixed_number2=None):
    possible_numbers1 = {fixed_number1} if fixed_number1 else set(raster1.keys())
    possible_numbers2 = {fixed_number2} if fixed_number2 else set(raster2.keys())

    best_combinations = []

    for number1, number2 in itertools.product(possible_numbers1, possible_numbers2):
        shared_home_games = 0
        common_weekends = []

        for match_day, weekend in season_calendar1.items():
            if match_day in raster1.get(number1, set()):
                for match_day2, weekend2 in season_calendar2.items():
                    if weekend == weekend2 and match_day2 in raster2.get(number2, set()):
                        shared_home_games += 1
                        common_weekends.append(weekend)

        best_combinations.append(((number1, number2), shared_home_games, common_weekends))

    best_combinations.sort(key=lambda x: x[1], reverse=True)
    return best_combinations[:results]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Finde die besten Kennziffern für gemeinsame Heimspieltage.")

    parser.add_argument("--seasonCalendarTeam1", required=True, help="CSV-Datei mit Saisonkalender der 1. Mannschaft")
    parser.add_argument("--rasterTeam1", required=True, help="YAML-Datei mit Raster der 1. Mannschaft")
    parser.add_argument("--fixedNumberTeam1", type=int, help="Feste Kennziffer für 1. Mannschaft", default=None)

    parser.add_argument("--seasonCalendarTeam2", required=True, help="CSV-Datei mit Saisonkalender der 2. Mannschaft")
    parser.add_argument("--rasterTeam2", required=True, help="YAML-Datei mit Raster der 2. Mannschaft")
    parser.add_argument("--fixedNumberTeam2", type=int, help="Feste Kennziffer für 2. Mannschaft", default=None)

    parser.add_argument("--results", type=int, help="Anzahl der auszugebenden Ergebnisse", default=3)

    args = parser.parse_args()

    seasonCalendarTeam1 = load_season_calendar(args.seasonCalendarTeam1)
    rasterTeam1 = load_raster(args.rasterTeam1)
    seasonCalendarTeam2 = load_season_calendar(args.seasonCalendarTeam2)
    rasterTeam2 = load_raster(args.rasterTeam2)

    validate_data(seasonCalendarTeam1, rasterTeam1, "Mannschaft 1")
    validate_data(seasonCalendarTeam2, rasterTeam2, "Mannschaft 2")

    best = find_best_combinations(seasonCalendarTeam1, rasterTeam1, seasonCalendarTeam2, rasterTeam2, args.results, args.fixedNumberTeam1, args.fixedNumberTeam2)

    print(f"\nDie {args.results} besten Kennziffern-Kombinationen mit den meisten gemeinsamen Heimspieltagen:\n")
    for (number1, number2), count, weekends in best:
        print(f"Kennziffer {number1} (Team 1) & Kennziffer {number2} (Team 2) → {count} gemeinsame Heimspieltage")
        print(f"  Gemeinsame Heimspieltage: {', '.join(weekends)}\n")
