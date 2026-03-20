# pipelines/ingestion/parse_gtfs_rt.py

from google.transit import gtfs_realtime_pb2

def parse_feed(content: bytes):
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(content)
    return feed