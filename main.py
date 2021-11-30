for i in range(128, 256):
    a = bin(i)[2:]
    b = ''
    for j in a:
        if j:
            b += '0'
        else:
            b += '1'
    if int(a, 2) - int(b, 2) == 105:
        print(i)