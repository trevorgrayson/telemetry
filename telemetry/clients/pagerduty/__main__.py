from argparse import ArgumentParser
from telemetry import loggers
import logging

parser = ArgumentParser(description="PagerDutyTelemeter CLI")
parser.add_argument("msg", type=str, help="error message to be sent")

args = parser.parse_args()

service = loggers.PagerDutyTelemeter()
logger = logging.getLogger('telemetry')
logger.addHandler(service)
logging.getLogger()
logger.info("info")
logger.warning("warning")
logger.error(args.msg)
