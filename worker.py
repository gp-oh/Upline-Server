#!/usr/bin/env python
import os
import sys

os.environ["DJANGO_SETTINGS_MODULE"] = "upline_server.settings"

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv(
    'REDISTOGO_URL', 'redis://redistogo:b63c57d5f901fca3b650b121d4a4eec2@gar.redistogo.com:9946/')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
