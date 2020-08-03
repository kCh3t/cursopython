def saludar(nombre):              #para crear funciones se utiliza la palabra reservada def
    return "Hola {} bienvenido al juego".format(nombre)
print ("Ingresa tu nombre")
nombre = input()
print (saludar (nombre))
