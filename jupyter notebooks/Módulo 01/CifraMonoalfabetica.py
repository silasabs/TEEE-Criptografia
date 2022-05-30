# Aluno: Silas João Bezerra Soares
# Disciplina: TEEE-Criptografia
#
# Implementação do Algoritmo de cifra monoalfabética.
# A cifra monoalfabética se utiliza da cifra de césar como forma de chave
# armazenando um alfabeto cifrado, dessa maneira o texto claro será substituido
# pela sequência do alfabeto cifrado.

import string
import random

LETRAS = "minha primeira cifra"
alphabet = string.ascii_lowercase

def KeyMonoCipher():
    """
    Gera um alfabeto aleatório para chave de cifra monoalfabética.
    """
    # mudança aleatória de posição da tabela do alfabeto
    shift = random.randint(1, 26)
    # gera uma tabela aleatória
    shifted_alphabet = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    table = str.maketrans(string.ascii_lowercase, shifted_alphabet)

    return string.ascii_lowercase.translate(table)

def MonoAlfabeticaCipher(str, key, mod):
    """
    Função responsável por encriptar ou decriptar utilizando a cifragem monoalfabética.

    param str: texto claro ou texto cifrado [str]
    param key: alfabeto aleatório [str]
    mod: encriptar ou decriptar mensagem [bool]

    return: mensagem decriptada ou encrptada [str]
    """
    cipher = ''

    if mod == True:
        for index in str:
            if index in string.ascii_lowercase:
                indexstr = ord(index) - ord('a')
                cipher = cipher + key[indexstr]
            else:
                cipher += index
    
    else:    
        translation = str.maketrans(key, string.ascii_lowercase)
        cipher = ''.join(translation.get(index, index) for index in str)

    return cipher


key = KeyMonoCipher()

print("key: " + key)
print("plaintext: " + LETRAS)
print("cipher: " + MonoAlfabeticaCipher(LETRAS, key, True))
print("decrypted: " + MonoAlfabeticaCipher(LETRAS, key, False))