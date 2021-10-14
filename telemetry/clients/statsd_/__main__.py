from argparse import ArgumentParser
from telemetry import StatsdTelemeter

parser = ArgumentParser(description="statsd test")

parser.add_argument("name", type=str)
args = parser.parse_args()

meter = StatsdTelemeter()

meter.incr(args.name)
print(f"{args.name} incremented.")
