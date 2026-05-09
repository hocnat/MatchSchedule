import argparse
from match_schedule_utils import load_season_calendar, load_raster, validate_data, find_combinations

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Finde die schlechtesten Kennziffern für gemeinsame Heimspieltage.")

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

    worst = find_combinations(seasonCalendarTeam1, rasterTeam1, seasonCalendarTeam2, rasterTeam2, args.results, args.fixedNumberTeam1, args.fixedNumberTeam2, mode="worst")

    print(f"\nDie {args.results} schlechtesten Kennziffern-Kombinationen mit den wenigsten gemeinsamen Heimspieltagen:\n")
    for (number1, number2), count, weekends in worst:
        print(f"Kennziffer {number1} (Mannschaft 1) & Kennziffer {number2} (Mannschaft 2) → {count} gemeinsame Heimspieltage")
        print(f"  Gemeinsame Heimspieltage: {', '.join(weekends)}\n")