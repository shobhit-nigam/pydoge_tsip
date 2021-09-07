from one import app

with app.test_client() as c:
    response = c.get('/')
    assert response.data == b"hello there !"
    assert response.status_code == 200
