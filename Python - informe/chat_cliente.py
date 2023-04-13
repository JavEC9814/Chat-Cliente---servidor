#Se importa librerias necesarias
from socket import *
import sys

#Se establece direccion y puerto del servidor
serveraddres = "localhost"
serverport = 9090

#Se crea un socket con dos argumentos (Se realiza conexion TCP)
socketclient = socket(AF_INET, SOCK_STREAM)
#Con connect establece una conexion mediante copn el servidor, por medio de la direccion y el puerto
socketclient.connect((serveraddres, serverport))

#crearemos un bulce infinito al momento que el cliente se conecte
while True:
    #si el cliente se ogra conectar mostrara el mensaje de conexion en consola del server
    print ("Conexion establecida")
    #se crea la variable que espera una entrada de un mensaje por parte del cliente
    #input(): función predefinida de Python que permite la entrada por parte de los usuarios
    sms = input()
    #si el mensaje que envio el cliente es diferente de Adios
    if sms != 'Adios':
        #Se enviara el mensaje al servidor
        #Send(): de la librería socket de Python se utiliza para enviar datos por medio de una conexión de red.
        #encode(): convierte la cadena de caracteres unicode a bytes al servidor 
        socketclient.send(sms.encode())
        #Despues de recicbir el mensaje, se decodifica mensaje de bytes a string
        #recv(): de la librería socket de Python, recibe datos por parte del servidor y son almacenados en el bufer
        #decode(): funcion que codifica los bytes y los comnvierte en caracteres
        res = socketclient.recv(4097).decode()
        #Muestra mensaje del servidor
        print("Servidor: "+res)
    #Si el mensaje es "Adios"    
    else:
        #Mostrara que la conexcion se ha cerrado
        print ("Conexion Cerrada")
        #se envia mensaje al servidor
        #Send(): de la librería socket de Python se utiliza para enviar datos por medio de una conexión de red.
        #encode(): convierte la cadena de caracteres unicode a bytes al servidor 
        socketclient.send(sms.encode())
        #se cierra el socket del cliente
        #Close(): Cierra los objetos en uso del socket
        socketclient.close()
        #Se finaliza el programa
        #exit(): finaliza la ejecucion del programa
        sys.exit()

