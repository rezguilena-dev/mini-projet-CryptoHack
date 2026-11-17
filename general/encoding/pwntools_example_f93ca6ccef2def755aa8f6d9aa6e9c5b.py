"""CryptoHack - General / Encoding - Encoding challenge"""

# L'objectif est de décoder automatiquement différents formats d'encodage
# (Base64,Hex,ROT13,Big Integer et UTF-8) afin de répondre aux requêtes
# d'un serveur distant et récupérer le flag .

from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes
r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decode(received):
    encoding = received["type"]
    encoded_val= received["encoded"]
    if encoding == "base64":
        return base64.b64decode(encoded_val).decode()
    elif encoding =="hex":
        return bytes.fromhex(encoded_val).decode()
    elif encoding == "rot13":
        return codecs.decode(encoded_val, "rot13")
    elif encoding == "bigint":
        return long_to_bytes(int(encoded_val, 16)).decode()
    elif encoding == "utf-8":
        return bytes(encoded_val).decode("utf-8")



received=json_recv()
for i in range(100):
    decoded_msg= decode(received)
    json_send({"decoded":decoded_msg})
    received = json_recv()
    if "flag" in received :
        print(received["flag"])
        break
r.close()


