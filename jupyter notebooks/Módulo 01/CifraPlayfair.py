# Aluno: Silas João Bezerra Soares
# Disciplina: TEEE-Criptografia
#

import string

def key_generation(key: str):
    """ Função responsável por inserir a chave na matriz de dimensão 5x5 além
    de adicionar o alfabéto levando em consideração letras já presentes na chave.

    Args:
        key (str): chave 

    Returns:
        array: matriz com a chave e demais caracteres do alfabeto.
    """
    key = key.upper()
    
    # Cria uma lista de listas assumindo uma matrix 5x5
    matrix = [[0 for i in range (5)] for j in range(5)]
    letters_added = []
    
    row = 0
    col = 0
   
    # Adiciona a chave na matriz
    for letter in key:
        
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
    
        if (col == 4):
            col = 0
            row += 1
        
        else:
            col += 1
    
    # Adiciona o alfabeto a matriz
    for letter in range(65, 91):
        if letter == 74: # I/J estão na mesma posição
            continue
        if chr(letter) not in letters_added:
            letters_added.append(chr(letter))
            
    #print (len(letters_added), letters_added)
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index += 1 
    
    return matrix


def separate_letters(message):
    """ Separa a mensagem em digramos concatenando X caso a mesma seja de tamanho ímpar

    Args:
        message (str): texto claro

    Returns:
        str: string separada por digramos
    """
    
    index = 0
    
    while (index < len(message)):
    
        char1 = message[index]

        if index == len(message) - 1:
            message = message + 'X'
            index += 2
            continue
        
        char2 = message[index+1]
    
        if char1 == char2:
            message = message[:index+1] + "X" + message[index+1:]
        index += 2
    
    return message


def indexOf(letter, matrix):
    """ Função de indexação responsável por retorna a posição na primeira ocorrência
    do caracter

    Args:
        letter (str): caracter de interesse
        matrix (str): matriz 5x5 

    Returns:
        Par de ocorrência
    """
    for i in range(5):
        try:
            index = matrix[i].index(letter)
            return (i, index)
        except:
            continue


def playfair(key, message, mod=True):
    """ Função responsável por realizar a cifra de playfair

    Args:
        key (str): chave definida pelo usuário
        message (str): texto claro
        mod (bool, optional): modo de encriptação ou decriptação. Defaults to True.

    Returns:
        str: mensagem cifrada ou decriptada.
    """

    inc = 1
    inc = inc if mod else inc*-1
    
    matrix = key_generation(key)
    message = message.upper()
    message = message.replace(' ', '')
    message = separate_letters(message)
    
    cipher_text = ''

    for (l1, l2) in zip(message[0::2], message[1::2]):
        
        row1, col1 = indexOf(l1, matrix)
        row2, col2 = indexOf(l2, matrix)
        
        if row1 == row2:
            cipher_text += matrix[row1][(col1+inc) % 5] + matrix[row2][(col2+inc) % 5]
        elif col1 == col2: 
            cipher_text += matrix[(row1+inc) % 5][col1] + matrix[(row2+inc) % 5][col2]
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]

    return cipher_text

print('Encripting:')
print(playfair('secret', 'my secret message'))
print('Decrypting:')
print(playfair('secret', 'LZECRTCSITCVAHBT', False))