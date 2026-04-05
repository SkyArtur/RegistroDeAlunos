from core import create_logger, display_top
from Labs.interface.menus import menu_confirmar
from .regiter import cadastro_aluno, cadastro_boletim
from .manager import GerenciadorDatabase


logger = create_logger()

INSERT_ALUNO = 'INSERT INTO aluno (nome, sobrenome, nascimento) VALUES (?, ?, ?);'
INSERT_NOTA = 'INSERT INTO nota (valor) VALUES (?);'
INSERT_BOLETIM = 'INSERT INTO boletim (id_aluno, id_nota) VALUES (?, ?);'


def salvar_aluno():
    while True:
        display_top('Cadastrar Aluno')
        aluno = cadastro_aluno()
        aluno.boletim = cadastro_boletim(aluno)
        with GerenciadorDatabase(INSERT_ALUNO, aluno.analisar()) as db:
            novo_aluno = db.alter()
        for nota in aluno.boletim.notas:
            with GerenciadorDatabase(INSERT_NOTA, (nota,)) as db:
                num = db.alter()
            with GerenciadorDatabase(INSERT_BOLETIM, (novo_aluno, num,)) as db:
                db.alter()
        logger.info(f'{aluno.nome} {aluno.sobrenome} cadastrado(a) com sucesso!')
        if not menu_confirmar('Deseja cadastrar novo aluno?'):
            break
