from aiohttp.web import Response
import json

def failure(exception):
    response = {'status': 'failed', 'reason': str(exception)}
    return Response(text=json.dumps(response), status=400)

def ok():
    return Response()