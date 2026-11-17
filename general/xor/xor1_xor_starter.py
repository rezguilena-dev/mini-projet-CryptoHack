"""CryptoHack - General / XOR - XOR Starter"""

#xor entre chaine de caractère et un entier 
#On convertit la chaine en code ascii ,on xor avec 13, puis on retransforme en chaine.
def xor_string(word, key):
    res=""
    for c in word :
        res+=chr(ord(c)^ key)
    return res
    


if __name__ == "__main__":
    result = xor_string("label", 13)
    print(result)