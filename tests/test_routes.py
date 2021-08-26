def test_login_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data


def test_valid_login_logout(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = client.post('/login',
                                data=dict(email='ataulm786@gmail.com', password='Ataul@786'),
                                follow_redirects=True)
    assert response.status_code == 200

    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200

