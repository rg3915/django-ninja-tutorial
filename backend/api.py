from ninja import NinjaAPI

from backend.core.api import router as core_router
from backend.todo.api import router as todo_router

api = NinjaAPI()

api.add_router("/core/", core_router)
api.add_router("/todo/", todo_router)
