"""
Fluxo: TRANSFERENCIA  (CT04, CT05, CT06)
Cada teste usa um cliente novo com 2 contas e compara os saldos ANTES e DEPOIS.
A mensagem e o print sao capturados logo apos a transferencia, antes de mudar de tela.
"""
from decimal import Decimal

import pytest

from pages.contas_page import ContasPage
from pages.evidencia import print_tela
from pages.transfer_page import TransferPage


def _saldos(contas, origem, destino):
    return contas.saldo(origem), contas.saldo(destino)


def test_ct04_transferencia_valida_atualiza_saldos(driver, base_url, cliente_com_duas_contas):
    origem, destino = cliente_com_duas_contas
    contas = ContasPage(driver, base_url)
    # Dado um cliente com duas contas e saldo suficiente
    antes_origem, antes_destino = _saldos(contas, origem, destino)
    # Quando transfere 10,00 da origem para o destino
    pagina = TransferPage(driver, base_url).abrir()
    pagina.transferir(origem, destino, "10.00")
    concluida = pagina.concluida()
    mensagem = pagina.mensagem()
    # Entao a transferencia conclui e os saldos mudam exatamente 10,00
    assert concluida, f"transferencia nao concluida: {mensagem!r}"
    depois_origem, depois_destino = _saldos(contas, origem, destino)
    assert depois_origem == antes_origem - Decimal("10.00")
    assert depois_destino == antes_destino + Decimal("10.00")


@pytest.mark.parametrize(
    "valor, deve_aceitar",
    [("-1.00", False), ("-0.01", False), ("0.00", False), ("0.01", True)],
    ids=["menos_1", "menos_0_01", "zero", "menor_valor_valido_0_01"],
)
def test_ct05_transferencia_valor_zero_e_negativo(
    driver, base_url, cliente_com_duas_contas, valor, deve_aceitar
):
    origem, destino = cliente_com_duas_contas
    contas = ContasPage(driver, base_url)
    antes_origem, antes_destino = _saldos(contas, origem, destino)

    pagina = TransferPage(driver, base_url).abrir()
    pagina.transferir(origem, destino, valor)
    concluida = pagina.concluida()
    mensagem = pagina.mensagem()  # ler ANTES de mudar de tela
    if concluida != deve_aceitar:  # resultado inesperado: guarda o print da tela do resultado
        print_tela(driver, "ct05_valor_" + valor.replace("-", "menos").replace(".", "_"))

    depois_origem, depois_destino = _saldos(contas, origem, destino)
    detalhe = (
        f"valor {valor}: mensagem={mensagem!r}; "
        f"origem {antes_origem}->{depois_origem}; destino {antes_destino}->{depois_destino}"
    )
    if deve_aceitar:
        assert concluida, detalhe
        assert depois_origem == antes_origem - Decimal(valor), detalhe
        assert depois_destino == antes_destino + Decimal(valor), detalhe
    else:
        assert not concluida, detalhe
        assert depois_origem == antes_origem, detalhe
        assert depois_destino == antes_destino, detalhe


@pytest.mark.parametrize(
    "delta, deve_aceitar",
    [(Decimal("0.00"), True), (Decimal("0.01"), False)],
    ids=["igual_ao_saldo", "acima_do_saldo_0_01"],
)
def test_ct06_transferencia_acima_do_saldo(
    driver, base_url, cliente_com_duas_contas, delta, deve_aceitar
):
    origem, destino = cliente_com_duas_contas
    contas = ContasPage(driver, base_url)
    antes_origem, antes_destino = _saldos(contas, origem, destino)
    valor = antes_origem + delta  # S (limite valido) ou S + 0,01 (primeiro invalido)

    pagina = TransferPage(driver, base_url).abrir()
    pagina.transferir(origem, destino, f"{valor:.2f}")
    concluida = pagina.concluida()
    mensagem = pagina.mensagem()  # ler ANTES de mudar de tela
    if concluida != deve_aceitar:
        print_tela(driver, f"ct06_valor_{valor:.2f}".replace(".", "_"))

    depois_origem, depois_destino = _saldos(contas, origem, destino)
    detalhe = (
        f"valor {valor}: mensagem={mensagem!r}; "
        f"origem {antes_origem}->{depois_origem}; destino {antes_destino}->{depois_destino}"
    )
    if deve_aceitar:
        assert concluida, detalhe
        assert depois_origem == antes_origem - valor, detalhe
    else:
        assert not concluida, detalhe
        assert depois_origem == antes_origem, detalhe
        assert depois_destino == antes_destino, detalhe