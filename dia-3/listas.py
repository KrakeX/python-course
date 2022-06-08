from unittest import result


mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
resultado = len(mi_lista)

resultado = mi_lista[0:2]

mi_lista.append(15)

print(type(mi_lista))
print(resultado)
print(mi_lista+mi_lista2)

mi_lista4 = mi_lista2.pop()
mi_lista4 = mi_lista2.pop(0)
print(mi_lista4)
