from jose import jwt, JWTError
from app.config import SECRET_KEY


def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except JWTError as e:
        print("Error al decodificar token:", e)
        return None
