import json
import hashlib
from aiohttp import web

async def healthcheck(request):
    """Return an empty JSON response."""
    return web.json_response({}, status=200)

async def hash_string(request):
    """Return SHA256 hash of provided string."""
    try:
        data = await request.json()
        input_string = data.get('string')
        if input_string is None:
            return web.json_response(
                {'validation_errors': 'Missing required field "string"'},
                status=400
            )
        hash_object = hashlib.sha256(input_string.encode())
        hash_hex = hash_object.hexdigest()
        return web.json_response({'hash_string': hash_hex})

    except json.JSONDecodeError:
        return web.json_response(
            {'validation_errors': 'Invalid JSON data'},
            status=400
        )
