# Aluno: Silas João Bezerra Soares
# Disciplina: TEEE-Criptografia
#

def VigenereCipher(plaintext, key, mod=True):
    """ Implementação da cifra de Vigenere

    Args:
        plaintext (str): texto claro
        key (str): chave
        mod (bool, optional): modo de operação. Defaults to False.

    Returns:
        str: texto claro ou texto cifrado
    """

    start = ord('a')
    cipher = []
    
    if mod == True:    
        for index, k in zip(plaintext, key):
            shift = ord(k) - start
            position = start + (ord(index) - start + shift) % 26
            cipher.append(chr(position))
    else:
        for index, k in zip(plaintext, key):
            position = start + ((ord(index) - start) + 26) % 26
            cipher.append(chr(position))

    return ''.join([index for index in cipher])

plaintext = "code"
key = "team"
print("Encrypt: ", VigenereCipher(plaintext, key))
print("Decrypt: ", VigenereCipher(plaintext, key, mod=False))
