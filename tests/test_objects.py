from datetime import date, timedelta

import pytest

from core.objects import Aluno, Boletim, Pessoa
from core.objects.boletim import Nota


class PessoaConcretaTeste(Pessoa):
    """Implementação concreta usada para testar o contrato abstrato de ``Pessoa``."""

    def analisar(self) -> tuple:
        """Retorna dados mínimos para validar a interface abstrata."""
        return self.nome, self.sobrenome, self.nascimento

    def dados(self) -> tuple:
        """Retorna dados completos para validar a interface abstrata."""
        return self.id, self.nome, self.sobrenome, self.nascimento

    @classmethod
    def gerar(cls, *args, **kwargs) -> "PessoaConcretaTeste":
        """Cria uma instância concreta para uso nos testes."""
        return cls(*args, **kwargs)


def test_pessoa_nao_pode_ser_instanciada_diretamente():
    """Garante que ``Pessoa`` permaneça abstrata para o CI e para o contrato do domínio."""
    with pytest.raises(TypeError):
        Pessoa(1, "Ana", "Silva", date(2000, 1, 1))


def test_pessoa_calcula_idade_quando_recebe_nascimento_como_date():
    """Confirma que a idade é derivada automaticamente a partir de uma data válida."""
    nascimento = date.today() - timedelta(days=365 * 20)

    pessoa = PessoaConcretaTeste(1, "Ana", "Silva", nascimento)

    assert pessoa.idade == 20


def test_pessoa_mantem_idade_padrao_quando_nascimento_nao_e_date():
    """Documenta o comportamento atual quando o campo nascimento não chega tipado como ``date``."""
    pessoa = PessoaConcretaTeste(1, "Ana", "Silva", "01/01/2000")

    assert pessoa.idade == 0


def test_pessoa_concreta_gerar_retorna_instancia_valida():
    """Verifica o método de fábrica abstrato implementado em uma subclasse concreta de teste."""
    pessoa = PessoaConcretaTeste.gerar(1, "Ana", "Silva", date(2000, 1, 1))

    assert isinstance(pessoa, PessoaConcretaTeste)
    assert pessoa.dados() == (1, "Ana", "Silva", date(2000, 1, 1))


def test_nota_suporta_igualdade_e_ordenacao_por_dataclass():
    """Valida o comportamento estrutural exposto pela dataclass ``Nota``."""
    nota_menor = Nota(1, 7.0)
    nota_maior = Nota(2, 9.0)

    assert nota_menor == Nota(1, 7.0)
    assert nota_menor < nota_maior


def test_boletim_cria_notas_a_partir_de_valores_numericos():
    """Garante que valores numéricos simples sejam convertidos internamente em ``Nota``."""
    boletim = Boletim(7.0, 8.5, 10.0)

    assert isinstance(boletim.n1, Nota)
    assert isinstance(boletim.n2, Nota)
    assert boletim.notas == [7.0, 8.5, 10.0]


def test_boletim_preserva_objetos_nota_recebidos_na_inicializacao():
    """Confirma que objetos ``Nota`` informados explicitamente não sejam recriados."""
    nota = Nota(10, 6.5)
    boletim = Boletim(nota)

    assert boletim.n1 is nota
    assert boletim.notas == [6.5]


def test_boletim_calcula_media_arredondada_com_duas_casas():
    """Verifica o arredondamento aplicado pela propriedade de média."""
    boletim = Boletim(7.0, 7.0, 7.03)

    assert boletim.media == 7.01


@pytest.mark.parametrize(
    ("notas", "situacao_esperada"),
    [
        pytest.param((7.0, 8.0), "Aprovado", id="aprovado"),
        pytest.param((3.0, 4.0), "Recuperação", id="recuperacao"),
        pytest.param((1.0, 2.5), "Reprovado", id="reprovado"),
    ],
)
def test_boletim_define_situacao_conforme_media(notas, situacao_esperada):
    """Garante a classificação acadêmica nas três faixas de média suportadas."""
    boletim = Boletim(*notas)

    assert boletim.situacao == situacao_esperada


def test_aluno_inicializa_com_boletim_e_retorna_dados_basicos():
    """Valida a integração entre ``Aluno`` e ``Boletim`` e os métodos de leitura expostos."""
    nascimento = date(2003, 2, 21)
    boletim = Boletim(8.0, 9.0)

    aluno = Aluno(1, "Joao", "Souza", nascimento, boletim=boletim)

    assert aluno.boletim is boletim
    assert aluno.analisar() == ("Joao", "Souza", nascimento)
    assert aluno.dados() == (1, "Joao", "Souza", nascimento)


def test_aluno_gerar_cria_instancia_com_argumentos_informados():
    """Confirma o método de fábrica de ``Aluno`` com repasse de argumentos nomeados."""
    boletim = Boletim(5.0, 6.0)

    aluno = Aluno.gerar(2, "Maria", "Lima", date(2004, 3, 10), boletim=boletim)

    assert isinstance(aluno, Aluno)
    assert aluno.boletim is boletim
    assert aluno.dados() == (2, "Maria", "Lima", date(2004, 3, 10))
