
"""CryptoHack - General / Encoding - ASCII"""
#L'objectif est de décoder les entiers en ASCII
def int_to_ascii(integer_array):
    result = ""
    for value in integer_array :
        result+= chr(value)
    return result

if __name__ == "__main__":
    integer_array =[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    print(int_to_ascii(integer_array))
