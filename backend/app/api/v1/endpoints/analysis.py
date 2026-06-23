from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, status, Depends
from app.core.security import get_current_user
from app.db.firebase_client import get_db
from app.schemas.analysis import AnalysisResult, AnalysisResultCreate

router = APIRouter(prefix='/analysis', tags=['analysis'])


def _doc_to_result(doc) -> AnalysisResult:
    data = doc.to_dict()
    return AnalysisResult(
        id=doc.id,
        sample_id=data['sample_id'],
        result_type=data['result_type'],
        value=data['value'],
        unit=data['unit'],
        reference_range=data.get('reference_range'),
        flagged=data.get('flagged', False),
        created_at=data['created_at'],
    )


def _assert_sample_owner(db, sample_id: str, uid: str):
    doc = db.collection('samples').document(sample_id).get()
    if not doc.exists or doc.to_dict().get('owner_id') != uid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sample not found')


@router.get('/samples/{sample_id}/results', response_model=list[AnalysisResult])
def list_results(sample_id: str, current_user: dict = Depends(get_current_user)):
    db = get_db()
    _assert_sample_owner(db, sample_id, current_user['uid'])
    docs = db.collection('analysis_results').where('sample_id', '==', sample_id).stream()
    return [_doc_to_result(d) for d in docs]


@router.post('/samples/{sample_id}/results', response_model=AnalysisResult, status_code=status.HTTP_201_CREATED)
def create_result(sample_id: str, body: AnalysisResultCreate, current_user: dict = Depends(get_current_user)):
    db = get_db()
    _assert_sample_owner(db, sample_id, current_user['uid'])
    payload = {**body.model_dump(), 'sample_id': sample_id, 'created_at': datetime.now(timezone.utc)}
    ref = db.collection('analysis_results').document()
    ref.set(payload)
    return _doc_to_result(ref.get())
