import logging

import azure.functions as func

"""
Clears the sensors database every 3 hours.
"""

def main(mytimer: func.TimerRequest, deleted: func.SqlRowList) -> None:
    logging.info("Cleared sensor database.")