from argparse import ArgumentParser

parser = ArgumentParser(description="telemetry python wrapper")
parser.add_argument("bob", help="python module to run")

args = parser.parse_args()

if __name__ == '__main__':
    print(args.bob)
