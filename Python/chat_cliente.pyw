#Se importa librerias necesarias
from socket import *
import threading
from tkinter import *

#Se establece direccion y puerto del servidor
serveraddres = 'localhost'
serverport = 9091

#Se crea un socket con dos argumentos (Se realiza conexion TCP)
client_socket = socket(AF_INET, SOCK_STREAM)
#Con connect establece una conexion mediante copn el servidor, por medio de la direccion y el puerto
client_socket.connect((serveraddres, serverport))

#Define funcion "mensaje:_recibido" el cual se encarga de recibir mensajes desde el servidor y agregarlos al historial 
def mensaje_recibido():
    try:
        #En este bucle estara escuchando continuamente los mensajes entrantes
        while True:
            #Despues de recicbir el mensaje se decodifica mensaje de bytes a string
            #Posteriormente se inserta en la ventana del chat con el metodo ".insert"
            msm_r = client_socket.recv(4097)
            historial.insert(END, msm_r.decode())
    except:
        #si ocure una excepcion se cierra el socket
        client_socket.close()

#Define funcion que se usa para enviar los mensajes desde el cliente al servidor
#"event=None" Permite enviar el mensaje en la interfaz grafica con enter
def mensaje_enviado(event=None):
    #Almacena enviado en "msm_e" usando el metodo ".get"
    msm_e = my_message.get()
    #vacia el texto donde se dijita el mensaje a enviar
    my_message.set('')
    #Permite enviar el mensaje activando el evento "event" ya sea con el boton enviar o la tecla enter
    client_socket.send(msm_e.encode())

#se crea ventana Tkinter de nombre "Cliente"
raiz = Tk()
raiz.title('Cliente')

#se crea un contenedor adicional sobre la ventana principal
chat_historial_frame = Frame(raiz)
#Se agrega un scrol en donde se almacenaran los mensajes
scrollbar = Scrollbar(chat_historial_frame)
#crea un caja de lista con su altura y anchura con el scrol anterior
historial = Listbox(chat_historial_frame, height=20, width=70, yscrollcommand=scrollbar.set)
#Se empaqueta el scrol dejandose a la derecha y en vertical
scrollbar.pack(side=RIGHT, fill=Y)
#Se empaqueta la caja de lista rellenando toda la ventana
historial.pack(side=LEFT, fill=BOTH)
historial.pack()
chat_historial_frame.pack()

#Se crea variable que es donde se almacenara el mensaje
my_message = StringVar()
#Campo donde el usuario pueda escribir su mensaje y despues sera almacenado en la variable
entry_field = Entry(raiz, textvariable=my_message)
#se realiza un enlace y el evento retur se vincula con la funcion mensaje_enviado
entry_field.bind('<Return>', mensaje_enviado)
entry_field.pack()
#boron enviar estara vinculado a la funcion definida como mensaje_enviado
send_button = Button(raiz, text='Enviar', command=mensaje_enviado)
send_button.pack()

#se crea un hilo la cual llama a la funcion de mensaje recibido y agrega el historial del chat 
receive_thread = threading.Thread(target=mensaje_recibido)
receive_thread.start()

#mantiene siempre la ventana principal en ejecucion
raiz.mainloop()
