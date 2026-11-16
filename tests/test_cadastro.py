"""
Fluxo: CADASTRO  (CT01 e CT02)
Cada teste cria o PROPRIO usuario (nome unico), pois a base do ParaBank e reiniciada.
"""
from pages.login_page import LoginPage
from pages.register_page import RegisterPage, dados_cliente


def test_ct01_cadastro_com_campos_validos(driver, base_url):
    # Dado que estou na tela de cadastro
    pagina = RegisterPage(driver, base_url).abrir()
    dados = dados_cliente()
    # Quando preencho todos os campos com dados validos e envio
    pagina.cadastrar(dados)
    # Entao a conta e criada e o cliente ja entra logado
    assert pagina.titulo() == "Welcome " + dados["username"]
    assert "created successfully" in pagina.texto_de_sucesso()


def test_ct02_cadastro_com_senhas_diferentes(driver, base_url):
    # Dado que estou na tela de cadastro
    pagina = RegisterPage(driver, base_url).abrir()
    # Quando a confirmacao de senha e diferente da senha
    dados = dados_cliente(confirm="Outra@456")
    pagina.cadastrar(dados)
    # Entao o cadastro nao e concluido, aparece o erro e o cliente nao fica logado
    assert "did not match" in pagina.erro_confirmacao_senha()
    assert "register.htm" in driver.current_url
    assert not LoginPage(driver, base_url).logado()