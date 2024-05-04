# PRACTICA 1

#VARIABLES

# Problema 1:
# Escribir un programa que solicite su nombre de usuario por consola y después de que el usuario lo
# introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es el nombre que el
# usuario haya introducido.

#Leer nombre solicitado
nombre = input("Introduce tu nombre: ")
#Imprimir cadena completa
print('¡Hola {}!'.format(nombre))

# Problema 2:
# En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
# restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
# Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
# porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
# dejar como propina.

#Pregunta al usuario
comida=float(input("Consumo en el restaurant: $"))
porcentaje_propina=float(input("Porcentaje de propina para el mesero: "))
#Calculo de la propina
propina=(porcentaje_propina*comida)/100
#Mostrar la propina
print('Monto a dejar como propina: ${}'.format(propina))

# Problema 3:
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
# por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
# peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
# cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
# último pedido y calcule el peso total del paquete que será enviado.
  
# Definir los pesos
peso_payaso = 112
peso_muñeca = 75
# Leer el número de payasos y muñecas
payasos = int(input("Ingrese el número de payasos vendidos en el último pedido: "))
muñecas = int(input("Ingrese el número de muñecas vendidas en el último pedido: "))
#Calcular el peso del paquete
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
#Mostrar peso total del paquete
print('El peso total del paquete es {}'.format(peso_total))