"""Page Object da tela de cadastro (Register) do ParaBank."""
import uuid

from selenium.webdriver.common.by import By


def dados_cliente(**sobrescrever):
    """Gera um cliente FICTICIO com usuario unico por execucao (a base do site e compartilhada)."""
    dados = {
        "first_name": "Aluno",
        "last_name": "Teste",
        "street": "Rua Ficticia, 100",
        "city": "Sao Paulo",
        "state": "SP",
        "zip_code": "01000000",
        "phone": "11999990000",
        "ssn": "123-45-6789",
        "username": "aluno" + uuid.uuid4().hex[:6],
        "password": "Senha@123",
        "confirm": "Senha@123",
    }
    dados.update(sobrescrever)
    return dados


class RegisterPage:
    CAMPOS = {
        "first_name": (By.ID, "customer.firstName"),
        "last_name": (By.ID, "customer.lastName"),
        "street": (By.ID, "customer.address.street"),
        "city": (By.ID, "customer.address.city"),
        "state": (By.ID, "customer.address.state"),
        "zip_code": (By.ID, "customer.address.zipCode"),
        "phone": (By.ID, "customer.phoneNumber"),
        "ssn": (By.ID, "customer.ssn"),
        "username": (By.ID, "customer.username"),
        "password": (By.ID, "customer.password"),
        "confirm": (By.ID, "repeatedPassword"),
    }
    BOTAO_REGISTER = (By.CSS_SELECTOR, "input[value='Register']")
    TITULO = (By.CSS_SELECTOR, "#rightPanel h1.title")
    TEXTO_SUCESSO = (By.CSS_SELECTOR, "#rightPanel p")
    ERRO_SENHA_CONFIRMACAO = (By.ID, "repeatedPassword.errors")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def abrir(self):
        self.driver.get(self.base_url + "/register.htm")
        return self

    def preencher(self, dados):
        for chave, seletor in self.CAMPOS.items():
            self.driver.find_element(*seletor).send_keys(dados[chave])

    def enviar(self):
        self.driver.find_element(*self.BOTAO_REGISTER).click()

    def cadastrar(self, dados):
        self.preencher(dados)
        self.enviar()

    def titulo(self):
        return self.driver.find_element(*self.TITULO).text

    def texto_de_sucesso(self):
        return self.driver.find_element(*self.TEXTO_SUCESSO).text

    def erro_confirmacao_senha(self):
        return self.driver.find_element(*self.ERRO_SENHA_CONFIRMACAO).text