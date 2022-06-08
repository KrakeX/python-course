# son inmutables
# permiten tuplas
# no admite listas ni diccionarios

mi_set = set([1, 2, 3, 4, 5])

print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3}

print(type(otro_set))
print(otro_set)


print(len(mi_set))
print(2 in mi_set)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.add(4)
s2.add(2)
s1.remove(3)

s1.discard(2)
s1.pop()  # Peligroso, puede eliminar cualquiera al azar (WTF? XD)
s3 = s1.union(s2)

print(s3)
