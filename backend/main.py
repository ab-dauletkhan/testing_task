import click
from aiohttp import web
import routes

app = web.Application()
routes.setup_routes(app)

@click.command()
@click.option('--host', default='0.0.0.0', help='Host to bind to.')
@click.option('--port', default=8080, help='Port to bind to.')
def run_server(host, port):
    """Run the aiohttp server."""
    web.run_app(app, host=host, port=port)

if __name__ == '__main__':
    run_server()
