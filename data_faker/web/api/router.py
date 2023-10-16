from fastapi.routing import APIRouter

from data_faker.web.api import docs, echo, monitoring, users

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(users.router, prefix="/users", tags=["user"])
