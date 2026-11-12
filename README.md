# Kit inicial do A3 — Garantia da Qualidade de Software

Este kit já vem com o ambiente configurado e um teste de login funcionando no SauceDemo.
O grupo parte daqui para construir o próprio trabalho.

## Lab 1 (04/11) — fazer o primeiro teste rodar

```bash
python -m pip install -r requirements.txt
python verificar_ambiente.py     # deve mostrar AMBIENTE OK
python -m pytest
```

O Chrome abre sozinho e o teste `test_ct01` passa no SauceDemo. Depois, adapte o kit ao case do grupo:

1. Troque o endereço padrão em `conftest.py` (linha `BASE_URL = ...`).
2. Abra o site no Chrome, clique com o botão direito no campo de login, escolha **Inspecionar**
   e copie o `id`, o `name` ou o `data-test` dos campos para `pages/login_page.py`.
3. Ajuste o usuário, a senha e o `assert` do `test_ct01`.

**Checkpoint:** primeiro teste rodando no case do grupo e capítulo 1 iniciado.

## Lab 2 (11/11) — especificar os casos e começar a automação

- Especifique os 8 casos de teste no relatório (cap. 2), usando partição de equivalência e valor-limite.
  O guia do grupo traz ideias de casos para começar.
- Para cada tela nova, crie um arquivo em `pages/` com os seletores e as ações, no modelo de `login_page.py`.
- Um arquivo de teste por fluxo em `tests/` (ex.: `test_carrinho.py`).

**Checkpoint:** 8 casos especificados e 2 testes rodando.

## Lab 3 (18/11) — completar a automação e registrar defeitos

- Complete os 5 testes automatizados. Teste vários dados de uma vez com `@pytest.mark.parametrize`.
- Teste que falha **não se apaga**: é um defeito. O print da tela vai para a pasta `evidencias/`.
- Registre cada defeito no relatório (seção 4.1) com severidade, passos e evidência.

**Checkpoint:** 5 testes rodando e defeitos registrados.

## Lab 4 (25/11) — métricas, ética e apresentação

- Rode `python3 -m pytest`, anote quantos passaram e falharam e calcule as 3 métricas (seção 4.2).
- Escreva o capítulo 5 (ética) a partir dos defeitos que o grupo encontrou.
- Monte os slides e ensaie a demo de 10 minutos. Grave um vídeo curto da execução como plano B.

**Checkpoint:** relatório completo em rascunho e slides prontos.

## Apresentação (02/12)

Entrega do relatório em PDF, da pasta do projeto e dos slides. Demo ao vivo de 10 minutos e 5 de perguntas.

## Comandos úteis

| Comando | Para quê |
| --- | --- |
| `python3 -m pytest` | roda todos os testes |
| `pytest tests/test_login.py` | roda um arquivo |
| `pytest -k ct01` | roda testes cujo nome contém "ct01" |
| `HEADLESS=1 pytest` | roda sem abrir a janela (Windows: `set HEADLESS=1 && pytest`) |

## Regras

Somente os sites dos cases. Dados fictícios (nunca e-mail, CPF ou senha reais).
Uso de IA é permitido, mas deve ser declarado no relatório.
