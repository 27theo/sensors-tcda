import datetime
import logging
import random

import azure.functions as func

from common.sensor import Sensor

TEMP_RANGE = (8, 15)
WIND_SPEED_RANGE = (15, 25)
HUMIDITY_RANGE = (40, 70)
CO2_RANGE = (500, 1500)

NUMBER_OF_SENSORS = 20

def main(mytimer: func.TimerRequest, sensors: func.Out[func.SqlRowList]) -> None:
    start = datetime.datetime.now()

    rows = func.SqlRowList()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for i in range(NUMBER_OF_SENSORS):
        temperature = random.uniform(*TEMP_RANGE)
        wind_speed = random.uniform(*WIND_SPEED_RANGE)
        relative_humidity = random.uniform(*HUMIDITY_RANGE)
        co2 = random.uniform(*CO2_RANGE)

        rows.append(
            func.SqlRow(Sensor(i, timestamp, temperature, wind_speed, relative_humidity, co2))
        )
    
    sensors.set(rows)

    duration = datetime.datetime.now() - start

    logging.info("Finished writing to database. Total time to create %s rows = %s",
                 str(NUMBER_OF_SENSORS), str(duration))