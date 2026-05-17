import random

from gestionnaire.gestSTR import*
from neuron.CNeuronBase import neuronBase,gestionnaire
from datetime import time,datetime

class neuroneAPI(neuronBase) :
    def __init__(self,gestionnaire:gestionnaire ):
        super().__init__(gestionnaire)
        self.__fncMeteo = self._gestFNC.getFNCMeteo()
        self.__fncBreef = self._gestFNC.getFNCBreef()
        self.__fncGPS = self._gestFNC.getFNCGPS()
        self.__fncActu = self._gestFNC.getFNCActu()
        self.__itineraire = False
        self.__arriver = ""
        self.__depart = ""

    def __texteMeteo(self,state:bool,a:int,b:int):
        if state:
            return self._language.getPhraseMeteo(str(random.randint(a, b)),
                                                  self.__fncMeteo.getNameTown(),
                                                  self.__fncMeteo.getDescription(),
                                                  self.__fncMeteo.getTemperature()
                                                 )[random.randint(0, 1)]
        else :
            return self._language.getPhraseMeteoError(str(random.randint(a, b)))

    def __texteBreef(self,outList:list,texte:str):
        self._listSortie = outList
        self._listSortie.append(texte)


    def __meteo(self,requette:str)->int:
        if not self._keyword.checkUtils(requette, "question-fonction"):
            townHouse = self._userConf.getLieuDomicile()
            townWork = self._userConf.getLieuTravail()

            if self._keyword.checkAPI(requette,"meteo"):
                if self._keyword.checkAPI(requette, "meteoDemainMatin"):
                    if self._keyword.checkAPI(townHouse,"lieuDomicile"):
                        state = self.__fncMeteo.getMeteoTowmorowMorning(town=townHouse)
                    elif self._keyword.checkAPI(townWork,"lieuTravail"):
                        state = self.__fncMeteo.getMeteoTowmorowMorning(town=townWork)
                    else :
                        state = self.__fncMeteo.getMeteoTowmorowMorning()

                    self._listSortie = [self.__texteMeteo(state,3,4),""]
                    return 4

                elif self._keyword.checkAPI(requette, "meteoDemainApresMidi"):
                    # Recuperation de la meteo de demain apres midi
                    if self._keyword.checkAPI(requette,"lieuDomicile"):
                        state = self.__fncMeteo.getMeteoTowmorowNoon(town=townHouse)
                    elif self._keyword.checkAPI(requette,"lieuTravail"):
                        state = self.__fncMeteo.getMeteoTowmorowNoon(town=townWork)
                    else :
                        state = self.__fncMeteo.getMeteoTowmorowNoon()

                    # Mise en place du texte de sortie
                    self._listSortie = [self.__texteMeteo(state, 1, 2), ""]
                    return 4

                else :
                    if self._keyword.checkAPI(requette, "lieuDomicile"):
                        state = self.__fncMeteo.getMeteoCurrentHour(town=townHouse)
                    elif self._keyword.checkAPI(requette, "lieuTravail"):
                        state = self.__fncMeteo.getMeteoCurrentHour(town=townWork)
                    else:
                        state = self.__fncMeteo.getMeteoCurrentHour()

                    self._listSortie = [self.__texteMeteo(state, 5, 6), ""]
                    return 4
            elif self._keyword.checkAPI(requette,"temperature"):
                if self._keyword.checkAPI(requette, "lieuDomicile"):
                    state = self.__fncMeteo.getMeteoCurrentHour(town=townHouse)
                elif self._keyword.checkAPI(requette, "lieuTravail"):
                    state = self.__fncMeteo.getMeteoCurrentHour(town=townWork)
                else:
                    state = self.__fncMeteo.getMeteoCurrentHour()

                if state:
                    texte = self._language.getPhraseTemperature(self.__fncMeteo.getTemperature())
                else :
                    texte = self._language.getPhraseMeteoError(str(random.randint(0, 1)))

                self._listSortie = [texte,""]
                return 4
        return 0

    def __breef(self,requette:str):
        """
        11 : Erreur du resumer actulités
        12 : Reussite du resumer actulités
        18 : Resumer tache / agenda
        19 : Resumer all ok
        20 : Resumer all fail
        """
        if not self._keyword.checkUtils(requette, "question-fonction"):
            if self._keyword.checkAPI(requette,"resumer"):
                if time(6,0) <= datetime.now().time() < time(11,0):
                    outInt = 5
                    self._gestGUI.setGUIActive("breef")
                    texte = self._language.getPhraseMorningBreef("1")
                elif self._keyword.checkAPI(requette,"actualite") or self._keyword.checkAPI(requette,"meteo"):
                    out = self.__fncBreef.summarizeActuAndMeteo(self._userConf.getLieuDomicile())
                    texte = self._language.getPhraseResumerActu()
                    if out is not None:
                        outInt = 12
                        self._gestGUI.setGUIActive("resumer",[out,None,outInt,texte])
                    else :
                        outInt = 11
                elif self._keyword.checkAPI(requette,"taches"):
                    out = self.__fncBreef.summarizeTask()
                    texte = self._language.getPhraseResumerTask()
                    if out is not None:
                        outInt = 18
                        self._gestGUI.setGUIActive("resumer",[None,out,outInt,texte])
                    else :
                        outInt = 11
                else:
                    out = self.__fncBreef.summarizeAll()
                    texte = self._language.getPhraseResumerAll("2")
                    if out is not None:
                        outInt = 19
                        self._gestGUI.setGUIActive("resumer",[out,None,outInt,texte])
                    else :
                        outInt = 20

                if outInt == 12 or outInt == 18 or outInt == 19 or outInt == 5:
                    self._listSortie = ["resumer",""]
                else :
                    self._listSortie = [self._language.getPhraseResumerAll("1"),""]
                return outInt
        return 0

    def __gps(self,requette:str):
        if not self._keyword.checkUtils(requette, "question-fonction"):
            if self._keyword.checkAPI(requette,"gps"):
                if self._keyword.checkAPI(requette,"coordonnees") :
                    if self.__fncGPS.locate():
                        self._listSortie = [self._language.getPhraseCoordonnees(latitude=str(self.__fncGPS.getLatitude()),
                                                                                longitude=str(self.__fncGPS.getLongitude()),
                                                                                ville=self.__fncGPS.getTown()),""]
                    else :
                        self._listSortie = [self._language.getPhraseGPSError(str(random.randint(0,1))),""]
                    return 4
                elif self._keyword.checkAPI(requette,"aide"):
                    self._gestGUI.setGUIActive("aide",[self._language.getTexteHelpIteneraire(),
                                                       self._language.getOpenHelpIteneraire()])
                    return 5
            elif self._keyword.checkAPI(requette,"launch-itinerary"):
                if not self.__itineraire:
                    self.__itineraire = True
                    self.__arriver = ""
                    self.__depart = ""
                    self._listSortie=[self._language.getPhraseIteneraire("1"),""]
                    return 1
                else :
                    if self.__arriver == "" and self.__depart == "":
                        self._listSortie = [self._language.getPhraseIteneraireError("4")
                            ,""]
                    else :
                        out = self.__fncGPS.launchGoogleMapItinerary(self.__depart,self.__arriver)
                        if not out :
                            self._listSortie = [self._language.getPhraseIteneraireError("5")
                                ,""]
                        else :
                            self._listSortie = [self._language.getPhraseIteneraire("4"),""]
                    return 1
            elif self.__itineraire:
                if self._keyword.checkAPI(requette,"add-start-itinerary"):
                    listDepart = self._keyword.getListKeyword("api","add-start-itinerary")

                    self.__depart = requette

                    if len(listDepart) == 0:
                        self._listSortie = [self._language.getPhraseIteneraireError("1"),
                                            ""]
                        return 1

                    for texte in listDepart:
                        self.__depart = self.__depart.replace(texte,"").strip()

                    if self.__depart != "":
                        self._listSortie = [self._language.getPhraseIteneraire("2",self.__depart),
                                            ""]
                        return 1
                    else :
                        self._listSortie = [self._language.getPhraseIteneraireError("2"),
                                            ""]
                        return 1
                elif self._keyword.checkAPI(requette,"add-end-itinerary"):
                        listArriver = self._keyword.getListKeyword("api","add-end-itinerary")

                        self.__arriver = requette

                        if len(listArriver) == 0:
                            self._listSortie = [self._language.getPhraseIteneraireError("4"),
                                                ""]
                            return 1

                        for texte in listArriver:
                            self.__arriver = self.__arriver.replace(texte,"").strip()

                        if self.__arriver != "":
                            self._listSortie = [self._language.getPhraseIteneraire("3",self.__arriver),
                                                ""]
                            return 1
                        else :
                            self._listSortie = [self._language.getPhraseIteneraireError("4"),
                                                ""]
                            return 1

        return 0

    def __news(self,requette:str):
        if not self._keyword.checkUtils(requette, "question-fonction"):
            if self._keyword.checkAPI(requette,"actualite"):
                if self.__fncActu.setActu(3,"fr"):
                    listActu = self.__fncActu.getActu()
                    if listActu != ["error","error"]:
                        self._listSortie = listActu
                        return 3
                    else :
                        self._listSortie = [self._language.getPhraseApi("1"),""]
                        return 1
                else :
                    self._listSortie = [self._language.getPhraseApi("1"), ""]
                    return 1
        return 0

    def __translate(self,requette:str):
        if not self._keyword.checkUtils(requette, "question-fonction"):
            if self._keyword.checkAPI(requette,"traducteur"):
                self._gestGUI.setGUIActive("traducteur")
                return 5
        return 0

    def neurone(self,requette:str):
        self._listSortie = ["", ""]
        self._valeurOut = 0
        self._valeurOut = self.__breef(requette)
        if self._valeurOut == 0:
            self._valeurOut = self.__meteo(requette)
            if self._valeurOut == 0:
                self._valeurOut = self.__gps(requette)
                if self._valeurOut == 0:
                    self._valeurOut = self.__news(requette)
                    if self._valeurOut == 0:
                        self._valeurOut = self.__translate(requette)