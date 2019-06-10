import logging
import telemetry
from unit.telemetry import TelemetryProbe

LOG = logging.getLogger(__name__)


LOG.info('Setting telemetry probe')
telemetry.set_client(TelemetryProbe())
