
p=161258
r=5
t=1

si=p*r*t*0.01

print("Si : ",si)


Amount = p * (pow((1 + r / 100), t))
ci = Amount - p 
print("Compound interest is", ci)