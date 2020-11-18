from math import*
from decimal import Decimal

# Distancia Euclidean
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

# Distancia de Manhattan
def manhattan_distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))

# Distancia Minkowski
def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)

# Distancia Coseno
def minkowski_distance(x,y,p_value): 
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)
 
def cosine_similarity(x,y): 
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)


print('Coseno: ')
print cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15])
print('Minkowski: ')
print minkowski_distance([0,3,4,5],[7,6,3,-1],3)
print('Manhattan: ')
print manhattan_distance([10,20,10],[10,20,20])
print('Eucidean: ')
print (euclidean_distance([0,3,4,5],[7,6,3,-1]))

