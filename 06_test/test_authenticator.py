import pytest
from authenticator import Authenticator

USER = "user"
PASSWORD = "password"
WRONG_PASSWORD = "wrong_password"

@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth

@pytest.fixture
def authenticator_user_registered():
    auth = Authenticator()
    auth.register(USER, PASSWORD)
    yield auth

def test_register(authenticator):
    authenticator.register(USER, PASSWORD)
    assert authenticator.users[USER] == PASSWORD

def test_register_user_already_exists(authenticator_user_registered):
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator_user_registered.register(USER, PASSWORD)

def test_login(authenticator_user_registered):
    assert authenticator_user_registered.login(USER, PASSWORD) == "ログイン成功"

def test_login_wrong_password(authenticator_user_registered):
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator_user_registered.login(USER, WRONG_PASSWORD)
