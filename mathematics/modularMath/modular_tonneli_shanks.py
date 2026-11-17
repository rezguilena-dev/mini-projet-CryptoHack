"""CryptoHack - MATHEMATICS /MODULAR MATH - Modular Square Root"""
#Tonelli-Shanks permet de retrouver une racine carrée modulo p
#Calculer pow(a,(p+1)//4,p) ne fonctionne pas lorsque p=1mod 4
def tonelli_shanks(a,p):
    if a%p == 0 or pow(a,(p-1)//2,p)!=1:
        raise ValueError(" a n'est pas un résidu quadratique")
    q=p-1
    s=0
    #trouver q*2^s
    while(q%2 ==0):
        q=q//2
        s=s+1
    z=2
    #trouver z residu non quadratique
    while(pow(z,(p-1)//2,p)!=-1+p):
        z+=1
    #c =z^q
    c = pow(z,q,p)
    t,r=pow(a,q,p),pow(a,(q+1)//2,p)
    while t!=1: 
        #t2 permet de calculer les t² successif
        i,t2=0,t
        #trouver i tq t²^i ==1
        while t2 !=1 :
            t2 =pow(t2,2,p)
            i +=1
        #calcul de c puissance j=s-i-1 

