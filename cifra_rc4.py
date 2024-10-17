import time as t
import unidecode as u
import os

def titulo():
    print("--------------------")
    print("Cifra RC4")
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


def key_scheduling(chave:str) -> list:
    sched = [i for i in range(0, 256)]
    
    i = 0
    for j in range(0, 256):
        i = (i + sched[j] + chave[j % len(chave)]) % 256
        
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        
    return sched
    

def stream_generation(sched:list):
    stream = []
    i = 0
    j = 0
    while True:
        i = (1 + i) % 256
        j = (sched[i] + j) % 256
        
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        
        yield sched[(sched[i] + sched[j]) % 256]        


def criptografar(texto:str, chave:str) -> str:
    texto = [ord(char) for char in texto]
    chave = [ord(char) for char in chave]
    
    sched = key_scheduling(chave)
    key_stream = stream_generation(sched)
    
    texto_criptografado = ''
    for char in texto:
        enc = str(hex(char ^ next(key_stream))).upper()
        texto_criptografado += (enc)
        
    return texto_criptografado
    

def descriptografar(texto_criptografado:str, chave:str) -> str:
    texto_criptografado = texto_criptografado.split('0X')[1:]
    texto_criptografado = [int('0x' + c.lower(), 0) for c in texto_criptografado]
    chave = [ord(char) for char in chave]
    
    sched = key_scheduling(chave)
    key_stream = stream_generation(sched)
    
    plaintext = ''
    for char in texto_criptografado:
        dec = str(chr(char ^ next(key_stream)))
        plaintext += dec
    
    return plaintext


def cifra_rc4():        
    escolha = 0
    opcao = 0
    chave = "Ola"
    
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
                texto_criptografado = criptografar(texto_unidecode, chave)
                gerar_arquivo_texto(texto_criptografado, escolha)
                input("Digite algo para continuar... ")
            case 2:
                escolha = opcao_arquivo_input()
                texto = ler_arquivo_texto(escolha)
                texto_unidecode, texto_alfa_num = tratar_texto(texto)
                texto_descriptografado = descriptografar(texto_unidecode, chave)
                gerar_arquivo_texto(texto_descriptografado, escolha)
                input("Digite algo para continuar... ")
            case 3:
                chave = input("Escolha uma palavra para a chave: ")
            case 4:
                break
            case _:
                print('A escolha precisa estar nas opções acima!')
                t.sleep(2)


def main():
    cifra_rc4()


if __name__ == "__main__":
    main()