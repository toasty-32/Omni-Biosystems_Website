from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from app.main import app

FAKE_USER = {'sub': 'user-uuid-1234', 'email': 'test@example.com'}

FAKE_SAMPLE = {
    'id': 'sample-uuid-1',
    'name': 'Test Blood Draw',
    'type': 'blood',
    'status': 'pending',
    'collected_at': '2025-01-01T00:00:00+00:00',
    'processed_at': None,
    'owner_id': 'user-uuid-1234',
    'metadata': {},
    'created_at': '2025-01-01T00:00:00+00:00',
}


def make_client():
    from app.core import security

    def override_auth():
        return FAKE_USER

    app.dependency_overrides[security.get_current_user] = override_auth
    return TestClient(app)


def test_list_samples_empty():
    client = make_client()
    mock_db = MagicMock()
    mock_db.table.return_value.select.return_value.eq.return_value.order.return_value.execute.return_value.data = []

    with patch('app.api.v1.endpoints.samples.get_supabase', return_value=mock_db):
        resp = client.get('/api/v1/samples/')

    assert resp.status_code == 200
    assert resp.json() == []


def test_create_sample():
    client = make_client()
    mock_db = MagicMock()
    mock_db.table.return_value.insert.return_value.single.return_value.execute.return_value.data = FAKE_SAMPLE

    with patch('app.api.v1.endpoints.samples.get_supabase', return_value=mock_db):
        resp = client.post(
            '/api/v1/samples/',
            json={'name': 'Test Blood Draw', 'type': 'blood', 'collected_at': '2025-01-01T00:00:00Z'},
        )

    assert resp.status_code == 201
    assert resp.json()['name'] == 'Test Blood Draw'
