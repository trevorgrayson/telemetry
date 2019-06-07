import os
import sys

from . import Telemetry



def main(host, key, value):
    client = Telemetry()
    client.gauge('statsd', key, value)
    


if __name__ == '__main__':
    host = os.environ.get('STATSD_HOST')

    if len(sys.argv) < 3:
        print("STATSD_HOST=hostname telemetry key.name value")
        exit(0)

    key = sys.argv[1]
    value = float(sys.argv[2])

    if host is None:
        print("please supply a host (e.g. STATSD_HOST=localhost)")

    main(host, key, value)
