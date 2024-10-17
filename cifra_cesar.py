import string as s
import time as t
import hashlib as h
import unidecode as u
import os

# Alfabeto em ordem
ALFABETO:list = s.ascii_uppercase + s.ascii_lowercase + s.digits

def titulo():
    print("--------------------")
    print("Cifra de César")
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
    if escolha == 1:
        print("Mensagem: ", texto)
    else:
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


def criptografar(texto_decodificado:str, numero_chave:int) -> str:
    texto_lista = list(texto_decodificado)
    for i in range(len(texto_lista)):
        if (texto_lista[i].isalnum()):
            ordem = ALFABETO.index(texto_lista[i])
            ordem = (ordem + numero_chave) % len(ALFABETO)
            texto_lista[i] = ALFABETO[ordem]
    texto_codificado = ''.join(texto_lista)
    print("Texto codificado: ", texto_codificado)
    return texto_codificado


def descriptografar(texto_codificado:str, numero_chave:int) -> str:
    texto_lista = list(texto_codificado)
    numero_chave = numero_chave % len(ALFABETO)
    for i in range(len(texto_lista)):
        if (texto_lista[i].isalnum()):
            ordem = ALFABETO.index(texto_lista[i])
            ordem = (len(ALFABETO) + ordem - numero_chave) % len(ALFABETO)
            texto_lista[i] = ALFABETO[ordem]
    texto_decodificado = ''.join(texto_lista)
    print("Texto decodificado: ", texto_decodificado)
    return texto_decodificado


def cifra_cesar():        
    escolha = 0
    opcao = 0
    numero_chave = 1
    
    while opcao != 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        titulo()
        print('1) Cifrar.')
        print('2) Decifrar.')
        print('3) Escolher Chave.')
        print('4) Sair.')
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                escolha = opcao_arquivo_input()
                texto = ler_arquivo_texto(escolha)
                texto_unidecode, texto_alfa_num = tratar_texto(texto)
                texto_criptografado = criptografar(texto_unidecode, numero_chave)
                gerar_arquivo_texto(texto_criptografado, escolha)
                input("Digite algo para continuar... ")
            case 2:
                escolha = opcao_arquivo_input()
                texto = ler_arquivo_texto(escolha)
                texto_unidecode, texto_alfa_num = tratar_texto(texto)
                texto_descriptografado = descriptografar(texto_unidecode, numero_chave)
                gerar_arquivo_texto(texto_descriptografado, escolha)
                input("Digite algo para continuar... ")
            case 3:
                numero_chave = int(input("Escolha um número de chave: "))
            case 4:
                break
            case _:
                print('A escolha precisa estar nas opções acima!')
                t.sleep(2)


def main():
    cifra_cesar()


if __name__ == "__main__":
    main()