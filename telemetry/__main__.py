import os
import sys

from . import Telemeter



def main(host, key, value):
    client = Telemeter()
    client.gauge('statsd', key, value)
    


if __name__ == '__main__':
    host = os.environ.get('TELEM_STATSD')

    if len(sys.argv) < 3:
        print("TELEM_STATSD=hostname telemetry key.name value")
        exit(0)

    key = sys.argv[1]
    value = float(sys.argv[2])

    if host is None:
        print("please supply a host (e.g. TELEM_STATSD=localhost)")

    main(host, key, value)
