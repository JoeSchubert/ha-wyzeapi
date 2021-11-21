#!/usr/bin/python3

"""Platform for sensor integration."""

from datetime import datetime as dt, time, timedelta, timezone
import logging
from typing import Any, Callable, List

from wyzeapy import Wyzeapy
from wyzeapy.services.camera_service import Camera
from wyzeapy.services.lock_service import Lock
from wyzeapy.services.switch_service import SwitchUsage, SwitchUsageService

from homeassistant.components.sensor import STATE_CLASS_TOTAL_INCREASING, SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION, DEVICE_CLASS_BATTERY, DEVICE_CLASS_ENERGY, ENERGY_KILO_WATT_HOUR, PERCENTAGE
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect

from .const import CONF_CLIENT, DOMAIN, LOCK_UPDATED, CAMERA_UPDATED
from .token_manager import token_exception_handler

_LOGGER = logging.getLogger(__name__)
ATTRIBUTION = "Data provided by Wyze"
CAMERAS_WITH_BATTERIES = ["WVOD1"]
PLUGS_WITH_USAGE =["WLPPO"]

@token_exception_handler
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry,
                            async_add_entities: Callable[[List[Any], bool], None]) -> None:
    """
    This function sets up the config_entry

    :param hass: Home Assistant instance
    :param config_entry: The current config_entry
    :param async_add_entities: This function adds entities to the config_entry
    :return:
    """
    _LOGGER.debug("""Creating new WyzeApi sensor component""")
    client: Wyzeapy = hass.data[DOMAIN][config_entry.entry_id][CONF_CLIENT]

    # Get the list of locks so that we can create lock and keypad battery sensors
    lock_service = await client.lock_service
    camera_service = await client.camera_service
    switch_usage_service = await client.switch_usage_service

    locks = await lock_service.get_locks()
    sensors = []
    for lock in locks:
        sensors.append(WyzeLockBatterySensor(lock, WyzeLockBatterySensor.LOCK_BATTERY))
        sensors.append(WyzeLockBatterySensor(lock, WyzeLockBatterySensor.KEYPAD_BATTERY))

    cameras = await camera_service.get_cameras()
    for camera in cameras:
        if camera.product_model in CAMERAS_WITH_BATTERIES:
            sensors.append(WyzeCameraBatterySensor(camera))

    plugs = await switch_usage_service.get_switches()
    for plug in plugs:
        if plug.product_model in PLUGS_WITH_USAGE:
            sensors.append(WyzePlugUsageSensor(plug, switch_usage_service))

    async_add_entities(sensors, True)

class WyzeLockBatterySensor(SensorEntity):
    """Representation of a Wyze Lock or Lock Keypad Battery"""
    LOCK_BATTERY = "lock_battery"
    KEYPAD_BATTERY = "keypad_battery"

    _attr_device_class = DEVICE_CLASS_BATTERY
    _attr_native_unit_of_measurement = PERCENTAGE

    # make the battery unavailable by default, this will be toggled after the first upate from the battery entity that has battery data.
    _available = False

    def __init__(self, lock, battery_type):
        self._lock = lock
        self._battery_type = battery_type

    @callback
    def handle_lock_update(self, lock: Lock) -> None:
        self._lock = lock
        if self._lock.raw_dict.get("power") and self._battery_type == self.LOCK_BATTERY:
            self._available = True
        if self._lock.raw_dict.get("keypad", {}).get("power") and self._battery_type == self.KEYPAD_BATTERY:
            if self.enabled is False:
                self.enabled = True
            self._available = True
        self.async_write_ha_state()

    async def async_added_to_hass(self) -> None:
        self.async_on_remove(
            async_dispatcher_connect(
                self.hass,
                f"{LOCK_UPDATED}-{self._lock.mac}",
                self.handle_lock_update,
            )
        )

    @property
    def name(self) -> str:
        battery_type = self._battery_type.replace("_", " ").title()
        return f"{self._lock.nickname} {battery_type}"

    @property
    def unique_id(self):
        return f"{self._lock.nickname}.{self._battery_type}"

    @property
    def available(self) -> bool:
        return self._available

    @property
    def should_poll(self) -> bool:
        return False

    @property
    def entity_registry_enabled_default(self) -> bool:
        if self._battery_type == self.KEYPAD_BATTERY:
            # The keypad battery may not be available if the lock has no keypad
            return False
        # The battery voltage will always be available for the lock
        return True

    @property
    def device_info(self):
        return {
            "identifiers": {
                (DOMAIN, self._lock.mac)
            },
            "name": f"{self._lock.nickname}.{self._battery_type}",
            "type": f"lock.{self._battery_type}"
        }

    @property
    def device_state_attributes(self):
        """Return device attributes of the entity."""
        return {
            ATTR_ATTRIBUTION: ATTRIBUTION,
            "available": self.available,
            "device model": f"{self._lock.product_model}.{self._battery_type}",
        }

    @property
    def native_value(self):
        """Return the state of the device."""
        if self._battery_type == self.LOCK_BATTERY:
            return str(self._lock.raw_dict.get("power"))
        elif (self._battery_type == self.KEYPAD_BATTERY):
            return str(self._lock.raw_dict.get("keypad", {}).get("power"))
        return 0

