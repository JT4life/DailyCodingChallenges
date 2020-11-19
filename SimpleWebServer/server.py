from socket import * 

def createServer():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        serverSocket.bind(('localhost',9000))
        serverSocket.listen(5)
        while(1):
            (clientSocket, address) = serverSocket.accept()

            rd = clientSocket.recv(5000).decode()
            pieces = rd.split("\n")
            if (len(pieces) > 0) : print(pieces[0])

            data= "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientSocket.sendall(data.encode()) # encode to UTF8
            clientSocket.shutdown(SHUT_WR) # Close connections

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as e:
        print("Error:\n")
        print(e)

    serverSocket.close()

print("Access http://localhost:9000")
createServer()