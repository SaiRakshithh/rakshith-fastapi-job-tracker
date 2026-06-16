
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from fastapi_users import schemas
import uuid

class PostCreate(BaseModel):
    caption: str  # Changed from 'title' to 'caption' to match your upload

class PostResponse(BaseModel):
    id: uuid.UUID
    caption: str
    url: str
    file_type: str
    file_name: str
    created_at: datetime
    user_id: uuid.UUID
    
class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass