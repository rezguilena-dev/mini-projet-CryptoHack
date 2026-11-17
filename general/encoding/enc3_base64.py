"""CryptoHack - General / Encoding - Base64"""

#l'objectif est de transformer une chaine hexadecimale en base 64 puis en chaine de caractères
import base64
def hex_to_64(hex_string):
    return base64.b64encode(bytes.fromhex(hex_string)).decode()


if __name__ == "__main__":
    hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    print(hex_to_64(hex_string))