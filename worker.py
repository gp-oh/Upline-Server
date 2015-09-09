#!/usr/bin/env python
import os, sys

os.environ["DJANGO_SETTINGS_MODULE"] = "upline_server.settings"

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://redistogo:a6174191576f0394ab151a0eee4cb03e@barb.redistogo.com:9179/')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()