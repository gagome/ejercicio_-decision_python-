"""Ejercicio N°1 
Programa para ubicar las coordenadas de un 
plano cartesiano"""

print("--------------------------------------------")
print("-----------lector de coordenadas------------")
print("--------------------------------------------")

# input

X = int(input("digite la coordenada en x: "))
Y = int(input("digite la coordenada en Y: "))

# prossecing 

if X==0 and Y==0:
    resultado=("El punto esta sobre el origen")
elif X==0 and Y>0:
    resultado=("El punto esta sobre el eje positivo de las abscisas")
elif X==0 and Y<0:
    resultado=("El punto esta sobre el eje negativo de las abscisas")
elif X>0 and Y>0:
    resultado=("El punto esta en el primer cuadrante")
elif X<0 and Y>0:
    resultado=("El punto esta en el segundo cuadrante")
elif X<0 and Y<0:
    resultado=("El punto esta en el tercer cuadrante")
elif X>0 and Y<0:
    resultado=("El punto esta en el cuarto cuadrante cuadrante")
elif X>0 and Y==0:
    resultado=("El punto esta sobre el eje positivo de las ordenadas")
elif X<0 and Y==0:
    resultado=("El punto esta sobre el eje negativo de las ordenadas")

# output

print("Si X equivale a : " + str(X) + " y Y equivale a " + str(Y) + " entonces... " + str(resultado))
