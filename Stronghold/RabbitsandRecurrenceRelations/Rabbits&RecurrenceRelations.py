


# n is the n(th) month 
# k is the number of offspring each adult generation creates 

def num_rabbits(n , k) :
    if (n == 1 ):
        return 1
    elif (n == 2): 
        return k
    oneGen = num_rabbits(n-1, k)
    twoGen = num_rabbits(n-2, k)
    if (n <= 4) :
        return (oneGen + twoGen)
    
    return (oneGen + (twoGen * k));         

print(num_rabbits(30,4))