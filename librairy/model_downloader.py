import requests
import platform
import os
import json

class model_downloader:
    def __init__(self):

        self.__dictModel = {"leger-gemma": {
                                "name": "Gemma 4 E2B Q4_K_M",
                                "url": "https://huggingface.co/bartowski/google_gemma-4-E2B-it-GGUF/resolve/main/google_gemma-4-E2B-it-Q4_K_M.gguf?download=true",
                                "description": "Le tout dernier petit modèle 'Edge' Google Gemma 4. Ultra-rapide et parfait pour tourner de manière fluide sur le processeur (CPU) d'un PC sans carte graphique."},
                            "moyen-gemma": {
                                "name": "Gemma 3 12B Q4_K_M",
                                "url": "https://huggingface.co/unsloth/gemma-3-12b-it-GGUF/resolve/main/gemma-3-12b-it-Q4_K_M.gguf?download=true",
                                "description": "Modèle Google Gemma 3 très équilibré. Idéal pour exploiter un PC équipé d'une carte graphique classique (entre 8 et 12 Go de VRAM)."},
                            "lourd-gemma": {
                                "name": "Gemma 4 31B Q4_K_M",
                                "url": "https://huggingface.co/bartowski/google_gemma-4-31B-it-GGUF/resolve/main/google_gemma-4-31B-it-Q4_K_M.gguf?download=true",
                                "description": "Le nouveau fleuron de Google (Gemma 4). Très lourd et puissant, il nécessite une grosse carte graphique (16 à 24 Go de VRAM minimum) ou beaucoup de RAM vive."},
                            "leger-mistral": {
                                "name": "Ministral 3B Instruct Q4_K_M",
                                "url": "https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-GGUF/resolve/main/Ministral-3-3B-Instruct-2512-Q4_K_M.gguf?download=true",
                                "description": "Petit modèle de la startup française Mistral. Très vif, parfait pour tourner de manière fluide sur un PC sans carte graphique dédiée (sur le CPU)."
                            },
                            "moyen-mistral": {
                                "name": "Mistral Nemo 12B Instruct Q4_K_M",
                                "url": "https://huggingface.co/bartowski/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407-Q4_K_M.gguf?download=true",
                                "description": "Excellent modèle de 12 Milliards de paramètres. Le compromis idéal pour un PC équipé d'une carte graphique de milieu de gamme (8 à 12 Go de VRAM)."
                            },
                            "lourd-mistral": {
                                "name": "Mistral Small 3 (24B) Instruct Q4_K_M",
                                "url": "https://huggingface.co/bartowski/Mistral-Small-24B-Instruct-2501-GGUF/resolve/main/Mistral-Small-24B-Instruct-2501-Q4_K_M.gguf?download=true",
                                "description": "Modèle avancé et très performant. Lourd, il nécessite une bonne carte graphique (au moins 16 Go de VRAM) ou beaucoup de RAM vive pour tourner confortablement."
                            },
                            "leger-llama": {
                                "name": "LLaMA 3.2 3B Instruct Q4_K_M",
                                "url": "https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf?download=true",
                                "description": "Petit modèle Meta très intelligent. Parfait pour tourner sur le processeur (CPU) d'un PC sans carte graphique, avec une excellente rapidité."},
                            "moyen-llama": {
                                "name": "LLaMA 3.1 8B Instruct Q4_K_M",
                                "url": "https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf?download=true",
                                "description": "Le classique incontournable de Meta. Taille moyenne, tourne parfaitement sur un PC avec une carte graphique standard (8 Go de VRAM)."},
                            "lourd-llama": {
                                "name": "LLaMA 3.3 70B Instruct Q3_K_M",
                                "url": "https://huggingface.co/bartowski/Llama-3.3-70B-Instruct-GGUF/resolve/main/Llama-3.3-70B-Instruct-Q3_K_M.gguf?download=true",
                                "description": "Un modèle massif aux performances comparables à GPT-4. Attention : très lourd ! Nécessite au moins 32 Go de mémoire (VRAM + RAM combinées) pour fonctionner."}}

        os_name = platform.system()

        if os_name == "Linux" or os_name == "Darwin":
            self.__modelDir = os.path.join(os.path.expanduser("~"), ".config", "arrera-model") + os.sep
        elif os_name == "Windows":
            self.__modelDir = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "arrera-model") + os.sep

        self.__modelDownloadFile = os.path.join(self.__modelDir, "model_download.json")

        if not os.path.isfile(self.__modelDownloadFile):
            os.makedirs(os.path.dirname(self.__modelDownloadFile), exist_ok=True)
            with open(self.__modelDownloadFile, "x", encoding="utf-8") as f:
                json.dump({"models": []}, f, ensure_ascii=False, indent=2)

    def get_model_list(self):
        return list(self.__dictModel.keys())

    def get_model_on_dir(self):
        list_model = []
        for dossier_racine, sous_dossiers, fichiers in os.walk(self.__modelDir):
            for fichier in fichiers:
                if fichier.endswith(".gguf"):
                    list_model.append(fichier)

        if len(list_model) == 0:
            return None
        else :
            return list_model

    def get_data_model(self,key:str):
        data = self.__dictModel[key]
        return data["name"],data["url"],data["description"]

    def get_model_download(self):
        with open(self.__modelDownloadFile, 'r' , encoding='utf-8') as openfile:
            return list(json.load(openfile)["models"])

    def download_model(self,key:str):
        url = self.get_data_model(key)[1]
        if key in self.get_model_download():
            return False

        try :
            response = requests.get(url, stream=True)

            if response.status_code == 200:
                full_path = self.__modelDir + key + ".gguf"

                with open(full_path, 'wb') as f:
                    # On télécharge par paquets de 8 Ko (ou plus)
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                    openfile = open(self.__modelDownloadFile, 'r' , encoding='utf-8')
                    dict = json.load(openfile)
                    openfile.close()
                    writeFile = open(self.__modelDownloadFile, 'w', encoding='utf-8')
                    dict["models"].append(key)
                    json.dump(dict,writeFile,indent=2)
                    writeFile.close()
                return True
            else :
                return False
        except Exception as e :
            return False

    def del_model(self,model:str):
        if model in self.get_model_download():
           file = self.get_path_model(model)
           if os.path.isfile(file):
               os.remove(file)
               openfile = open(self.__modelDownloadFile, 'r' , encoding='utf-8')
               dict = json.load(openfile)
               openfile.close()
               writeFile = open(self.__modelDownloadFile, 'w', encoding='utf-8')
               dict["models"].remove(model)
               json.dump(dict,writeFile,indent=2)
               writeFile.close()
               return True
           else :
               return False


    def get_path_model(self,key:str):
        if key in self.get_model_download():
            return self.__modelDir+key+".gguf"
        else :
            return None