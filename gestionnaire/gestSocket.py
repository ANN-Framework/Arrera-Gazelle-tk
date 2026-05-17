from librairy.parreraclient import PArreraClient
from librairy.PArreraServer import PArreraServer
import time

class gestSocket :
    def __init__(self,name:str):
        self.__out_socket_client = None
        # Init de la partie serveur
        self.__socket_server = PArreraServer(port=6780)
        self.__socket_server.start()
        self.__state_server_running = True
        # Init de la partie client
        self.__socket_client = PArreraClient(name)
        self.__state_connection_client = self.__socket_client.connectToServeur("ws://127.0.0.1:6666")
        self.__message_is_received_client = False
        self.__client_running = True
        if not self.__state_connection_client:
            self.__socket_client = None
        elif not self.__socket_client.sendMessage("ArreraSoftConnected"):
            self.__state_connection_client = False
            self.__socket_client = None

    # Partie client

    def received_message_client(self):
        # print("Thread de réception WebSocket démarré...")
        while self.__client_running and self.__state_connection_client:
            try:
                # print("Attente message serveur...")
                message = self.__socket_client.receiveMessage()
                if message:
                    # Traitement du message reçu
                    self.__out_socket_client = message
                    self.__message_is_received_client = True
                    # print(f"Message reçu: {message}")
                else:
                    # Petit délai pour éviter une boucle trop rapide
                    time.sleep(0.1)
            except Exception as e:
                # print(f"Erreur lors de la réception du message: {e}")
                time.sleep(1)  # Attendre avant de réessayer
        # print("Thread de réception WebSocket arrêté.")

    def send_data_with_clien(self, data):
        if self.__state_connection_client:
            return self.__socket_client.sendMessage(data)
        else :
            return False

    def get_message_form_client(self):
        return self.__out_socket_client

    def stop_socket_client(self):
        self.__client_running = False
        self.__socket_client.disconnect()
        self.__state_connection_client = False

    def get_client_is_on(self):
        return self.__state_connection_client

    def get_message_is_received_form_client(self):
        if self.__message_is_received_client :
            self.__message_is_received_client = False
            return True
        else :
            return False

    # Partie serveur

    def get_server_is_on(self) -> bool:
        """Retourne l'état du serveur."""
        return self.__state_server_running

    def get_message_is_received_from_server(self) -> bool:
        """Vérifie si des messages sont en attente de lecture sur le serveur."""
        if self.__state_server_running:
            return self.__socket_server.a_des_messages()
        return False

    def get_message_from_server(self):
        if self.__state_server_running:
            return self.__socket_server.recuperer_message()
        return None

    def send_data_with_server_to(self, target_name: str, data: str) -> bool:
        if self.__state_server_running:
            self.__socket_server.sendTo(target_name, data)
            return True
        return False

    def broadcast_data_with_server(self, data: str) -> bool:
        if self.__state_server_running:
            self.__socket_server.broadcast(data)
            return True
        return False

    def is_client_connected_to_server(self, client_name: str) -> bool:
        if self.__state_server_running:
            return client_name in self.__socket_server.clients
        return False

    def get_server_clients_list(self) -> list:
        if self.__state_server_running:
            return list(self.__socket_server.clients.keys())
        return []

    def stop_socket_server(self):
        self.__state_server_running = False

    def get_new_client_is_connected(self) -> bool:
        if self.__state_server_running:
            return self.__socket_server.verifier_et_baisser_drapeau()
        return False

    def get_name_new_client(self):
        if self.__state_server_running:
            return self.__socket_server.lire_dernier_client()
        return None