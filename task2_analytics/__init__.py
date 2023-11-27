import logging
import json

import azure.functions as func

FIELDS = ["temperature", "wind_speed", "relative_humidity", "co2"]

import common.analysis

def main(req: func.HttpRequest, readings: func.SqlRowList) -> func.HttpResponse:
	# Calculate the analytics
	calcs = common.analysis.analyse(readings)

	for id in calcs.keys():
		for field in calcs[id].keys():
			# Remove the "total" and "readings" keys
			calcs[id][field].pop("total")
			calcs[id][field].pop("readings")

	# Return the analytics
	return func.HttpResponse(
		body=json.dumps(calcs),
		mimetype="application/json",
		status_code=200
	)