import network
import remoteEvent
import detecteur


ADDRESS = "10.0.0.111"
PORT = 1111

socket = network.newServerSocket()
socket.bind((ADDRESS,PORT))

stop = False
threadDistance= detecteur.distance(stop)
threadDistance.daemon = True
threadDistance.start()

continuer= True
while continuer:
    socket.listen(10)
    print("en ecoute...")

    thread = network.newThread(socket.accept())
    thread.start()

    lettre = thread.clientsocket.recv(4096)
    lettre = lettre.decode()

    print("lettre recu:",lettre)
    remoteEvent.commande(lettre)
    if lettre =="p":
        continuer = False

