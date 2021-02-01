import os

from celery import Celery
from flask import Flask

from utils.config import Config


class Setup:
    config = None
    celery = None
    app = None

    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), '../resources/config.yaml')
        if not self.config:
            self.config = Config().setup_config(self.config_path)
        if not self.app:
            self.app = Flask(self.config['app']['name'])
            self.app.config.update(
                CELERY_BROKER_URL=self.config['app']['celery_broker_url'],
                CELERY_RESULT_BACKEND=self.config['app']['celery_result_backend'],
                CELERY_TASK_TRACK_STARTED=True
            )
        if not self.celery:
            self.celery = self.make_celery(self.app)

    def make_celery(self, app):
        celery = Celery(
            app.import_name,
            backend=app.config['CELERY_RESULT_BACKEND'],
            broker=app.config['CELERY_BROKER_URL']
        )
        celery.conf.update(app.config)

        class ContextTask(celery.Task):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return self.run(*args, **kwargs)

        celery.Task = ContextTask
        return celery

    def get_config(self):
        if self.config:
            return self.config
        else:
            self.config = Config().setup_config(self.config_path)

    def get_celery(self):
        if self.celery:
            return self.celery
        return None

    def get_app(self):
        if self.app:
            return self.app
        return None
