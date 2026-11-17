"""CryptoHack - General / XOR - Lemur XOR"""

#pour retrouver le flag suffit de xorer les deux images ce qui annule la clé et superpose les pixels
#on ne xor pas les fichiers images directement mais les pixels RGB
import PIL.Image
import numpy as np

lemur ="annexe/lemur.png"
flag ="annexe/flag.png"
image1= np.array(PIL.Image.open(lemur).convert("RGB"))
image2= np.array(PIL.Image.open(flag).convert("RGB"))

result = image1 ^ image2
PIL.Image.fromarray(result).save("annexe/result.png")