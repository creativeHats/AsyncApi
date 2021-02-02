def test_group_pass(client):
    """
    GIVEN a Flask application
    WHEN the '/group/<group_name>' page is requested (GET)
    THEN check the response is valid
    """

    response = client.get('/group/group_a')
    assert response.status_code == 202


def test_group_job_fail(client):
    """
    GIVEN a Flask application
    WHEN the '/group/<group_name>' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/group/group_b')
    assert response.status_code == 400


def test_group_fail(client):
    """
    GIVEN a Flask application
    WHEN the '/status/<status_name>' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/group/random')
    assert response.status_code == 400


def test_job_fail(client):
    """
    GIVEN a Flask application
    WHEN the '/status/<status_name>' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/status/random')
    assert response.status_code == 400
