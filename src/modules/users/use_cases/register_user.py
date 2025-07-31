# src/modules/users/use_cases/register_user.py

from modules.users.domain.models import UserCreate
from modules.users.infrastructure.user_repository import UserRepository

def register_user(user_data: UserCreate, repo: UserRepository):
    existing_user = repo.get_by_email(user_data.email)
    if existing_user:
        raise ValueError("E-mail já está em uso.")
    
    new_user = repo.save(user_data)
    return new_user
