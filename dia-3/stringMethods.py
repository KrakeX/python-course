texto = 'Este es el texto de Federico'

resultado = texto.upper()
resultado = texto[2].upper()

resultado = texto.lower()

resultado = texto.split('t')

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])

# Retorna un -1 si no encuentra el índice
resultadoFind = texto.find("g")


resultadoReplace = texto.replace('e', 'x')

print(resultado)
print(e)
print(resultadoReplace)
