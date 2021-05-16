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

def get_numbers(text):
    numeros = "0123456789"
    str = ""
    for c in text:
        if c in numeros:
            str += c
    return str

def valida_cpf(cpf):
    cpf_valido = True
    cpf_str = str(cpf)

    old_str = cpf_str
    cpf_str = get_numbers(cpf_str)

    if old_str != cpf_str:
        cpf_valido = False

    if cpf_valido:
        if len(cpf_str) != 11:
            cpf_valido = False

    if cpf_valido:
        digitos_principal = cpf_str[0:9]
        digitos_verificacao = cpf_str[9:12]

        primeiro_digito_esperado = calcula_digito(digitos_principal)
        segundo_digito_esperado = calcula_digito(digitos_principal + str(primeiro_digito_esperado))

        condicional_primeiro = str(primeiro_digito_esperado) == digitos_verificacao[0]
        condicional_segundo = str(segundo_digito_esperado) == digitos_verificacao[1]

        cpf_valido = condicional_primeiro and condicional_segundo

    return cpf_valido