def soma_digitos_validacao(digitos):
    digitos_str = str(digitos)
    soma_digitos = 0
    for digito_posicao in range(len(digitos_str)):
        soma_digitos += int(digitos_str[digito_posicao]) * (len(digitos_str)+3 - (2 + digito_posicao))
    return soma_digitos

def calcula_digito(digitos_str):
    soma_digitos = soma_digitos_validacao(digitos_str)
    resto_divisao_soma_digitos = soma_digitos % 11
    digito_esperado = 0 if resto_divisao_soma_digitos < 2 else 11 - resto_divisao_soma_digitos
    return digito_esperado

def valida_cpf(cpf):
    cpf_str = str(cpf)
    digitos_principal = cpf_str[0:9]
    digitos_verificacao = cpf_str[9:12]

    primeiro_digito_esperado = calcula_digito(digitos_principal)
    segundo_digitoEsperado = calcula_digito(digitos_principal + str(primeiro_digito_esperado))
    
    return (primeiro_digito_esperado == digitos_verificacao[0]) and (segundo_digito_esperado == digitos_verificacao[1])