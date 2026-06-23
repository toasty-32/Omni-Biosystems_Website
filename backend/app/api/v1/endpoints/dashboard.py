from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.db.firebase_client import get_db
from app.schemas.analysis import DashboardStats

router = APIRouter(prefix='/dashboard', tags=['dashboard'])


@router.get('/stats', response_model=DashboardStats)
def get_stats(current_user: dict = Depends(get_current_user)):
    db = get_db()
    uid = current_user['uid']

    samples = list(db.collection('samples').where('owner_id', '==', uid).stream())
    total = len(samples)
    pending = sum(1 for s in samples if s.to_dict()['status'] == 'pending')
    completed = sum(1 for s in samples if s.to_dict()['status'] == 'completed')

    sample_ids = [s.id for s in samples]
    flagged = 0
    if sample_ids:
        # Firestore 'in' supports up to 30 items per query
        for i in range(0, len(sample_ids), 30):
            chunk = sample_ids[i:i + 30]
            results = (
                db.collection('analysis_results')
                .where('sample_id', 'in', chunk)
                .where('flagged', '==', True)
                .stream()
            )
            flagged += sum(1 for _ in results)

    return DashboardStats(
        total_samples=total,
        pending_samples=pending,
        completed_samples=completed,
        flagged_results=flagged,
    )
