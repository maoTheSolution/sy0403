def fibo(th):
    if th <= 2:
        return 1
    else :
        return fibo(th-1) + fibo(th-2)
    


print(fibo(8))