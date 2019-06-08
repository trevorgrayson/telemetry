# telemetry

Remote measuring abstraction for software applications.

`telemetry` serves as a simple facade or abstraction for various telemetry frameworks (e.g. statsd, graphite) 
allowing the end user to plug in the desired telemetry framework at deployment time. Think [slf4j](https://www.slf4j.org/)
but for events and numbers, not logs.  This library borrows from their example (and copy.)

As your projects grow, their telemetry requirements will change.  The purpose of this library is to simplify
implementation, provide easy configuration, encourage testing, and avoid vendor lock.


## Supported Services:

* statsd/graphite

Furture Implementations

* elasticsearch
* NewRelic Insights

## Implementation

The application data that you would like to report likely varies considerably
between applications and even environments. This library favors [environment variables](https://en.wikipedia.org/wiki/Environment_variable) for turning services on/off and configuration.  You may implement this library in other ways.

Generally, after implementation, the easiest configuration will be:

```bash
TELEM_STATSD=your.graphite-host.com python your-app.py
```

Excluding a configuration will default to a no-operation implementation.

## Data Types with Examples

Presently only the `gauge` method is available.  The rest will be added shortly.

### Gauge 

Gauge reports on values that will change over time and whose future and past measurements won't affect its present value.  If you wanted to report the value of the speedometer in your car, this is your best choice.

```python
import telemetry

telemetry.gauge('statsd', 'test.some.key', 10)

```

### Timing

Benchmarking and time measurements should be reported using these.  Values are submitted in milliseconds.

You have a couple of different ways to implement this.

#### Decorators

You may decorate a method to report on its runtime after completion.

```python
from telemetry.decorators import report_time

@report_runtime('test.some.key')
def some_long_method(a, b):
	sleep(10)

```

#### `with` blocks

You may use a `benchmark` block to report the runtime of the code inside its block.

```python
from telemetry import benchmark

with benchmark('test.some.other.key'):
	sleep(10)
```

### Increment


You may want to test in your development 
environment, but don't want to run it consistently.  You may or may not collect in staging,
a


## Testing

Some telemetry data can be mission critical. Test for it.  Since you have a facade in front of your service, you don't need to test that it gets to your service.

```python
import telemetry
from telemetry.test import TelemetryProbe

telemetry.setClient(TelemetryProbe())

telemetry.gauge("some.key", 10)

assert telemetry.getClient.messages[0].name = "some.key"
assert telemetry.getClient.messages[0].value = 10

```
