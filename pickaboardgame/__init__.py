import logging
import random
import json
import azure.functions as func

#For Docs Info see
#https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings?tabs=python
#https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-table-input?tabs=python#example


def main(req: func.HttpRequest, boardgameTableData) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    list_of_games = json.loads(boardgameTableData)

    i = random.randint(0,(len(list_of_games)-1))

    board_game = {"game": list_of_games[i]}
    json_response_body = json.dumps(board_game)
    return func.HttpResponse(
        json_response_body,
        status_code=200,
        mimetype="application/json"
    )


