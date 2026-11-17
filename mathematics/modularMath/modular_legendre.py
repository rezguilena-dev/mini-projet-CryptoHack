"""CryptoHack - MATHEMATICS /MODULAR MATH - Legendre Symbol"""
#l'objectif est d'identifier une racine quadratique grâce au symbole de legendre
#puis calculer ses racines 

def extract_data(file_path):
    with open(file_path,"r") as f:
        for line in f :
            if line.startswith("p ="):
                p= int(line.split("=")[1])
            elif line.startswith("ints ="):
                tab= line.split("=")[1].strip()
                text = tab.strip("[]")
                ints=[]
                for x in text.split(","):
                    ints.append(int(x))
        return p,ints

if __name__ == "__main__":
    file_path = "annexe/output.txt"
    p,ints= extract_data(file_path)
    for a in ints :
        if a%p!=0 and pow(a,(p-1)//2,p) == 1 :
            r=pow(a,(p+1)//4,p)
            print(max(r,p-r))
            