from core import Boletim, Aluno, entrada_datas, entrada_numeros, entrada_padrao, create_logger
from Labs.interface.menus import menu_confirmar


logger = create_logger()


def cadastro_aluno():
    print("Cadastrar novo aluno:")
    aluno = Aluno(
        _id=None,
        nome=entrada_padrao('Primeiro nome: '),
        sobrenome=entrada_padrao('Sobrenome: '),
        nascimento=entrada_datas('Data de nascimento: '),
    )
    return aluno

def cadastro_boletim(aluno: Aluno):
    print("Cadastrar boletim do aluno:")
    notas = []
    print(f'Notas cadastradas {notas}')
    while True:
        nota = entrada_numeros(f"Digite a nota {len(notas) + 1}: ")
        notas.append(nota)
        if len(notas) >= 4:
            if not menu_confirmar('Deseja cadastrar outra nota?'):
                break
    return Boletim(*notas)

