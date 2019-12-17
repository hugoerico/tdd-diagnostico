def hugo(palavra_frase):
    for c in range(0, len(palavra_frase)):
        if palavra_frase[c] in 'a':
             palavra_frase = palavra_frase.replace('a', '@')
        elif palavra_frase[c] in 'e':
            palavra_frase = palavra_frase.replace('e', '&')
        elif palavra_frase[c] in 'i':
            palavra_frase = palavra_frase.replace('i', '!')

    return palavra_frase


print(hugo('luar'))

