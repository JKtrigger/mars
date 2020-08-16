from test.fixture import *


def test_application(client):
    """Start testing"""
    request = client.get('/')
    assert request.status_code == http200
    assert request.get_data() == b'Hello World!'
