import math

n = int(input("how many numbers? "))
x,a = [], 0

for i in range(n):
    t = int(input("ente>> "))
    x.append(t)
    
m = sum(x) / n 

for j in x:
    a += math.pow((j-m), 2)
    
sd = math.sqrt(a/n)

print(sd)
