from fastapi import APIRouter
from .migration_controller import router as migration
from .authentification_controller import router as authentication
from .user_controller import router as user
from .storage_controller import router as storage
from .address_controller import router as address
from .category_blog_controller import router as category_blog
from .category_product_controller import router as category_product
from .unit_product_controller import router as unit_product
from .blog_controller import router as blog 
api_router = APIRouter()

api_router.include_router(migration)
api_router.include_router(authentication)
api_router.include_router(user)
api_router.include_router(storage)
api_router.include_router(address)
api_router.include_router(category_blog)
api_router.include_router(category_product)
api_router.include_router(unit_product)
api_router.include_router(blog)