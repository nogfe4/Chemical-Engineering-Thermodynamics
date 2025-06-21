#Exemplo 10.3 - Smith Van Ness
import math

y1 = 0.6
y2 = 0.4

P1sat = 45.51 #kPa
P2sat = 65.64

gamma1 = 1
gamma2 = 1

P = (1/((gamma1/(y1*P1sat))+(y2/(gamma2*P2sat))))

print(f"Pressão:{round( P, 2)} Kpa")


x1 = (y1*P)/(gamma1*P1sat)

x2 = 1 - x1

print(f"x1:{round( x1, 2)}")
print(f"x2:{round( x2, 2)}")