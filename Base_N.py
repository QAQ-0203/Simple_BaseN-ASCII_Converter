#a simple converter between base N and ASCII


def encoder(basenum : int, map : str, entxt : str):
    if basenum != len(map):
        return "Base number is not equal to the number of the MAP"
    dec123 = ord(entxt[0])
    result = []
    for i in range(1,len(entxt)):
        dec123 = ord(entxt[i])+256*dec123

    while dec123 > 0:
        result.append(dec123%basenum)
        dec123 //= basenum
    for i in range(len(result)):
        result[i] = map[result[i]]
    result.reverse()
    encoded_txt = "".join(result)
    return encoded_txt

def decoder(basenum : int, map, detxt):
    if basenum != len(map):
        return "Base number is not equal to the number of the MAP"
    dec123 = 0
    result = []
    for i in range(len(detxt)):
        dec123 += map.index(detxt[i])*(basenum**(len(detxt)-1-i))

    while dec123 > 0:
        result.append(chr(dec123%256))
        dec123 //= 256
    result.reverse()
    decoded_txt = "".join(result)
    return decoded_txt
