def perimetri(a, b):
    p = 0
    for i in range(2):
        p = p + a + b
    return p

def syprina(a, b):
    s = a * b
    return s

def drejtekendeshi(a, b):
    if a <=0:
        print("Brinja a duhet te jete numer pozitiv!")
    elif b <= 0:
        print("Brinja b duhet te jete numer pozitiv!")
    else:
        p = perimetri(a, b)
        s = syprina(a, b)
        print("Perimetri i drejtekendeshit me brinje ", a, " dhe ", b, " eshte: ", p)
        print("Syprina e drejtekendeshit me brinje ", a, " dhe ", b, " eshte: ", s)

drejtekendeshi(2, 5)