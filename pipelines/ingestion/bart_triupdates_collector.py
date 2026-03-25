# pipelines/ingestion/bart_tripupdates_collector.py
import requests
from parse_gtfs_rt import parse_feed

URL = "http://api.bart.gov/gtfsrt/tripupdate.aspx"

def main():
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    feed = parse_feed(response.content)

    for entity in feed.entity:
        if entity.HasField("trip_update"):
            print(entity.trip_update)

if __name__ == "__main__":
    main()