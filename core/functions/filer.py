from pathlib import Path

def criar_arquivo(file: Path) -> Path:
    if not file.parent.exists():
        file.parent.mkdir(exist_ok=True, parents=True)
    if not file.exists():
        file.touch()
    return file

def caminho_database(*, debug: bool = False) -> Path:
    raiz = Path(__file__).parent.parent.parent.resolve()
    diretorio_database = raiz.joinpath('database')
    diretorio_testes = raiz.joinpath('tests')
    if debug:
        return criar_arquivo(diretorio_testes / 'fixtures/artifacts/db_test.sqlite').resolve()
    return criar_arquivo(diretorio_database / 'data/db.sqlite').resolve()