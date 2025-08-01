from modules.users.infrastructure.user_repository import UserRepository

def delete_user(user_id: int, repo: UserRepository):
    result = repo.delete(user_id)
    if not result:
        raise ValueError("Usuário não encontrado para deletar.")
    return {"detail": "Usuário deletado com sucesso."}
