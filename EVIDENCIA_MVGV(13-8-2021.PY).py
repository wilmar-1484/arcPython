#@archivo EVIDENCIA_MVGV(13-8-2021)
#@autor MADAIVALENTINAGARCIAVEALSQUEZ
#@fecha 13/08/2021

#Operaciones
# val=0
# print( val==3)
# print ( val==0)
# print(val!=0)
# print(val > 0)
# print(val<0)
# print(val<=0)
# print(val >=0)
# print(3+ 5 > 9-6)
# print("Madai==" "Madai")

# # usando uno de los operadores de compracion de python,escribir un programa de dos lineas que tome el paramatro n entrda que es un entero o imprimafalse si n es menor que 100 y truel si n es mayor o igual que 100
# #no se debe crear ingun bloque if
# #datos de prueba:
# #ejemplo de entrada 55 resultado False
# #ejemplo de entrada 99 resulstado False
# #ejemplo de  entrada100 resultado truel
# n= int
# print(n>100)

# #tarea
# #agregar un codigo sin modificar el codigo  que tedemos

# #leedos numeros
# numero1=int (input("ingrese el primer numero"))
# numero2=int(input("ingresa el sugundo numero"))

# #elegir el numero mas grande
# if numero1> numero2:nmasGrande=numero1
# else: nmasGrande=numero2
# #imprimir el resultado
# print("el numero mas grande es", nmasGrande)

#almacenar el numero mas grande actual  aqui
numeroMayor = -999999999
#ingresa el primer valor
numero=int(input("introduzca un numero o escriba -1 para detener"))
#si el numero no es igual a -1, continuaremos
while numero !=-1:
    #¿es el numero mas grande que el numero mas grande?
    if numero> numeroMayor:
#si, si actualiza el mayor numeroMayor
     numeroMayor=numero
#ingresa el siguiente numero
numero=int (input("indtroduzca un  numero o escriba -1 para detener"))

# imprimir el resultado
print("El numero mas grande es:", numeroMayor)

#ejemplo
#progrma que lee una secuencia de numeros y cuenta cuantos numeros son pares
#y cuantos son impares.El progrma termina cuando se ingresa 0
# contadorpares=0
# contadoresimpares=0
# numero=int (int(input("introduce un numero o escribe 0 para detener:")))
# while numero!=0:
#     if numero % 2==1:
#        contadoresimpares+=1
#     else:
#         contadorpares +=1
#     numero=int(input("introduce un numero o escriba 0 para detener:"))
# print("numeros pares:" , contadorpares)
# print("numeros impares",contadorpares)

#ejemplo
# for i in range(100):
# #hacer algo
# pass

# #ejemplo
# for i in range (2,8):
#     print("el valor de i es actualmente", i)
# #ejemplo
# for i in range (2,8,3):
#      print("el valor de i es actualmente", i)

#  #ejemplo
# for i in  range (1,6):
#       print (i, "missisisipi") 
#       tiem.slepp(1)
# print ("¡listo o no, ahi voy!")















