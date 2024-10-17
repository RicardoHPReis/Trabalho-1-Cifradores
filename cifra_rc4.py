import time as t
import os

def key_scheduling(chave):
    sched = [i for i in range(0, 256)]
    
    i = 0
    for j in range(0, 256):
        i = (i + sched[j] + chave[j % len(chave)]) % 256
        
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        
    return sched
    

def stream_generation(sched):
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


def criptografar(text, chave):
    text = [ord(char) for char in text]
    chave = [ord(char) for char in chave]
    
    sched = key_scheduling(chave)
    key_stream = stream_generation(sched)
    
    ciphertext = ''
    for char in text:
        enc = str(hex(char ^ next(key_stream))).upper()
        ciphertext += (enc)
        
    return ciphertext
    

def descriptografar(ciphertext, chave):
    ciphertext = ciphertext.split('0X')[1:]
    ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
    chave = [ord(char) for char in chave]
    
    sched = key_scheduling(chave)
    key_stream = stream_generation(sched)
    
    plaintext = ''
    for char in ciphertext:
        dec = str(chr(char ^ next(key_stream)))
        plaintext += dec
    
    return plaintext


if __name__ == '__main__':
    ed = input('Enter E for criptografar, or D for descriptografar: ').upper()
    if ed == 'E':
        plaintext = input('Enter your plaintext: ')
        chave = input('Enter your secret chave: ')
        result = criptografar(plaintext, chave)
        print('Result: ')
        print(result)
    elif ed == 'D': 
        ciphertext = input('Enter your ciphertext: ')
        chave = input('Enter your secret chave: ')
        result = descriptografar(ciphertext, chave)
        print('Result: ')
        print(result)
    else:
        print('Error in input - try again.')