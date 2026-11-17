"""CryptoHack - General / Encoding - Bytes and Big Integers"""
#l'objectif est de tranformer un grand nombre en base 256 puis en chaine de caractères
from Crypto.Util.number import *


def int_to_message(n):
    print(long_to_bytes(n))
    return long_to_bytes(n).decode()


if __name__ == "__main__":
    n = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    print(int_to_message(n))