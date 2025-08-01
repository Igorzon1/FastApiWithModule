from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from shared.database import get_db
from modules.users.infrastructure.user_repository import UserRepository
from modules.users.domain.models import UserCreate, UserOut, UserUpdate

from modules.users.use_cases.register_user import register_user
from modules.users.use_cases.get_user_by_id import get_user_by_id
from modules.users.use_cases.get_all_user import get_all_users
from modules.users.use_cases.update_user import update_user
from modules.users.use_cases.delete_user import delete_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    try:
        return register_user(user, repo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return get_all_users(repo)

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    try:
        return get_user_by_id(user_id, repo)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{user_id}", response_model=UserOut)
def update_user_data(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    try:
        return update_user(user_id, user, repo)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{user_id}")
def delete_user_data(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    try:
        return delete_user(user_id, repo)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
