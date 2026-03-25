import os
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipelines.utils.db import get_database_url


def _gtfs_static_dir() -> Path:
    """Directory with GTFS .txt files (default: data/raw/gtfs_static/bart/extracted)."""
    load_dotenv()
    default = ROOT / "data" / "raw" / "gtfs_static" / "bart" / "extracted"
    return Path(os.environ.get("GTFS_STATIC_BART_DIR", str(default)))


def main():
    base = _gtfs_static_dir()
    engine = create_engine(get_database_url())

    required_files = ["agency.txt", "stops.txt", "routes.txt", "trips.txt", "stop_times.txt"]
    for name in required_files:
        path = base / name
        if not path.exists():
            raise FileNotFoundError(f"Missing required GTFS file: {path}")

    agency = pd.read_csv(base / "agency.txt", usecols=["agency_id", "agency_name"])
    stops = pd.read_csv(base / "stops.txt", usecols=["stop_id", "stop_name", "stop_lat", "stop_lon"])
    routes = pd.read_csv(
        base / "routes.txt",
        usecols=["route_id", "route_short_name", "route_long_name", "route_type"],
    )
    trips = pd.read_csv(
        base / "trips.txt",
        usecols=["trip_id", "route_id", "service_id", "trip_headsign", "direction_id"],
    )
    stop_times = pd.read_csv(
        base / "stop_times.txt",
        usecols=["trip_id", "arrival_time", "departure_time", "stop_id", "stop_sequence"],
    )

    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE gtfs_static.stop_times RESTART IDENTITY CASCADE"))
        conn.execute(text("TRUNCATE TABLE gtfs_static.trips RESTART IDENTITY CASCADE"))
        conn.execute(text("TRUNCATE TABLE gtfs_static.routes RESTART IDENTITY CASCADE"))
        conn.execute(text("TRUNCATE TABLE gtfs_static.stops RESTART IDENTITY CASCADE"))
        conn.execute(text("TRUNCATE TABLE gtfs_static.agency RESTART IDENTITY CASCADE"))

    agency.to_sql("agency", engine, schema="gtfs_static", if_exists="append", index=False)
    stops.to_sql("stops", engine, schema="gtfs_static", if_exists="append", index=False)
    routes.to_sql("routes", engine, schema="gtfs_static", if_exists="append", index=False)
    trips.to_sql("trips", engine, schema="gtfs_static", if_exists="append", index=False)
    stop_times.to_sql("stop_times", engine, schema="gtfs_static", if_exists="append", index=False)

    print("Loaded static GTFS data into gtfs_static schema successfully.")


if __name__ == "__main__":
    main()