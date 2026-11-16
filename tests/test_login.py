"""
Fluxo: LOGIN  (CT03)
"""
import uuid

from pages.login_page import LoginPage


def test_ct03_login_credenciais_invalidas(driver, base_url):
    # Dado que estou na tela de login
    pagina = LoginPage(driver, base_url).abrir()
    # Quando entro com um usuario que nao existe e uma senha errada
    pagina.entrar("inexistente" + uuid.uuid4().hex[:6], "errada123")
    # Entao o acesso e negado com mensagem de erro e nao ha sessao aberta
    assert "could not be verified" in pagina.mensagem_de_erro()
    assert not pagina.logado()