from fastapi import APIRouter, Header, HTTPException
from app.utils.jwt_utils import decode_token
from app.services.payment_service import list_user_payments_logic

payment_router = APIRouter()


@payment_router.get("/my-payments")
def get_my_payments(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Formato Bearer inválido")

    token = authorization.replace("Bearer ", "")
    user = decode_token(token)

    # Validación robusta del token
    if not user or "email" not in user:
        raise HTTPException(status_code=403, detail="Token inválido o expirado")

    email = user["email"]
    return list_user_payments_logic(email)
