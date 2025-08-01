from modules.users.domain.models import UserUpdate
from modules.users.infrastructure.user_repository import UserRepository

def update_user(user_id: int, user_data: UserUpdate, repo: UserRepository):
    user = repo.update(user_id, user_data)
    if not user:
        raise ValueError("Usuário não encontrado para atualizar.")
    return user
