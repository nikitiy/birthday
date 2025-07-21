from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select

from qr_cards.cards.models import CardModel
from qr_cards.cards.schemas import CardReadSchema
from qr_cards.database.core import DbSession

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/cards/{card_slug}", response_class=HTMLResponse)
async def get_card_detail(request: Request, db_session: DbSession, card_slug: str):
    stmt = select(CardModel).where(CardModel.slug == card_slug)
    result = await db_session.execute(stmt)
    card = result.scalar_one_or_none()

    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")

    return templates.TemplateResponse(
        request=request, name="cards/index.html", context={"item": card}
    )
