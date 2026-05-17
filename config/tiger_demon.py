import requests

# Class du demon qui teste la versio
class tiger_demon :
    def __init__(self,name:str,version:str):
        # Teste internet
        try:
            requests.get("https://www.google.com/", timeout=5)
            self.__internet = True
        except requests.RequestException:
            self.__internet = False
        # Variable
        self.__nameSoft = name
        self.__version_local = version
        self.__url = "https://raw.githubusercontent.com/Arrera-Software/distribution/refs/heads/main/index.json"
        # load depots
        self.__version_online = ""
        self.__state_depots = self.load_version()


    # Gestion du fichier de depots
    def load_version(self):
        if not self.__internet:
            return False

        try:
            response = requests.get(self.__url)
            response.raise_for_status()
            data = response.json()
            list_key = ["application", "assistants"]
            for key in list_key:
                if key in data:
                    items_list = data[key]
                    for app in items_list:
                        if app.get("name") == self.__nameSoft:
                            self.__version_online = app.get("version")
                            return True

            return False
        except requests.RequestException:
            return False
        except ValueError:
            return False


    def checkUpdate(self):
        if self.__internet and self.__state_depots:
            if self.__version_local != "dev":
                if self.__version_local != self.__version_online:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def get_local_version(self):
        return self.__version_local

    def get_online_version(self):
        return self.__version_online

    def getInternet(self):
        return self.__internet