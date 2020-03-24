# import this
from patterns.singleton import Singleton


A = Singleton()
B = Singleton()

print(id(A) == id(B))
A.some_business_logic()

