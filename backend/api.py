from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI


api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

api.add_router('/core/', 'backend.core.api.router')
api.add_router('/crm/', 'backend.crm.api.router')
api.add_router('/todo/', 'backend.todo.api.router')
