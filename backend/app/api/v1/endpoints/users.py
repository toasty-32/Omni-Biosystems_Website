from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import get_current_user
from app.db.supabase_client import get_supabase
from app.schemas.user import UserProfile, UserProfileUpdate

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/me', response_model=UserProfile)
def get_me(current_user: dict = Depends(get_current_user)):
    db = get_supabase()
    user_id = current_user['sub']
    resp = db.table('profiles').select('*').eq('id', user_id).single().execute()
    if not resp.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Profile not found')
    return resp.data


@router.patch('/me', response_model=UserProfile)
def update_me(
    body: UserProfileUpdate,
    current_user: dict = Depends(get_current_user),
):
    db = get_supabase()
    user_id = current_user['sub']
    resp = (
        db.table('profiles')
        .update(body.model_dump(exclude_none=True))
        .eq('id', user_id)
        .single()
        .execute()
    )
    return resp.data
