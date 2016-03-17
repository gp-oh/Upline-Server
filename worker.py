#!/usr/bin/env python
import os
import sys

os.environ["DJANGO_SETTINGS_MODULE"] = "upline_server.settings"

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv(
    'REDISTOGO_URL', 'redis://redistogo:e89b77c6893f7af344cf69762fb45b2c@tarpon.redistogo.com:9497/')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
