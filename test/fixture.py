import os
import tempfile

import pytest

from flask import Flask

from main import app

http200 = 200


@pytest.fixture
def client():

    # db_fd, base.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            os.environ['REGION'] = 'JUST FOR TEST'
        yield client

    # os.close(db_fd)
    # os.unlink(base.config['DATABASE'])
