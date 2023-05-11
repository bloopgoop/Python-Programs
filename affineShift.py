#Affine shift caesar cipher
def affineShift(text, key1, key2):
    ciphertext = ''
    for char in text:
        num = (ord(char) - 96) % 26
        print(num)
        if ((num * key1 + key2) % 26) + 96 == 96:
            ciphertext += 'z'
        else:
            ciphertext += chr(((num * key1 + key2) % 26) + 96)

    return ciphertext

#print(affineShift("attackatdawn", 5, 3))

def decodeAffine(text, key1, key2):
    cleartext = ''
    for char in text:
        num = ((ord(char) - 96 - 2) * 3) % 26
        print(num)
        cleartext += chr(num + 96)
    return cleartext

print(decodeAffine("pgzkzg", 9, 2))
