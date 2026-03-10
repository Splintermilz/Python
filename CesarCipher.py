# CesarCipher

def plaintext(cleartext: list ) -> int:
    plaintext=""
    for i in cleartext:
        plaintext = plaintext+chr(ord(i)+3)
    return plaintext

def cipher(ciphertext: list) -> str:
    cipher=""
    for i in ciphertext:
        cipher=cipher+chr(ord(i)-n)
    return cipher



cleartext = input("Please introduce your plaintext password : ")
ciphertext = ""

