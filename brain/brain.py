import threading as th
from gestionnaire.gestion import *
from datetime import datetime, time


class ABrain :
    def __init__(self,config:confNeuron):
        # Declaration des diferente var
        self.__listOut =  [] 
        self.__valeurOut = 0
        self.__networkRunning = True
        self.__update = False
        self.__neuronUsed = str
        self.__listNeuron = ["chatBot","service","api",
                             "software","open","search",
                             "time","codehelp","word"]
        # Gestionnaire
        self.__gestionnaire = gestionnaire(config)
        self.__gestNeuron = self.__gestionnaire.getGestNeuron()
        # Partie serveur
        self.__gestSocket = self.__gestionnaire.getSocketObjet()
        #initilisation du gestionnaire du reseau de neuron
        self.__gestLangue = self.__gestionnaire.getLanguageObjet()
        #recuperation etat du reseau
        self.__etatReseau = self.__gestionnaire.getNetworkObjet().getEtatInternet()
        # Theard recevied message socket
        if self.__gestSocket is not None and self.__gestSocket.get_client_is_on():
            self.__threadSocket = th.Thread(target=self.__gestSocket.received_message_client)
            self.__threadSocket.daemon = True
            self.__threadSocket.start()


    def getGestionnaire(self):
        return self.__gestionnaire

    def getNeuronRunning(self):
        return self.__networkRunning

    def boot(self):
        return self.__gestionnaire.boot()
    
    def shutdown(self):
        hour = datetime.now().hour
        text = self.__gestLangue.aurevoir(hour)
        if self.__gestionnaire.getGestNeuron().getSocket():
            if self.__gestSocket.get_client_is_on():
                self.__gestSocket.stop_socket_client()

            if self.__gestSocket.get_server_is_on():
                self.__gestSocket.broadcast_data_with_server("closed")
                self.__gestSocket.stop_socket_server()
        self.__gestionnaire.getGestHist().saveHist()
        return str(text)
    
    def getListSortie(self)->list :
        if self.__valeurOut == 5 or self.__valeurOut == 12 or self.__valeurOut == 18 or self.__valeurOut == 19:
            if not self.__valeurOut == 12 or not self.__valeurOut == 18 or not self.__valeurOut == 19:
                texte = self.__getTextWithTkinterWindows()
                if texte is not None:
                    self.__listOut = texte

        if self.__valeurOut == 23 :
            self.__gestionnaire.getGestFNC().getFNCCodeHelp().launchGui()

        if self.__listOut == ["",""]:
            self.__listOut = [self.__gestLangue.nocomprehension(), ""]

        return self.__listOut

    def getNeuronUsed(self)-> type[str]:
        return self.__neuronUsed

    def getValeurSortie(self)->int :
        """
        0 : Aucun sortie
        1 : Sortie normale
        3 : Sortie actu
        4 : Meteo / temperature / GPS
        5 : Sortie avec fenetre tkinter
        6 : Erreur actu
        7 : Ouverture de fichier
        8 : Fermeture de fichier
        9 : Lecture fichier
        10 : Creation d'un projet
        11 : Erreur du resumer actulités
        12 : Reussite du resumer actulités
        13 : Lecture tableur
        14 : Ouverture d'un projet
        15 : Arret de l'assistant
        16 : Creation d'un fichier dans un projet
        17 : Affichage aide
        18 : Resumer tache / agenda
        19 : Resumer all ok 
        20 : Resumer all fail
        21 : Close projet
        22 : Lancement de radio
        23 : GUI Codehelp
        """
        return self.__valeurOut

    def __getTextWithTkinterWindows(self):
        if self.__gestionnaire.getGestGUI().launch_gui():
            return [self.__gestionnaire.getGestGUI().textOut(),""]
        else :
            return None
    
    def getTableur(self):
        return self.__gestionnaire.getGestFNC().getFNCWork().getEtatTableur()
    
    def getWord(self):
        return self.__gestionnaire.getGestFNC().getFNCWork().getEtatWord()

    def getProject(self):
        return self.__gestionnaire.getGestFNC().getFNCWork().getEtatProject()

    def getUserData(self):
        return self.__gestionnaire.getLanguageObjet().getDataUser()

    def neuron(self,var:str) :
        # Var local
        requetteNo = str(var).lower()
        requette = self.__gestionnaire.netoyageChaine(str(var))
        # Var de l'objet
        self.__valeurOut = 0
        self.__listOut =  []
        self.__neuronUsed = "none"
        # Service
        if self.__gestNeuron.nservice is None:
            self.__valeurOut = 0
        else :
            self.__gestNeuron.nservice.neurone(requetteNo)
            self.__valeurOut = self.__gestNeuron.nservice.getValeurSortie()
        if self.__valeurOut == 0 :
            #time
            if self.__gestNeuron.ntime is None:
                self.__valeurOut = 0
            else :
                self.__gestNeuron.ntime.neurone(requette)
                self.__valeurOut = self.__gestNeuron.ntime.getValeurSortie()

            if self.__valeurOut == 0 :
                #code help
                if self.__gestNeuron.ncodehelp is None:
                    self.__valeurOut = 0
                else :
                    self.__gestNeuron.ncodehelp.neurone(requette)
                    self.__valeurOut = self.__gestNeuron.ncodehelp.getValeurSortie()

                if self.__valeurOut == 0:
                    #work
                    if self.__gestNeuron.nwork is None:
                        self.__valeurOut = 0
                    else :
                        self.__gestNeuron.nwork.neurone(requette)
                        self.__valeurOut = self.__gestNeuron.nwork.getValeurSortie()

                    if self.__valeurOut == 0:
                        #open
                        if self.__gestNeuron.nopen is None:
                            self.__valeurOut = 0
                        else :
                            self.__gestNeuron.nopen.neurone(requette)
                            self.__valeurOut = self.__gestNeuron.nopen.getValeurSortie()

                        if self.__valeurOut == 0 :
                            #search
                            if not self.__etatReseau or self.__gestNeuron.nsearch is None :
                                self.__valeurOut = 0
                            else :
                                self.__gestNeuron.nsearch.neurone(requette)
                                self.__valeurOut = self.__gestNeuron.nsearch.getValeurSortie()

                            if self.__valeurOut == 0 :
                                #api
                                if not self.__etatReseau  or self.__gestNeuron.napi is None :
                                    self.__valeurOut = 0
                                else :
                                    self.__gestNeuron.napi.neurone(requette)
                                    self.__valeurOut = self.__gestNeuron.napi.getValeurSortie()

                                if self.__valeurOut == 0 :
                                    #chatBot
                                    if self.__gestNeuron.nchatbot is None:
                                        self.__valeurOut = 0
                                    else :
                                        self.__gestNeuron.nchatbot.neurone(requette)
                                        self.__valeurOut = self.__gestNeuron.nchatbot.getValeurSortie()

                                    if self.__valeurOut == 0 :
                                        if self.__gestionnaire.getKeywordObjet().checkUtils(requette, "stop") :
                                            self.__listOut = [self.shutdown(),""]
                                            self.__valeurOut = 15
                                        else :
                                            self.__valeurOut = 0
                                            self.__listOut = [self.__gestLangue.nocomprehension(), ""]
                                    else :
                                        self.__listOut = self.__gestNeuron.nchatbot.getListSortie()
                                        self.__neuronUsed = self.__listNeuron[2]
                                else :
                                    self.__listOut = self.__gestNeuron.napi.getListSortie()
                                    self.__neuronUsed = self.__listNeuron[0]
                            else :
                                self.__listOut = self.__gestNeuron.nsearch.getListSortie()
                                self.__neuronUsed = self.__listNeuron[5]
                        else :
                            self.__listOut = self.__gestNeuron.nopen.getListSortie()
                            self.__neuronUsed = self.__listNeuron[4]
                    else :
                        self.__listOut = self.__gestNeuron.nwork.getListSortie()
                        self.__neuronUsed = self.__listNeuron[8]
                else :
                    self.__listOut = self.__gestNeuron.ncodehelp.getListSortie()
                    self.__neuronUsed = self.__listNeuron[7]
            else :
                self.__listOut = self.__gestNeuron.ntime.getListSortie()
                self.__neuronUsed = self.__listNeuron[6]
        else :
            self.__listOut = self.__gestNeuron.nservice.getListSortie()
            self.__neuronUsed = self.__listNeuron[1]

        #Sauvegarde de la sortie et de l'entrée
        if (self.__valeurOut == 3) or (self.__valeurOut == 12) or (self.__valeurOut == 11):
            self.__gestionnaire.setOld("requette api",requette)
        else :
            self.__gestionnaire.setOld(self.__listOut[0],requette)

    def updateAssistant(self):
        # print("updateAssistant")
        # Ajouter la partie mise a jour du socket
        self.__gestionnaire.updateDate()
        if (time(6,0) <= datetime.now().time() < time(11,0) and not
        self.__gestionnaire.getBreefIsLaunch()):
            self.__gestionnaire.setBreefIsLaunch()
            self.__gestionnaire.getGestGUI().activeBreef()
            self.__listOut = [self.__gestionnaire.getLanguageObjet().getPhraseMorningBreef("1"),""]
            self.__valeurOut = 5
            return True
        elif self.__gestSocket is not None:
            if self.__gestSocket.get_new_client_is_connected():
                self.__listOut = [self.__gestionnaire.getLanguageObjet().getPhraseSoftConnected(self.__gestSocket.get_name_new_client()),""]
                self.__valeurOut = 1
                return True
            elif self.__gestSocket.get_message_is_received_from_server():
                out = self.__gestSocket.get_message_from_server()
                client = out["client"]
                message = out["message"]
                if message != "Message Received" :
                    if client == "arrera_markdown":
                        self.__gestNeuron.nmarkdown.neurone(message)
                        self.__listOut = self.__gestNeuron.nmarkdown.getListSortie()
                        self.__valeurOut = self.__gestNeuron.nmarkdown.getValeurSortie()
                        return True
                    else :
                        return False
                else :
                    return False
            elif self.__gestSocket.get_message_is_received_form_client():
                if self.__gestionnaire.getKeywordObjet().checkInterface(
                        self.__gestSocket.get_message_form_client(), "requette"):
                    mots = self.__gestionnaire.getKeywordObjet().getListKeyword("interface","requette")
                    message = self.__gestSocket.get_message_form_client().replace(mots[0], "").strip()
                    self.neuron(message)
                    return True
                elif self.__gestionnaire.getKeywordObjet().checkInterface(self.__gestSocket.get_message_form_client(), "namemode"):
                    self.__gestionnaire.setNameMode(self.__gestSocket.get_message_form_client())
                    return False
                else:
                    message = self.__gestSocket.get_message_form_client()
                    self.__gestNeuron.ninterface.neurone(message)
                    self.__listOut = self.__gestNeuron.ninterface.getListSortie()
                    self.__valeurOut = self.__gestNeuron.ninterface.getValeurSortie()
                    return  True
            else :
                return False
        else :
            return False
