def zad3():
    
    invrs = 0
    print("iput digit")
    a = int(input())
    b = a
    c= 0
    while b > 0:
        invrs += int(a%10)
        invrs *= 10
        a=a/10
        b = int(b/10)
        c+=1
    print (a*(10**c))
    print(invrs/10)