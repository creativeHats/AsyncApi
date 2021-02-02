from api.app import app as flask_app

import pytest

@pytest.fixture(scope='session')
def client():
    return flask_app.test_client()

@pytest.fixture(scope='session')
def app():
    return flask_app
#
# @pytest.fixture(scope='session')
# def celery_config():
#     return {
#         'broker_url': 'redis://',
#         'result_backend': 'redis://'
#     }
#
#
# @pytest.fixture(scope='session')
# def celery_app(app):
#     # for use celery_worker fixture
#     from celery.contrib.testing import tasks  # NOQA
#     return celery
