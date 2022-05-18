import string
from hunspell import Hunspell

# Cria um objeto de discinário
h = Hunspell()

#LETRAS = 'ABCDEFGHIJKLMNOPQRSTUV'
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
    iterando sobre a chave e verificando se a nova cifra pertence
    a um discionário válido. 
    """
    flag = False
    key = 1
    
    cipher = CaesarCipher(True, "Hello", 8)

    while(flag != True):
        newcipher = CaesarCipher(False, cipher, key)
        print("key: {} cipher: {}".format(key, newcipher))
        
        if h.spell(newcipher): flag = True
        key += 1

#print(CaesarCipher(True, LETRAS, 2))
BreakCipher()

