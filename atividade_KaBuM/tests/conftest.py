import pytest
from atividade_KaBuM.app import create_app

@pytest.fixture(scope="module")
def app():
    return create_app()