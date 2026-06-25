from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, status, Depends
from app.core.security import get_current_user
from app.db.firebase_client import get_db
from app.schemas.sample import Sample, SampleCreate, SampleUpdate

router = APIRouter(prefix='/samples', tags=['samples'])


def _doc_to_sample(doc) -> Sample:
    data = doc.to_dict()
    return Sample(
        id=doc.id,
        name=data['name'],
        type=data['type'],
        status=data['status'],
        collected_at=data['collected_at'],
        processed_at=data.get('processed_at'),
        owner_id=data['owner_id'],
        metadata=data.get('metadata', {}),
        created_at=data['created_at'],
    )


@router.get('', response_model=list[Sample])
def list_samples(current_user: dict = Depends(get_current_user)):
    db = get_db()
    docs = (
        db.collection('samples')
        .where('owner_id', '==', current_user['uid'])
        .order_by('collected_at', direction='DESCENDING')
        .stream()
    )
    return [_doc_to_sample(d) for d in docs]


@router.post('', response_model=Sample, status_code=status.HTTP_201_CREATED)
def create_sample(body: SampleCreate, current_user: dict = Depends(get_current_user)):
    db = get_db()
    payload = {
        **body.model_dump(),
        'owner_id': current_user['uid'],
        'status': 'pending',
        'created_at': datetime.now(timezone.utc),
        'processed_at': None,
    }
    ref = db.collection('samples').document()
    ref.set(payload)
    return _doc_to_sample(ref.get())


@router.get('/{sample_id}', response_model=Sample)
def get_sample(sample_id: str, current_user: dict = Depends(get_current_user)):
    db = get_db()
    doc = db.collection('samples').document(sample_id).get()
    if not doc.exists or doc.to_dict().get('owner_id') != current_user['uid']:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sample not found')
    return _doc_to_sample(doc)


@router.patch('/{sample_id}', response_model=Sample)
def update_sample(sample_id: str, body: SampleUpdate, current_user: dict = Depends(get_current_user)):
    db = get_db()
    ref = db.collection('samples').document(sample_id)
    doc = ref.get()
    if not doc.exists or doc.to_dict().get('owner_id') != current_user['uid']:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sample not found')
    ref.update(body.model_dump(exclude_none=True))
    return _doc_to_sample(ref.get())


@router.delete('/{sample_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_sample(sample_id: str, current_user: dict = Depends(get_current_user)):
    db = get_db()
    ref = db.collection('samples').document(sample_id)
    doc = ref.get()
    if not doc.exists or doc.to_dict().get('owner_id') != current_user['uid']:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sample not found')
    ref.delete()
