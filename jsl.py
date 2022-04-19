"""
Just a socket lib.
By: EssEnemiGz
"""

# Módulos
import time
import base64

def sendFile(filename, socket, code = "utf-8"):
    with open(filename, "rb") as file:
        socket.send(filename.encode(code))
        time.sleep(0.5)
        fileR = base64.b64encode(file.read())
        socket.send(str(len(fileR)).encode(code))
        time.sleep(0.5)
        send1 = socket.send(fileR)
        socket.send("CONFIRMATIONTerminado".encode(code))
        return True

def recvFile(socket, code = "utf-8"):
    filename = socket.recv(1024).decode(code)
    long = socket.recv(1024).decode(code)
    realFile = ""
    while 1:
        if int(long) > 1024:
            result = socket.recv(int(long)).decode(code)
        else:
            result = socket.recv(1024).decode(code)
        realFile = f"{realFile}{result}"
        try:
            if result.split("CONFIRMATION")[1] == "Terminado":
                break
        except IndexError:
            pass

    with open(filename, "wb") as file:
        file.write(base64.b64decode(realFile))
        return True

if __name__ == "__main__":
    print("Esto es jsl, una librería para facilitar el usar sockets para algunas tareas.")
