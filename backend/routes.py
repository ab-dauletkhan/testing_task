from .views import healthcheck, hash_string


def setup_routes(app):
    app.router.add_get("/healthcheck", healthcheck)
    app.router.add_post("/hash", hash_string)
