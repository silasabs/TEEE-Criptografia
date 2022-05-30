# Aluno: Silas JoÃ£o Bezerra Soares
# Disciplina: TEEE-Criptografia
#
# Implementação do Algoritmo de cifra Playfair.

from pydoc import plain
import string

alphabet = string.ascii_lowercase

def key_generation(key: str):
    """
    Gera uma matriz 5x5 com a chave e os demais caracteres do alfabeto  
    param key: chave a ser utilizada na matriz [str]
    
    return matrix2D: retorna a matriz 5x5 [array]
    """
    key = ''.join(key.split(' '))
    matrix = []
    
    for index in key.lower():
        if index not in matrix:
            matrix.append(index)
    pad = [index for index in alphabet if index not in matrix]
    
    matrix += pad
    matrix2D = [matrix[index*5:(index+1)*5] for index in range(5)]

    return matrix2D

def digramos(plaintext):
    """
    Separa o texto claro em digramos
    param plaintext: texto claro

    return pair: digramos do texto claro
    """
    plaintext = ''.join(plaintext.split(' ')).lower()
    # número ímpar de letras então concatenamos 'x'
    if len(plaintext) % 2 == 1:
        plaintext += 'x'
    
    pair = [list(plaintext[index:index + 2]) for index in range(0, len(plaintext), 2)]
    pair = [''.join(pair[index]) for index in range(0, len(pair))]
    
    return pair

print(digramos('silasjoao'))