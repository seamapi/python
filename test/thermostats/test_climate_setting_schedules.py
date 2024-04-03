from seam import Seam
import datetime


def add_month_to_date(date: datetime.date, months: int) -> datetime.date:
    return datetime.datetime(
        date.year + int(date.month / 12), ((date.month % 12) + months), 1
    )


def test_climate_setting_schedules(seam: Seam):

    thermostat = seam.thermostats.list()[0]

    base_date = datetime.date.today()

    schedule_starts_at = add_month_to_date(base_date, months=1).isoformat()
    schedule_ends_at = add_month_to_date(base_date, months=2).isoformat()

    # Test Create
    climate_setting_schedule = seam.thermostats.climate_setting_schedules.create(
        device_id=thermostat.device_id,
        name="Vacation Setting",
        schedule_starts_at=schedule_starts_at,
        schedule_ends_at=schedule_ends_at,
        schedule_type="time_bound",
        automatic_heating_enabled=True,
        automatic_cooling_enabled=True,
        heating_set_point_fahrenheit=40,
        cooling_set_point_fahrenheit=80,
        manual_override_allowed=True,
    )

    assert climate_setting_schedule.name == "Vacation Setting"

    # Test List
    climate_setting_schedules = seam.thermostats.climate_setting_schedules.list(
        device_id=thermostat.device_id
    )
    assert len(climate_setting_schedules) == 1

    # Test Get
    climate_setting_schedule = seam.thermostats.climate_setting_schedules.get(
        climate_setting_schedule_id=climate_setting_schedule.climate_setting_schedule_id,
    )

    assert climate_setting_schedule.name == "Vacation Setting"

    # Test Update
    seam.thermostats.climate_setting_schedules.update(
        climate_setting_schedule_id=climate_setting_schedule.climate_setting_schedule_id,
        name="Vacation Setting 2",
    )

    updated_climate_setting_schedule = seam.thermostats.climate_setting_schedules.get(
        climate_setting_schedule_id=climate_setting_schedule.climate_setting_schedule_id,
    )

    assert updated_climate_setting_schedule.name == "Vacation Setting 2"

    # Test Delete
    deleted_climate_setting_schedule = seam.thermostats.climate_setting_schedules.delete(
        climate_setting_schedule_id=climate_setting_schedule.climate_setting_schedule_id,
    )

    assert deleted_climate_setting_schedule == None
