from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from modules.auth.infrastructure.jwt_service import create_access_token
from modules.auth.domain.models import LoginInput, TokenResponse
from modules.users.infrastructure.user_repository import UserRepository

# Para verificar senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def login_user(login_data: LoginInput, db: Session) -> TokenResponse:
    # Busca o usuário pelo email
    user_repo = UserRepository(db)
    user = user_repo.get_by_email(login_data.email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
        )

    # Verifica se a senha está correta
    if not verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
        )

    # Gera token com o email do usuário
    token_data = {"sub": user.email}
    token = create_access_token(token_data)

    return TokenResponse(access_token=token)
