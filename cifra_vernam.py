import string as s
import time as t
import random as r
import os

ALFABETO:list = s.ascii_uppercase + s.digits
palavra_chave = ""

def titulo() -> None:
    print("--------------------")
    print("Cifra de Vernam")
    print("--------------------\n")


def ler_arquivo_texto(escolha:int):
    texto = ""
    
    if escolha == 1:
        texto = input("Escreva um texto: ")
    else:
        nome_arquivo = input("Escolha o nome do arquivo: ")
        if nome_arquivo.find(".txt") == -1:
            nome_arquivo = nome_arquivo + ".txt"
        
        with open(nome_arquivo, 'r') as arquivo:
            texto = arquivo.read()
            
    return texto


def gerar_arquivo_texto(texto:str, escolha:int) -> None:
    if escolha == 1:
        print("Mensagem: ", texto)
    else:
        nome_arquivo = input("Escolha o nome do arquivo para salvar a mensagem: ")
        if nome_arquivo.find(".txt") == -1:
            nome_arquivo = nome_arquivo + ".txt"
        
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(texto)


def xor(x: str, y: str) -> str:
    return '{0:b}'.format(int(x, 2) ^ int(y, 2))


def formatar_lista(lista: list) -> str:
    return ''.join(str(i) for i in lista)


def gerar_chaves_aleatorias(texto: str) -> str:
    item = ''
    chave = []
    for i in range(len(texto)):
        for i in range(0, 7):
            item += str(r.choice([0, 1]))
        chave.append(item)
        item = ''
    return chave


def texto_para_binario(texto: str) -> str:
    binario = [format(ord(i), 'b') for i in texto]
    print("Texto em binário: {}\n".format(formatar_lista(binario)))
    
    return binario


def gerar_chave_criptografica(texto: str) -> str:
    chave = gerar_chaves_aleatorias(texto)
    chave = formatar_lista(chave)
    print("Chave gerada: {}\n".format(chave))
    
    return chave


def one_time_pad(msg: str, pad: list) -> str:
    cifra = [xor(msg[i], pad[i]) for i in range(len(msg))]
    cifra = formatar_lista(cifra)
    print("Cifra gerada: {}\n".format(cifra))
    return cifra


def criptografar(texto: list) -> tuple:
    msg = texto_para_binario(texto)
    pad = gerar_chave_criptografica(msg)
    cifra = one_time_pad(msg, pad)

    return cifra, pad


def descriptografar(cifra: list, pad: list) -> list:
    mensagem_original = [xor(cifra[i], pad[i]) for i in range(len(cifra))]

    print("Mensagem original em binário: {}\n".format(''.join(str(i) for i in mensagem_original)))

    msg = [chr(int(item, 2)) for _, item in enumerate(mensagem_original)]
    msg = formatar_lista(msg)

    return msg


def opcao_arquivo_input() -> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo()
    print('1) Input.')
    print('2) Arquivo.')
    
    escolha = int(input("Escolha uma opção: "))
    if escolha != 1 and escolha != 2:
        print('A escolha precisa estar nas opções acima!')
        t.sleep(2)
        opcao_arquivo_input()
    
    return escolha


def cifra_vernam():
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo()
    print('1) Cifrar.')
    print('2) Decifrar.')
    
    escolha = 0
    texto = ""
    cifra = []
    pad = ""
    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            escolha = opcao_arquivo_input()
            texto = ler_arquivo_texto(escolha)
            cifra, pad = criptografar(texto)
            gerar_arquivo_texto(cifra, escolha)
            texto_descriptografado = descriptografar(cifra, pad)
            gerar_arquivo_texto(texto_descriptografado, escolha)
        case 2:
            escolha = opcao_arquivo_input()
            cifra = ler_arquivo_texto(escolha)
            texto_descriptografado = descriptografar(cifra, pad)
            gerar_arquivo_texto(texto_descriptografado, escolha)
        case _:
            print('A escolha precisa estar nas opções acima!')
            t.sleep(2)
            cifra_vernam()


def main():
    cifra_vernam()

    
if __name__ == "__main__":
    main()