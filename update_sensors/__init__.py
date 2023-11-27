import azure.functions as func

import common.sensor

NUMBER_OF_SENSORS = 20

def main(mytimer: func.TimerRequest, sensors: func.Out[func.SqlRowList]) -> None:
    generated = common.sensor.generate(NUMBER_OF_SENSORS)
    sensors.set(generated)