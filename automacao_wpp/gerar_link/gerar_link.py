def gerar_link_wpp(numero, msg=None):
    """
    Recebe um número e uma mensagem e gera um link de WhatsApp para o numero com a mensagem.
    :param numero: str com o número de telefone
    :param msg: str com a mensagem que será enviada
    :return: str com o link para a iniciar a conversa com o numero enviando a mensagem
    """
    msg = '&text=' + msg if msg else ""
    if not numero.isdigit():
        raise NumeroInvalido('O número digitado é inválido.')

    numero = f'https://api.whatsapp.com/send?phone=55{numero}' if numero else ''
    return f'{numero}{msg}'


class NumeroInvalido(Exception):
    pass
