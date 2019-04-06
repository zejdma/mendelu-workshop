#!/bin/python3
# Let's do some headers
print("Content-type: text/plain")
print()

# Body starts now...
with open("/dev/shm/output") as f:
    print(f.read())
