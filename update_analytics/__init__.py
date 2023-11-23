import json
import logging

import azure.functions as func

from common.analysis import AnalysisEntry

FIELDS = ["temperature", "wind_speed", "relative_humidity", "co2"]
VALUES = ["minimum", "maximum", "average"]

def main(changes, readings: func.SqlRowList, analytics: func.Out[func.SqlRow]):
    # Get total, minimum, maximum
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
    
    # Store analytics data
    rows = func.SqlRowList()
    for id, data in calcs.items():
        temperature =         { value: data["temperature"][value]       for value in VALUES }
        wind_speed =          { value: data["wind_speed"][value]        for value in VALUES }
        relative_humidity =   { value: data["relative_humidity"][value] for value in VALUES }
        co2 =                 { value: data["co2"][value]               for value in VALUES }
        rows.append(AnalysisEntry(id, temperature, wind_speed, relative_humidity, co2))

    analytics.set(rows)

    logging.info("Wrote analytics to database.")