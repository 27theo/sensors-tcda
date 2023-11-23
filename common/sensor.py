import collections

class Sensor(collections.UserDict):
	"""Class to represent a sensor."""
	def __init__(self, sensor_id, timestamp, temperature, wind_speed, relative_humidity, co2):
		super().__init__()

		self["sensor_id"] = sensor_id
		self["timestamp"] = timestamp
		self["temperature"] = temperature
		self["wind_speed"] = wind_speed
		self["relative_humidity"] = relative_humidity
		self["co2"] = co2

"""
create table sensors(
	sensor_id int NOT NULL,
	timestamp datetime2(0) NOT NULL,
	temperature float NOT NULL,
	wind_speed float NOT NULL,
	relative_humidity float NOT NULL,
	co2 float NOT NULL,
	CONSTRAINT PK_sensors PRIMARY KEY (sensor_id, timestamp)
);

select * from sensors where timestamp = '2023-11-23T11:08:20.0000000';

alter database "env-leeds-sensor-db"
set CHANGE_TRACKING = ON
(CHANGE_RETENTION = 1 HOURS, AUTO_CLEANUP = ON);

alter table sensors 
enable CHANGE_TRACKING 
with (TRACK_COLUMNS_UPDATED = ON);
"""