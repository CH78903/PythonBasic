#Loops

mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("El numero es:",i)

resultado=0
for i in mi_lista:
     resultado += i

print(f"El resultado de la suma de mi lista es: {resultado}")   

for i in range(2, 9):
    print(i)

mi_lista_2 = ["lunes","martes","miercoles","jueves","viernes"] 
contador = 0 
while contador < 3: 
    for i in mi_lista_2: 
        if i != "lunes":
            print(i) 
    contador += 1
# While loop
    

#Practica 2
# Dada la lista mi_lista_2 = ["Lunes", "Martes", "Miercoles","Jueves","Viernes"]
# Imprimer cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
# PISTA: usa los dos tipos de loops while y for en el mimo programa para lograrlo 
# Resultado
# Martes
# Miercoles
# Jueves 
# Viernes 
# Martes 
# Miercoles
# Jueves 
# Viernes
# Martes 
# Miercoles
# Jueves 
# Viernes

