"""CryptoHack - General / XOR - You either know, XOR you don't"""
#le message est xoré avec une clé et donne le flag 
#on connait le debut et la fin du flag : {crypto{ , } 
#On sait que m^k = c alors m^c = k 

def xor_repeating(xor_result,key):
    liste=[]
    for i,octet in enumerate(xor_result):
        liste.append(octet ^key[i%len(key)])
    return bytes(liste)


if __name__ == "__main__":
    xor_result = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
    key_begin =[]
    for c1,c2 in zip(xor_result,b"crypto{"):
    #xor octet par octet
        key_begin.append(c1^c2)
    print(bytes(key_begin))        
    print(chr(xor_result[-1] ^ ord("}")))
    key = b"myXORkey"
    print(xor_repeating(xor_result,key).decode())