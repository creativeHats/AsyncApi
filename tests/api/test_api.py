import pytest


@pytest.mark.usefixtures('celery_session_app')
@pytest.mark.usefixtures('celery_session_worker')
class TestAPI():
    def test_group_pass(self,test_client):
        """
        GIVEN a Flask application
        WHEN the '/group/<group_name>' page is requested (GET)
        THEN check the response is valid
        """
        response = test_client.post('/group/group_a')
        assert response.status_code == 202


    def test_group_job_fail(self,test_client):
        """
        GIVEN a Flask application
        WHEN the '/group/<group_name>' page is requested (GET)
        THEN check the response is valid
        """
        response = test_client.get('/group/group_b')
        assert response.status_code == 400

    def test_group_fail(self,test_client):
        """
        GIVEN a Flask application
        WHEN the '/group/<group_name>' page is requested (GET)
        THEN check the response is valid
        """
        response = test_client.get('/group/random')
        assert response.status_code == 400



    def test_job_fail(self,test_client):
        """
        GIVEN a Flask application
        WHEN the '/group/<group_name>' page is requested (GET)
        THEN check the response is valid
        """
        response = test_client.get('/status/random')
        assert response.status_code == 400
