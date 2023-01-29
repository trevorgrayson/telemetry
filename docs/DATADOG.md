# `DataDogStatsdTelemeter` 

This is a straight forward [Data Dog statsd](https://docs.datadoghq.com/developers/dogstatsd/?tab=hostagent) client implementation.
See [STATSD](./STATSD.md) for interface details. You may pass extra params, like tags when instantiating.

## DataDogStatsdTelemeter

```python
# export STATSD_HOST="localhost:8125"

from telemetry import DataDogStatsdTelemeter

meter = DataDogStatsdTelemeter()
```

## Methods

`telemetry` supports the following methods: 
`gauge`, `incr`, `decr`, `timing`, `send`

## Kubernetes

Confirm your `statsd` host relative to your pods, it may not be `127.0.0.1`.

If `statsd` is being run on your host machine, add this to your [pod's environment vars](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/) 
(k8s v1.7.0-alpha.1+.)

```yaml
    env:
    - name: STATSD_HOST
      value: status.hostIP
```
