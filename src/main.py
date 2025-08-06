from fastapi import FastAPI
from modules.users.api.routes import router as user_router
from modules.auth.api.routes import router as auth_router  # 👈 novo import

app = FastAPI()

# Rotas de usuários
app.include_router(user_router, prefix="/users", tags=["Users"])

# Rota de login
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
