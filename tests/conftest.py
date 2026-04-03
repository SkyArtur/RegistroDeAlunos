"""Configuracoes compartilhadas do pytest para o projeto."""
from pathlib import Path

import pytest


@pytest.fixture
def caminho_database_test(tmp_path: Path) -> Path:
    return tmp_path / "db_test.sqlite"
