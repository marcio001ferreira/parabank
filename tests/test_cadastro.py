"""
Fluxo: CADASTRO  (CT01 e CT02)
Cada teste cria o PROPRIO usuario (nome unico), pois a base do ParaBank e reiniciada.
"""
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