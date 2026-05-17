from websocket import create_connection

class PArreraClient:
    def __init__(self,nameSoftware: str):
        self.__uri = None
        self.__connection = None
        self.__nameSoftware = nameSoftware

    def connectToServeur(self, uri: str) -> bool:
        if not uri:
            return False
        self.__uri = uri
        try:
            self.__connection = create_connection(self.__uri)
            self.__connection.send("namesoft "+self.__nameSoftware)
            return True
        except Exception as e:
            self.__connection = None
            return False

    def sendMessage(self, message: str) -> bool:
        if self.__connection:
            try:
                self.__connection.send(message)
                return True
            except Exception as e:
                return False
        else:
            return False

    def receiveMessage(self):
        if self.__connection:
            try:
                response = self.__connection.recv()
                if (response == "Message Received"):
                    return None
                else :
                    self.__connection.send("Message Received")
                    return response
            except Exception as e:
                # print(f"Erreur receiveMessage: {e}")
                return None
        else:
            return None

    def disconnect(self) -> bool:
        if self.__connection:
            try:
                # self.__connection.send("closed")
                self.__connection.close()
                self.__connection = None
                return True
            except Exception as e:

                return False
        return True