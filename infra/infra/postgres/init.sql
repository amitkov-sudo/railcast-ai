CREATE SCHEMA IF NOT EXISTS gtfs_static;

CREATE TABLE IF NOT EXISTS gtfs_static.agency (
    agency_id TEXT PRIMARY KEY,
    agency_name TEXT
);

CREATE TABLE IF NOT EXISTS gtfs_static.stops (
    stop_id TEXT PRIMARY KEY,
    stop_name TEXT,
    stop_lat DOUBLE PRECISION,
    stop_lon DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS gtfs_static.routes (
    route_id TEXT PRIMARY KEY,
    route_short_name TEXT,
    route_long_name TEXT,
    route_type INTEGER
);

CREATE TABLE IF NOT EXISTS gtfs_static.trips (
    trip_id TEXT PRIMARY KEY,
    route_id TEXT,
    service_id TEXT,
    trip_headsign TEXT,
    direction_id INT
);

CREATE TABLE IF NOT EXISTS gtfs_static.stop_times (
    trip_id TEXT NOT NULL,
    arrival_time TEXT,
    departure_time TEXT,
    stop_id TEXT NOT NULL,
    stop_sequence INT NOT NULL,
    PRIMARY KEY (trip_id, stop_sequence)
);