print("Bienvenido a ... ")
print("""                    _____           
  ___ _ __ _   _/ _  / __ _ _ __ 
 / __| '__| | | \// / / _` | '__|
| (__| |  | |_| |/ //\ (_| | |   
 \___|_|   \__,_/____/\__,_|_|   
                                 
""")
##datos
# nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

# edad
año = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2022 - año
print()

# altura
estatura = float(input("Contame más de vos, para agregarlo a tu perfil. Cuanto medís? Decimelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

# amiguis
num_amigos = int(input("Muy bien. Finalmente, contame cuantos amigos tenes. "))

# origen
país = input("Genial! Ahora decime de que país sos! ")
print()
print("QUE LINDO LUGAR", país, ", me encantaría ir denuevo")
print()

# estado civill
pareja = input(" Me gustaria saber si tenés pareja, decime si o no!")
print()

#tattos
tatuajes = input("Tu mamá te deja tatuarte?Contestame con si o con no")
print()
num_detattos = int(input("Si la respuesta es sí, cuantos tenés?"))
print("Mira vos, no sabia que tenias", num_detattos, "Yo tengo 1, pero mamá no me deja hacerme otro")

# resumen de datos
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("país:", país)
print("En pareja?:", pareja)
print("--------------------------------------------------")
print("Gracias por la info. Esperamos que disfrutes cruZar")
print()
print("Tatujaes", tatuajes, num_detattos)
#primer mensaje
mensaje = input("Ahora vamos a publicar tu primer mensaje. Como te sentis hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
