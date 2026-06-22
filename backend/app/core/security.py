import base64
import hashlib
import hmac
import json
import time
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .config import settings

bearer = HTTPBearer()


def _b64decode(s: str) -> bytes:
    # Add padding then decode URL-safe base64
    return base64.urlsafe_b64decode(s + '=' * (-len(s) % 4))


def decode_supabase_jwt(token: str) -> dict:
    parts = token.split('.')
    if len(parts) != 3:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token format')

    header_b64, payload_b64, sig_b64 = parts

    # Verify HMAC-SHA256 signature using stdlib only
    signing_input = f'{header_b64}.{payload_b64}'.encode()
    expected = hmac.new(settings.supabase_jwt_secret.encode(), signing_input, hashlib.sha256).digest()
    actual = _b64decode(sig_b64)
    if not hmac.compare_digest(expected, actual):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token signature')

    try:
        payload: dict = json.loads(_b64decode(payload_b64))
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Malformed token payload') from exc

    # Validate expiry
    if 'exp' in payload and payload['exp'] < time.time():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token expired')

    # Validate audience
    aud = payload.get('aud', '')
    if isinstance(aud, str):
        aud = [aud]
    if 'authenticated' not in aud:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token audience')

    return payload


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer),
) -> dict:
    return decode_supabase_jwt(credentials.credentials)
