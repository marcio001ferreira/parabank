"""Page Object das telas de contas: Open New Account e Accounts Overview."""
from decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

ESPERA = 10


def para_decimal(texto):
    """Converte '$515.50' ou '-$5.00' em Decimal."""
    return Decimal(texto.replace("$", "").replace(",", "").strip())


class ContasPage:
    TIPO_CONTA = (By.ID, "type")
    CONTA_ORIGEM = (By.ID, "fromAccountId")
    BOTAO_ABRIR = (By.CSS_SELECTOR, "input[value='Open New Account']")
    NOVA_CONTA = (By.ID, "newAccountId")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def abrir_segunda_conta(self):
        """Abre uma conta SAVINGS a partir da conta atual. Devolve (origem, destino)."""
        self.driver.get(self.base_url + "/openaccount.htm")
        espera = WebDriverWait(self.driver, ESPERA)
        # a lista de contas e carregada por JavaScript
        espera.until(lambda d: len(Select(d.find_element(*self.CONTA_ORIGEM)).options) > 0)
        origem = Select(self.driver.find_element(*self.CONTA_ORIGEM)).first_selected_option.text
        Select(self.driver.find_element(*self.TIPO_CONTA)).select_by_visible_text("SAVINGS")
        self.driver.find_element(*self.BOTAO_ABRIR).click()
        espera.until(lambda d: d.find_element(*self.NOVA_CONTA).text.strip())
        destino = self.driver.find_element(*self.NOVA_CONTA).text.strip()
        return origem, destino

    def saldo(self, conta):
        """Le o saldo de uma conta na tela Accounts Overview."""
        self.driver.get(self.base_url + "/overview.htm")
        celula = (
            By.XPATH,
            f"//table[@id='accountTable']//a[normalize-space()='{conta}']/ancestor::tr/td[2]",
        )
        WebDriverWait(self.driver, ESPERA).until(EC.visibility_of_element_located(celula))
        return para_decimal(self.driver.find_element(*celula).text)