import random

from neuron.CNeuronBase import gestionnaire,neuronBase

class neuroneOpen(neuronBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__fncOpen = self._gestionnaire.getGestFNC().getFNCOpen()
        self.__fncRadio = self._gestionnaire.getGestFNC().getFNCRadio()
        self.__gestUser = self._gestionnaire.getUserConf()

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0

        if self.partUserRadio(requette) == 1:
            return

        if self.partListSoftWebRadio(requette) == 1:
            return

        if self.__partSocket(requette) == 1:
            return

        if self._keyword.checkOpen(requette,"open"):

            if self.partPreSaved(requette) == 1:
                return

            if self.partArreraSoft(requette) == 1:
                return

            if self.partUserSoft(requette) == 1:
                return

    def partUserSoft(self, requette: str) -> int:
        listKeyword = self._keyword.getListKeyword("open","open")
        software = requette
        for keyword in listKeyword:
            software = software.replace(keyword, "")
        software = software.strip().replace(" ","")
        outfnc = self.__fncOpen.openSoft(software)

        if outfnc == 1:
            nbRand = str(random.randint(1,2))
            self._listSortie = [
                self._language.getPhraseUserSoft(nbRand,software)
                ,""]
            self._valeurOut = 1
            self._gestHist.add_action("open_soft",software)
            return 1
        elif outfnc == 2:
            nbRand = str(random.randint(3,4))
            self._listSortie = [
                self._language.getPhraseUserSoft(nbRand,software)
                ,""]
            self._valeurOut = 1
            self._gestHist.add_action("open_soft",software)
            return 1
        elif outfnc == 0:
            return self.partUserWeb(requette)


    def partUserWeb(self, requette: str) -> int:
        listKeyword = self._keyword.getListKeyword("open","open")
        site = requette
        for keyword in listKeyword:
            site = site.replace(keyword, "")
        site = site.strip()

        outfnc = self.__fncOpen.openSaveWebSite(site)

        if  outfnc == 1:
            nbRand = str(random.randint(1,2))
            self._listSortie = [self._language.getPhraseUserWeb(nbRand,site)]
            self._valeurOut = 1
            self._gestHist.add_action("open_website",site)
            return 1
        elif outfnc == 2:
            nbRand = str(random.randint(3,4))
            self._listSortie = [self._language.getPhraseUserWeb(nbRand,site)]
            self._valeurOut = 1
            self._gestHist.add_action("open_website",site)
            return 1
        elif outfnc == 0:
            self._listSortie = [self._language.getPhraseNoOpen("1")]
            self._valeurOut = 1
            return 0
        else :
            return 0


    def partUserRadio(self, requette: str) -> int:
        if (self._keyword.checkOpen(requette,"launch") and
                self._keyword.checkOpen(requette,"radio")):
            if not self.__fncRadio.getRadioRunning():
                nbRadom = str(random.randint(1,6))
                if "eupope 1" in requette:
                    try :
                        if self.__fncRadio.startEurope1():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"Europe 1"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "europe 2" in requette:
                    try :
                        if self.__fncRadio.startEurope2():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"Europe 2"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "france info" in requette:
                    try :
                        if self.__fncRadio.startFranceInfo():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"France info"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "france inter" in requette:
                    try :
                        if self.__fncRadio.startFranceInter():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"France inter"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "france musique" in requette:
                    try :
                        if self.__fncRadio.startFranceMusique():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"France Musique"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "france culture" in requette:
                    try :
                        if self.__fncRadio.startFranceCulture():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"France Culture"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "france bleu" in requette:
                    try :
                        if self.__fncRadio.startFranceBleu():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"France bleu"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "fun radio" in requette:
                    try :
                        if self.__fncRadio.startFunRadio():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"Fun radio"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "nrj" in requette:
                    try :
                        if self.__fncRadio.startNRJ():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"NRJ"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "rfm" in requette:
                    try :
                        if self.__fncRadio.startRFM():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"RFM"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "nostalgi" in requette:
                    try :
                        if self.__fncRadio.startNostalgi():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"Nostalgi"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "skyrock" in requette:
                    try :
                        if self.__fncRadio.startSkyrock():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"Skyrock"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                elif "rtl" in requette:
                    try :
                        if self.__fncRadio.startRTL():
                            self._listSortie = [self._language.getPhraseRadioLaunch(nbRadom,"RTL"),""]
                            self._valeurOut = 22
                        else :
                            self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                            self._valeurOut = 1
                    except :
                        self._listSortie = [self._language.getPhraseRadioLaunch("8"),""]
                        self._valeurOut = 1
                return 1
            else :
                self._listSortie = [self._language.getPhraseRadioLaunch("7"),""]
                self._valeurOut = 1
                return 1
        elif (self._keyword.checkOpen(requette,"stop") and
              self._keyword.checkOpen(requette,"radio")):
            if self.__fncRadio.stop():
                self._listSortie = [self._language.getPhraseRadioLaunch("9"),""]
            else :
                self._listSortie = [self._language.getPhraseRadioLaunch("10"),""]
            self._valeurOut = 1
            return 1
        else :
            return 0

    def partArreraSoft(self, requette: str) -> int:
        if (not self._keyword.checkOpen(requette,"youtube_music")
              and self._keyword.checkOpen(requette,"youtube_downloader")):
            self._gestGUI.setGUIActive("arrera_download")
            self._valeurOut = 5
            return 1
        if self._keyword.checkOpen(requette,"calculator"):
            if self._keyword.checkOpen(requette,"complex_mode"):
                self._gestGUI.setGUIActive("calculatrice_complex")
                self._valeurOut = 5
            elif self._keyword.checkOpen(requette,"pythagore_mode"):
                self._gestGUI.setGUIActive("calculatrice_pythagore")
                self._valeurOut = 5
            else :
                self._gestGUI.setGUIActive("calculatrice_normal")
                self._valeurOut = 5
            return 1
        else :
            return 0

    def partPreSaved(self, requette: str) -> int:

        if (self._keyword.checkOpen(requette,"youtube")
                and not self._keyword.checkOpen(requette,"youtube_music")
                and not self._keyword.checkOpen(requette,"youtube_downloader")
                and not self._keyword.checkOpen(requette,"pythagore_mode")):
            outfnc = self.__fncOpen.openWebSite("https://www.youtube.com/")

            if  outfnc == 1:
                self._listSortie = [self._language.getPhrasePresavedOpen("1"),""]
            elif outfnc == 2:
                self._listSortie = [self._language.getPhrasePresavedOpen("2"),""]
            else :
                self._listSortie = [self._language.getPhrasePresavedOpen("3"),""]
            self._valeurOut = 1
            return 1

        elif (self._keyword.checkOpen(requette,"youtube_music")
              and not self._keyword.checkOpen(requette,"youtube_downloader")):
            outfnc = self.__fncOpen.openWebSite("https://music.youtube.com/")
            if  outfnc == 1:
                self._listSortie = [self._language.getPhrasePresavedOpen("4"),""]
            elif outfnc == 2:
                self._listSortie = [self._language.getPhrasePresavedOpen("5"),""]
            else :
                self._listSortie = [self._language.getPhrasePresavedOpen("6"),""]
            self._valeurOut = 1
            return 1

        else :
            return 0

    def partListSoftWebRadio(self,requette:str)->int:
        if self._keyword.checkOpen(requette,"say") :
            if self._keyword.checkOpen(requette,"software"):
                listNameSoft = list(self.__gestUser.getSoft().keys())
                print(listNameSoft)
                nbSoft = len(listNameSoft)
                if nbSoft == 0 :
                    self._listSortie = [self._language.getNbRadioSoftSite("2"),""]
                    self._valeurOut = 1
                elif nbSoft == 1 :
                    text = self._language.getNbRadioSoftSite("3")+listNameSoft[0]
                    self._listSortie = [text,""]
                    self._valeurOut = 1
                else :
                    text = self._language.getNbRadioSoftSite("1",str(nbSoft))
                    for nameSoft in listNameSoft :
                        text = text + "- " + nameSoft + "\n"
                    self._listSortie = [text,""]
                    self._valeurOut = 1
                return 1
            elif self._keyword.checkOpen(requette,"site"):
                listNameSite = list(self.__gestUser.getSite().keys())
                print(listNameSite)
                nbSite = len(listNameSite)
                if nbSite == 0 :
                    self._listSortie = [self._language.getNbRadioSoftSite("5"),""]
                    self._valeurOut = 1
                elif nbSite == 1 :
                    text = self._language.getNbRadioSoftSite("6")+listNameSite[0]
                    self._listSortie = [text,""]
                    self._valeurOut = 1
                else :
                    text = self._language.getNbRadioSoftSite("4",str(nbSite))
                    for nameSite in listNameSite :
                        text = text + "- " + nameSite + "\n"
                    self._listSortie = [text,""]
                    self._valeurOut = 1
                return 1
            elif self._keyword.checkOpen(requette,"radio"):
                radios = list(self._language.getListRadio())
                baseTexte = self._language.getNbRadioSoftSite("7")

                texte = baseTexte  # on part de la base
                nbRadio = len(radios)

                for i, nom in enumerate(radios):
                    if i == 0:
                        # premier élément : on colle directement
                        separateur = ""
                    elif i == nbRadio - 1:
                        # dernier élément : on met " et "
                        separateur = " et "
                    else:
                        # éléments intermédiaires : virgule + espace
                        separateur = ", "
                    texte += separateur + str(nom)

                self._listSortie = [texte,""]
                self._valeurOut = 1
                return 1
            else :
                return 0
        else :
            return 0

    def __partSocket(self,requette:str)->int:
        if self._keyword.checkOpen(requette,"mode_interface"):
            if self._keyword.checkOpen(requette,"open"):
                if self._gestionnaire.getSocketObjet() is not None:
                    if self._gestionnaire.getSocketObjet().get_client_is_on():
                        dictMode = self._gestionnaire.getNameMode()
                        if dictMode == {}:
                            return 0
                        else :
                            if ("mode1" in dictMode and (requette in dictMode["mode1"] or
                                                         self._keyword.checkOpen(requette,"mode_one"))):
                                self._listSortie = [self._language.getPhraseModeInterface("1", dictMode["mode1"])
                                    ,""]
                                self._valeurOut = 1
                                self._gestionnaire.getSocketObjet().send_data_with_clien("launch mode1")
                                return 1
                            elif ("mode2" in dictMode and (requette in dictMode["mode2"] or
                                                           self._keyword.checkOpen(requette,"mode_two"))):
                                self._listSortie = [self._language.getPhraseModeInterface("2", dictMode["mode2"])
                                    ,""]
                                self._valeurOut = 1
                                self._gestionnaire.getSocketObjet().send_data_with_clien("launch mode2")
                                return 1
                            elif ("mode3" in dictMode and (requette in dictMode["mode3"] or
                                                           self._keyword.checkOpen(requette,"mode_three"))):
                                self._listSortie = [self._language.getPhraseModeInterface("3", dictMode["mode3"])
                                    ,""]
                                self._valeurOut = 1
                                self._gestionnaire.getSocketObjet().send_data_with_clien("launch mode3")
                                return 1
                            elif ("mode4" in dictMode and (requette in dictMode["mode4"] or
                                                           self._keyword.checkOpen(requette,"mode_four"))):
                                self._listSortie = [self._language.getPhraseModeInterface("4", dictMode["mode4"])
                                    ,""]
                                self._valeurOut = 1
                                self._gestionnaire.getSocketObjet().send_data_with_clien("launch mode4")
                                return 1
                            elif ("mode5" in dictMode and (requette in dictMode["mode5"] or
                                                           self._keyword.checkOpen(requette,"mode_five"))):
                                self._listSortie = [self._language.getPhraseModeInterface("5", dictMode["mode5"])
                                    ,""]
                                self._valeurOut = 1
                                self._gestionnaire.getSocketObjet().send_data_with_clien("launch mode5")
                                return 1
                            elif ("mode6" in dictMode and (requette in dictMode["mode6"] or
                                                           self._keyword.checkOpen(requette,"mode_six"))):
                                self._listSortie = [self._language.getPhraseModeInterface("6", dictMode["mode6"])
                                    ,""]
                                self._valeurOut = 1
                                self._gestionnaire.getSocketObjet().send_data_with_clien("launch mode6")
                                return 1
                            else :
                                return 0
                    else :
                        return 0
                else :
                    return 0
            elif (self._keyword.checkOpen(requette,"close") and
                  self._gestionnaire.getModeIsEnabled()):
                self._listSortie = [self._language.getPhraseModeInterface("7")
                    ,""]
                self._valeurOut = 1
                self._gestionnaire.getSocketObjet().send_data_with_clien("close mode")
                return 1
            else:
                return 0
        else :
            return 0