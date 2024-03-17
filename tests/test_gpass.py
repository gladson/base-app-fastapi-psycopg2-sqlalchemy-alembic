import pytest

from src.core.utils.gpass import GPass


@pytest.fixture
def hashed_password():
    # Senha a ser utilizada nos testes
    password = '2024@testGBack#2024'
    return GPass.get_password_hash(password)


def test_password_hashing(hashed_password):
    # Verificar se a função get_password_hash retorna um hash válido
    assert hashed_password is not None
    assert isinstance(
        hashed_password,
        str,
    )
    assert len(hashed_password) > 0


def test_password_verification(hashed_password):
    # Senha correta
    password = '2024@testGBack#2024'
    assert GPass.verify_password(password, hashed_password) is True
    # Senha incorreta
    wrong_password = 'wrong_password'
    assert GPass.verify_password(wrong_password, hashed_password) is False
