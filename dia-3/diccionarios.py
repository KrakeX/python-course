diccionario = {
    "c1": "valor1",
    "c2": "valor1"
}

resultado = diccionario['c1']
print(type(diccionario))
print(resultado)


cliente = {
    'nombre': 'Juan',
    'apellido': 'Fuentes',
    'peso': 88,
    'talla': 1.76
}

consulta = cliente['talla']
print(consulta)

dic = {
    'c1': ['a', 'b', 'c'],
    'c2': ['d', 'e', 'f']
}

print(dic['c2'][1].upper())
