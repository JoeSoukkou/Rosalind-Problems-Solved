# Given n < 25 , Generate the corresponding F(n)
# n = 0 => F(n) = 0
# n = 1 => F(n) = 1
# n > 1 => F(n) = F(n-1) + F(n-2)

def FIBO(n):
    if (n == 0) : 
        return 0
    elif (n == 1) : 
        return 1
    else :
        return (FIBO(n-1) + FIBO(n-2))

n = int(input("n = "))
if (n): 
    print("F("+str(n)+") = "+str(FIBO(n)))                