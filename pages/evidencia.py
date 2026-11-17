"""Salva prints de evidencia (com data e hora no nome) na pasta evidencias/."""
from datetime import datetime
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "evidencias"


def print_tela(driver, nome):
    PASTA.mkdir(exist_ok=True)
    carimbo = datetime.now().strftime("%Y%m%d_%H%M%S")
    caminho = PASTA / f"{nome}_{carimbo}.png"
    driver.save_screenshot(str(caminho))
    return caminho