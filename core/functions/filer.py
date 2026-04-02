from pathlib import Path

def criar_arquivo(file: Path) -> Path:
    if not file.parent.exists():
        file.parent.mkdir(exist_ok=True, parents=True)
    if not file.exists():
        file.touch()
    return file