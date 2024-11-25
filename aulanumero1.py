def aumentar_preco(preco_antigo:float, porcentagem:int):

    valor_porcentagem = 1 + (porcentagem /100)
    preco_novo=preco_antigo*valor_porcentagem
    return preco_novo