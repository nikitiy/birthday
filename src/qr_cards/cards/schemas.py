from typing import Any, Dict, Optional

from pydantic import BaseModel


class CardCreateSchema(BaseModel):
    slug: str
    name: str
    description: str
    image: str
    custom_data: Optional[Dict[str, Any]]

    class Config:
        from_attributes = True


class CardReadSchema(CardCreateSchema):
    id: int

    class Config:
        from_attributes = True
