from fastapi import HTTPException
from app.database import payments


def list_user_payments_logic(email: str):
    user_payments = list(payments.find({"user_email": email}).sort("timestamp", -1))
    if not user_payments:
        raise HTTPException(status_code=404, detail="No se encontraron pagos")

    for p in user_payments:
        p["_id"] = str(p["_id"])
        p["timestamp"] = p["timestamp"].isoformat() if "timestamp" in p else None
    return user_payments
