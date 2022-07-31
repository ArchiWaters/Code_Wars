def divisors(n):
    k = 0
    for num in range(1,n+1):
        if n%num == 0:
            k += 1
    print(k)
    
divisors(4096)