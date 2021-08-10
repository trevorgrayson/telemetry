from argparse import ArgumentParser
from . import PagerDutyTelemeter
import telemetry

parser = ArgumentParser(description="PagerDutyTelemeter CLI")
parser.add_argument("msg", type=str, help="error message to be sent")

args = parser.parse_args()

service = PagerDutyTelemeter()
meter = telemetry.get_telemeter()
meter.addHandler(service)

meter.message(args.msg)
