from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import get_current_user
from app.db.supabase_client import get_supabase
from app.schemas.sample import Sample, SampleCreate, SampleUpdate

router = APIRouter(prefix='/samples', tags=['samples'])


@router.get('/', response_model=list[Sample])
def list_samples(current_user: dict = Depends(get_current_user)):
    db = get_supabase()
    user_id = current_user['sub']
    resp = db.table('samples').select('*').eq('owner_id', user_id).order('collected_at', desc=True).execute()
    return resp.data


@router.post('/', response_model=Sample, status_code=status.HTTP_201_CREATED)
def create_sample(body: SampleCreate, current_user: dict = Depends(get_current_user)):
    db = get_supabase()
    payload = {**body.model_dump(), 'owner_id': current_user['sub'], 'status': 'pending'}
    resp = db.table('samples').insert(payload).single().execute()
    return resp.data


@router.get('/{sample_id}', response_model=Sample)
def get_sample(sample_id: str, current_user: dict = Depends(get_current_user)):
    db = get_supabase()
    resp = db.table('samples').select('*').eq('id', sample_id).eq('owner_id', current_user['sub']).single().execute()
    if not resp.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sample not found')
    return resp.data


@router.patch('/{sample_id}', response_model=Sample)
def update_sample(
    sample_id: str,
    body: SampleUpdate,
    current_user: dict = Depends(get_current_user),
):
    db = get_supabase()
    resp = (
        db.table('samples')
        .update(body.model_dump(exclude_none=True))
        .eq('id', sample_id)
        .eq('owner_id', current_user['sub'])
        .single()
        .execute()
    )
    if not resp.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sample not found')
    return resp.data


@router.delete('/{sample_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_sample(sample_id: str, current_user: dict = Depends(get_current_user)):
    db = get_supabase()
    db.table('samples').delete().eq('id', sample_id).eq('owner_id', current_user['sub']).execute()
