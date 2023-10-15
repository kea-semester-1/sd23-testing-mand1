from importlib import metadata
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from fastapi.staticfiles import StaticFiles

from data_faker.logging import configure_logging
from data_faker.web.api.router import api_router
from data_faker.web.lifetime import register_shutdown_event, register_startup_event

from data_faker import constants

APP_ROOT = Path(__file__).parent.parent


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    configure_logging()
    app = FastAPI(
        title="data_faker",
        version=metadata.version("data_faker"),
        openapi_url=f"{constants.API_PREFIX}/openapi.json",
        docs_url=f"{constants.API_PREFIX}/docs",
        redoc_url=f"{constants.API_PREFIX}/redoc",
        default_response_class=UJSONResponse,
    )

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")
    # Adds static directory.
    # This directory is used to access swagger files.
    app.mount(
        "/static",
        StaticFiles(directory=APP_ROOT / "static"),
        name="static",
    )

    return app
