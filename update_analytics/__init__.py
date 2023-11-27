import json
import logging

import azure.functions as func

import common.analysis

VALUES = ["minimum", "maximum", "average"]

def main(changes, readings: func.SqlRowList, analytics: func.Out[func.SqlRow]):
    # Calculate analytics
    calcs = common.analysis.analyse(readings)

    # Store analytics data
    rows = func.SqlRowList()
    for id, data in calcs.items():
        temperature =         { value: data["temperature"][value]       for value in VALUES }
        wind_speed =          { value: data["wind_speed"][value]        for value in VALUES }
        relative_humidity =   { value: data["relative_humidity"][value] for value in VALUES }
        co2 =                 { value: data["co2"][value]               for value in VALUES }
        rows.append(common.analysis.AnalysisEntry(id, temperature, wind_speed, relative_humidity, co2))

    analytics.set(rows)

    logging.info("Wrote analytics to database.")