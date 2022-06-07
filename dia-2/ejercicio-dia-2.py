nombre_usuario = input('Indique su nombre\n')
apellido_usuario = input('Indique su apellido \n')
ventas = input('Indique cuáles fueron sus ventas\n')

calculo_ventas = round(float(ventas)*0.13, 2)

print(
    f'La comisión por ventas del usuario {nombre_usuario} {apellido_usuario} por las ventas de {ventas} es de ${calculo_ventas}')
