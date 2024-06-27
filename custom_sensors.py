import sensors

from datadog_checks.checks import AgentCheck


class SensorsMon(AgentCheck):

    def check(self, instance):
        sensors.init()
        try:
            for chip in sensors.iter_detected_chips():
                for feature in chip:
                    if feature.label.startswith("Core"):
                        self.gauge(
                            "sensors.core",
                            feature.get_value(),
                            tags=[f"device:{chip}", f"core:{feature.label}"],
                        )
                    else:
                        self.gauge(
                            "sensors." + feature.label,
                            feature.get_value(),
                            tags=[f"device:{chip}"],
                        )
        finally:
            sensors.cleanup()
