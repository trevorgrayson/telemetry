from argparse import ArgumentParser
from . import SlackTelemeter

parser = ArgumentParser(description="SlackTelemeter CLI")
parser.add_argument("msg", type=str, help="message to be sent")
parser.add_argument("--room", type=str, help="Room Id in TXXX/BYYY/ZZZ format")

args = parser.parse_args()

slack = SlackTelemeter(args.room)
slack.message(args.msg)
