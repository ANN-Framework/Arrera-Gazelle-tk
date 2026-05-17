import random
from librairy.travailJSON import *
from gestionnaire.gestion import gestionnaire
from datetime import datetime
from librairy.resource_lib import resource_lib


class gestLangue:
    def __init__(self,emplacement:str,gestion:gestionnaire,listVar:list,listFonc:list):
        ressource_lib = resource_lib()
        index = jsonWork(ressource_lib.resource_path(emplacement+"index.json"))
        self.__formule = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("formule")))
        self.__chatbot = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("chatbot")))
        self.__codeHelp = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("codeHelp")))
        self.__open = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("open")))
        self.__search = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("search")))
        self.__service = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("service")))
        self.__api = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("api")))
        self.__time = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("time")))
        self.__work = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("work")))
        self.__socket = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("socket")))
        self.__interface = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("interface")))
        self.__connection = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("connection")))
        self.__markdown = jsonWork(ressource_lib.resource_path(emplacement + index.getContentJsonFlag("markdown")))
        self.__fncHist = gestion.getGestHist()
        # Variable
        self.__listFonction = listFonc
        self.__nbFonction = len(self.__listFonction)
        # Fichier JSON
        self.__userData = gestion.getUserConf()
        # Atribut
        self.__userFirstname = ""
        self.__genre = ""
        self.__nameAssistant = listVar[0]
        self.__bute = listVar[1]
        self.__createur = listVar[2]
        self.setVarUser()

    # Partie des formule

    def nocomprehension(self):
        return self.getNoComprehension()

    def bootNoHist(self):
        hour = datetime.now().hour
        nbrand = random.randrange(0, 1)
        if 0 <= hour < 3:
            formule = self.getPhraseBootNormale("1")
            return formule[nbrand]
        elif 3 <= hour <= 6:
            formule = self.getPhraseBootNormale("2")
            return formule[nbrand]
        elif 6 <= hour <= 10:
            formule = self.getPhraseBootNormale("3")
            return formule[nbrand]
        elif 10 <= hour <= 12:
            formule = self.getPhraseBootNormale("4")
            return formule[nbrand]
        elif 13 <= hour <= 14:
            formule = self.getPhraseBootNormale("5")
            return formule[nbrand]
        elif 15 <= hour <= 18:
            formule = self.getPhraseBootNormale("6")
            return formule[nbrand]
        elif 18 <= hour <= 20:
            formule = self.getPhraseBootNormale("7")
            return formule[nbrand]
        elif 20 <= hour <= 23:
            formule = self.getPhraseBootNormale("8")
            return formule[nbrand]
        elif 0 <= hour < 3:
            formule = self.getPhraseBootNormale("9")
            return formule[nbrand]
        else:
            formule = self.getPhraseBootNormale("10")
            return formule

    def aurevoir(self, hour):
        nbrand = random.randrange(0, 1)
        if 0 <= hour < 3:
            formule = self.getPhraseAurevoir("1")
            return formule[nbrand]
        elif 3 <= hour <= 6:
            formule = self.getPhraseAurevoir("2")
            return formule[nbrand]
        elif 6 <= hour <= 10:
            formule = self.getPhraseAurevoir("3")
            return formule[nbrand]
        elif 10 <= hour <= 12:
            formule = self.getPhraseAurevoir("4")
            return formule[nbrand]
        elif 13 <= hour <= 16:
            formule = self.getPhraseAurevoir("5")
            return formule[nbrand]
        elif 16 <= hour <= 18:
            formule = self.getPhraseAurevoir("6")
            return formule[nbrand]
        elif 18 <= hour <= 20:
            formule = self.getPhraseAurevoir("7")
            return formule[nbrand]
        elif 20 <= hour <= 23:
            formule = self.getPhraseAurevoir("8")
            return formule[nbrand]
        elif 0 <= hour < 3:
            formule = self.getPhraseAurevoir("9")
            return formule[nbrand]
        else:
            formule = self.getPhraseAurevoir("10")
            return formule[nbrand]

    def bootWithHist(self):
        hour = datetime.now().hour
        if 0 <= hour < 3:
            formule = self.getPhraseBootHist("1")
            return formule
        elif 3 <= hour <= 6:
            formule = self.getPhraseBootHist("2")
            return formule
        elif 6 <= hour <= 10:
            formule = self.getPhraseBootHist("3")
            return formule
        elif 10 <= hour <= 12:
            formule = self.getPhraseBootHist("4")
            return formule
        elif 13 <= hour <= 14:
            formule = self.getPhraseBootHist("5")
            return formule
        elif 15 <= hour <= 18:
            formule = self.getPhraseBootHist("6")
            return formule
        elif 18 <= hour <= 20:
            formule = self.getPhraseBootHist("7")
            return formule
        elif 20 <= hour <= 23:
            formule = self.getPhraseBootHist("8")
            return formule
        elif 0 <= hour < 3:
            formule = self.getPhraseBootHist("9")
            return formule
        else:
            formule = self.getPhraseBootHist("10")
            return formule




    def setVarUser(self):
        self.__userFirstname = self.__userData.getFirstnameUser()
        self.__userLastname = self.__userData.getLastnameUser()
        self.__genre = self.__userData.getGenre()

    def getDataUser(self):
        return [self.__userFirstname,self.__userLastname,self.__genre]

    def getNoComprehension(self):
        return self.__formule.getContentJsonFlag("nc")

    def getPhraseBootNormale(self,nb:str):
        phrases = self.__formule.getFlagListJson("bootN" + nb)
        return [phrase.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname) for phrase in phrases]

    def getPhraseAurevoir(self,nb:str):
        phrases = self.__formule.getFlagListJson("stop" + nb)
        return [phrase.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname) for phrase in phrases]

    def getPhraseBootHist(self,nb:str):
        phrase = self.__formule.getContentJsonFlag("bootHist" + nb)
        return phrase.format(genre=self.__genre, user_firstname=self.__userFirstname,
                             user_lastname=self.__userLastname)

    def getPhraseChatBot(self,nb:str):
        formule = self.__chatbot.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseCodehelp(self,nb:str):
        formule = self.__codeHelp.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)


    def getPhraseSearch(self,nb:str):
        formule = self.__search.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseResultatCalcule(self,resultat:str):
        formule = self.__service.getContentJsonFlag("phcalcule")
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname, resultat=resultat)

    def getPhraseService(self,nb:str):
        formule = self.__service.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseResumerActu(self):
        formule = self.__api.getContentJsonFlag("phResumerActu")
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseResumerTask(self):
        formule = self.__api.getContentJsonFlag("phResumerTask")
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseResumerAll(self,nb:str):
        formule = self.__api.getContentJsonFlag("phResumerAll" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseApi(self,nb:str):
        formule = self.__api.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseMeteo(self,nb:str,ville:str,description:str,temperature:str):
        phrases = self.__api.getFlagListJson("phMeteo" + nb)
        return [phrase.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname, ville=ville,
                              description=description,
                              temperature=temperature) for phrase in phrases]

    def getPhraseMeteoError(self,nb:str):
        formule = self.__api.getContentJsonFlag("phMeteoError" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseCoordonnees(self,ville:str,latitude:str,longitude:str):
        phrases = self.__api.getContentJsonFlag("phCoordonnees")
        return phrases.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname, ville=ville,
                              latitude=latitude, longitude=longitude)

    def getPhraseTemperature(self,temperature:str):
        formule = self.__api.getContentJsonFlag("phTemperature")
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname, temperature=temperature)

    def getPhraseGPSError(self,nb:str):
        formule = self.__api.getContentJsonFlag("phGPSError" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseIteneraireError(self,nb:str):
        formule = self.__api.getContentJsonFlag("phIteneraireError" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseIteneraire(self,nb:str,texte:str=""):
        formule = self.__api.getContentJsonFlag("phIteneraire"+nb)
        if texte != "":
            return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                                  user_lastname=self.__userLastname, texte=texte)
        else :
            return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                                  user_lastname=self.__userLastname)

    def getTexteHelpIteneraire(self):
        formule = self.__api.getContentJsonFlag("phhelpIteneraire")
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getOpenHelpIteneraire(self):
        formule = self.__api.getContentJsonFlag("phOpenHelpIteneraire")
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseOpenTraducteur(self):
        formule = self.__api.getContentJsonFlag("phTraducteur")
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseErrorLangue(self):
        formule = self.__api.getContentJsonFlag("phErrorLangue")
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseHeure(self,heure:str,minute:str):
        formule = self.__time.getContentJsonFlag("phHeure")
        return formule.format(ggenre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname, heure=heure, minute=minute)

    def getPhraseDate(self,jour:str,mois:str,annee:str):
        formule = self.__time.getContentJsonFlag("phDate")
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname, jour=jour, mois=mois, annee=annee)

    def getPhraseTime(self,nb:str,task:str=""):
        formule = self.__time.getContentJsonFlag("ph" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname, task=task)
    def getPhraseEvent(self,nb:str):
        formule = self.__time.getContentJsonFlag("phEvent")
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname, nombre=nb)

    def getPhraseNBTache(self,nb:str,nombre1:str,nombre2:str):
        formule = self.__time.getContentJsonFlag("phNBTache" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname, nombre1=nombre1, nombre2=nombre2)

    def getPhraseSocket(self,name:str):
        return self.__socket.getContentJsonFlag(name)

    def getPhraseMorningBreef(self,nb:str):
        formule = self.__api.getContentJsonFlag("phMorningBreef" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)


    # Partie work

    def getPhraseHelpArreraWork(self,nb:str):
        formule = self.__work.getFlagListJson("phHelpArreraWork" + nb)
        liste = [phrase.format(genre=self.__genre, user_firstname=self.__userFirstname,
                               user_lastname=self.__userLastname) for phrase in formule]
        phraseOut = ""
        for i in range(0,len(liste)):
            if i == 0:
                phraseOut = liste[i]
            else:
                phraseOut = phraseOut + "\n\n- " + liste[i]
        return phraseOut

    def getPhraseArreraWorkNeuron(self,nb:str):
        formule = self.__work.getContentJsonFlag("phArreraWork" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseArreraWorkTableur(self,nb:str):
        formule = self.__work.getContentJsonFlag("phTableur" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseArreraWorkProjet(self,nb:str,name:str=""):
        formule = self.__work.getContentJsonFlag("phProjet" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname, name=name)

    def getPhraseArreraWorkWord(self,nb:str,):
        formule = self.__work.getContentJsonFlag("phWord" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseOpenGUIWork(self,nb:str):
        formule = self.__work.getContentJsonFlag("phOpenGUIWork" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    # Open
    def getPhrasePresavedOpen(self,nb:str):
        formule = self.__open.getContentJsonFlag("open_presaved" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseArreraSoftOpen(self,nb:str):
        formule = self.__open.getContentJsonFlag("open_arrerasoft" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getPhraseRadioLaunch(self,nb:str,radio:str=""):
        formule = self.__open.getContentJsonFlag("ph_radio" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname,radio=radio)

    def getPhraseUserSoft(self,nb:str,soft:str=""):
        formule = self.__open.getContentJsonFlag("ph_user_soft" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname,soft=soft)

    def getPhraseUserWeb(self,nb:str,site:str=""):
        formule = self.__open.getContentJsonFlag("ph_user_web" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname,site=site)

    def getPhraseNoOpen(self,nb:str):
        formule = self.__open.getContentJsonFlag("ph_user_noopen" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    def getNbRadioSoftSite(self,nb:str,nombre:str=""):
        formule = self.__open.getContentJsonFlag("ph_nb-softradiosite" + nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname,nombre=nombre)

    def getListRadio(self):
        return self.__open.getFlagListJson("ph_list_radio")

    def getPhraseModeInterface(self, nb:str, name:str= ""):
        formule = self.__open.getContentJsonFlag("ph_mode_interface"+nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname,name=name)

    # Interface

    def getPhraseInterfaceOpenSoft(self,nb:str,soft:str=""):
        formule = self.__interface.getContentJsonFlag("phOpenSoft"+nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname,soft=soft)

    def getPhraseInterfaceLaunchModeLieu(self,nb:str,name:str=""):
        formule = self.__interface.getContentJsonFlag("phModeLieu"+nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname,name=name)

    def getPhraseCloseMode(self):
        nb = str(random.randint(1,2))
        formule = self.__interface.getContentJsonFlag("phCloseMode"+nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    # Connection

    def getPhraseSoftConnected(self,soft:str):
        formule = self.__connection.getContentJsonFlag(soft)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)

    # Markdown

    def getPhraseMarkdownt(self,nb:str):
        formule = self.__markdown.getContentJsonFlag("ph"+nb)
        return formule.format(genre=self.__genre, user_firstname=self.__userFirstname,
                              user_lastname=self.__userLastname)
