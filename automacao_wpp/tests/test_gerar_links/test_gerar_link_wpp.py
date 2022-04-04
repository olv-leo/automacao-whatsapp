from automacao_wpp.gerar_link.gerar_link import gerar_link_wpp
import pytest


@pytest.mark.parametrize(
    'numero, msg, resultado',
    [
        ('16997952356', '', 'https://api.whatsapp.com/send?phone=5516997952356'),
        ('16997952356', 'Teste', 'https://api.whatsapp.com/send?phone=5516997952356&text=Teste'),
    ]
)
def test_gerar_link_wpp(numero, msg, resultado):
    assert gerar_link_wpp(numero, msg) == resultado
