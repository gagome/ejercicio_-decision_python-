"""Ejercicio N°4
Programa para calcular el IMC de una persona"""

print("---------------------------------------")
print("-------Indice de masa corporal---------")
print("---------------------------------------")

# input

peso =int(input("Ingrese su peso en kilos: "))
estatura =float(input("Ingrese su estatura en metros: "))

# prcessing

imc=peso/(estatura**2)

#output

if imc<16:
    print("Criterio de ingreso en hospital")
if imc>16 and imc<=17:
    print("Infrapeso")
if imc>17 and imc<=18:
    print("Bajo peso")
if imc>18 and imc<=25:
    print("Peso normal (saludable)")
if imc>25 and imc<=30:
    print("Sobrepeso (obesidad de grado I)")
if imc>=30 and imc<=35:
    print("Sobrepeso crónico (obesidad de grado II)")
if imc>35 and imc<=40:
    print("Obesidad premórbida (obesidad de grado III)")
if imc>40:
    print("Obesidad mórbida (obesidad de grado IV)")