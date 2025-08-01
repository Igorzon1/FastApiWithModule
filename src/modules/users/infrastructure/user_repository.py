from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import Session
from shared.database import Base
from modules.users.domain.models import UserCreate
from shared.security import hash_password

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(UserDB).filter(UserDB.email == email).first()
    
    def get_by_id(self, user_id: int):
        return self.db.query(UserDB).filter(UserDB.id == user_id).first()

    def get_all(self):
        return self.db.query(UserDB).all()

    def save(self, user_data: UserCreate):
        hashed_pw = hash_password(user_data.password)
        db_user = UserDB(
            username=user_data.username,
            email=user_data.email,
            password=hashed_pw
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def update(self, user_id: int, user_data: UserCreate):
        user = self.get_by_id(user_id)
        if not user:
            return None
        if user_data.username:
            user.username = user_data.username
        if user_data.email:
            user.email = user_data.email
        if user_data.password:
            user.password = hash_password(user_data.password)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user_id: int):
        user = self.get_by_id(user_id)
        if not user:
            return None
        self.db.delete(user)
        self.db.commit()
        return user
