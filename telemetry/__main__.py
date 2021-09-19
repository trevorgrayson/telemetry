import sys
import runpy
import logging
from argparse import ArgumentParser

import telemetry

parser = ArgumentParser(description="telemetry python wrapper")
parser.add_argument("module", help="python module to run")
args, _ = parser.parse_known_args()

main_logger = logging.getLogger()
telem_logger = logging.getLogger("telemetry")

loggers = telemetry.env_loggers()
for logger in loggers:
    logging.info(f"loading {logger.__name__}")
    main_logger.addHandler(logger)
    telem_logger.addHandler(logger)

sys.argv = sys.argv[1:]
runpy.run_module(args.module, run_name="__main__")
