# Exception Telemetry

Measuring exceptions is a critical part of understanding the health of your 
application. When an exception occurs, it can be logged and/or reported to a 
telemetry system. This allows you to monitor the frequency and types of 
exceptions that are occurring in your application.

See exceptions_test.py and decorators_test.py for examples.

## decorators

```python
from telemetry import Telemeter, PagerDutyTelemeter

meter = Telemeter()
meter.addHandler(PagerDutyTelemeter())

@meter.catch("your_failure_name")
def some_function():
    raise Exception("This is a test exception")

```

```python
from telemetry import PagerDutyTelemeter

meter = PagerDutyTelemeter()

@meter.catch("your_failure_name")
def some_function():
    raise Exception("This is a test exception")

```

## configuration

Set appropriate environment variables.  Configuration will cascade attribute
definition from the environment, to the constructor, decoration/method call. 

Consider the following values:

- routing_key
- source
- dedupe_key
- client
- client_url