def Fibonacci ():
    a = 0
    b = 1
    for i in range(10):
        print(a)
       #a, b = b, a+b forma mas elegante
        c = a+b
        a = b
        b = c
Fibonacci()