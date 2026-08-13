from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata


class AbstractThermostatsSimulate(abc.ABC):

    @abc.abstractmethod
    def hvac_mode_adjusted(
        self,
        *,
        device_id: str,
        hvac_mode: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
    ) -> None:
        """Simulates having adjusted the `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ for a `thermostat <https://docs.seam.co/capability-guides/thermostats>`_. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your Thermostat App with Simulate Endpoints <https://docs.seam.co/capability-guides/thermostats/testing-your-thermostat-app-with-simulate-endpoints>`_.

        :param device_id: ID of the thermostat device for which you want to simulate having adjusted the HVAC mode.

        :param hvac_mode: HVAC mode that you want to simulate.

        :param cooling_set_point_celsius: Cooling `set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to simulate. You must set ``cooling_set_point_celsius`` or ``cooling_set_point_fahrenheit``.

        :param cooling_set_point_fahrenheit: Cooling `set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to simulate. You must set ``cooling_set_point_fahrenheit`` or ``cooling_set_point_celsius``.

        :param heating_set_point_celsius: Heating `set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to simulate. You must set ``heating_set_point_celsius`` or ``heating_set_point_fahrenheit``.

        :param heating_set_point_fahrenheit: Heating `set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to simulate. You must set ``heating_set_point_fahrenheit`` or ``heating_set_point_celsius``.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def temperature_reached(
        self,
        *,
        device_id: str,
        temperature_celsius: Optional[float] = None,
        temperature_fahrenheit: Optional[float] = None,
    ) -> None:
        """Simulates a `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ reaching a specified temperature. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your Thermostat App with Simulate Endpoints <https://docs.seam.co/capability-guides/thermostats/testing-your-thermostat-app-with-simulate-endpoints>`_.

        :param device_id: ID of the thermostat device that you want to simulate reaching a specified temperature.

        :param temperature_celsius: Temperature in °C that you want simulate the thermostat reaching. You must set ``temperature_celsius`` or ``temperature_fahrenheit``.

        :param temperature_fahrenheit: Temperature in °F that you want simulate the thermostat reaching. You must set ``temperature_fahrenheit`` or ``temperature_celsius``.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class ThermostatsSimulate(AbstractThermostatsSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/thermostats/simulate/hvac_mode_adjusted",
        has_required_parameters=True,
        has_pagination=False,
    )
    def hvac_mode_adjusted(
        self,
        *,
        device_id: str,
        hvac_mode: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
    ) -> None:
        """Simulates having adjusted the `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ for a `thermostat <https://docs.seam.co/capability-guides/thermostats>`_. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your Thermostat App with Simulate Endpoints <https://docs.seam.co/capability-guides/thermostats/testing-your-thermostat-app-with-simulate-endpoints>`_.

        :param device_id: ID of the thermostat device for which you want to simulate having adjusted the HVAC mode.

        :param hvac_mode: HVAC mode that you want to simulate.

        :param cooling_set_point_celsius: Cooling `set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to simulate. You must set ``cooling_set_point_celsius`` or ``cooling_set_point_fahrenheit``.

        :param cooling_set_point_fahrenheit: Cooling `set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to simulate. You must set ``cooling_set_point_fahrenheit`` or ``cooling_set_point_celsius``.

        :param heating_set_point_celsius: Heating `set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to simulate. You must set ``heating_set_point_celsius`` or ``heating_set_point_fahrenheit``.

        :param heating_set_point_fahrenheit: Heating `set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to simulate. You must set ``heating_set_point_fahrenheit`` or ``heating_set_point_celsius``.

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            device_id is not None,
            hvac_mode is not None,
            cooling_set_point_celsius is not None,
            cooling_set_point_fahrenheit is not None,
            heating_set_point_celsius is not None,
            heating_set_point_fahrenheit is not None,
        ):
            raise ValueError(
                "At least one parameter is required for /thermostats/simulate/hvac_mode_adjusted"
            )
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if hvac_mode is not None:
            json_payload["hvac_mode"] = hvac_mode
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit

        self.client.post("/thermostats/simulate/hvac_mode_adjusted", json=json_payload)

        return None

    @route_metadata(
        path="/thermostats/simulate/temperature_reached",
        has_required_parameters=True,
        has_pagination=False,
    )
    def temperature_reached(
        self,
        *,
        device_id: str,
        temperature_celsius: Optional[float] = None,
        temperature_fahrenheit: Optional[float] = None,
    ) -> None:
        """Simulates a `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ reaching a specified temperature. Only applicable for `sandbox devices <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Testing Your Thermostat App with Simulate Endpoints <https://docs.seam.co/capability-guides/thermostats/testing-your-thermostat-app-with-simulate-endpoints>`_.

        :param device_id: ID of the thermostat device that you want to simulate reaching a specified temperature.

        :param temperature_celsius: Temperature in °C that you want simulate the thermostat reaching. You must set ``temperature_celsius`` or ``temperature_fahrenheit``.

        :param temperature_fahrenheit: Temperature in °F that you want simulate the thermostat reaching. You must set ``temperature_fahrenheit`` or ``temperature_celsius``.

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            device_id is not None,
            temperature_celsius is not None,
            temperature_fahrenheit is not None,
        ):
            raise ValueError(
                "At least one parameter is required for /thermostats/simulate/temperature_reached"
            )
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if temperature_celsius is not None:
            json_payload["temperature_celsius"] = temperature_celsius
        if temperature_fahrenheit is not None:
            json_payload["temperature_fahrenheit"] = temperature_fahrenheit

        self.client.post("/thermostats/simulate/temperature_reached", json=json_payload)

        return None
