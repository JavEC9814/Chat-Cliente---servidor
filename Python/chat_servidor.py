#Se importa librerias necesarias
from socket import *
import threading

#Se establece direccion y puerto del servidor
serveraddres = "localhost"
serverport = 9091

#Se crea un socket con dos argumentos (Se realiza conexion TCP)
socketServer = socket(AF_INET, SOCK_STREAM)

#Permite usar el socket que se cerro por otro usuario.
socketServer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#Con bind se realiza el enlce, por medio de la direccion y el puerto
socketServer.bind((serveraddres, serverport))

#se indica que esta listo el servidor pára recibir los usuarios
socketServer.listen()

#En esta lista se almacena cada cliente conectado al servidor
clientes = []

#se encarga de la gestion del envio de los mensajes a cada uno de los clientes conectados
def msm(mensaje):
    for client in clientes:
        client.send(mensaje)

#Se encarga de manejar la conexion de cada cliente en el servidor
def cliente_conect(client_socket):
    try:
        #ciclo de espera de mensajes de los clientes 
        while True:
            #Si recibe un mensaje lo envia a los clientes conectados bajo la funcion "msm"
            #recv(4097) refiere a la cantidad de bytes que el metodo puede recibir
            message = client_socket.recv(4097)
            if message:
                msm(message)
            #En caso de no recibir el mensaje llama la funcion "sacar_cliente" para sacarlo de la lista de los clientes conectados
            else:
                sacar_cliente(client_socket)
                break
    except:
        sacar_cliente(client_socket)

#La funcion "sacar_cliente" se encarga de la eliminacion de cada uno de los clientes y cerrar el socket de cada uno
def sacar_cliente(client_socket):
    if client_socket in clientes:
        clientes.remove(client_socket)
        client_socket.close()

#Se define la funcion nuevo_cliente, la cual es un bucle infinito y se encarga de aceptar las conexiones entrantes de los clientes
def nuevo_cliente():
    while True:
        client_socket, _ = socketServer.accept()
        clientes.append(client_socket)
        threading.Thread(target=cliente_conect, args=(client_socket,)).start()

#Se crea un nuevo hilo de ejecuvion con la libreria threading, donde siempre va a ejecutar la funcion "nuevo_cliente"
threading.Thread(target=nuevo_cliente).start()