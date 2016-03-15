#!/usr/bin/env python
import os
import sys

os.environ["DJANGO_SETTINGS_MODULE"] = "upline_server.settings"

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv(
    'REDISTOGO_URL', 'redis://redistogo:2e95371aee3dee1a000dc0c21f116701@telescopefish.redistogo.com:9237/')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
