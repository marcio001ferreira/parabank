"""Page Object da tela Transfer Funds do ParaBank."""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait

ESPERA = 10


class TransferPage:
    VALOR = (By.ID, "amount")
    ORIGEM = (By.ID, "fromAccountId")
    DESTINO = (By.ID, "toAccountId")
    BOTAO = (By.CSS_SELECTOR, "input[value='Transfer']")
    RESULTADO = (By.ID, "showResult")
    ERRO = (By.ID, "showError")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def abrir(self):
        self.driver.get(self.base_url + "/transfer.htm")
        # as listas de contas sao carregadas por JavaScript
        WebDriverWait(self.driver, ESPERA).until(
            lambda d: len(Select(d.find_element(*self.ORIGEM)).options) >= 2
            and len(Select(d.find_element(*self.DESTINO)).options) >= 2
        )
        return self

    def transferir(self, origem, destino, valor):
        campo = self.driver.find_element(*self.VALOR)
        campo.clear()
        campo.send_keys(valor)
        Select(self.driver.find_element(*self.ORIGEM)).select_by_visible_text(str(origem))
        Select(self.driver.find_element(*self.DESTINO)).select_by_visible_text(str(destino))
        self.driver.find_element(*self.BOTAO).click()

    def concluida(self, espera=5):
        """True se aparecer 'Transfer Complete!'. False se aparecer erro ou nada."""
        def resposta(d):
            if d.find_element(*self.RESULTADO).is_displayed():
                return "ok"
            if d.find_element(*self.ERRO).is_displayed():
                return "erro"
            return False

        try:
            return WebDriverWait(self.driver, espera).until(resposta) == "ok"
        except TimeoutException:
            return False

    def mensagem(self):
        """Texto da mensagem visivel (sucesso ou erro), para citar no defeito."""
        for local in (self.RESULTADO, self.ERRO):
            for elemento in self.driver.find_elements(*local):
                if elemento.is_displayed():
                    return elemento.text.strip()
        return ""