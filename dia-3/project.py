ingreso_usuario = input('Por favor ingrese un texto cualquiera\n')

parametro1, parametro2, parametro3 = [input('Ingrese una letra\n'), input(
    'Ingrese otra letra\n'), input('Ingrese una última letra\n')]

print(
    f'La letra {parametro1} aparece {ingreso_usuario.lower().count(parametro1.lower())}')
print(
    f'La letra {parametro2} aparece {ingreso_usuario.lower().count(parametro2.lower())}')
print(
    f'La letra {parametro3} aparece {ingreso_usuario.lower().count(parametro3.lower())}')

numero_de_palabras = len(ingreso_usuario.split())
print(f'El texto tiene un total de {numero_de_palabras} palabras')

print(
    f'La primera letra del texto es {ingreso_usuario[0]} y la última es {ingreso_usuario[-1]}')

orden_inverso = " ".join(ingreso_usuario.split(' ')[::-1])
print('Las palabras en orden inverso serían: {orden_inverso}')


python_found = ingreso_usuario.find('python') != -1
print(f'La palabra python aparece?: {python_found}')
