# Aluno: Silas João Bezerra Soares
# Disciplina: TEEE-Criptografia
#
# Implementação do algoritmo de cifra de césar

import string
import re
from hunspell import Hunspell

# Cria um objeto de dicinário
h = Hunspell()

#LETRAS = "ABCDEFGHIJKLMNOPQRSTUV"
LETRAS = "CDEFGHIJKLMNOPQRSTUVWX"

def CaesarCipher(mod, text, shift):
    """
    Função que implementa a cifra de cesar

    param mod: encriptação ou decriptação [bool] 
    param text: texto claro [str]
    praram shift: chave de deslocamento do alfabeto [int]

    return: texto cifrado com a nova tabela deslocada ou texto claro.
    """
    shift = shift if mod else shift*-1

    shifted_alphabet = string.ascii_letters[shift:] + string.ascii_letters[:shift]
    table = str.maketrans(string.ascii_letters, shifted_alphabet)
    
    return text.translate(table)

def BreakCipher():
    """
    Função que executa ataque de força bruta a cifra de césar
    iterando sobre a chave e verificando se as palavras que estão
    na nova cifra pertencem a um dicionário válido. 
    """
    flag = False
    key = 1
    
    cipher = CaesarCipher(True, "ml guys this is a secret message", 8)

    while(flag != True):
        newcipher = CaesarCipher(False, cipher, key)
        print("key: {} cipher: {}".format(key, newcipher))
        
        cipher_split = newcipher.split()
        for index in range(len(cipher_split)):
            if h.spell(cipher_split[index]):
                flag = True
            else:
                flag = False
        key += 1

#print(CaesarCipher(True, LETRAS, 2))
BreakCipher()

