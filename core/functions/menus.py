from core.inputs import entrada_numeros


def menu_numerico(mensagem: str, **kwargs) -> int | float:
    opcao = entrada_numeros(mensagem, **kwargs)
    return opcao

def menu_confirmar(mensagem: str) -> int | float:
    menu = f"""{mensagem}
    [1] Sim;
    [0] Não;\n=> """
    return menu_numerico(menu, minn=0, maxx=1)

def menu_inicial() -> int | float:
    menu = """O que deseja fazer?
    [1] Registrar aluno(a);
    [2] Atualizar aluno(a);
    [3] Exibir aluno(a);
    [4] Exibir todos os alunos;
    [5] Deletar aluno(a);
    [0] Sair;\n=> """
    return menu_numerico(menu, minn=0, maxx=5)
