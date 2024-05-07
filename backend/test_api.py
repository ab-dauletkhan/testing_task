import pytest
from aiohttp import web
from .routes import setup_routes  # Adjust based on your actual import paths
import hashlib


@pytest.fixture
async def app():
    app = web.Application()
    setup_routes(app)
    return app


@pytest.fixture
async def cli(aiohttp_client, app):
    return await aiohttp_client(app)


@pytest.mark.asyncio
async def test_healthcheck(cli):
    resp = await cli.get("/healthcheck")
    assert resp.status == 200
    json_response = await resp.json()
    assert json_response == {}


@pytest.mark.asyncio
async def test_hash_post_with_string(cli):
    payload = {"string": "hello"}
    expected_hash = hashlib.sha256(payload["string"].encode()).hexdigest()
    resp = await cli.post("/hash", json=payload)
    assert resp.status == 200
    result = await resp.json()
    assert result["hash_string"] == expected_hash


@pytest.mark.asyncio
async def test_hash_post_without_string(cli):
    resp = await cli.post("/hash", json={})
    assert resp.status == 400
    result = await resp.json()
    assert "validation_errors" in result
    assert result["validation_errors"] == 'Missing required field "string"'
