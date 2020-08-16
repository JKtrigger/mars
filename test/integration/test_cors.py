from test.fixture import *


def test_cors(client):
    """Start testing"""
    request = client.get('/')
    assert request.headers[2] == ('Access-Control-Allow-Origin', '*')
