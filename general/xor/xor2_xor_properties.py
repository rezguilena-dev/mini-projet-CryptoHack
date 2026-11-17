"""CryptoHack - General / XOR - XOR Properties"""
#On xor les informations entre elles pour annuler les clés 1,2,3 jusqu'à retomber sur le flag
def xor_bytes(x1,x2):
    liste=[]
    for x,y in zip(x1,x2):
        liste.append(x ^ y)
    return bytes(liste)


if __name__ == "__main__":
    key1 =bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
    k2_k3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
    final = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
    flag = xor_bytes(xor_bytes(final,k2_k3),key1)
    print(flag.decode())