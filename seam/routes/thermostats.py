from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..resources import ActionAttempt, Device
from .thermostats_daily_programs import (
    AbstractThermostatsDailyPrograms,
    ThermostatsDailyPrograms,
)
from .thermostats_schedules import AbstractThermostatsSchedules, ThermostatsSchedules
from .thermostats_simulate import AbstractThermostatsSimulate, ThermostatsSimulate
from ..modules.action_attempts import resolve_action_attempt


class AbstractThermostats(abc.ABC):

    @property
    @abc.abstractmethod
    def daily_programs(self) -> AbstractThermostatsDailyPrograms:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def schedules(self) -> AbstractThermostatsSchedules:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractThermostatsSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
    def activate_climate_preset(
        self,
        *,
        climate_preset_key: str,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Activates a specified `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Climate preset key of the climate preset that you want to activate.

        :param device_id: ID of the thermostat device for which you want to activate a climate preset.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def cool(
        self,
        *,
        device_id: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ to `cool mode <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings>`_.

        :param device_id: ID of the thermostat device that you want to set to cool mode.

        :param cooling_set_point_celsius: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param cooling_set_point_fahrenheit: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def create_climate_preset(
        self,
        *,
        climate_preset_key: str,
        device_id: str,
        climate_preset_mode: Optional[str] = None,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        ecobee_metadata: Optional[Dict[str, Any]] = None,
        fan_mode_setting: Optional[str] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        hvac_mode_setting: Optional[str] = None,
        manual_override_allowed: Optional[bool] = None,
        name: Optional[str] = None,
    ) -> None:
        """Creates a `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Unique key to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

        :param device_id: ID of the thermostat device for which you want create a climate preset.

        :param climate_preset_mode: The climate preset mode for the thermostat, based on the available climate preset modes reported by the device.

        :param cooling_set_point_celsius: Temperature to which the thermostat should cool (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param cooling_set_point_fahrenheit: Temperature to which the thermostat should cool (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param ecobee_metadata: Metadata specific to the Ecobee climate, if applicable.

        :param fan_mode_setting: Desired `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_, such as ``on``, ``auto``, or ``circulate``.

        :param heating_set_point_celsius: Temperature to which the thermostat should heat (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param heating_set_point_fahrenheit: Temperature to which the thermostat should heat (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param hvac_mode_setting: Desired `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ setting, such as ``heat``, ``cool``, ``heat_cool``, or ``off``.

        :param manual_override_allowed: Deprecated: Use 'thermostat_schedule.is_override_allowed' Indicates whether a person at the thermostat or using the API can change the thermostat's settings.

        :param name: User-friendly name to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_climate_preset(self, *, climate_preset_key: str, device_id: str) -> None:
        """Deletes a specified `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Climate preset key of the climate preset that you want to delete.

        :param device_id: ID of the thermostat device for which you want to delete a climate preset.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def heat(
        self,
        *,
        device_id: str,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ to `heat mode <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings>`_.

        :param device_id: ID of the thermostat device that you want to set to heat mode.

        :param heating_set_point_celsius: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param heating_set_point_fahrenheit: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def heat_cool(
        self,
        *,
        device_id: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ to `heat-cool ("auto") mode <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings>`_.

        :param device_id: ID of the thermostat device that you want to set to heat-cool mode.

        :param cooling_set_point_celsius: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param cooling_set_point_fahrenheit: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param heating_set_point_celsius: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param heating_set_point_fahrenheit: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        manufacturer: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `thermostats <https://docs.seam.co/capability-guides/thermostats>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param customer_key: Customer key for which you want to list devices.

        :param device_type: Device type by which you want to filter thermostat devices.

        :param device_types: Array of device types by which you want to filter thermostat devices.

        :param manufacturer: Manufacturer by which you want to filter thermostat devices.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def off(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ to `"off" mode <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings>`_.

        :param device_id: ID of the thermostat device that you want to set to off mode.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def set_fallback_climate_preset(
        self, *, climate_preset_key: str, device_id: str
    ) -> None:
        """Sets a specified `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ as the `"fallback" <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets/setting-the-fallback-climate-preset>`_ preset for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Climate preset key of the climate preset that you want to set as the fallback climate preset.

        :param device_id: ID of the thermostat device for which you want to set the fallback climate preset.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def set_fan_mode(
        self,
        *,
        device_id: str,
        fan_mode: Optional[str] = None,
        fan_mode_setting: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets the `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param device_id: ID of the thermostat device for which you want to set the fan mode.

        :param fan_mode: Deprecated: Use ``fan_mode_setting`` instead. Fan mode setting for the thermostat, such as ``auto``, ``on``, or ``circulate``.

        :param fan_mode_setting: `Fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_ that you want to set for the thermostat.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def set_hvac_mode(
        self,
        *,
        device_id: str,
        hvac_mode_setting: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets the `HVAC mode <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param device_id: ID of the thermostat device for which you want to set the HVAC mode.

        :param hvac_mode_setting:

        :param cooling_set_point_celsius: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param cooling_set_point_fahrenheit: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param heating_set_point_celsius: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param heating_set_point_fahrenheit: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def set_temperature_threshold(
        self,
        *,
        device_id: str,
        lower_limit_celsius: Optional[float] = None,
        lower_limit_fahrenheit: Optional[float] = None,
        upper_limit_celsius: Optional[float] = None,
        upper_limit_fahrenheit: Optional[float] = None,
    ) -> None:
        """Sets a `temperature threshold <https://docs.seam.co/capability-guides/thermostats/setting-and-monitoring-temperature-thresholds>`_ for a specified thermostat. Seam emits a ``thermostat.temperature_threshold_exceeded`` event and adds a warning on a thermostat if it reports a temperature outside the threshold range.

        :param device_id: ID of the thermostat device for which you want to set a temperature threshold.

        :param lower_limit_celsius: Lower temperature limit in in °C. Seam alerts you if the reported temperature is lower than this value. You can specify either ``lower_limit`` but not both.

        :param lower_limit_fahrenheit: Lower temperature limit in in °F. Seam alerts you if the reported temperature is lower than this value. You can specify either ``lower_limit`` but not both.

        :param upper_limit_celsius: Upper temperature limit in in °C. Seam alerts you if the reported temperature is higher than this value. You can specify either ``upper_limit`` but not both.

        :param upper_limit_fahrenheit: Upper temperature limit in in °C. Seam alerts you if the reported temperature is higher than this value. You can specify either ``upper_limit`` but not both.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update_climate_preset(
        self,
        *,
        climate_preset_key: str,
        device_id: str,
        climate_preset_mode: Optional[str] = None,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        ecobee_metadata: Optional[Dict[str, Any]] = None,
        fan_mode_setting: Optional[str] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        hvac_mode_setting: Optional[str] = None,
        manual_override_allowed: Optional[bool] = None,
        name: Optional[str] = None,
    ) -> None:
        """Updates a specified `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Unique key to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

        :param device_id: ID of the thermostat device for which you want to update a climate preset.

        :param climate_preset_mode: The climate preset mode for the thermostat, based on the available climate preset modes reported by the device.

        :param cooling_set_point_celsius: Temperature to which the thermostat should cool (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param cooling_set_point_fahrenheit: Temperature to which the thermostat should cool (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param ecobee_metadata: Metadata specific to the Ecobee climate, if applicable.

        :param fan_mode_setting: Desired `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_, such as ``on``, ``auto``, or ``circulate``.

        :param heating_set_point_celsius: Temperature to which the thermostat should heat (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param heating_set_point_fahrenheit: Temperature to which the thermostat should heat (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param hvac_mode_setting: Desired `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ setting, such as ``heat``, ``cool``, ``heat_cool``, or ``off``.

        :param manual_override_allowed: Deprecated: Use 'thermostat_schedule.is_override_allowed' Indicates whether a person at the thermostat can change the thermostat's settings. See `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

        :param name: User-friendly name to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def update_weekly_program(
        self,
        *,
        device_id: str,
        friday_program_id: Optional[str] = None,
        monday_program_id: Optional[str] = None,
        saturday_program_id: Optional[str] = None,
        sunday_program_id: Optional[str] = None,
        thursday_program_id: Optional[str] = None,
        tuesday_program_id: Optional[str] = None,
        wednesday_program_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Updates the thermostat weekly program for a thermostat device. To configure a weekly program, specify the ID of the daily program that you want to use for each day of the week. When you update a weekly program, the set of programs that you specify overwrites any previous weekly program for the thermostat.

        :param device_id: ID of the thermostat device for which you want to update the weekly program.

        :param friday_program_id: ID of the thermostat daily program to run on Fridays.

        :param monday_program_id: ID of the thermostat daily program to run on Mondays.

        :param saturday_program_id: ID of the thermostat daily program to run on Saturdays.

        :param sunday_program_id: ID of the thermostat daily program to run on Sundays.

        :param thursday_program_id: ID of the thermostat daily program to run on Thursdays.

        :param tuesday_program_id: ID of the thermostat daily program to run on Tuesdays.

        :param wednesday_program_id: ID of the thermostat daily program to run on Wednesdays.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class Thermostats(AbstractThermostats):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._daily_programs = ThermostatsDailyPrograms(
            client=client, defaults=defaults
        )
        self._schedules = ThermostatsSchedules(client=client, defaults=defaults)
        self._simulate = ThermostatsSimulate(client=client, defaults=defaults)

    @property
    def daily_programs(self) -> ThermostatsDailyPrograms:
        return self._daily_programs

    @property
    def schedules(self) -> ThermostatsSchedules:
        return self._schedules

    @property
    def simulate(self) -> ThermostatsSimulate:
        return self._simulate

    @route_metadata(
        path="/thermostats/activate_climate_preset",
        has_required_parameters=True,
        has_pagination=False,
    )
    def activate_climate_preset(
        self,
        *,
        climate_preset_key: str,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Activates a specified `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Climate preset key of the climate preset that you want to activate.

        :param device_id: ID of the thermostat device for which you want to activate a climate preset.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any([climate_preset_key is not None, device_id is not None]):
            raise ValueError(
                "At least one parameter is required for /thermostats/activate_climate_preset"
            )
        json_payload: Dict[str, Any] = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post(
            "/thermostats/activate_climate_preset", json=json_payload
        )

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/thermostats/cool", has_required_parameters=True, has_pagination=False
    )
    def cool(
        self,
        *,
        device_id: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ to `cool mode <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings>`_.

        :param device_id: ID of the thermostat device that you want to set to cool mode.

        :param cooling_set_point_celsius: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param cooling_set_point_fahrenheit: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                device_id is not None,
                cooling_set_point_celsius is not None,
                cooling_set_point_fahrenheit is not None,
            ]
        ):
            raise ValueError("At least one parameter is required for /thermostats/cool")
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit

        res = self.client.post("/thermostats/cool", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/thermostats/create_climate_preset",
        has_required_parameters=True,
        has_pagination=False,
    )
    def create_climate_preset(
        self,
        *,
        climate_preset_key: str,
        device_id: str,
        climate_preset_mode: Optional[str] = None,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        ecobee_metadata: Optional[Dict[str, Any]] = None,
        fan_mode_setting: Optional[str] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        hvac_mode_setting: Optional[str] = None,
        manual_override_allowed: Optional[bool] = None,
        name: Optional[str] = None,
    ) -> None:
        """Creates a `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Unique key to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

        :param device_id: ID of the thermostat device for which you want create a climate preset.

        :param climate_preset_mode: The climate preset mode for the thermostat, based on the available climate preset modes reported by the device.

        :param cooling_set_point_celsius: Temperature to which the thermostat should cool (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param cooling_set_point_fahrenheit: Temperature to which the thermostat should cool (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param ecobee_metadata: Metadata specific to the Ecobee climate, if applicable.

        :param fan_mode_setting: Desired `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_, such as ``on``, ``auto``, or ``circulate``.

        :param heating_set_point_celsius: Temperature to which the thermostat should heat (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param heating_set_point_fahrenheit: Temperature to which the thermostat should heat (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param hvac_mode_setting: Desired `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ setting, such as ``heat``, ``cool``, ``heat_cool``, or ``off``.

        :param manual_override_allowed: Deprecated: Use 'thermostat_schedule.is_override_allowed' Indicates whether a person at the thermostat or using the API can change the thermostat's settings.

        :param name: User-friendly name to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                climate_preset_key is not None,
                device_id is not None,
                climate_preset_mode is not None,
                cooling_set_point_celsius is not None,
                cooling_set_point_fahrenheit is not None,
                ecobee_metadata is not None,
                fan_mode_setting is not None,
                heating_set_point_celsius is not None,
                heating_set_point_fahrenheit is not None,
                hvac_mode_setting is not None,
                manual_override_allowed is not None,
                name is not None,
            ]
        ):
            raise ValueError(
                "At least one parameter is required for /thermostats/create_climate_preset"
            )
        json_payload: Dict[str, Any] = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id
        if climate_preset_mode is not None:
            json_payload["climate_preset_mode"] = climate_preset_mode
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if ecobee_metadata is not None:
            json_payload["ecobee_metadata"] = ecobee_metadata
        if fan_mode_setting is not None:
            json_payload["fan_mode_setting"] = fan_mode_setting
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if hvac_mode_setting is not None:
            json_payload["hvac_mode_setting"] = hvac_mode_setting
        if manual_override_allowed is not None:
            json_payload["manual_override_allowed"] = manual_override_allowed
        if name is not None:
            json_payload["name"] = name

        self.client.post("/thermostats/create_climate_preset", json=json_payload)

        return None

    @route_metadata(
        path="/thermostats/delete_climate_preset",
        has_required_parameters=True,
        has_pagination=False,
    )
    def delete_climate_preset(self, *, climate_preset_key: str, device_id: str) -> None:
        """Deletes a specified `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Climate preset key of the climate preset that you want to delete.

        :param device_id: ID of the thermostat device for which you want to delete a climate preset.

        :raises ValueError: At least one parameter must be provided."""
        if not any([climate_preset_key is not None, device_id is not None]):
            raise ValueError(
                "At least one parameter is required for /thermostats/delete_climate_preset"
            )
        params: Dict[str, Any] = {}

        if climate_preset_key is not None:
            params["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            params["device_id"] = device_id

        self.client.delete("/thermostats/delete_climate_preset", params=params)

        return None

    @route_metadata(
        path="/thermostats/heat", has_required_parameters=True, has_pagination=False
    )
    def heat(
        self,
        *,
        device_id: str,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ to `heat mode <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings>`_.

        :param device_id: ID of the thermostat device that you want to set to heat mode.

        :param heating_set_point_celsius: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param heating_set_point_fahrenheit: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                device_id is not None,
                heating_set_point_celsius is not None,
                heating_set_point_fahrenheit is not None,
            ]
        ):
            raise ValueError("At least one parameter is required for /thermostats/heat")
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit

        res = self.client.post("/thermostats/heat", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/thermostats/heat_cool",
        has_required_parameters=True,
        has_pagination=False,
    )
    def heat_cool(
        self,
        *,
        device_id: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ to `heat-cool ("auto") mode <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings>`_.

        :param device_id: ID of the thermostat device that you want to set to heat-cool mode.

        :param cooling_set_point_celsius: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param cooling_set_point_fahrenheit: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param heating_set_point_celsius: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param heating_set_point_fahrenheit: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                device_id is not None,
                cooling_set_point_celsius is not None,
                cooling_set_point_fahrenheit is not None,
                heating_set_point_celsius is not None,
                heating_set_point_fahrenheit is not None,
            ]
        ):
            raise ValueError(
                "At least one parameter is required for /thermostats/heat_cool"
            )
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit

        res = self.client.post("/thermostats/heat_cool", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/thermostats/list", has_required_parameters=False, has_pagination=False
    )
    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        manufacturer: Optional[str] = None,
    ) -> List[Device]:
        """Returns a list of all `thermostats <https://docs.seam.co/capability-guides/thermostats>`_.

        :param connect_webview_id: ID of the Connect Webview for which you want to list devices.

        :param connected_account_id: ID of the connected account for which you want to list devices.

        :param customer_key: Customer key for which you want to list devices.

        :param device_type: Device type by which you want to filter thermostat devices.

        :param device_types: Array of device types by which you want to filter thermostat devices.

        :param manufacturer: Manufacturer by which you want to filter thermostat devices.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if device_type is not None:
            json_payload["device_type"] = device_type
        if device_types is not None:
            json_payload["device_types"] = device_types
        if manufacturer is not None:
            json_payload["manufacturer"] = manufacturer

        res = self.client.post("/thermostats/list", json=json_payload)

        return [Device.from_dict(item) for item in res["devices"]]

    @route_metadata(
        path="/thermostats/off", has_required_parameters=True, has_pagination=False
    )
    def off(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ to `"off" mode <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings>`_.

        :param device_id: ID of the thermostat device that you want to set to off mode.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any([device_id is not None]):
            raise ValueError("At least one parameter is required for /thermostats/off")
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post("/thermostats/off", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/thermostats/set_fallback_climate_preset",
        has_required_parameters=True,
        has_pagination=False,
    )
    def set_fallback_climate_preset(
        self, *, climate_preset_key: str, device_id: str
    ) -> None:
        """Sets a specified `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ as the `"fallback" <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets/setting-the-fallback-climate-preset>`_ preset for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Climate preset key of the climate preset that you want to set as the fallback climate preset.

        :param device_id: ID of the thermostat device for which you want to set the fallback climate preset.

        :raises ValueError: At least one parameter must be provided."""
        if not any([climate_preset_key is not None, device_id is not None]):
            raise ValueError(
                "At least one parameter is required for /thermostats/set_fallback_climate_preset"
            )
        json_payload: Dict[str, Any] = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/thermostats/set_fallback_climate_preset", json=json_payload)

        return None

    @route_metadata(
        path="/thermostats/set_fan_mode",
        has_required_parameters=True,
        has_pagination=False,
    )
    def set_fan_mode(
        self,
        *,
        device_id: str,
        fan_mode: Optional[str] = None,
        fan_mode_setting: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets the `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param device_id: ID of the thermostat device for which you want to set the fan mode.

        :param fan_mode: Deprecated: Use ``fan_mode_setting`` instead. Fan mode setting for the thermostat, such as ``auto``, ``on``, or ``circulate``.

        :param fan_mode_setting: `Fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_ that you want to set for the thermostat.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [device_id is not None, fan_mode is not None, fan_mode_setting is not None]
        ):
            raise ValueError(
                "At least one parameter is required for /thermostats/set_fan_mode"
            )
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if fan_mode is not None:
            json_payload["fan_mode"] = fan_mode
        if fan_mode_setting is not None:
            json_payload["fan_mode_setting"] = fan_mode_setting

        res = self.client.post("/thermostats/set_fan_mode", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/thermostats/set_hvac_mode",
        has_required_parameters=True,
        has_pagination=False,
    )
    def set_hvac_mode(
        self,
        *,
        device_id: str,
        hvac_mode_setting: str,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Sets the `HVAC mode <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param device_id: ID of the thermostat device for which you want to set the HVAC mode.

        :param hvac_mode_setting:

        :param cooling_set_point_celsius: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param cooling_set_point_fahrenheit: `Cooling set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``cooling_set_point`` parameters.

        :param heating_set_point_celsius: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °C that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param heating_set_point_fahrenheit: `Heating set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_ in °F that you want to set for the thermostat. You must set one of the ``heating_set_point`` parameters.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                device_id is not None,
                hvac_mode_setting is not None,
                cooling_set_point_celsius is not None,
                cooling_set_point_fahrenheit is not None,
                heating_set_point_celsius is not None,
                heating_set_point_fahrenheit is not None,
            ]
        ):
            raise ValueError(
                "At least one parameter is required for /thermostats/set_hvac_mode"
            )
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if hvac_mode_setting is not None:
            json_payload["hvac_mode_setting"] = hvac_mode_setting
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit

        res = self.client.post("/thermostats/set_hvac_mode", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/thermostats/set_temperature_threshold",
        has_required_parameters=True,
        has_pagination=False,
    )
    def set_temperature_threshold(
        self,
        *,
        device_id: str,
        lower_limit_celsius: Optional[float] = None,
        lower_limit_fahrenheit: Optional[float] = None,
        upper_limit_celsius: Optional[float] = None,
        upper_limit_fahrenheit: Optional[float] = None,
    ) -> None:
        """Sets a `temperature threshold <https://docs.seam.co/capability-guides/thermostats/setting-and-monitoring-temperature-thresholds>`_ for a specified thermostat. Seam emits a ``thermostat.temperature_threshold_exceeded`` event and adds a warning on a thermostat if it reports a temperature outside the threshold range.

        :param device_id: ID of the thermostat device for which you want to set a temperature threshold.

        :param lower_limit_celsius: Lower temperature limit in in °C. Seam alerts you if the reported temperature is lower than this value. You can specify either ``lower_limit`` but not both.

        :param lower_limit_fahrenheit: Lower temperature limit in in °F. Seam alerts you if the reported temperature is lower than this value. You can specify either ``lower_limit`` but not both.

        :param upper_limit_celsius: Upper temperature limit in in °C. Seam alerts you if the reported temperature is higher than this value. You can specify either ``upper_limit`` but not both.

        :param upper_limit_fahrenheit: Upper temperature limit in in °C. Seam alerts you if the reported temperature is higher than this value. You can specify either ``upper_limit`` but not both.

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                device_id is not None,
                lower_limit_celsius is not None,
                lower_limit_fahrenheit is not None,
                upper_limit_celsius is not None,
                upper_limit_fahrenheit is not None,
            ]
        ):
            raise ValueError(
                "At least one parameter is required for /thermostats/set_temperature_threshold"
            )
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if lower_limit_celsius is not None:
            json_payload["lower_limit_celsius"] = lower_limit_celsius
        if lower_limit_fahrenheit is not None:
            json_payload["lower_limit_fahrenheit"] = lower_limit_fahrenheit
        if upper_limit_celsius is not None:
            json_payload["upper_limit_celsius"] = upper_limit_celsius
        if upper_limit_fahrenheit is not None:
            json_payload["upper_limit_fahrenheit"] = upper_limit_fahrenheit

        self.client.patch("/thermostats/set_temperature_threshold", json=json_payload)

        return None

    @route_metadata(
        path="/thermostats/update_climate_preset",
        has_required_parameters=True,
        has_pagination=False,
    )
    def update_climate_preset(
        self,
        *,
        climate_preset_key: str,
        device_id: str,
        climate_preset_mode: Optional[str] = None,
        cooling_set_point_celsius: Optional[float] = None,
        cooling_set_point_fahrenheit: Optional[float] = None,
        ecobee_metadata: Optional[Dict[str, Any]] = None,
        fan_mode_setting: Optional[str] = None,
        heating_set_point_celsius: Optional[float] = None,
        heating_set_point_fahrenheit: Optional[float] = None,
        hvac_mode_setting: Optional[str] = None,
        manual_override_allowed: Optional[bool] = None,
        name: Optional[str] = None,
    ) -> None:
        """Updates a specified `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ for a specified `thermostat <https://docs.seam.co/capability-guides/thermostats>`_.

        :param climate_preset_key: Unique key to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

        :param device_id: ID of the thermostat device for which you want to update a climate preset.

        :param climate_preset_mode: The climate preset mode for the thermostat, based on the available climate preset modes reported by the device.

        :param cooling_set_point_celsius: Temperature to which the thermostat should cool (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param cooling_set_point_fahrenheit: Temperature to which the thermostat should cool (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param ecobee_metadata: Metadata specific to the Ecobee climate, if applicable.

        :param fan_mode_setting: Desired `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_, such as ``on``, ``auto``, or ``circulate``.

        :param heating_set_point_celsius: Temperature to which the thermostat should heat (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param heating_set_point_fahrenheit: Temperature to which the thermostat should heat (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

        :param hvac_mode_setting: Desired `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ setting, such as ``heat``, ``cool``, ``heat_cool``, or ``off``.

        :param manual_override_allowed: Deprecated: Use 'thermostat_schedule.is_override_allowed' Indicates whether a person at the thermostat can change the thermostat's settings. See `Specifying Manual Override Permissions <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-thermostat-schedules#specifying-manual-override-permissions>`_.

        :param name: User-friendly name to identify the `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_.

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                climate_preset_key is not None,
                device_id is not None,
                climate_preset_mode is not None,
                cooling_set_point_celsius is not None,
                cooling_set_point_fahrenheit is not None,
                ecobee_metadata is not None,
                fan_mode_setting is not None,
                heating_set_point_celsius is not None,
                heating_set_point_fahrenheit is not None,
                hvac_mode_setting is not None,
                manual_override_allowed is not None,
                name is not None,
            ]
        ):
            raise ValueError(
                "At least one parameter is required for /thermostats/update_climate_preset"
            )
        json_payload: Dict[str, Any] = {}

        if climate_preset_key is not None:
            json_payload["climate_preset_key"] = climate_preset_key
        if device_id is not None:
            json_payload["device_id"] = device_id
        if climate_preset_mode is not None:
            json_payload["climate_preset_mode"] = climate_preset_mode
        if cooling_set_point_celsius is not None:
            json_payload["cooling_set_point_celsius"] = cooling_set_point_celsius
        if cooling_set_point_fahrenheit is not None:
            json_payload["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if ecobee_metadata is not None:
            json_payload["ecobee_metadata"] = ecobee_metadata
        if fan_mode_setting is not None:
            json_payload["fan_mode_setting"] = fan_mode_setting
        if heating_set_point_celsius is not None:
            json_payload["heating_set_point_celsius"] = heating_set_point_celsius
        if heating_set_point_fahrenheit is not None:
            json_payload["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if hvac_mode_setting is not None:
            json_payload["hvac_mode_setting"] = hvac_mode_setting
        if manual_override_allowed is not None:
            json_payload["manual_override_allowed"] = manual_override_allowed
        if name is not None:
            json_payload["name"] = name

        self.client.patch("/thermostats/update_climate_preset", json=json_payload)

        return None

    @route_metadata(
        path="/thermostats/update_weekly_program",
        has_required_parameters=True,
        has_pagination=False,
    )
    def update_weekly_program(
        self,
        *,
        device_id: str,
        friday_program_id: Optional[str] = None,
        monday_program_id: Optional[str] = None,
        saturday_program_id: Optional[str] = None,
        sunday_program_id: Optional[str] = None,
        thursday_program_id: Optional[str] = None,
        tuesday_program_id: Optional[str] = None,
        wednesday_program_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Updates the thermostat weekly program for a thermostat device. To configure a weekly program, specify the ID of the daily program that you want to use for each day of the week. When you update a weekly program, the set of programs that you specify overwrites any previous weekly program for the thermostat.

        :param device_id: ID of the thermostat device for which you want to update the weekly program.

        :param friday_program_id: ID of the thermostat daily program to run on Fridays.

        :param monday_program_id: ID of the thermostat daily program to run on Mondays.

        :param saturday_program_id: ID of the thermostat daily program to run on Saturdays.

        :param sunday_program_id: ID of the thermostat daily program to run on Sundays.

        :param thursday_program_id: ID of the thermostat daily program to run on Thursdays.

        :param tuesday_program_id: ID of the thermostat daily program to run on Tuesdays.

        :param wednesday_program_id: ID of the thermostat daily program to run on Wednesdays.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(
            [
                device_id is not None,
                friday_program_id is not None,
                monday_program_id is not None,
                saturday_program_id is not None,
                sunday_program_id is not None,
                thursday_program_id is not None,
                tuesday_program_id is not None,
                wednesday_program_id is not None,
            ]
        ):
            raise ValueError(
                "At least one parameter is required for /thermostats/update_weekly_program"
            )
        json_payload: Dict[str, Any] = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if friday_program_id is not None:
            json_payload["friday_program_id"] = friday_program_id
        if monday_program_id is not None:
            json_payload["monday_program_id"] = monday_program_id
        if saturday_program_id is not None:
            json_payload["saturday_program_id"] = saturday_program_id
        if sunday_program_id is not None:
            json_payload["sunday_program_id"] = sunday_program_id
        if thursday_program_id is not None:
            json_payload["thursday_program_id"] = thursday_program_id
        if tuesday_program_id is not None:
            json_payload["tuesday_program_id"] = tuesday_program_id
        if wednesday_program_id is not None:
            json_payload["wednesday_program_id"] = wednesday_program_id

        res = self.client.post("/thermostats/update_weekly_program", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )
