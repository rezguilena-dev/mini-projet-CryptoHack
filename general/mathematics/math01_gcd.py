"""CryptoHack - General / MATHEMATICS - Greatest Common Divisor
    CryptoHack - General / MATHEMATICS - Extended GCD

"""
def pgcd(a:int, b:int) ->int: 
    a=abs(a)
    b=abs(b)
    while(b != 0):
        r= a % b
        a= b 
        b= r
    return a

def Bezout(x:int ,y:int) :
    u0,u1=1,0
    v0,v1=0,1
    while y !=0 :
        q= x // y
        r = x%y 
        x,y=y,r
        u0,u1 = u1,u0 - q*u1
        
        v0,v1 = v1,v0-q*v1
    d,u,v = x, u0, v0
    if  d<0 : 
        d=-d
        u=-u
        v=-v
    return d,u,v
if __name__ == "__main__":
    print(pgcd(12,8))
    print(pgcd(66528,52920))
    d,u,v = Bezout(26513,32321)
    print(d,u,v)
