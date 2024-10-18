import time as t
import random as r
import unidecode as u
import os

def titulo() -> None:
    print("--------------------")
    print("One Time Pad (OTP)")
    print("--------------------\n")


def ler_arquivo_texto(escolha:int) -> str:
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
    if escolha == 2:
        nome_arquivo = input("Escolha o nome do arquivo para salvar a mensagem: ")
        if nome_arquivo.find(".txt") == -1:
            nome_arquivo = nome_arquivo + ".txt"
        
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(texto)
            
            
def tratar_texto(texto:str) -> tuple:
    texto_unidecode = u.unidecode(texto)
    
    texto_alfa_num = list([val for val in texto_unidecode if val.isalpha() or val.isnumeric()])
    texto_alfa_num = "".join(texto_alfa_num)
            
    return texto_unidecode, texto_alfa_num

            
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


def criptografar(texto:str) -> tuple:
    binario = [format(ord(i), 'b') for i in texto]
    print("Texto em binário: {}\n".format(formatar_lista(binario)))
    
    chave = gerar_chaves_aleatorias(binario)
    print("Chave gerada: {}\n".format(formatar_lista(chave)))
    
    cifra = [xor(binario[i], chave[i]) for i in range(len(binario))]
    print("Cifra gerada: {}\n".format(formatar_lista(cifra)))
    
    return cifra, chave


def descriptografar(cifra: list, pad: list) -> list:
    mensagem_original = [xor(cifra[i], pad[i]) for i in range(len(cifra))]

    print("Mensagem original em binário: {}\n".format(formatar_lista(mensagem_original)))

    msg = [chr(int(item, 2)) for _, item in enumerate(mensagem_original)]
    print(formatar_lista(msg))

    return mensagem_original


def cifra_vernam2():
    texto = input('Entre com o texto a ser cifrado (ou aperte enter para texto padrão):')

    if texto == '':
        texto = "O rato roeu a roupa do rei de roma"
        
    cifra, pad = criptografar(texto, pad)
    descriptografar(cifra, pad)


def one_time_pad():        
    escolha = 0
    opcao = 0
    cifra = []
    chave = ""
    
    while opcao != 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo()
        print('1) Cifrar.')
        print('2) Decifrar.')
        print('3) Sair.')
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                escolha = opcao_arquivo_input()
                texto = ler_arquivo_texto(escolha)
                texto_unidecode, texto_alfa_num = tratar_texto(texto)
                cifra, chave = criptografar(texto_unidecode)
                gerar_arquivo_texto(formatar_lista(cifra), escolha)
                input("Digite algo para continuar... ")
            case 2:
                escolha = opcao_arquivo_input()
                texto = list(ler_arquivo_texto(escolha))
                texto_descriptografado = descriptografar(cifra, chave)
                gerar_arquivo_texto(texto_descriptografado, escolha)
                input("Digite algo para continuar... ")
            case 3:
                break
            case _:
                print('A escolha precisa estar nas opções acima!')
                t.sleep(2)


def main():
    one_time_pad()

    
if __name__ == "__main__":
    main()