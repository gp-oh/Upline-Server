#!/usr/bin/env python
import os
import sys

os.environ["DJANGO_SETTINGS_MODULE"] = "upline_server.settings"

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv(
    'REDISTOGO_URL', 'redis://redistogo:312e2d275e412e2171878bda15a62d27@catfish.redistogo.com:10501/')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
