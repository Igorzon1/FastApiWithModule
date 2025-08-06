from pydantic import BaseModel, EmailStr

# Entrada: o que o usuário envia no login
class LoginInput(BaseModel):
    email: EmailStr
    password: str

# Saída: o que o sistema retorna ao fazer login
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
