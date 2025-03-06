from fastapi import FastAPI

from backend.app.config.settings import Settings
from backend.app.routes import restaurant_router
from backend.app.routes import menu_router
from backend.app.routes import user_router
from backend.app.routes import vote_router
from backend.app.routes import auth_router

app = FastAPI(title="Lunch voting")

print(Settings().BASE_DIR)
print(Settings().PATH_TO_DB)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(restaurant_router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(menu_router, prefix="/menus", tags=["Menus"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(vote_router, prefix="/votes", tags=["Votes"])
