from gestionnaire.gestion import gestionnaire
from neuron.API import neuroneAPI
from neuron.chatBots import neuroneChatbot
from neuron.codehelp import neuroneCodehelp
from neuron.open import neuroneOpen
from neuron.search import neuroneSearch
from neuron.service import neuroneService
from neuron.time import neuroneTime
from neuron.work import neuroneWork
from neuron.interface import interface
from neuron.markdown import neuroneMarkdown

class gestNeuron :
    def __init__(self,gestionnaire:gestionnaire) -> None:
        # Recuperation des etat de chaque neurone
        self.__etatService = gestionnaire.getConfigFile().etatService
        self.__etatTime = gestionnaire.getConfigFile().etatTime
        self.__etatOpen = gestionnaire.getConfigFile().etatOpen
        self.__etatSearch = gestionnaire.getConfigFile().etatSearch
        self.__etatChatbot = gestionnaire.getConfigFile().etatChatbot
        self.__etatApi = gestionnaire.getConfigFile().etatApi
        self.__etatCodehelp = gestionnaire.getConfigFile().etatCodehelp
        self.__etatWork = gestionnaire.getConfigFile().etatWork
        self.__etatSocket = gestionnaire.getConfigFile().etatSocket
        # Creation des varriable des neurones
        self.napi = None
        self.nchatbot = None
        self.ncodehelp = None
        self.nopen = None
        self.nsearch = None
        self.nservice = None
        self.ntime = None
        self.nwork = None
        self.ninterface = None
        # Init des neurones
        if self.__etatService == 1 :
            self.nservice = neuroneService(gestionnaire)
        if self.__etatTime == 1 :
            self.ntime = neuroneTime(gestionnaire)
        if self.__etatOpen == 1 :
            self.nopen = neuroneOpen(gestionnaire)
        if self.__etatSearch == 1 :
            self.nsearch = neuroneSearch(gestionnaire)
        if self.__etatChatbot == 1 :
            self.nchatbot = neuroneChatbot(gestionnaire)
        if self.__etatApi == 1 :
            self.napi = neuroneAPI(gestionnaire)
        if self.__etatCodehelp == 1 :
            self.ncodehelp = neuroneCodehelp(gestionnaire)
        if self.__etatWork == 1 :
            self.nwork = neuroneWork(gestionnaire)
        if self.__etatSocket == 1 :
            self.ninterface = interface(gestionnaire)
            self.nmarkdown = neuroneMarkdown(gestionnaire)


    def getSocket(self):
        if self.__etatSocket == 1 :
            return True
        else :
            return False