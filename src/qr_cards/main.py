from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin, ModelView

from src.qr_cards.cards.models import CardModel
from src.qr_cards.cards.views import router as card_router
from src.qr_cards.database.core import async_engine

load_dotenv()

app = FastAPI()

admin = Admin(app, engine=async_engine)


class CardAdmin(ModelView, model=CardModel):
    column_list = [CardModel.id, CardModel.name, CardModel.description]


admin.add_view(CardAdmin)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(card_router)
