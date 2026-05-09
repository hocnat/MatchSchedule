import argparse
from match_schedule_utils import load_season_calendar, load_raster, validate_data, find_combinations

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zeige alle gemeinsamen Heimspieltage für zwei feste Kennziffern.")

    parser.add_argument("--seasonCalendarTeam1", required=True, help="CSV-Datei mit Saisonkalender der 1. Mannschaft")
    parser.add_argument("--rasterTeam1", required=True, help="YAML-Datei mit Raster der 1. Mannschaft")
    parser.add_argument("--fixedNumberTeam1", type=int, required=True, help="Feste Kennziffer für 1. Mannschaft")

    parser.add_argument("--seasonCalendarTeam2", required=True, help="CSV-Datei mit Saisonkalender der 2. Mannschaft")
    parser.add_argument("--rasterTeam2", required=True, help="YAML-Datei mit Raster der 2. Mannschaft")
    parser.add_argument("--fixedNumberTeam2", type=int, required=True, help="Feste Kennziffer für 2. Mannschaft")

    args = parser.parse_args()

    seasonCalendarTeam1 = load_season_calendar(args.seasonCalendarTeam1)
    rasterTeam1 = load_raster(args.rasterTeam1)
    seasonCalendarTeam2 = load_season_calendar(args.seasonCalendarTeam2)
    rasterTeam2 = load_raster(args.rasterTeam2)

    validate_data(seasonCalendarTeam1, rasterTeam1, "Mannschaft 1")
    validate_data(seasonCalendarTeam2, rasterTeam2, "Mannschaft 2")

    # Since fixed numbers are given, there is only one combination
    combinations = find_combinations(seasonCalendarTeam1, rasterTeam1, seasonCalendarTeam2, rasterTeam2, results=1, fixed_number1=args.fixedNumberTeam1, fixed_number2=args.fixedNumberTeam2, mode="best")

    if combinations:
        (number1, number2), count, weekends = combinations[0]
        print(f"\nGemeinsame Heimspieltage für Kennziffer {number1} (Mannschaft 1) & Kennziffer {number2} (Mannschaft 2):")
        print(f"  Anzahl: {count}")
        if weekends:
            print(f"  Wochenenden: {', '.join(weekends)}")
        else:
            print("  Keine gemeinsamen Heimspieltage.")
    else:
        print("\nKeine gültige Kombination gefunden.")