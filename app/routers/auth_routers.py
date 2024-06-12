from fastapi import APIRouter, HTTPException
from datetime import timedelta
from pydantic import BaseModel
from app.auth.security import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, Token, API_KEY

class TokenRequest(BaseModel):
    api_key: str

auth_router = APIRouter()

@auth_router.post('/token', tags=['auth'], response_model=Token)
def login_for_access_token(form_data: TokenRequest):
    if form_data.api_key != API_KEY:
        raise HTTPException(
            status_code=400, detail="Incorrect API Key"
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": "api_user"}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}