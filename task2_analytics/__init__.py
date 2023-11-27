import logging
import json

import azure.functions as func

import common.analysis

def main(req: func.HttpRequest, readings: func.SqlRowList) -> func.HttpResponse:
    # Calculate the analytics
    calcs = common.analysis.analyse(readings)

    # Return the analytics
    return func.HttpResponse(
        body=json.dumps(calcs),
        mimetype="application/json",
        status_code=200
    )