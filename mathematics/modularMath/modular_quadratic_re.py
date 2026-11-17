"""CryptoHack - MATHEMATICS /MODULAR MATH - Quadratic residues"""
#sur une liste de int ,l'objectif est de retrouver lequel est un residu quadratique 
#l'idée : rechercher a tel que a²= x mod p avec x dans ints

if __name__ == "__main__":
    p=29
    ints =[14,6,11]
    for x in ints : 
        for a in range(1,(p-1)//2+1):
            if a*a %p == x: 
                print(x)
                print(a)
                break