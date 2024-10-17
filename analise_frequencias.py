import collections as c
import string as s
import time as t
import unidecode as u
import os

ALFABETO:list = s.ascii_uppercase + s.ascii_lowercase + s.digits

FREQUENCIA:dict = {
    'A': 14.63,
    'B': 1.04,
    'C': 3.88,
    'D': 4.99,
    'E': 12.57,
    'F': 1.02,
    'G': 1.30,
    'H': 1.28,
    'I': 6.18,
    'J': 0.40,
    'K': 0.02,
    'L': 2.78,
    'M': 4.74,
    'N': 5.05,
    'O': 10.73,
    'P': 2.52,
    'Q': 1.20,
    'R': 6.53,
    'S': 7.81,
    'T': 4.34,
    'U': 4.63,
    'V': 1.67,
    'W': 0.01,
    'X': 0.21,
    'Y': 0.01,
    'Z': 0.47
}

FREQUENCIA_ORDENADA = dict(sorted(FREQUENCIA.items(), key=lambda x:x[1], reverse=True))

def titulo() -> None:
    print("--------------------")
    print("Análise de Frequências")
    print("--------------------\n")


def analise_frequencia(texto_alfa_num:str) -> int:  
    dicionario_letras = c.Counter(texto_alfa_num)
    dicionario_letras = dict(sorted(dicionario_letras.items(), key=lambda x:x[1], reverse=True))
    
    media = 0
    alcance = range(0,2)
    for i in alcance:
        ordem_msg = ALFABETO.index(list(dicionario_letras)[i])
        ordem_resp = ALFABETO.index(list(FREQUENCIA_ORDENADA)[i])
        media += (len(ALFABETO) + ordem_msg - ordem_resp) % len(ALFABETO)
    possivel_chave = int(media/len(alcance))
    print("Possível chave da Cifra de César: ", possivel_chave)
    return possivel_chave
    

def ler_arquivo() -> str:
    nome_arquivo = input("Escolha o nome do arquivo para descriptografar: ")
    if nome_arquivo.find(".txt") == -1:
        nome_arquivo = nome_arquivo + ".txt"
        
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()
            
    return texto


def gerar_arquivo(texto:str) -> None:
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


def decifrar_texto(texto_codificado:str, numero_chave:int) -> str:
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


def main() -> None:
    texto = ler_arquivo()
    texto_unidecode, texto_alfa_num = tratar_texto(texto)
    numero_chave = analise_frequencia(texto_alfa_num)
    texto_descriptografado = decifrar_texto(texto, numero_chave)
    gerar_arquivo(texto_descriptografado)

if __name__ == "__main__":
    main()