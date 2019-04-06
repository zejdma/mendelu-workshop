#!/bin/python3
import os

# Let's do some headers
print("Content-type: text/plain")
print()

# Body starts now...
query = os.environ.get("QUERY_STRING", "")
data = query.split("&")
value = 0
for item in data:
    key, val = item.split("=")
    if key == "value":
        value = val

with open("/dev/shm/countdown", "w") as f:
    f.write(value)

print("Heya! Seems we have a new bug count: %s\n" % value)
