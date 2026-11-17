"""CryptoHack - General / XOR - favorite byte"""

#-le message est XORé avec un seul octet inconnu
"""pour le retrouver il suffit de tester par force brute et on vérifie cele qui donne  
le flag "commençant par  crypto{"""
def xor_same_byte(xor_result,key):
    res=[]
    for octet in xor_result :
        res.append(octet ^ key )
    return bytes(res)



if __name__ == "__main__":
    xor_result = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
    for key in range(256):
        result = xor_same_byte(xor_result,key)
        if result.startswith(b"crypto{"):
            print(key, result.decode())