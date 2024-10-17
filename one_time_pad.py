import random

def xor(x: str, y: str) -> str:
    return '{0:b}'.format(int(x, 2) ^ int(y, 2))


def formatar_lista(lista: list) -> str:
    return ''.join(str(i) for i in lista)


def gerar_chaves_aleatorias(texto: str) -> str:
    item = ''
    chave = []
    for i in range(len(texto)):
        for i in range(0, 7):
            item += str(random.choice([0, 1]))
        chave.append(item)
        item = ''
    return chave


def texto_para_binario(texto: str) -> str:
    binario = [format(ord(i), 'b') for i in texto]
    print("Texto em binário: {}\n".format(formatar_lista(binario)))
    
    return binario


def gerar_chave_criptografica(texto: str) -> str:
    chave = gerar_chaves_aleatorias(texto)
    print("Chave gerada: {}\n".format(formatar_lista(chave)))
    
    return chave


def one_time_pad(msg: list, pad: list) -> list:
    cifra = [xor(msg[i], pad[i]) for i in range(len(msg))]
    print("Cifra gerada: {}\n".format(formatar_lista(cifra)))
    return cifra


def descriptografar(cifra: list, pad: list) -> list:
    mensagem_original = [xor(cifra[i], pad[i]) for i in range(len(cifra))]

    print("Mensagem original em binário: {}\n".format(formatar_lista(mensagem_original)))

    msg = [chr(int(item, 2)) for _, item in enumerate(mensagem_original)]
    print(formatar_lista(msg))

    return mensagem_original


def main():
    texto = input('Entre com o texto a ser cifrado (ou aperte enter para texto padrão):')

    if texto == '':
        texto = "O rato roeu a roupa do rei de roma"
        
    msg = texto_para_binario(texto)
    pad = gerar_chave_criptografica(msg)
    cifra = one_time_pad(msg, pad)
    descriptografar(cifra, pad)
    
if __name__ == "__main__":
    main()