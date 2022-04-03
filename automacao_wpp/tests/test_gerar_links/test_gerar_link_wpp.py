from automacao_wpp.gerar_link.gerar_link import gerar_link_wpp


def test_gerar_link_wpp():
    assert gerar_link_wpp(16997952356) == 'https://api.whatsapp.com/send?phone=5516997952356'
