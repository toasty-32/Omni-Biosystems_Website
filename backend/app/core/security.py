from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth as firebase_auth
from app.db.firebase_client import get_firebase_app  # ensures app is initialised

bearer = HTTPBearer()

# Keep the unused import to guarantee initialisation before first request
_ = get_firebase_app


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer),
) -> dict:
    try:
        decoded = firebase_auth.verify_id_token(credentials.credentials)
        return decoded
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid or expired token',
        ) from exc
