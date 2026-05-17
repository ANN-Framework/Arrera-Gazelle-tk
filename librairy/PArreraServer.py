import threading
import asyncio
import websockets

class PArreraServer:
    def __init__(self, host="localhost", port=9000):
        self.host = host
        self.port = port
        self.clients = {}
        self.loop = None
        self.__flag_nouveau_client = False
        self.messages_recus = []

    async def handler(self, websocket):
        client_name = "Inconnu"
        try:
            async for message in websocket:
                if message.startswith("namesoft"):
                    client_name = message.replace("namesoft ", "").strip()
                    self.clients[client_name] = websocket
                    self.__flag_nouveau_client = True
                    await websocket.send("Message Received")

                else:
                    self.messages_recus.append({
                        "client": client_name,
                        "message": message
                    })
                    await websocket.send("Message Received")

        except websockets.ConnectionClosed:
            pass
        finally:
            if client_name in self.clients:
                del self.clients[client_name]

    def sendTo(self, target_name: str, message: str):
        if self.loop and target_name in self.clients:
            websocket = self.clients[target_name]
            asyncio.run_coroutine_threadsafe(websocket.send(message), self.loop)

    def broadcast(self, message: str):
        for name in list(self.clients.keys()):
            self.sendTo(name, message)

    def a_des_messages(self) -> bool:
        return len(self.messages_recus) > 0

    def recuperer_message(self):
        if self.a_des_messages():
            return self.messages_recus.pop(0)
        return None

    def start(self):
        thread = threading.Thread(target=self._run_server, daemon=True)
        thread.start()

    def _run_server(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._serve())

    async def _serve(self):
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()

    def verifier_et_baisser_drapeau(self) -> bool:
        if self.__flag_nouveau_client:
            self.__flag_nouveau_client = False
            return True
        return False

    def lire_dernier_client(self):
        liste_client = list(self.clients.keys())
        if len(liste_client) > 0:
            return liste_client[-1]
        return None