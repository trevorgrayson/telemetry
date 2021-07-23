from os import environ
import sys

from . import get_telemeter


if __name__ == '__main__':
    meter = get_telemeter()
    # meter.find_handlers(environ)

