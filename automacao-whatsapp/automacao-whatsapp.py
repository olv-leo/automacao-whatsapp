

def gerar_link_wpp(numero, msg=None) :



    """
    Recebe um número e uma mensagem e gera um link de WhatsApp para o numero com a mensagem.
    :param numero: str com o número de telefone
    :param msg: str com a mensagem que será enviada
    :return: str com o link para a iniciar a conversa com o numero enviando a mensagem
    """
    msg = "&text=" + msg if msg else ""
    return f"https://api.whatsapp.com/send?phone=55{numero}{msg}"
if __name__ == "__main__" :
    print(gerar_link_wpp(16997952356))
    print(gerar_link_wpp(16997952356, "Teste"))



