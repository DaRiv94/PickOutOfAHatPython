import logging
import json

import azure.functions as func

#For Docs Info see
#https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings?tabs=python
#https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-output?tabs=python

def main(req: func.HttpRequest, boardgameTable: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    boardgame_name=''

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        boardgame_name = req_body.get('boardgame_name')

    if not boardgame_name:
        return func.HttpResponse(
        "please pass 'boardgame_name' in post body",
        status_code=400
        )

    data = {
        "game": boardgame_name,
        "PartitionKey": "boardgames",
        "RowKey": f"r_{boardgame_name}"
    }

    boardgameTable.set(json.dumps(data))

    return func.HttpResponse(
        json.dumps({"new_game":data}),
        status_code=200,
        mimetype="application/json"
    )
