from neuron.CNeuronBase import neuronBase,gestionnaire
from tkinter.filedialog import askopenfilename


class neuroneWork(neuronBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__fonctionWork = self._gestionnaire.getGestFNC().getFNCWork()
        self.__fileProjectCreate = False
        self.__nameFileProjectCreate = ""
        self.__typeFileProjectCreate = ""

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["",""]
        self._valeurOut = 0
        self._valeurOut = self.__neuronTableur(requette)
        if not self._keyword.checkUtils(requette,"question-fonction"):
            if self._valeurOut == 0:
                self._valeurOut = self.__neuronProjet(requette)
                if self._valeurOut == 0:
                    self._valeurOut = self.__neuronHelp(requette)
                    if self._valeurOut == 0:
                        self._valeurOut = self.__neuronWord(requette)
                        if self._valeurOut == 0:
                            self._valeurOut = self.__neuronGUI(requette)


    def __neuronHelp(self,requette:str):
        if self._keyword.checkWork(requette,"help-work"):
            self._listSortie = [self._language.getPhraseHelpArreraWork("5"),""]
            return 17
        elif self._keyword.checkWork(requette,"question-open") and self._keyword.checkOpen(requette,"open") and self._keyword.checkWork(requette,"open-file"):
            word = self.__fonctionWork.getEtatWord()
            tableur = self.__fonctionWork.getEtatTableur()

            if word and tableur:
                self._listSortie = [self._language.getPhraseArreraWorkNeuron("1"),""]
            elif tableur and not word:
                self._listSortie = [self._language.getPhraseArreraWorkNeuron("2"),""]
            elif word and not tableur:
                self._listSortie = [self._language.getPhraseArreraWorkNeuron("3"),""]
            else :
                self._listSortie = [self._language.getPhraseArreraWorkNeuron("4"),""]

            return 1
        else :
            return 0

    def __neuronTableur(self,requette:str):
        if not self.__fonctionWork.getEtatTableur() :
            if (self._keyword.checkOpen(requette,"open") and
                    self._keyword.checkWork(requette,"tableur-file") and
                    not self._keyword.checkWork(requette,"gui-work")):

                if self.__fonctionWork.openTableur():
                    self._listSortie = [self._language.getPhraseArreraWorkTableur("1"),""]
                else :
                    self._listSortie = [self._language.getPhraseArreraWorkTableur("2"),""]

                return 7
            elif self._keyword.checkWork(requette,"help-tableur"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("1")
                    ,"tableur"]
                return 17
            else :
                return 0
        else:
            if self._keyword.checkWork(requette,"help-tableur"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("1")
                    ,"tableur"]
                return 17
            elif (self._keyword.checkOpen(requette,"open") and
                  self._keyword.checkWork(requette,"tableur-file") and
                  self._keyword.checkOpen(requette,"computer")):

                if self.__fonctionWork.openTableurOs():
                    self._listSortie = [self._language.getPhraseArreraWorkTableur("3"), ""]
                else :
                    self._listSortie = [self._language.getPhraseArreraWorkTableur("4"), ""]

                return 1
            elif (self._keyword.checkWork(requette,"close") and
                  self._keyword.checkWork(requette,"tableur-file")):

                if self.__fonctionWork.closeTableur():
                    self._listSortie = [self._language.getPhraseArreraWorkTableur("5"), ""]
                else :
                    self._listSortie = [self._language.getPhraseArreraWorkTableur("6"), ""]

                return 8
            elif self._keyword.checkWork(requette,"add") and self._keyword.checkWork(requette,"tableur-file"):
                if self._keyword.checkWork(requette,"valeur"):
                    self._gestGUI.setGUIActive("work_manage_tableur",1)
                    return 5
                elif self._keyword.checkWork(requette,"somme"):
                    self._gestGUI.setGUIActive("work_manage_tableur",2)
                    return 5
                elif self._keyword.checkWork(requette,"moyenne"):
                    self._gestGUI.setGUIActive("work_manage_tableur",3)
                    return 5
                elif self._keyword.checkWork(requette,"comptage"):
                    self._gestGUI.setGUIActive("work_manage_tableur",4)
                    return 5
                elif self._keyword.checkWork(requette,"min"):
                    self._gestGUI.setGUIActive("work_manage_tableur",5)
                    return 5
                elif self._keyword.checkWork(requette,"max"):
                    self._gestGUI.setGUIActive("work_manage_tableur",6)
                    return 5
                else :
                    return 0
            elif self._keyword.checkWork(requette,"del") and self._keyword.checkWork(requette,"tableur-file"):
                self._gestGUI.setGUIActive("work_manage_tableur",7)
                return 5
            elif self._keyword.checkWork(requette,"read") and self._keyword.checkWork(requette,"tableur-file"):
                self._gestGUI.setGUIActive("work_read_tableur")
                return 5
            else :
                return 0

    def __neuronProjet(self,requette:str):
        if not self.__fonctionWork.getEtatProject():
            if (self._keyword.checkWork(requette,"open-project")and
                    not self._keyword.checkWork(requette,"gui-work")):
                listKeyword = self._keyword.getListKeyword("work","list-word-open-project")
                for mot in listKeyword:
                    requette = requette.replace(mot,"")
                project = requette.strip()
                if self.__fonctionWork.openProjet(project):
                    self._listSortie = [self._language.getPhraseArreraWorkProjet("1",project),""]
                    self._gestHist.add_action("open_project",project)
                    return 14
                else :
                    self._listSortie = [self._language.getPhraseArreraWorkProjet("2",project),""]
                    return 1
            elif self._keyword.checkWork(requette, "create-project"):
                listKeyword = self._keyword.getListKeyword("work","create-project")
                for mot in listKeyword:
                    requette = requette.replace(mot,"")
                project = requette.strip()
                if self.__fonctionWork.createProjet(project):
                    self._listSortie = [self._language.getPhraseArreraWorkProjet("3",project),""]
                    self._gestHist.add_action("open_project",project)
                    return 10
                else :
                    self._listSortie = [self._language.getPhraseArreraWorkProjet("4",project),""]
                    return 1
            elif (self._keyword.checkWork(requette,"liste") and
                  self._keyword.checkWork(requette,"project-file")):
                listProject = self.__fonctionWork.getListProjet()

                if listProject is not None:
                    nbProject = len(listProject)

                    if nbProject == 0:
                        self._listSortie = [self._language.getPhraseArreraWorkProjet("5"),""]
                        return 1

                    elif nbProject == 1:
                        debutPhrase = self._language.getPhraseArreraWorkProjet("6")

                    else :
                        debutPhrase = self._language.getPhraseArreraWorkProjet("7")

                    text = ""

                    for i in range(0,nbProject):
                        if i == nbProject-1:
                            if nbProject == 1:
                                text = debutPhrase + " " + listProject[i] + "."
                            else :
                                text = text + " et " + listProject[i] + "."
                        elif i == 0:
                            text = debutPhrase + " " + listProject[i]
                        else :
                            text = text + ", " + listProject[i]

                    self._listSortie = [text,"liste project"]
                    return 1
                else :
                    self._listSortie = [self._language.getPhraseArreraWorkProjet("5"),""]
                    self._valeurOut = 1
                    return 1
            elif self._keyword.checkWork(requette,"help-project"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("3"),
                                    "project"]
                return 17
        else :
            if self._keyword.checkWork(requette,"help-project"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("3"),
                                    "project"]
                return 17
            elif (self._keyword.checkWork(requette,"project-file") and
                  self._keyword.checkWork(requette,"close")):
                project = self.__fonctionWork.getNameProjet()
                if self.__fonctionWork.closeProjet():
                    self._listSortie = [self._language.getPhraseArreraWorkProjet("8"),""]
                    self.__fileProjectCreate = False
                    self.__nameFileProjectCreate = ""
                    self.__typeFileProjectCreate = ""
                    self._gestHist.add_action("close_project",project)
                    return 21
                else :
                    self._listSortie = [self._language.getPhraseArreraWorkProjet("9"),""]
                    return 1
            elif (self._keyword.checkWork(requette,"project-file") and
                  self._keyword.checkWork(requette,"file") and
                  self._keyword.checkWork(requette,"liste")):
                self._listSortie = [self._language.getPhraseHelpArreraWork("4"),""]
                return 17
            elif (self._keyword.checkWork(requette,"project-file") and
                  (self._keyword.checkTime(requette,"montre") or
                   self._keyword.checkTime(requette,"open")) and
                  self._keyword.checkTime(requette,"tache")):
                self._gestGUI.setGUIActive("tache_projet")
                return 5
            elif (self._keyword.checkWork(requette,"project-file") and
                  self._keyword.checkTime(requette,"add") and
                  self._keyword.checkTime(requette,"tache")):

                self._gestGUI.setGUIActive("tache_projet_add")
                return 5
            elif (self._keyword.checkWork(requette,"project-file") and
                  self._keyword.checkTime(requette,"delete") and
                  self._keyword.checkTime(requette,"tache")):

                self._gestGUI.setGUIActive("tache_projet_del")
                return 5

            elif (self._keyword.checkWork(requette,"project-file") and
                  self._keyword.checkWork(requette,"file") and
                  self._keyword.checkWork(requette,"create")):
                self._listSortie = [self._language.getPhraseArreraWorkProjet("16")
                    ,""]
                self.__fileProjectCreate = True
                self.__nameFileProjectCreate = ""
                self.__typeFileProjectCreate = ""
                return 1

            elif self.__fileProjectCreate:
                if self._keyword.checkWork(requette,"name-file"):
                    listKeyword = self._keyword.getListKeyword("work","name-file")
                    for mot in listKeyword:
                        requette = requette.replace(mot,"")

                    self.__nameFileProjectCreate = requette.strip()

                    if self.__nameFileProjectCreate != "":
                        if self.__typeFileProjectCreate == "":
                            self._listSortie = [self._language.getPhraseArreraWorkProjet("17")
                                ,""]
                            return 1
                        elif self.__fonctionWork.createFileProject(self.__nameFileProjectCreate,
                                                                   self.__typeFileProjectCreate):
                            nameTypeFile = self.__nameFileProjectCreate+"."+self.__typeFileProjectCreate
                            self._listSortie = [
                                self._language.getPhraseArreraWorkProjet("18",
                                                                         nameTypeFile),""]
                            self.__fileProjectCreate = False
                            self.__nameFileProjectCreate = ""
                            self.__typeFileProjectCreate = ""
                            return 1
                        else :
                            self._listSortie = [self._language.getPhraseArreraWorkProjet("19")
                                ,""]
                            return 1
                    else :
                        self._listSortie = [self._language.getPhraseArreraWorkProjet("20")
                            ,""]
                        return 1

                elif self._keyword.checkWork(requette,"type-file"):
                    listKeyword = self._keyword.getListKeyword("work","type-file")
                    for mot in listKeyword:
                        requette = requette.replace(mot,"")

                    self.__typeFileProjectCreate = requette.strip().replace(" ","")

                    if (self.__typeFileProjectCreate in self.__fonctionWork.getListTypeFileName()
                            or self.__typeFileProjectCreate in self.__fonctionWork.getListTypeFileExtension() or
                            self.__typeFileProjectCreate != ""):

                        if self.__nameFileProjectCreate == "":
                            self._listSortie = [
                                self._language.getPhraseArreraWorkProjet("21")
                                ,""]
                            return 1
                        elif self.__fonctionWork.createFileProject(self.__nameFileProjectCreate,
                                                                   self.__typeFileProjectCreate):
                            nameTypeFile = self.__nameFileProjectCreate+"."+self.__typeFileProjectCreate
                            self._listSortie = [
                                self._language.getPhraseArreraWorkProjet("18",
                                                                         nameTypeFile),""]
                            self.__fileProjectCreate = False
                            self.__nameFileProjectCreate = ""
                            self.__typeFileProjectCreate = ""
                            return 1
                        else :
                            self._listSortie = [self._language.getPhraseArreraWorkProjet("19")
                                ,""]
                            return 1

                    else :
                        self._listSortie = [
                            self._language.getPhraseArreraWorkProjet("22")
                            ,""]
                        return 1
        return 0

    def __neuronWord(self,requette:str):
        if not self.__fonctionWork.getEtatWord():
            if (self._keyword.checkOpen(requette,"open") and
                    self._keyword.checkWork(requette,"word-file")and
                    not self._keyword.checkWork(requette,"gui-work")):
                if self.__fonctionWork.openWord():
                    self._listSortie = [self._language.getPhraseArreraWorkWord("1"),""]
                    return 7
                else :
                    self._listSortie = [self._language.getPhraseArreraWorkWord("2"),""]
                    return 1
            elif self._keyword.checkWork(requette,"help-word"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("2"),"word"]
                return 17
            else :
                return 0
        else :
            if self._keyword.checkWork(requette,"help-word"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("2"),"word"]
                return 17
            elif (self._keyword.checkOpen(requette,"open") and
                  self._keyword.checkWork(requette,"word-file") and
                  self._keyword.checkOpen(requette,"computer")):

                if self.__fonctionWork.openWordOs():
                    self._listSortie = [self._language.getPhraseArreraWorkWord("3"), ""]
                    return 1
                else :
                    self._listSortie = [self._language.getPhraseArreraWorkWord("4"), ""]
                    return 1
            elif (self._keyword.checkWork(requette,"close") and
                  self._keyword.checkWork(requette,"word-file")):

                if self.__fonctionWork.closeWord():
                    self._listSortie = [self._language.getPhraseArreraWorkWord("5"), ""]
                    return 8
                else :
                    self._listSortie = [self._language.getPhraseArreraWorkWord("6"), ""]
                    return 8

            elif self._keyword.checkWork(requette,"help-word"):
                self._listSortie = [self._language.getPhraseHelpArreraWork("2"),"word"]
                return 17
            elif (self._keyword.checkWork(requette,"write") and
                  self._keyword.checkWork(requette,"word-file")):
                self._gestGUI.setGUIActive("work_word_write")
                return 5
            elif (self._keyword.checkWork(requette,"read") and
                  self._keyword.checkWork(requette,"word-file")):
                self._gestGUI.setGUIActive("work_word_read")
                return 5
            else :
                return 0

    def __neuronGUI(self,requette):
        if self._keyword.checkOpen(requette,"open") and self._keyword.checkWork(requette,"gui-work"):# open
            if self._keyword.checkWork(requette,"project-file"): # projet
                self._gestGUI.setGUIActive("work_projet")
                return 5
            elif self._keyword.checkWork(requette,"tableur-file"): # tableur
                self._gestGUI.setGUIActive("work_tableur")
                return 5
            elif self._keyword.checkWork(requette,"word-file"): # word
                self._gestGUI.setGUIActive("work_word")
                return 5
            else :
                self._gestGUI.setGUIActive("work")
                return 5
        else :
            return 0