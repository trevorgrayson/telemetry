from dataclasses import dataclass


@dataclass(frozen=True)
class GaugeMessage:
    name: str
    value: float


def parse_gauge(line):
    if not line:
        return None
    line = line.strip()
    if not line:
        return None
    if ":" not in line:
        return None
    name, rest = line.split(":", 1)
    name = name.strip()
    if not name:
        return None
    parts = rest.split("|")
    if len(parts) < 2:
        return None
    value_str = parts[0].strip()
    metric_type = parts[1].strip().lower()
    if metric_type != "g":
        return None
    try:
        value = float(value_str)
    except ValueError:
        return None
    return GaugeMessage(name=name, value=value)
