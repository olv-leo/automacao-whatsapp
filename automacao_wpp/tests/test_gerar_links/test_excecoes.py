from automacao_wpp.gerar_link.gerar_link import gerar_link_wpp, NumeroInvalido
import pytest


@pytest.mark.parametrize(
    'numero, msg',
    [
        ('', ''),
        ('', 'Teste')
    ]
)
def test_gerar_link_wpp(numero, msg):
    with pytest.raises(NumeroInvalido):
        gerar_link_wpp(numero, msg)
