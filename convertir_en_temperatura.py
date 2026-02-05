#programa de covertir en temperatura

#libreria
import math


print("                                   ")
print("convertir grados farenheit y kelvil")
print("                                   ")

#imput
c=int(input("ingrese el valor de grados centigrados: "))

#procedimiento
f= (c*9/5) + 32
k= c + 273.15

#output
print("              ")
print("   Resultado  ")
print("              ")
print("Los grados farenheit es : " + str(f))
print("Los grados kelvil es: " + str(k))
