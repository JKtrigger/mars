from test.fixture import *


def test_application(client):
    """Start testing"""
    request = client.get('/stripe')
    json_body = request.json
    assert request.status_code == http200
    assert json_body
