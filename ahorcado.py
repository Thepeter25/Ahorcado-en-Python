import random
import time

## Fecha de inicio 27-1-22
 
## Listado de palabras
marcas_de_ordenadores = ["acer", "lenovo", "asus", "msi", "hp", "xiaomi", "dell"]
 
modelos_de_seat = [ "arona", "altea", "leon", "alhambra", "toledo", "ateca", "tarraco"]

## Marcas de ordenadores posibles: Chuwi, Medion
 
print ("Juego del ahorcado. © Thepeter25. Disfruta del juego!")
time.sleep (1)
print("Vamos a jugar al ahorcado!")
time.sleep(2)
print("Para ganar el juego, tienes que adivinar una palabra la cual no conoces y para adivinarla tienes que elegir una letra.")
print("Dispones de 5 vidas, pierdes una vida cada vez que eliges una letra y no está en la palabra.")
print (" En caso de quedarte sin vidas, perderás el juego")
time.sleep(2)

## Pantalla de carga troll xD

print ("Cargando") 
time.sleep (2) 
print ("...")

## Elegir palabras
 
print("¿Deseas jugar con palabras que son marcas de ordenadores o modelos de seat?")
time.sleep(2)
 
cat_seleccionada = input("Pulsa la tecla O para marcas de ordenadores y S para modelos de seat: ")
## Elegir: cat_seleccionada.lower () == ''letra'':

while True:
    if cat_seleccionada.lower() == "o":
        print("Has seleccionado marcas de ordenadores")
        palabra_secreta = random.choice(marcas_de_ordenadores)
        break
    elif cat_seleccionada.lower() == "s":
        print("Has seleccionado modelos de seat")
        palabra_secreta = random.choice(modelos_de_seat)
        break
 
    else:
        print("Por favor selecciona una categoria válida")
        cat_seleccionada = input("Pulsa la tecla O para marcas de ordenadores y S para modelos de seat: ")
 
 
 
## Nº de vidas
vidas = 5

## Juego
 
lista_letras_adivinadas = []
 
print('_' * len(palabra_secreta))
 
while True:
 
    while True:
        letra_adivinada = input("Adivina una letra: ")
        if(len(letra_adivinada)!=1 and letra_adivinada.isnumeric()):
            print("Solo puedes utilizar letras")
        else:
            if letra_adivinada.lower() in lista_letras_adivinadas:
                print("Ya has usado esa letra, utiliza otra")
            else:
                lista_letras_adivinadas.append(letra_adivinada)
 
                if letra_adivinada.lower() in palabra_secreta:
                    print("Felicidades has adivinado una letra")
                    break
                else:
                    vidas = vidas-1
                    print("Te has equivocado, por lo tanto, has perdido una vida")
                    print("Te quedan " + str(vidas) + " vidas")
                    break
 
## No se adivina la palabra
    if vidas==0:
        print("Has perdido :'(. La palabra secreta era: "+ palabra_secreta)
        time.sleep (3)
        break
 
 
    estatus_actual = ""
 
    letras_faltantes = 0
    for letra in palabra_secreta:
 
 
        if letra in lista_letras_adivinadas:
            estatus_actual = estatus_actual + letra
 
        else:
            estatus_actual = estatus_actual + "_"
            letras_faltantes = letras_faltantes + 1
 
    print(estatus_actual)
 
## Se adivina la palabra

    if letras_faltantes == 0:
        print("Felicidades! :D has adivinado la palabra")
        print("La palabra secreta es: " + palabra_secreta)
        time.sleep (3)
        break
        
## Fecha de finalización 4-2-22