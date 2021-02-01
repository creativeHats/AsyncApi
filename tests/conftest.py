import pytest
from setup import Setup

setup = Setup()


@pytest.fixture(scope="session", autouse=True)
def setup_test(request):
    config = setup.get_config()
    request.config.cache.set('config', config)


@pytest.fixture(scope='session')
def test_client():
    flask_app = setup.get_app()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture(scope='session')
def celery_config():
    return {
        'broker_url': 'amqp://',
        'result_backend': 'rpc',
    }