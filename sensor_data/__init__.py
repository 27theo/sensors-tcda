import logging

import azure.functions as func
import json

def main(req: func.HttpRequest, sensors: func.SqlRowList) -> func.HttpResponse:
    rows = list(map(lambda r: json.loads(r.to_json()), sensors))
    return func.HttpResponse(
        json.dumps(rows),
        status_code=200,
        mimetype="application/json"
    )