"""Page Object da tela de login do ParaBank: seletores e acoes em um so lugar."""
from selenium.webdriver.common.by import By


class LoginPage:
    CAMPO_USUARIO = (By.NAME, "username")
    CAMPO_SENHA = (By.NAME, "password")
    BOTAO_LOGIN = (By.CSS_SELECTOR, "input[value='Log In']")
    MENSAGEM_ERRO = (By.CSS_SELECTOR, "#rightPanel .error")
    LINK_REGISTER = (By.LINK_TEXT, "Register")
    LINK_LOGOUT = (By.LINK_TEXT, "Log Out")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def abrir(self):
        self.driver.get(self.base_url + "/index.htm")
        return self

    def entrar(self, usuario, senha):
        self.driver.find_element(*self.CAMPO_USUARIO).send_keys(usuario)
        self.driver.find_element(*self.CAMPO_SENHA).send_keys(senha)
        self.driver.find_element(*self.BOTAO_LOGIN).click()

    def mensagem_de_erro(self):
        return self.driver.find_element(*self.MENSAGEM_ERRO).text

    def logado(self):
        return len(self.driver.find_elements(*self.LINK_LOGOUT)) > 0