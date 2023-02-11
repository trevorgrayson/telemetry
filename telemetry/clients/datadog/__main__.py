from argparse import ArgumentParser
from . import DataDogStatsdTelemeter

parser = ArgumentParser(description="data dog statsd test")

parser.add_argument("name", type=str)
args = parser.parse_args()

meter = DataDogStatsdTelemeter()

meter.incr(args.name)
print(f"{args.name} incremented.")
