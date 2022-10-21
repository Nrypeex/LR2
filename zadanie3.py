def zad3():
    
    invrs = []
    print("iput digit")
    a = int(input())
    b = a
    while b > 0:
        invrs.append(int(a%10))
        a=a/10
        b = int(b/10)
    print (a)
    print(invrs)