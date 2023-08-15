from fastapi import APIRouter

from app.api.endpoints.debug import router as debug_router

routers = APIRouter()
router_list = [debug_router]

for router in router_list:
    routers.include_router(router)
