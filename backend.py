#!/bin/python

import os
import logging
import time

COUNTDOWN = "/dev/shm/countdown"
OUTPUT = "/dev/shm/output"

logging.basicConfig(level=logging.INFO)

last_count = 0
while True:
    try:
        with open(COUNTDOWN) as f:
            start = f.read()
        os.remove(COUNTDOWN)
        start = int(start)
    except FileNotFoundError:
        logging.info("No new countdown file found.")
        time.sleep(0.5)
        continue

    if start == last_count:
        logging.info("Skipping. Count of bugs unchanged.")
        time.sleep(0.5)
        continue

    logging.info("Counting down bugs from %s", start)
    lines = []
    for i in range(start, 0, -1):
        lines.append("%s little bugs in the code. "
                     "Take one down, patch it around." % i)

    with open(OUTPUT, "w") as f:
        f.write("\n".join(lines))

    last_count = start
    time.sleep(0.5)
