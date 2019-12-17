def hugo(palavra):
    for c in range(0, len(palavra)):
        if palavra[c] in 'a':
             palavra = palavra.replace('a', '@')
        elif palavra[c] in 'e':
            palavra = palavra.replace('e', '&')
        elif palavra[c] in 'i':
            palavra = palavra.replace('i', '!')

    return palavra


print(hugo('luar'))

