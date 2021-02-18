# include the clients that have libraries loaded,
# otherwise, ignore
try:
    from .graphite import Statsd
except ImportError:
    pass

try:
    from .slack import SlackTelemeter
except ImportError:
    pass
