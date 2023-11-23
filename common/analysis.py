import collections

class AnalysisEntry(collections.UserDict):
	"""Class to represent a sensor."""
	def __init__(self, sensor_id, temperature: dict, wind_speed: dict, relative_humidity: dict, co2: dict):
		super().__init__()
		
		self["sensor_id"] = sensor_id

		for value in ["average", "minimum", "maximum"]:
			self["temperature_" + value] = temperature[value]
			self["wind_speed_" + value] = wind_speed[value]
			self["relative_humidity_" + value] = relative_humidity[value]
			self["co2_" + value] = co2[value]

"""
create table analytics(
	sensor_id int NOT NULL,

	temperature_average float NOT NULL,
	temperature_minimum float NOT NULL,
	temperature_maximum float NOT NULL,

	wind_speed_average float NOT NULL,
	wind_speed_minimum float NOT NULL,
	wind_speed_maximum float NOT NULL,

	relative_humidity_average float NOT NULL,
	relative_humidity_minimum float NOT NULL,
	relative_humidity_maximum float NOT NULL,

	co2_average float NOT NULL,
	co2_minimum float NOT NULL,
	co2_maximum float NOT NULL,

	CONSTRAINT PK_analytics PRIMARY KEY (sensor_id)
);
"""