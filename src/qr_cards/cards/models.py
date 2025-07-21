from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column

from qr_cards.database.core import Base


class CardModel(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    description: Mapped[str]
    image: Mapped[str]
    custom_data: Mapped[dict] = mapped_column(JSON)
