from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from app.main import app
from app.core.security import get_current_user

FAKE_USER = {'uid': 'user-uid-1234', 'email': 'test@example.com'}

FAKE_SAMPLE_DATA = {
    'name': 'Test Blood Draw',
    'type': 'blood',
    'status': 'pending',
    'collected_at': '2025-01-01T00:00:00+00:00',
    'processed_at': None,
    'owner_id': 'user-uid-1234',
    'metadata': {},
    'created_at': '2025-01-01T00:00:00+00:00',
}

app.dependency_overrides[get_current_user] = lambda: FAKE_USER
client = TestClient(app)


def _make_doc(doc_id: str, data: dict) -> MagicMock:
    doc = MagicMock()
    doc.id = doc_id
    doc.exists = True
    doc.to_dict.return_value = data
    return doc


def test_list_samples_empty():
    mock_db = MagicMock()
    mock_db.collection.return_value.where.return_value.order_by.return_value.stream.return_value = iter([])

    with patch('app.api.v1.endpoints.samples.get_db', return_value=mock_db):
        resp = client.get('/api/v1/samples/')

    assert resp.status_code == 200
    assert resp.json() == []


def test_create_sample():
    doc = _make_doc('sample-1', FAKE_SAMPLE_DATA)
    mock_db = MagicMock()
    mock_db.collection.return_value.document.return_value.get.return_value = doc

    with patch('app.api.v1.endpoints.samples.get_db', return_value=mock_db):
        resp = client.post(
            '/api/v1/samples/',
            json={'name': 'Test Blood Draw', 'type': 'blood', 'collected_at': '2025-01-01T00:00:00Z'},
        )

    assert resp.status_code == 201
    assert resp.json()['name'] == 'Test Blood Draw'
