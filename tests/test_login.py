"""
Fluxo: LOGIN  (ponto de partida do grupo)

O CT01 ja esta pronto e deve passar no Lab 1.
Depois, o grupo escreve os proximos testes seguindo o mesmo modelo:
  Dado (pre-condicao)  ->  Quando (acao)  ->  Entao (assert com o resultado esperado)
"""
import pytest

from pages.login_page import LoginPage

SENHA = "secret_sauce"


def test_ct01_login_valido_abre_vitrine(driver, base_url):
    # Dado que estou na tela de login
    pagina = LoginPage(driver, base_url).abrir()
    # Quando entro com um usuario valido
    pagina.entrar("standard_user", SENHA)
    # Entao vejo a vitrine de produtos
    assert "inventory.html" in driver.current_url


def test_ct02_usuario_bloqueado(driver, base_url):
    # TODO (grupo): faca login com "locked_out_user" e verifique a mensagem de erro.
    # Dica: use pagina.mensagem_de_erro()
    # Apague a linha abaixo quando o teste estiver escrito
    # (um teste vazio "passaria" sem testar nada).
    pytest.skip("A fazer pelo grupo")
