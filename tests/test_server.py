import warnings

from fastapi.testclient import TestClient

from src.server import app


def test_main_health_return_404():
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
