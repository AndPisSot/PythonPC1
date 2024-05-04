# PRACTICA 1

#VARIABLES

# Problema 1:
# Escribir un programa que solicite su nombre de usuario por consola y después de que el usuario lo
# introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es el nombre que el
# usuario haya introducido.


nombre = input("Introduce tu nombre: ")
print('¡Hola {}!'.format(nombre))

# Problema 2:
# En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
# restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
# Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
# porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
# dejar como propina.


comida=float(input("Consumo en el restaurant: $"))
porcentaje_propina=float(input("Porcentaje de propina para el mesero: "))
propina=(porcentaje_propina*comida)/100
print('Monto a dejar como propina: ${}'.format(propina))

    

peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))