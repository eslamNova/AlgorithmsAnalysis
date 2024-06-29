import math

a,n,sd,ave = 0,0,0,0

n = int(input("how many numbers? "))
x = [0]*n

for i in range(n):
    x[i] = int(input("n>>"))
    ave += x[i]
    
ave = ave / n 

for j in x:
    a += math.pow((j-ave), 2)
    
sd = math.sqrt(a/n)

print(sd)
