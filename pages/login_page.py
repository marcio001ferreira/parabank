"""Page Object da tela de login: guarda os seletores e as acoes da tela em um so lugar."""
from selenium.webdriver.common.by import By


class LoginPage:
    CAMPO_USUARIO = (By.ID, "Log In")
    CAMPO_SENHA = (By.ID, "password")
    BOTAO_LOGIN = (By.ID, "login-button")
    MENSAGEM_ERRO = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def abrir(self):
        self.driver.get(self.base_url + "/")
        return self

    def entrar(self, usuario, senha):
        self.driver.find_element(*self.CAMPO_USUARIO).send_keys(usuario)
        self.driver.find_element(*self.CAMPO_SENHA).send_keys(senha)
        self.driver.find_element(*self.BOTAO_LOGIN).click()

    def mensagem_de_erro(self):
        return self.driver.find_element(*self.MENSAGEM_ERRO).text
