"""CryptoHack - MATHEMATICS /MODULAR MATH - Chinese Remainder Theorem"""
# L'objectif est de trouver un entier x qui satisfait plusieurs congruences
# en utilisant le théorème des restes chinois
from functools import reduce
from math import gcd

def restes_chinois(restes,modules):
    x,N=restes[0],modules[0]
    for pi,ni in zip(restes[1:],modules[1:]):
        k=(pi-x)*pow(N,-1,ni)%ni
        x+=N*k 
        N*=ni 
    return x%N

if __name__ == "__main__":
    reste=[2,3,5]
    modules=[5,11,17]
    print(restes_chinois(reste,modules))

   