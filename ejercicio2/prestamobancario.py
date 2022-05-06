"""Ejercicio N°2 
Programa para realizar un prestamo bancario"""

print("--------------------------------------")
print("---------Prestamo Bancario------------")
print("--------------------------------------")

# input 

ingresos=int(input("Digite sus ingresos: "))
otrasdeudas=int(input("Digite 0 si no tiene otras deudas o 1 si tiene otras deudas: "))

# prossecing

if ingresos>945200 and otrasdeudas==0:
    print("Prestamo aprobado")
else:
    print("Prestamo denegado")