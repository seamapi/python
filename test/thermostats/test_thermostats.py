from seam import Seam
import json


def test_thermostats(seam: Seam):

    # Test List
    thermostats = seam.thermostats.list()

    thermostat = thermostats[0]

    assert thermostat.device_type == "ecobee_thermostat"

    # Test Get
    thermostat = seam.thermostats.get(device_id=thermostat.device_id)
    assert thermostat.device_type == "ecobee_thermostat"

    # Test Update
    result = seam.thermostats.update(
        device_id=thermostat.device_id,
        default_climate_setting={
            "hvac_mode_setting": "cool",
            "cooling_set_point_celsius": 20,
            "manual_override_allowed": True,
        },
    )
    assert result == None

    # Test Cool
    seam.thermostats.cool(
        device_id=thermostat.device_id,
        cooling_set_point_celsius=27,
    )
    thermostat = seam.thermostats.get(device_id=thermostat.device_id)
    assert (
        round(thermostat.properties.current_climate_setting.cooling_set_point_celsius)
        == 27
    )
    assert thermostat.properties.current_climate_setting.hvac_mode_setting == "cool"

    # Test Heat
    seam.thermostats.heat(
        device_id=thermostat.device_id,
        heating_set_point_celsius=18,
    )
    thermostat = seam.thermostats.get(device_id=thermostat.device_id)
    assert (
        round(thermostat.properties.current_climate_setting.heating_set_point_celsius)
        == 18
    )

    # Test Heat Cool
    seam.thermostats.heat_cool(
        device_id=thermostat.device_id,
        cooling_set_point_celsius=28,
        heating_set_point_celsius=19,
    )
    thermostat = seam.thermostats.get(device_id=thermostat.device_id)
    assert (
        thermostat.properties.current_climate_setting.hvac_mode_setting == "heat_cool"
    )
    assert (
        round(thermostat.properties.current_climate_setting.cooling_set_point_celsius)
        == 28
    )
    assert (
        round(thermostat.properties.current_climate_setting.heating_set_point_celsius)
        == 19
    )

    # Test Off
    seam.thermostats.off(
        device_id=thermostat.device_id,
    )
    thermostat = seam.thermostats.get(device_id=thermostat.device_id)
    assert thermostat.properties.current_climate_setting.hvac_mode_setting == "off"

    # Test Set Fan Mode
    seam.thermostats.set_fan_mode(
        device_id=thermostat.device_id,
        fan_mode="on",
        fan_mode_setting="auto",
    )
    thermostat = seam.thermostats.get(device_id=thermostat.device_id)
    assert thermostat.properties.is_fan_running == True
