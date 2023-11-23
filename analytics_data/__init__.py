import logging
import json

import azure.functions as func


def main(req: func.HttpRequest, analytics: func.SqlRowList) -> func.HttpResponse:
    rows = list(map(lambda r: json.loads(r.to_json()), analytics))
    return func.HttpResponse(
        json.dumps(rows),
        status_code=200,
        mimetype="application/json"
    )