from gestionnaire.gestion import gestionnaire,confNeuron
from gestionnaire.gestUserSetting import gestionnaire
from librairy.arrera_tk import *

def create_conf():
    conf = confNeuron(name="Opale",
                      lang="fr",
                      icon="asset/icon.png",
                      asset="asset/",
                      assistant_color="white",
                      assistant_texte_color="black",
                      bute="developper un algo de ChatBot qui sera inclut dans SIX et Ryley",
                      createur="Pauchet Baptiste",
                      listFonction=["ouvrir une application", "aider sur les recherches de internet", "donner la meteo",
                                    "faire un résumer des actualités"],
                      moteurderecherche="google",
                      etatService=1,
                      etatTime=1,
                      etatOpen=1,
                      etatSearch=1,
                      etatChatbot=1,
                      etatApi=1,
                      etatCodehelp=1,
                      etatWork=1,
                      etatSocket=1,
                      lienDoc="www.google.com",
                      fichierLangue="language/vouvoiment/",
                      fichierKeyword="keyword/",
                      voiceAssistant=True)

    return gestionnaire(conf)

def launch_setting():
    from arrera_gazelle.arrera_gazelle import arrera_gazelle
    windows = aTk(theme_file="asset/theme/theme_bleu_blanc.json")
    gui = arrera_gazelle(windows, create_conf(), "json_conf/conf-setting.json")
    windows.maxsize(500,400)
    windows.minsize(500,400)
    gui.passFNCQuit(lambda  : windows.destroy())
    gui.passFNCBTNIcon(lambda  : print("Icon"))
    gui.active()
    windows.mainloop()