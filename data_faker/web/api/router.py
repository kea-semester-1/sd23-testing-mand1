from fastapi.routing import APIRouter

from data_faker.web.api import docs, faker

api_router = APIRouter()
api_router.include_router(docs.router)
api_router.include_router(faker.router, prefix="/faker", tags=["faker"])
