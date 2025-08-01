from modules.users.infrastructure.user_repository import UserRepository

def get_user_by_id(user_id: int, repo: UserRepository):
    user = repo.get_by_id(user_id)
    if not user:
        raise ValueError("Usuário não encontrado.")
    return user
