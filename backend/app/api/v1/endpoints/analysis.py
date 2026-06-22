from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import get_current_user
from app.db.supabase_client import get_supabase
from app.schemas.analysis import AnalysisResult, AnalysisResultCreate

router = APIRouter(prefix='/analysis', tags=['analysis'])


@router.get('/samples/{sample_id}/results', response_model=list[AnalysisResult])
def list_results(sample_id: str, current_user: dict = Depends(get_current_user)):
    db = get_supabase()
    sample = db.table('samples').select('id').eq('id', sample_id).eq('owner_id', current_user['sub']).single().execute()
    if not sample.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sample not found')
    resp = db.table('analysis_results').select('*').eq('sample_id', sample_id).execute()
    return resp.data


@router.post('/samples/{sample_id}/results', response_model=AnalysisResult, status_code=status.HTTP_201_CREATED)
def create_result(
    sample_id: str,
    body: AnalysisResultCreate,
    current_user: dict = Depends(get_current_user),
):
    db = get_supabase()
    payload = {**body.model_dump(), 'sample_id': sample_id}
    resp = db.table('analysis_results').insert(payload).single().execute()
    return resp.data
