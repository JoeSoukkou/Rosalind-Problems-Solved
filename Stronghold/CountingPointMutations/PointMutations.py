


f = open("rosalind_hamm.txt", "r")
lines = f.readlines()
s = lines[0]
t = lines[1]
HammingDistance = 0
counter = 0
while (counter <= len(s) - 1):
    if (s[counter] != t[counter]):
        HammingDistance += 1
    counter += 1
print(s)
print(t)    
print(HammingDistance)        