class WyzeCameraBatterySensor(SensorEntity):
    """Representation of a Wyze Camera Battery"""
    _attr_device_class = DEVICE_CLASS_BATTERY
    _attr_native_unit_of_measurement = PERCENTAGE

    def __init__(self, camera):
        self._camera = camera

    @callback
    def handle_camera_update(self, camera: Camera) -> None:
        self._camera = camera
        self.async_write_ha_state()

    async def async_added_to_hass(self) -> None:
        self.async_on_remove(
            async_dispatcher_connect(
                self.hass,
                f"{CAMERA_UPDATED}-{self._camera.mac}",
                self.handle_camera_update,
            )
        )

    @property
    def name(self) -> str:
        return f"{self._camera.nickname} Battery"

    @property
    def unique_id(self):
        return f"{self._camera.nickname}.battery"

    @property
    def should_poll(self) -> bool:
        return False

    @property
    def device_info(self):
        return {
            "identifiers": {
                (DOMAIN, self._camera.mac)
            },
            "name": f"{self._camera.nickname}.battery",
            "type": "camera.battery"
        }

    @property
    def device_state_attributes(self):
        """Return device attributes of the entity."""
        return {
            ATTR_ATTRIBUTION: ATTRIBUTION,
            "available": self.available,
            "device model": f"{self._camera.product_model}.battery",
        }

    @property
    def native_value(self):
        return self._camera.device_params.get("electricity")


class WyzePlugUsageSensor(SensorEntity):
    """Representation of a Wyze Plug Usage History"""
    _attr_device_class = DEVICE_CLASS_ENERGY
    _attr_state_class = STATE_CLASS_TOTAL_INCREASING
    _attr_unit_of_measurement = ENERGY_KILO_WATT_HOUR
    SCAN_INTERVAL = timedelta(seconds=300) # update sensor every 5 minutes, this is independent of the updated data from wyzeapy
    _previous_value = 0
    _previous_hour = None
    _current_value = 0
    _should_reset = False

    def __init__(self, switch_usage: SwitchUsage, switch_usage_service: SwitchUsageService):
        self._switch_usage = switch_usage
        self._switch_usage_service = switch_usage_service

    @property
    def name(self) -> str:
        return f"{self._switch_usage.nickname} Usage History"

    @property
    def unique_id(self):
        return f"{self._switch_usage.nickname}.usage"

    @property
    def should_poll(self) -> bool:
        # lets have the sensor poll so that we can process the data more often than it comes in.
        return True

    @property
    def device_info(self):
        return {
            "identifiers": {
                (DOMAIN, self._switch_usage.mac)
            },
            "name": f"{self._switch_usage.nickname}.usage",
            "type": "plug.usage"
        }

    @property
    def device_state_attributes(self):
        """Return device attributes of the entity."""
        return {
            ATTR_ATTRIBUTION: ATTRIBUTION,
            "available": self.available,
            "device model": f"{self._switch_usage.product_model}.usage",
        }

    @callback
    def async_update_callback(self, _switch_usage: SwitchUsage):
        """Update the switch's state."""
        self._switch_usage = _switch_usage
        self.async_schedule_update_ha_state()

    async def async_added_to_hass(self) -> None:
        """Subscribe to update events."""
        self._switch_usage.callback_function = self.async_update_callback
        self._switch_usage_service.register_updater(self._switch_usage, 30) # Updates only appear to happen every ~20 minutes
        await self._switch_usage_service.start_update_manager()
        return await super().async_added_to_hass()

    async def async_will_remove_from_hass(self) -> None:
        self._switch_usage_service.unregister_updater()

    # Use an update function here so that we can poll the data more often than it comes in to handle old data coming in during a poll
    def update(self):
        if len(self._switch_usage._usage_history) > 0:
            current_hour = dt.now(timezone.utc).hour
            yesterday_millis = int(dt.timestamp(dt.combine(dt.utcnow(), time.min, tzinfo=timezone.utc) - timedelta(days=1)) * 1000)
            today_millis = int(dt.timestamp(dt.combine(dt.utcnow(), time.min, tzinfo=timezone.utc)) * 1000)
            if not self._should_reset:
                if not self._previous_hour:
                    # No previous hour stored, lets go ahead and set the _current_value to the current hour's stats
                    self._previous_hour = current_hour
                if self._previous_hour != current_hour:
                    if self._previous_hour == 23:
                        # We've started a new day, lets get the value from the last hour of the day before
                        if self._switch_usage._usage_history.get(yesterday_millis):
                            self._current_value = self._switch_usage._usage_history.get(yesterday_millis)[23] / 1000
                    else:
                        # We've started a new hour, lets get the value of the previous hour 1 more time to make sure we have the latest value
                        if self._switch_usage._usage_history.get(today_millis):
                            self._current_value = self._switch_usage._usage_history.get(today_millis)[current_hour - 1] / 1000
                if self._previous_hour == current_hour:
                    # We're still in the same hour, lets just update the current value
                    if self._switch_usage._usage_history.get(today_millis):
                        self._current_value = self._switch_usage._usage_history.get(today_millis)[current_hour] / 1000
                if self._previous_value == self._current_value and self._previous_hour != current_hour:
                    # We've moved on to a new hour and the values haven't changed, lets reset the values for a new hour
                    self._should_reset = True
                self._previous_value = self._current_value
                self._previous_hour = current_hour
            else:
                # Trigger the reset by setting the current value to 0 and toggling the reset flag
                self._should_reset = False
                self._current_value = 0

    @property
    def native_value(self):
        return self._current_value
