from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.db.supabase_client import get_supabase
from app.schemas.analysis import DashboardStats

router = APIRouter(prefix='/dashboard', tags=['dashboard'])


@router.get('/stats', response_model=DashboardStats)
def get_stats(current_user: dict = Depends(get_current_user)):
    db = get_supabase()
    user_id = current_user['sub']

    samples = db.table('samples').select('status').eq('owner_id', user_id).execute().data
    total = len(samples)
    pending = sum(1 for s in samples if s['status'] == 'pending')
    completed = sum(1 for s in samples if s['status'] == 'completed')

    sample_ids = [s['id'] for s in db.table('samples').select('id').eq('owner_id', user_id).execute().data]
    flagged = 0
    if sample_ids:
        flagged_resp = (
            db.table('analysis_results')
            .select('id')
            .in_('sample_id', sample_ids)
            .eq('flagged', True)
            .execute()
        )
        flagged = len(flagged_resp.data)

    return DashboardStats(
        total_samples=total,
        pending_samples=pending,
        completed_samples=completed,
        flagged_results=flagged,
    )
