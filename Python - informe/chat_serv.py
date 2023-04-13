#Se importa librerias necesarias
from socket import *

#Se establece direccion y puerto del servidor
serveraddres = "Localhost"
serverport = 9090

#Se crea un socket con dos argumentos (Se realiza conexion TCP)
socketServer = socket ( AF_INET, SOCK_STREAM )

#se crea objeto socket usando el pueto y la ip definidas anteriormente
#bind(): Permite asociar e puerto y la direccion ip
socketServer.bind(( serveraddres, serverport ))
#listen(): Permite al servidor escuchar y aceptar las conexciones entrantes
socketServer.listen()

#crearemos un bulce infinito al momento que el servidor y el cliente se conecten
while True:
    # Se confirma la conexión entrante y se retorna un objeto socket con la dirección del cliente
    #accept():Acepta las conexiones entrantes de un socket
    socketCon, addr = socketServer.accept()
    print("Cliente conectado", addr)
    while True:
        #Despues de recicbir el mensaje por parte del cliente, se decodifica mensaje de bytes a string
        #recv(): de la librería socket de Python, recibe datos por parte del cliente y son almacenados en el bufer
        #decode(): funcion que codifica los bytes y los comnvierte en caracteres
        smsrecibido = socketCon.recv(4097).decode()
        print("Cliente: "+smsrecibido)

        if smsrecibido == 'Adios':
            break
        #Se envía un mensaje al cliente por el método send(), tambien se usa la entrada del usuario en la consola
        socketCon.send(input().encode())
        
    #se cierra la conexion y el socket del cliente
    #Close(): Cierra los objetos en uso del socket
    print("Se descoecto el cliente", addr)
    socketCon.close()    


