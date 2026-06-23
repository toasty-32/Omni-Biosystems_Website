from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, status, Depends
from app.core.security import get_current_user
from app.db.firebase_client import get_db
from app.schemas.user import UserProfile, UserProfileUpdate

router = APIRouter(prefix='/users', tags=['users'])


def _doc_to_profile(uid: str, data: dict) -> UserProfile:
    return UserProfile(
        uid=uid,
        email=data.get('email', ''),
        display_name=data.get('display_name'),
        role=data.get('role', 'viewer'),
        organization=data.get('organization'),
        created_at=data.get('created_at', datetime.now(timezone.utc)),
    )


@router.get('/me', response_model=UserProfile)
def get_me(current_user: dict = Depends(get_current_user)):
    db = get_db()
    uid = current_user['uid']
    doc = db.collection('users').document(uid).get()
    if not doc.exists:
        # Auto-create profile on first access
        payload = {
            'email': current_user.get('email', ''),
            'role': 'viewer',
            'created_at': datetime.now(timezone.utc),
        }
        db.collection('users').document(uid).set(payload)
        return _doc_to_profile(uid, payload)
    return _doc_to_profile(uid, doc.to_dict())


@router.patch('/me', response_model=UserProfile)
def update_me(body: UserProfileUpdate, current_user: dict = Depends(get_current_user)):
    db = get_db()
    uid = current_user['uid']
    ref = db.collection('users').document(uid)
    ref.update(body.model_dump(exclude_none=True))
    doc = ref.get()
    return _doc_to_profile(uid, doc.to_dict())
