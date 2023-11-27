import collections

import azure.functions as func

FIELDS = ["temperature", "wind_speed", "relative_humidity", "co2"]

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

def analyse(readings: func.SqlRowList) -> dict:
	"""Calculate analytics from the given readings."""
	calcs = {}

	for row in readings:
		item = row.data
		id = item["sensor_id"]

		if item["sensor_id"] not in calcs:
			calcs[id] = {f: dict(total=0, minimum=9999, maximum=0, readings=0) for f in FIELDS}
			for field in FIELDS:
				calcs[id][field]["readings"] += 1
				calcs[id][field]["total"] += item[field]
				if item[field] < calcs[id][field]["minimum"]:
					calcs[id][field]["minimum"] = item[field]
				if item[field] > calcs[id][field]["maximum"]:
					calcs[id][field]["maximum"] = item[field]

	# Calculate averages
	for id in calcs:
		for field in FIELDS:
			calcs[id][field]["average"] = calcs[id][field]["total"] / calcs[id][field]["readings"]
	
	return calcs

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