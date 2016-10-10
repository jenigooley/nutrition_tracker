import pytest
import access_logic


@pytest.fixture
def db_profile():
    class F():
        def read_user(self, username):
            return ('user', 'password', 'email', 'height', 'weight')
    return F()


def test_get_user(db_profile):
    user_deets = access_logic.get_user('blah')
    assert user_deets == {
        'username': username,
        'password': password,
        'email': email,
        'height': height,
        'weight': weight
    }
