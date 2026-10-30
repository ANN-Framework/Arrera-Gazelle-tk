import webbrowser

from librairy.arrera_tk import *
from tkinter import messagebox
from typing import Union
import threading as th
from librairy.travailJSON import jsonWork
from gestionnaire.gestion import gestionnaire

class arrera_gazelle :
    def __init__(self,windows:Union[aTk,aTopLevel],gest:gestionnaire,file_setting:str):
        # Ouverture de l'objet
        self.__gestUser = gest.getUserConf()
        self.__arrVoice = gest.getArrVoice()
        self.__jsonSetting = jsonWork(file_setting)
        # Var qui contient les thead
        self.__threadSaveVoicePrint = th.Thread()
        self.__theardDownloadModel = th.Thread()
        # Var BTN
        github_use = self.__jsonSetting.getContentJsonFlag("github_integration")
        micro_use = self.__jsonSetting.getContentJsonFlag("micro_use")
        self.__coordinated_btn_back = []
        # Var Triger Word
        self.__varOutTriger = 0
        self.__outTexteMicro = ""

        # Mise de la fenetre dans un atribut
        self.__windows = windows

        # Declaration des partie
        self.__main_setting_display()
        self.__user_display()
        self.__meteo_display()
        self.__ia_display()
        self.__gps_display()
        self.__search_display()
        self.__web_display()
        self.__software_display()
        self.__microphone_display()
        self.__github_display()

        # Declaration des cardre
        self.__main_frame = aFrame(self.__windows, width=500, height=400)
        self.__backFrame = aFrame(self.__windows,width=500,height=70)

        # Configuration du mainframe
        for col in range(4):
            self.__main_frame.columnconfigure(col, weight=1)

        for row in range(4):
            self.__main_frame.rowconfigure(row, weight=1)

        icon_assistant = aImage(path_light=self.__jsonSetting.getContentJsonFlag("iconSoft"),width=85,height=85)
        self.__btn_icon = aButton(self.__main_frame, image=icon_assistant, text="", corner_radius=8, width=125, height=125)
        btn_welcome = [aButton(self.__main_frame, text="Paramètres\ngénéraux", command=self.__viewMainSetting),
                      aButton(self.__main_frame, text="Paramètres\nutilisateur", command=self.__viewUserAcceuil),
                      aButton(self.__main_frame, text="Météo", command=self.__viewMeteoAcceuil),
                      aButton(self.__main_frame, text="Intelligence\nartificielle", command=self.__viewIAAcceuil),
                      aButton(self.__main_frame, text="Paramètres\nde\nrecherche", command=self.__viewRecherche),
                      aButton(self.__main_frame, text="Logiciels\nexternes", command=self.__viewSoftAcceuil),
                      aButton(self.__main_frame, text="Raccourcis\nInternet", command=self.__viewInternetAcceuil),
                      aButton(self.__main_frame, text="Adresses\nGPS", command=self.__viewGPSAcceuil),
                      aButton(self.__main_frame, text="Intégration\nGitHub", command=self.__viewGithub),
                      aButton(self.__main_frame, text="Paramètres\ndu\nMicro", command=self.__viewMicroAcceuil)]

        for i in btn_welcome:
            if gest.getOSObjet().osMac():
                i.configure(width=125, height=125, font=("Roboto", 11.4, "bold"))
            else :
                i.configure(width=125, height=125,font=("Roboto",12.5,"bold"))

        self.__btn_back_assistant = aButton(self.__main_frame, text="Retour", width=125, height=125)
        self.__btn_back_assistant.configure(font=("Roboto",12.5,"bold"))

        # backFrame
        btn_back_welcome = aButton(self.__backFrame,text="Retour Accueil",command=self.__backAcceuil)

        # Affichage
        self.__main_frame.grid_propagate(False)

        index = 1

        for i in range(8):
            row = index // 4
            col = index % 4
            btn_welcome[i].grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            index += 1

        if github_use == "1":
            row = index // 4
            col = index % 4
            btn_welcome[8].grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            index += 1

        if micro_use == "1":
            row = index // 4
            col = index % 4
            btn_welcome[9].grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            index += 1

        # ✅ Bouton Back (toujours à la bonne place)
        row = index // 4
        col = index % 4

        self.__coordinated_btn_back = [row, col]

        # backFrame
        btn_back_welcome.placeCenterRight()

    def __main_setting_display(self):
        self.__main_setting_frame = aFrame(self.__windows,width=500,height=330)

        self.__main_setting_welcome_frame = aFrame(self.__main_setting_frame,width=500,height=330)
        self.__work_folder_frame = aFrame(self.__main_setting_frame,width=500,height=330)
        self.__download_folder_frame = aFrame(self.__main_setting_frame,width=500,height=330)

        # Widget
        l_title_main_setting = [aLabel(self.__main_setting_welcome_frame,text="Paramètres généraux",police_size=25),
                                aLabel(self.__work_folder_frame,text="Dossier de travail",police_size=25),
                                aLabel(self.__download_folder_frame,text="Dossier de téléchargement",police_size=25)]

        # Welcome
        btn_folder_work = aButton(self.__main_setting_welcome_frame,size=15,
                                  text="Gestion\ndu\ndossier de\ntravail\nArrera Work",
                                  command=self.__viewWorkFolder)
        btn_folder_download = aButton(self.__main_setting_welcome_frame,size=15,
                                  text="Gestion\ndu\ndossier\nde\ntéléchargement",
                                  command=self.__viewDownloadFolder)
        self.__btn_enable_hist = aSwicht(self.__main_setting_welcome_frame,
                                  text="Activer l'historique",default_value=False,
                                         command=self.__set_hist_state)

        # Work folder
        self.__l_state_work_folder = aLabel(self.__work_folder_frame,police_size=15)
        self.__btn_work_folder = aButton(self.__work_folder_frame,size=15)
        # Download folder
        self.__l_state_download_folder = aLabel(self.__download_folder_frame,police_size=15)
        self.__btn_download_folder = aButton(self.__download_folder_frame,size=15)
        # Back
        btn_back_main = [aButton(self.__work_folder_frame,text="Retour",
                               command=self.__viewMainSetting),
                       aButton(self.__download_folder_frame,text="Retour",
                               command=self.__viewMainSetting)]

        # Affichage
        for i in l_title_main_setting:
            i.placeTopCenter()

        for i in btn_back_main:
            i.placeBottomLeft()

        btn_folder_work.placeLeftCenter()
        btn_folder_download.placeRightCenter()
        self.__btn_enable_hist.placeBottomCenter()

        self.__l_state_work_folder.placeCenter()
        self.__btn_work_folder.placeBottomCenter()

        self.__l_state_download_folder.placeCenter()
        self.__btn_download_folder.placeBottomCenter()

        self.__initBtnEnableHist()

    def __user_display(self):
        self.__user_frame = aFrame(self.__windows, width=500, height=330)
        self.__user_welcome_frame = aFrame(self.__user_frame, width=500, height=330)
        self.__userName = aFrame(self.__user_frame, width=500, height=330)
        self.__userGenre = aFrame(self.__user_frame, width=500, height=330)

        # userFrame
        # Label
        labelTitleUser = [aLabel(self.__user_welcome_frame, text="Gestion utilisateur", police_size=25),
                          aLabel(self.__userName,text="Nom de l'utilisateur",police_size=25),
                          aLabel(self.__userGenre,text="Genre de l'utilisateur",police_size=25)]
        # entry
        entryFirstNameUser = aEntryLengend(self.__userName,text="Prénom",bg=self.__userName.cget("fg_color"))
        entryLastNameUser = aEntryLengend(self.__userName,text="Nom",bg=self.__userName.cget("fg_color"))
        # option menu
        listGenre = self.__jsonSetting.getFlagListJson("listGenre")
        menuUserGenre = aOptionMenu(self.__userGenre,value = listGenre)

        # Button
        btnUserName = aButton(self.__user_welcome_frame, text="Nom\nde\nl'utilisateur",
                              command=lambda:self.__viewUserName())
        btnUserGenre = aButton(self.__user_welcome_frame, text="Genre\nde\nl'utilisateur",
                               command=lambda:self.__viewUserGenre())
        btnValiderUserName = aButton(self.__userName,text="Valider",
                                     command=lambda:
                                     self.__saveUserName(entryLastNameUser.getEntry(),entryFirstNameUser.getEntry()))
        btnValiderUserGenre = aButton(self.__userGenre,text="Valider",
                                      command=lambda:self.__saveUserGenre(menuUserGenre))
        btnRetourUserName = aButton(self.__userName, text="Retour",
                                    command=lambda:self.__viewUserAcceuil())
        btnRetourUserGenre = aButton(self.__userGenre, text="Retour",
                                     command=lambda:self.__viewUserAcceuil())


        # userFrame
        for i in (range(0,len(labelTitleUser))):
            labelTitleUser[i].placeTopCenter()

        btnUserName.placeRightCenter()
        btnUserGenre.placeLeftCenter()

        btnValiderUserName.placeBottomLeft()
        btnValiderUserGenre.placeBottomLeft()
        btnRetourUserName.placeBottomRight()
        btnRetourUserGenre.placeBottomRight()

        entryFirstNameUser.placeCenterOnWidth(60)
        entryLastNameUser.placeCenterOnWidth(140)
        menuUserGenre.placeCenter()

    def __meteo_display(self):
        self.__meteoFrame = aFrame(self.__windows,width=500,height=330)
        self.__meteoAcceuil = aFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoDomicile = aFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoTravail = aFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoVille = aFrame(self.__meteoFrame,width=500,height=330)
        self.__meteoSuppr = aFrame(self.__meteoFrame,width=500,height=330)

        # meteoFrame
        # Label
        labelTitleMeteo = [aLabel(self.__meteoAcceuil,text="Gestion de la météo",police_size=25),
                           aLabel(self.__meteoDomicile,text="Lieu Domicile",police_size=25),
                           aLabel(self.__meteoTravail,text="Lieu Travail",police_size=25),
                           aLabel(self.__meteoVille,text="Autre Ville",police_size=25),
                           aLabel(self.__meteoSuppr,text="Supprimer un lieu",police_size=25)]
        # Button
        btnAcceuilMeteoDomicile = aButton(self.__meteoAcceuil,text="Lieu\nDomicile",
                                          command=lambda:self.__viewMeteoDomicile())
        btnAcceuilMeteoTravail = aButton(self.__meteoAcceuil,text="Lieu\nTravail",
                                         command=lambda:self.__viewMeteoTravail())
        btnAcceuiMeteolVille = aButton(self.__meteoAcceuil,text="Autre\nVille",
                                       command=lambda:self.__viewMeteoVille())
        btnAcceuilMeteoSuppr = aButton(self.__meteoAcceuil,text="Supprimer un lieu",
                                       command=lambda:self.__viewMeteoSuppr())

        btnValiderMeteoDomicile = aButton(self.__meteoDomicile,text="Valider",
                                          command=lambda:self.__saveMeteoDomicile())
        btnValiderMeteoTravail = aButton(self.__meteoTravail,text="Valider",
                                         command=lambda:self.__saveMeteoTravail())
        btnValiderMeteoVille = aButton(self.__meteoVille,text="Valider",
                                       command=lambda:self.__saveMeteoVille())
        btnValiderMeteoSuppr = aButton(self.__meteoSuppr,text="Supprimer",
                                       command=lambda:self.__supprMeteoVille())

        btnRetourMeteoDomicile = aButton(self.__meteoDomicile,text="Retour",
                                         command=lambda:self.__viewMeteoAcceuil())
        btnRetourMeteoTravail = aButton(self.__meteoTravail,text="Retour",
                                        command=lambda:self.__viewMeteoAcceuil())
        btnRetourMeteoVille = aButton(self.__meteoVille,text="Retour",
                                      command=lambda:self.__viewMeteoAcceuil())
        btnRetourMeteoSuppr = aButton(self.__meteoSuppr,text="Retour",
                                      command=lambda:self.__viewMeteoAcceuil())
        # entry
        self.__entryMeteoDomicile = aEntry(self.__meteoDomicile, width=300)
        self.__entryMeteoTravail = aEntry(self.__meteoTravail, width=300)
        self.__entryMeteoVille = aEntry(self.__meteoVille, width=300)
        #option menu
        self.__menuMeteoSuppr = aOptionMenu(self.__meteoSuppr, value = ["", ""])

        # meteoFrame
        for i in (range(0,len(labelTitleMeteo))):
            labelTitleMeteo[i].placeTopCenter()

        btnAcceuilMeteoDomicile.placeRightCenter()
        btnAcceuilMeteoTravail.placeLeftCenter()
        btnAcceuiMeteolVille.placeCenter()
        btnAcceuilMeteoSuppr.placeBottomCenter()

        btnValiderMeteoDomicile.placeBottomLeft()
        btnRetourMeteoDomicile.placeBottomRight()

        btnValiderMeteoVille.placeBottomLeft()
        btnRetourMeteoVille.placeBottomRight()

        btnValiderMeteoTravail.placeBottomLeft()
        btnRetourMeteoTravail.placeBottomRight()

        btnValiderMeteoSuppr.placeBottomLeft()
        btnRetourMeteoSuppr.placeBottomRight()

        self.__entryMeteoDomicile.placeCenter()
        self.__entryMeteoTravail.placeCenter()
        self.__entryMeteoVille.placeCenter()

    def __ia_display(self):
        self.__iaFrame = aFrame(self.__windows,width=500,height=330)

        self.__iaAcceuil = aFrame(self.__iaFrame,width=500,height=330)
        self.__iaDownload = aFrame(self.__iaFrame,width=500,height=330)
        self.__iaChoose = aFrame(self.__iaFrame,width=500,height=330)

        # Widget
        labelTitleIA = [aLabel(self.__iaAcceuil,text="Gestion des modèles \nd'intelligence artificielle",police_size=25),
                        aLabel(self.__iaDownload,text="Choix du modèle \nd'intelligence artificielle",police_size=25),
                        aLabel(self.__iaChoose,text="Téléchargement \nd'un modèle d'intelligence artificielle",police_size=25)]

        btnChoixModel = aButton(self.__iaAcceuil,text="Choix d'un modèle",command=self.__viewIAChoose)
        btnDownloadModel = aButton(self.__iaAcceuil,text="Téléchargement d'un modèle",command=self.__viewDownloadIA)

        self.__btnEnableIA = aSwicht(self.__iaAcceuil, text="Activer le mode IA",
                                     default_value=False,
                                     command=self.__set_enable_ia_mode)

        # General
        backBtnIA = [aButton(self.__iaDownload,text="Terminer",command=lambda:self.__viewIAAcceuil()),
                     aButton(self.__iaChoose,text="Retour",command=lambda:self.__viewIAAcceuil())]

        # Choose model
        self.__menuChooseIAModel = aOptionMenu(self.__iaChoose,value=["",""])
        validerChooseModel = aButton(self.__iaChoose,text="Valider",command=self.__setModelToUse)

        # Download
        self.__downloadIA = aScrollableFrame(self.__iaDownload,width=450,corner_radius=0)
        self.__duringDownloadModel = aFrame(self.__iaFrame,width=500,height=330)

        # During Download Model
        labelViewDownload = aLabel(self.__duringDownloadModel,
                                   text="Téléchargement d'un modèle\nen cours...",
                                   police_size=25)

        # Placement
        for i in (range(0,len(labelTitleIA))):
            labelTitleIA[i].placeTopCenter()

        for i in (range(0,len(backBtnIA))):
            backBtnIA[i].placeBottomLeft()

        btnChoixModel.placeLeftCenter()
        btnDownloadModel.placeRightCenter()

        self.__menuChooseIAModel.placeCenter()
        validerChooseModel.placeBottomRight()

        labelViewDownload.placeCenter()

        self.__downloadIA.placeCenter()

        self.__btnEnableIA.placeBottomCenter()

        self.__initBtnEnableIAMode()

    def __gps_display(self):
        self.__gpsFrame = aFrame(self.__windows,width=500,height=330)
        self.__gpsAcceuil = aFrame(self.__gpsFrame,width=500,height=330)
        self.__gpsDomicile = aFrame(self.__gpsFrame,width=500,height=330)
        self.__gpsTravail = aFrame(self.__gpsFrame,width=500,height=330)

        # GPS Frame
        # Label
        labelTitleGPS = [aLabel(self.__gpsAcceuil,text="Gestion de vos adresses",police_size=25),
                         aLabel(self.__gpsDomicile,text="Adresse de votre Domicile",police_size=25),
                         aLabel(self.__gpsTravail,text="Adresse de votre Travail",police_size=25)]
        # Button
        btnAcceuilGPSDomicile = aButton(self.__gpsAcceuil,text="Adresse\nde\nDomicile",
                                        command=lambda:self.__viewGPSDomicile())
        btnAcceuilGPSTravail = aButton(self.__gpsAcceuil,text="Adresse\nde\nTravail",
                                       command=lambda:self.__viewGPSTravail())

        btnValiderGPS = [aButton(self.__gpsDomicile,text="Valider",
                                 command=lambda:self.__saveGPSDomicile()),
                         aButton(self.__gpsTravail,text="Valider",
                                 command=lambda:self.__saveGPSTravail())]

        btnBackGPS = [aButton(self.__gpsDomicile,text="Retour",
                              command=lambda:self.__viewGPSAcceuil()),
                      aButton(self.__gpsTravail,text="Retour",
                              command=lambda:self.__viewGPSAcceuil())]

        self.__btnSupprGPS = [aButton(self.__gpsDomicile,text="Supprimer l'adresse",
                                command=self.__supprAdresseDomicile),
                        aButton(self.__gpsTravail,text="Supprimer l'adresse",
                                command=self.__supprAdresseWork)]

        # entry
        self.__entryGPS = [aEntry(self.__gpsDomicile, width=300),
                           aEntry(self.__gpsTravail, width=300)]

        for i in range(0,len(labelTitleGPS)):
            labelTitleGPS[i].placeTopCenter()

        btnAcceuilGPSDomicile.placeRightCenter()
        btnAcceuilGPSTravail.placeLeftCenter()

        for i in btnValiderGPS:
            i.placeBottomLeft()

        for i in btnBackGPS:
            i.placeBottomRight()

    def __search_display(self):
        listMoteurRecherche = self.__jsonSetting.getFlagListJson("listMoteurRecherche")

        self.__rechercheFrame = aFrame(self.__windows,width=500,height=330)

        labelTitleRecherche = aLabel(self.__rechercheFrame,text="Gestion du moteur de recherche",police_size=25)
        btnValiderRecherche = aButton(self.__rechercheFrame,text="Valider",
                                      command=lambda:self.__saveRecherche())
        self.__mSearch = aOptionMenu(self.__rechercheFrame,value = listMoteurRecherche)

        labelTitleRecherche.placeTopCenter()
        self.__mSearch.placeCenter()
        btnValiderRecherche.placeBottomCenter()

    def __web_display(self):
        self.__webFrame = aFrame(self.__windows, width=500, height=330)
        self.__webAcceuil = aFrame(self.__webFrame, width=500, height=330)
        self.__webAddShortcut = aFrame(self.__webFrame, width=500, height=330)
        self.__webDelShortcut = aFrame(self.__webFrame, width=500, height=330)
        self.__webSavedShortcut = aFrame(self.__webFrame, width=500, height=330)

        # Internet Frame
        # Label
        labelTitleInternet = [aLabel(self.__webAcceuil, text="Gestion des raccourcis\ninternet",
                                     police_size=25),
                              aLabel(self.__webAddShortcut, text="Ajouter un raccourci",
                                     police_size=25),
                              aLabel(self.__webDelShortcut, text="Supprimer un raccourci",
                                     police_size=25),
                              aLabel(self.__webSavedShortcut, text="Liste des raccourcis enregistrés",
                                     police_size=25)]

        # Bouton
        btnAddWebShortcut = aButton(self.__webAcceuil, text="Ajouter\nun raccourci",
                                            command=self.__viewInternetSiteWeb, size=15)
        btnDelWebShortcut = aButton(self.__webAcceuil, text="Supprimer\nun raccourci",
                                              command= self.__viewInternetSupprSite, size=15)
        btnViewWebShortcut = aButton(self.__webAcceuil, text="Raccourcis\nenregistrés",
                                              command= self.__viewInternetListeSite, size=15)

        btnBackWeb = [aButton(self.__webAddShortcut, text="Retour"
                              ,command=self.__viewInternetAcceuil),
                      aButton(self.__webDelShortcut, text="Retour"
                              , command=self.__viewInternetAcceuil),
                      aButton(self.__webSavedShortcut, text="Retour"
                              , command=self.__viewInternetAcceuil)]

        btnValiderSiteWeb = aButton(self.__webAddShortcut, text="Valider",
                                    command=self.__saveSiteWeb)

        btnInternetValiderSuppr = aButton(self.__webDelShortcut, text="Valider"
                                          , command=lambda:self.__supprSiteWeb())

        self.__listSite = aText(self.__webSavedShortcut, width=450, height=250,
                                wrap="word", state="normal")

        # Entry
        self.__entruWebSortCut = [aEntryLengend(self.__webAddShortcut, text="Nom",width=250),
                                  aEntryLengend(self.__webAddShortcut, text="URL",width=250)]


        # option menu
        self.__menuSiteWeb = aOptionMenu(self.__webDelShortcut, value = ["", ""])


        for i in range(0,len(labelTitleInternet)):
            labelTitleInternet[i].placeTopCenter()

        btnAddWebShortcut.placeLeftCenter()
        btnDelWebShortcut.placeRightCenter()
        btnViewWebShortcut.placeCenter()

        btnValiderSiteWeb.placeBottomRight()

        btnInternetValiderSuppr.placeBottomRight()

        self.__entruWebSortCut[0].placeCenterOnWidth(y=100)
        self.__entruWebSortCut[1].placeCenterOnWidth(y=150)

        for i in btnBackWeb:
            i.placeBottomLeft()

        self.__listSite.placeCenter()

    def __software_display(self):
        self.__softFrame = aFrame(self.__windows,width=500,height=330)
        self.__softAcceuil = aFrame(self.__softFrame,width=500,height=330)
        self.__softAdd = aFrame(self.__softFrame,width=500,height=330)
        self.__softSuppr = aFrame(self.__softFrame,width=500,height=330)
        self.__softListe = aFrame(self.__softFrame,width=500,height=330)
        # Soft Frame
        # Label
        labelTitleSoft = [aLabel(self.__softAcceuil,text="Gestion des logiciels",police_size=25),
                          aLabel(self.__softAdd,text="Nom du logiciel à ajouter",police_size=25),
                          aLabel(self.__softSuppr,text="Suppression d'un logiciel",police_size=25),
                          aLabel(self.__softListe,text="Liste des logiciels enregistrés",police_size=25)]

        self.__listSoftware = aText(self.__softListe, width=450, height=250,
                                    wrap="word", state="normal")

        # Button
        btnAcceuilSoftAdd = aButton(self.__softAcceuil,text="Ajout\nd'un\nlogiciel"
                                    ,command=self.__viewSoftAdd,size=15)
        btnAcceuilSoftSuppr = aButton(self.__softAcceuil,text="Suppression\nd'un\nlogiciel"
                                      ,command=self.__viewSoftSuppr,size=15)
        btnAcceuilSoftList = aButton(self.__softAcceuil,text="Logiciels\nSauvegardés"
                                     ,command=self.__viewSoftList,size=15)

        btnAddSoftValider = aButton(self.__softAdd, text="Valider"
                                    , command=self.__addSoft)

        btnSupprSoftValider = aButton(self.__softSuppr,text="Valider",
                                      command=self.__supprSoft)

        btnBackSoft = [aButton(self.__softSuppr,text="Retour",
                               command=self.__viewSoftAcceuil),
                       aButton(self.__softListe,text="Retour",
                               command=self.__viewSoftAcceuil),
                       aButton(self.__softAdd,text="Retour"
                               ,command=self.__viewSoftAcceuil)]

        # Entry
        self.__eAddSoft = aEntryLengend(self.__softAdd,text="Nom du logiciel", width=200)

        # Option Menu
        self.__menuSoftSuppr = aOptionMenu(self.__softSuppr,value = ["",""])

        for i in labelTitleSoft:
            i.placeTopCenter()

        for i in btnBackSoft:
            i.placeBottomLeft()

        btnAcceuilSoftAdd.placeLeftCenter()
        btnAcceuilSoftSuppr.placeRightCenter()
        btnAcceuilSoftList.placeCenter()

        self.__eAddSoft.placeCenter()
        btnAddSoftValider.placeBottomRight()

        btnSupprSoftValider.placeBottomRight()
        self.__listSoftware.placeCenter()

    def __microphone_display(self):
        self.__microFrame = aFrame(self.__windows,width=500,height=330)
        self.__microAcceuil = aFrame(self.__microFrame,width=500,height=330)
        self.__microSound = aFrame(self.__microFrame,width=500,height=330)
        self.__microTigerWord = aFrame(self.__microFrame,width=500,height=330)
        self.__microVoicePrint = aFrame(self.__microFrame,width=500,height=330)
        self.__microDuringSave = aFrame(self.__microFrame,width=500,height=330)
        self.__microViewSave = aFrame(self.__microFrame,width=500,height=330)
        self.__microViewWordSave = aFrame(self.__microFrame,width=500,height=330)

        # Micro Frame
        # Label
        labelTitleMicro = [aLabel(self.__microAcceuil,text="Gestion du microphone",
                                  police_size=25),
                           aLabel(self.__microSound,text="Son émis à l'écoute du micro",
                                  police_size=25),
                           aLabel(self.__microTigerWord,text="Définition du mot\nde déclenchement du micro",
                                  police_size=25),
                           aLabel(self.__microViewSave,text="Enregistrement de l'empreinte vocale",
                                  police_size=25),
                           aLabel(self.__microViewWordSave,text="Mots enregistrés"),]
        self.__labelVoicePrint = aLabel(self.__microVoicePrint,text="Empreinte vocale",
                                        police_size=25)
        self.__labelWordVoicePrint = aLabel(self.__microViewSave,text="",
                                            police_size=20)
        self.__labelWordViewSave = aLabel(self.__microViewWordSave,text="",
                                          police_size=15)
        labelDuringSave = aLabel(self.__microDuringSave,text="Dites le mot de déclenchement que vous voulez",
                                 police_size=15)

        # Button
        btnAcceuilMicroSound = aButton(self.__microAcceuil,text="Son\némis",
                                       command=lambda:self.__viewMicroSound())
        btnAcceuilMicroTigerWord = aButton(self.__microAcceuil,text="Empreinte\nvocale",
                                           command=lambda:self.__viewMicroTigerWord())

        self.__btnMicroSoundChangeEtat = aButton(self.__microSound,text="",
                                                 command=lambda:self.__changeMicroSound())

        btnBackMicro = [aButton(self.__microSound, text="Retour",
                                command=self.__viewMicroAcceuil),
                        aButton(self.__microTigerWord, text="Retour",
                                command=self.__viewMicroAcceuil)]

        self.__btnTrigerWordVoicePrint1 = aButton(self.__microTigerWord,text="Empreinte\nvocale 1"
                                                  ,command=lambda : self.__viewVoicePrint(1))
        self.__btnTrigerWordVoicePrint2 = aButton(self.__microTigerWord, text="Empreinte\nvocale 2"
                                                  ,command=lambda : self.__viewVoicePrint(2))
        self.__btnTrigerWordVoicePrint3 = aButton(self.__microTigerWord, text="Empreinte\nvocale 3"
                                                  ,command=lambda : self.__viewVoicePrint(3))
        btnSauvegarderVoicePrint = aButton(self.__microViewSave,text="Sauvegarder",
                                           command=lambda : self.__saveTigerWord() )

        btnBackVoicePrint = [ aButton(self.__microVoicePrint, text="Retour",
                                      command=self.__viewMicroTigerWord),
                              aButton(self.__microViewSave, text="Annuler",
                                      command=self.__viewMicroAcceuil)]

        btnRetourViewWord = aButton(self.__microViewWordSave, text="Retour",
                                    command=lambda:self.__viewMicroTigerWord())

        self.__btnSaveVoicePrint = aButton(self.__microVoicePrint,text="Enregistrer",
                                           command=lambda :self.__saveVoicePrint())

        self.__btnSupprVoicePrint = aButton(self.__microVoicePrint,text="Supprimer")

        self.__btnViewVoicePrint = aButton(self.__microVoicePrint, text="Voir le mot")

        for i in labelTitleMicro:
            i.placeTopCenter()

        self.__labelVoicePrint.placeTopCenter()
        self.__labelWordVoicePrint.placeCenter()
        btnSauvegarderVoicePrint.placeBottomLeft()
        btnRetourViewWord.placeBottomRight()
        self.__labelWordViewSave.placeCenter()
        labelDuringSave.placeCenter()

        btnAcceuilMicroSound.placeRightCenter()
        btnAcceuilMicroTigerWord.placeLeftCenter()

        self.__btnMicroSoundChangeEtat.placeCenter()

        for i in btnBackMicro:
            i.placeBottomCenter()

        for i in btnBackVoicePrint:
            i.placeBottomRight()

    def __github_display(self):
        self.__githubFrame = aFrame(self.__windows,width=500,height=330)

        self.__githubAcceuil = aFrame(self.__githubFrame,width=500,height=330)
        self.__githubToken = aFrame(self.__githubFrame,width=500,height=330)

        l_title_github = [aLabel(self.__githubAcceuil,text="Gestion des accès GitHub",police_size=25),
                          aLabel(self.__githubToken,text="Ajout du token GitHub",police_size=25)]

        self.__btnToken = aButton(self.__githubAcceuil,size=15)

        self.__eToken = aEntryLengend(self.__githubToken,text="Token GitHub",width=200)

        btnValiderToken = aButton(self.__githubToken,text="Valider",size=15,command=self.__saveToken)
        btnCancelToken = aButton(self.__githubToken,text="Annuler",size=15,command=self.__viewGithub)

        # Affichage
        for i in l_title_github:
            i.placeTopCenter()

        self.__eToken.placeCenter()

        self.__btnToken.placeCenter()

        btnValiderToken.placeBottomLeft()
        btnCancelToken.placeBottomRight()

    def __initBtnEnableIAMode(self):
        if self.__getStateIAMode():
            self.__btnEnableIA.setOn()
        else :
            self.__btnEnableIA.setOff()

    def __initBtnEnableHist(self):
        if self.__gestUser.getHist() == 1 :
            self.__btn_enable_hist.setOn()
        else :
            self.__btn_enable_hist.setOff()

    # Methode generale
    def active(self):
        self.__main_frame.pack()

    def __clearAll(self):
        self.__main_frame.pack_forget()
        self.__main_setting_frame.pack_forget()
        self.__user_frame.pack_forget()
        self.__iaFrame.pack_forget()
        self.__backFrame.pack_forget()
        self.__meteoFrame.pack_forget()
        self.__gpsFrame.pack_forget()
        self.__rechercheFrame.pack_forget()
        self.__softFrame.pack_forget()
        self.__webFrame.pack_forget()
        self.__microFrame.pack_forget()
        self.__githubFrame.pack_forget()
        self.__windows.update()

    def __backAcceuil(self):
        self.__clearAll()
        self.__main_frame.pack()

    def passFNCQuit(self,fnc):
        self.__btn_back_assistant.configure(command=fnc)
        self.__btn_back_assistant.grid(row=self.__coordinated_btn_back[0],
                                       column=self.__coordinated_btn_back[1],
                                       padx=10, pady=10, sticky="nsew")

    def passFNCBTNIcon(self,fnc):
        self.__btn_icon.configure(command=fnc)
        self.__btn_icon.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def clearAllFrame(self):
        self.__clearAll()

    # Methode pour la partie general

    def __viewMainSetting(self):
        self.__clearAll()
        self.__main_setting_frame.pack()
        self.__backFrame.pack()
        self.__main_setting_welcome_frame.pack()
        self.__work_folder_frame.pack_forget()
        self.__download_folder_frame.pack_forget()
        self.__windows.update()

    def __viewWorkFolder(self):
        self.__main_setting_welcome_frame.pack_forget()
        self.__work_folder_frame.pack()
        self.__download_folder_frame.pack_forget()

        folder = self.__gestUser.getWorkFolder()
        if folder == "":
            self.__l_state_work_folder.configure(text="Dossier de travail\nnon configuré",justify="center")
            self.__btn_work_folder.configure(text="Configurer le dossier\nde travail\nArrera Work",
                                                 command=self.__addWorkFolder)
        else :
            self.__l_state_work_folder.configure(text=f"Emplacement du dossier de travail :\n{folder}",justify="center")
            self.__btn_work_folder.configure(text="Supprimer le dossier\nde travail\nArrera Work",
                                                 command=self.__delWorkFolder)

        self.__windows.update()

    def __addWorkFolder(self):
        if self.__gestUser.setWorkFolder():
            messagebox.showinfo("Paramètres","Le dossier de travail a bien été enregistré")

        self.__viewMainSetting()

    def __delWorkFolder(self):
        if self.__gestUser.removeWorkFolder():
            messagebox.showinfo("Paramètres","Le dossier de travail a bien été supprimé")

        self.__viewMainSetting()

    def __viewDownloadFolder(self):
        self.__main_setting_welcome_frame.pack_forget()
        self.__work_folder_frame.pack_forget()
        self.__download_folder_frame.pack()

        folder = self.__gestUser.getVideoDownloadFolder()
        if folder == "":
            self.__l_state_download_folder.configure(text="Dossier de téléchargement\nnon configuré",justify="center")
            self.__btn_download_folder.configure(text="Configurer le dossier\nde téléchargement",
                                             command=self.__addDownloadFolder)
        else :
            self.__l_state_download_folder.configure(text=f"Emplacement du dossier de téléchargement :\n{folder}",justify="center")
            self.__btn_download_folder.configure(text="Supprimer le dossier\nde téléchargement",
                                             command=self.__delDownloadFolder)

        self.__windows.update()

    def __addDownloadFolder(self):
        if self.__gestUser.setVideoDownloadFolder():
            messagebox.showinfo("Paramètres","Le dossier de téléchargement a bien été enregistré")

        self.__viewMainSetting()

    def __delDownloadFolder(self):
        if self.__gestUser.removeVideoDownloadFolder():
            messagebox.showinfo("Paramètres","Le dossier de téléchargement a bien été supprimé")

        self.__viewMainSetting()


    def __set_hist_state(self):
        b = bool(self.__btn_enable_hist.get())
        print(b)
        if self.__gestUser.setHist(b):
            messagebox.showinfo("Paramètres","L'état de l'historique a bien été enregistré")

        self.__initBtnEnableHist()

    # Methode pour la partie User
    def __viewUserAcceuil(self):
        self.__clearAll()
        self.__userName.pack_forget()
        self.__userGenre.pack_forget()
        self.__user_welcome_frame.pack()
        self.__user_frame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __viewUserName(self):
        self.__userName.pack()
        self.__userGenre.pack_forget()
        self.__user_welcome_frame.pack_forget()
        self.__windows.update()

    def __viewUserGenre(self):
        self.__userName.pack_forget()
        self.__userGenre.pack()
        self.__user_welcome_frame.pack_forget()
        self.__windows.update()

    def __saveUserName(self,eLast:aEntry,eFirst:aEntry):
        first = str(eFirst.get())
        last = str(eLast.get())
        if first == "":
            messagebox.showerror("Paramètres","Le prénom de l'utilisateur ne peut pas être vide")
            return
        else :
            if self.__gestUser.setFirstnameUser(first):
                messagebox.showinfo("Paramètres","Le prénom de l'utilisateur a bien été enregistré")
            eFirst.delete(0,END)

        if last == "":
            messagebox.showerror("Paramètres","Le nom de l'utilisateur ne peut pas être vide")
            return
        else :
            if self.__gestUser.setLastnameUser(last):
                messagebox.showinfo("Paramètres","Le nom de l'utilisateur a bien été enregistré")
            eLast.delete(0,END)

        self.__viewUserAcceuil()

    def __saveUserGenre(self,m:aOptionMenu):
        genre = m.getValue()
        if self.__gestUser.setGenre(genre):
            messagebox.showinfo("Paramètres","Le genre de l'utilisateur a bien été enregistré")
        self.__viewUserAcceuil()

    # Methode partie Meteo

    def __viewMeteoAcceuil(self):
        self.__clearAll()
        self.__meteoVille.pack_forget()
        self.__meteoTravail.pack_forget()
        self.__meteoDomicile.pack_forget()
        self.__meteoSuppr.pack_forget()
        self.__meteoAcceuil.pack()
        self.__meteoFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __viewMeteoDomicile(self):
        self.__entryMeteoDomicile.delete(0,END)
        self.__meteoDomicile.pack()
        self.__meteoTravail.pack_forget()
        self.__meteoVille.pack_forget()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack_forget()
        self.__windows.update()

    def __viewMeteoTravail(self):
        self.__entryMeteoTravail.delete(0, END)
        self.__meteoDomicile.pack_forget()
        self.__meteoTravail.pack()
        self.__meteoVille.pack_forget()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack_forget()
        self.__windows.update()

    def __viewMeteoVille(self):
        self.__entryMeteoVille.delete(0, END)
        self.__meteoDomicile.pack_forget()
        self.__meteoTravail.pack_forget()
        self.__meteoVille.pack()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack_forget()
        self.__windows.update()

    def __viewMeteoSuppr(self):
        listVille = self.__gestUser.getTowns()
        if len(listVille) == 0:
            messagebox.showerror("Erreur", "Aucune ville n'a été enregistrée")
            return
        self.__meteoDomicile.pack_forget()
        self.__meteoTravail.pack_forget()
        self.__meteoVille.pack_forget()
        self.__meteoAcceuil.pack_forget()
        self.__meteoSuppr.pack()
        del self.__menuMeteoSuppr
        self.__menuMeteoSuppr = aOptionMenu(self.__meteoSuppr,value = listVille)
        self.__menuMeteoSuppr.placeCenter()

    def __saveMeteoDomicile(self):
        domicile = self.__entryMeteoDomicile.get()
        if domicile == "":
            messagebox.showerror("Paramètres","Le lieu domicile ne peut pas être vide")
            return
        else :
            if self.__gestUser.setLieuDomicile(domicile):
                messagebox.showinfo("Paramètres","Le lieu domicile a bien été enregistré")
            self.__entryMeteoDomicile.delete(0,END)
            self.__viewMeteoAcceuil()

    def __saveMeteoTravail(self):
        travail = self.__entryMeteoTravail.get()
        if travail == "":
            messagebox.showerror("Paramètres","Le lieu travail ne peut pas être vide")
            return
        else :
            if self.__gestUser.setLieuTravail(travail):
                messagebox.showinfo("Paramètres","Le lieu travail a bien été enregistré")
            self.__entryMeteoTravail.delete(0,END)
            self.__viewMeteoAcceuil()

    def __saveMeteoVille(self):
        ville = self.__entryMeteoVille.get()
        if ville == "":
            messagebox.showerror("Paramètres","Le lieu ville ne peut pas être vide")
            return
        else :
            if self.__gestUser.addTown(ville):
                messagebox.showinfo("Paramètres","Le lieu ville a bien été enregistré")
            self.__entryMeteoVille.delete(0,END)
            self.__viewMeteoAcceuil()

    def __supprMeteoVille(self):
        ville = self.__menuMeteoSuppr.getValue()
        if ville == "":
            messagebox.showerror("Erreur","Aucune ville n'a été sélectionnée")
            return
        else :
            if self.__gestUser.removeTown(ville):
                messagebox.showinfo("Paramètres","Le lieu a bien été supprimé")
            self.__viewMeteoAcceuil()

    # Methode partie GPS

    def __viewGPSAcceuil(self):
        self.__clearAll()
        self.__gpsDomicile.pack_forget()
        self.__gpsTravail.pack_forget()
        self.__gpsAcceuil.pack()
        self.__gpsFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __viewGPSDomicile(self):
        self.__gpsDomicile.pack()

        self.__entryGPS[0].place_forget()
        self.__btnSupprGPS[0].place_forget()
        if self.__gestUser.getAdresseDomicile() == "":
            self.__entryGPS[0].delete(0,END)
            self.__entryGPS[0].placeCenter()
        else :
            self.__btnSupprGPS[0].placeCenter()


        self.__gpsTravail.pack_forget()
        self.__gpsAcceuil.pack_forget()
        self.__windows.update()

    def __viewGPSTravail(self):
        self.__gpsDomicile.pack_forget()
        self.__gpsTravail.pack()

        self.__entryGPS[1].place_forget()
        self.__btnSupprGPS[1].place_forget()
        if self.__gestUser.getAdresseTravail() == "":
            self.__entryGPS[1].delete(0,END)
            self.__entryGPS[1].placeCenter()
        else :
            self.__btnSupprGPS[1].placeCenter()

        self.__gpsAcceuil.pack_forget()
        self.__windows.update()

    def __saveGPSDomicile(self):
        domicile = self.__entryGPS[0].get()
        if domicile == "":
            messagebox.showerror("Paramètres","L'adresse de domicile ne peut pas être vide")
            return
        else :
            if self.__gestUser.setAdresseDomicile(domicile):
                messagebox.showinfo("Paramètres","L'adresse de domicile a bien été enregistrée")
            self.__entryGPS[0].delete(0,END)
            self.__viewGPSAcceuil()

    def __saveGPSTravail(self):
        travail = self.__entryGPS[1].get()
        if travail == "":
            messagebox.showerror("Paramètres","L'adresse de travail ne peut pas être vide")
            return
        else :
            if self.__gestUser.setAdresseTravail(travail):
                messagebox.showinfo("Paramètres","L'adresse de travail a bien été enregistrée")
            self.__entryGPS[1].delete(0,END)
            self.__viewGPSAcceuil()

    def __supprAdresseWork(self):
        if self.__gestUser.delAdresseTravail():
            messagebox.showinfo("Paramètres","L'adresse de travail a bien été supprimée")
        self.__viewGPSAcceuil()

    def __supprAdresseDomicile(self):
        if self.__gestUser.delAdresseDomicile():
            messagebox.showinfo("Paramètres","L'adresse de domicile a bien été supprimée")
        self.__viewGPSAcceuil()


    # Methode recherche

    def __viewRecherche(self):
        self.__clearAll()
        self.__rechercheFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __saveRecherche(self):
        if self.__gestUser.setMoteurRecherche(self.__mSearch.getValue()):
            messagebox.showinfo("Paramètres","Le moteur de recherche a bien été enregistré")
        self.__backAcceuil()
        self.__windows.update()

    # Methode soft

    def __viewSoftAcceuil(self):
        self.__clearAll()
        self.__softFrame.pack()
        self.__backFrame.pack()
        self.__softAcceuil.pack()
        self.__softAdd.pack_forget()
        self.__softSuppr.pack_forget()
        self.__softListe.pack_forget()
        self.__windows.update()

    def __viewSoftAdd(self):
        self.__softAcceuil.pack_forget()
        self.__softAdd.pack_forget()
        self.__softSuppr.pack_forget()
        self.__softAdd.pack()
        self.__eAddSoft.getEntry().delete(0,END)
        self.__windows.update()

    def __viewSoftSuppr(self):
        listSoft = list(self.__gestUser.getSoft().keys())
        if (len(listSoft) == 0):
            messagebox.showerror("Erreur", "Aucun logiciel n'a été enregistré")
            return
        self.__softAcceuil.pack_forget()
        self.__softAdd.pack_forget()
        self.__softSuppr.pack()
        del self.__menuSoftSuppr
        self.__menuSoftSuppr = aOptionMenu(self.__softSuppr,value = listSoft)
        self.__menuSoftSuppr.placeCenter()

    def __viewSoftList(self):
        self.__listSoftware.configure(state="normal")
        self.__listSoftware.delete(1.0, END)
        listSoft = list(self.__gestUser.getSoft().keys())
        if len(listSoft) == 0:
            messagebox.showerror("Erreur", "Aucun logiciel n'a été enregistré")
            return
        for i in range(0,len(listSoft)):
            self.__listSoftware.insert(END, listSoft[i] + "\n")
        self.__listSoftware.configure(state="disabled")
        self.__softAcceuil.pack_forget()
        self.__softSuppr.pack_forget()
        self.__softAdd.pack_forget()
        self.__softListe.pack()
        self.__windows.update()

    def __viewSoftSoft(self):
        self.__softAcceuil.pack_forget()
        self.__softAdd.pack()
        self.__softSuppr.pack_forget()
        self.__eAddSoft.delete(0, END)

    def __addSoft(self):
        soft = self.__eAddSoft.getEntry().get()
        if soft == "":
            messagebox.showerror("Erreur","Le nom du logiciel ne peut pas être vide")
            return
        else :
            if self.__gestUser.setSoft(soft):
                messagebox.showinfo("Paramètres","Le logiciel a bien été ajouté")
            self.__eAddSoft.getEntry().delete(0, END)
            self.__viewSoftAcceuil()

    def __supprSoft(self):
        soft = self.__menuSoftSuppr.getValue()
        if not self.__gestUser.removeSoft(soft):
            messagebox.showinfo("Paramètres", "Le logiciel n'a pas pu être supprimé.")
        else :
            messagebox.showinfo("Paramètres", "Le logiciel a bien été supprimé")
        self.__viewSoftAcceuil()

    # Methode internet

    def __viewInternetAcceuil(self):
        self.__clearAll()
        self.__webAddShortcut.pack_forget()
        self.__webDelShortcut.pack_forget()
        self.__webSavedShortcut.pack_forget()
        self.__webAcceuil.pack()
        self.__webFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __viewInternetSiteWeb(self):
        self.__entruWebSortCut[0].getEntry().delete(0,END)
        self.__entruWebSortCut[1].getEntry().delete(0,END)
        self.__webAddShortcut.pack()
        self.__webDelShortcut.pack_forget()
        self.__webAcceuil.pack_forget()
        self.__webSavedShortcut.pack_forget()
        self.__windows.update()

    def __viewInternetSupprSite(self):
        listSite = list(self.__gestUser.getSite().keys())
        if len(listSite) == 0:
            messagebox.showerror("Erreur", "Aucun site web n'a été enregistré")
            return
        self.__webAddShortcut.pack_forget()
        self.__webDelShortcut.pack()
        self.__webAcceuil.pack_forget()
        del self.__menuSiteWeb
        self.__menuSiteWeb = aOptionMenu(self.__webDelShortcut, value = listSite)
        self.__menuSiteWeb.placeCenter()

    def __viewInternetListeSite(self):
        listSite = list(self.__gestUser.getSite().keys())
        if len(listSite) == 0:
            messagebox.showerror("Erreur", "Aucun site web n'a été enregistré")
            return
        self.__webAddShortcut.pack_forget()
        self.__webDelShortcut.pack_forget()
        self.__webAcceuil.pack_forget()
        self.__listSite.configure(state="normal")
        self.__listSite.delete(1.0, END)
        for i in range(0,len(listSite)):
            self.__listSite.insert(END, listSite[i] + "\n")
        self.__listSite.configure(state="disabled")
        self.__webSavedShortcut.pack()

    def __saveSiteWeb(self):
        """
        :param mode: 1. Site web 2. Cloud Link
        :return:
        """
        name = self.__entruWebSortCut[0].getEntry().get()
        link = self.__entruWebSortCut[1].getEntry().get()

        if name == "" or link == "":
            messagebox.showerror("Erreur","Le nom ou le lien ne peut pas être vide")
            return
        else :
            if self.__gestUser.setSite(name,link):
                messagebox.showinfo("Paramètres","Le site web a bien été ajouté")
            self.__entruWebSortCut[0].getEntry().delete(0,END)
            self.__entruWebSortCut[1].getEntry().delete(0,END)
            self.__viewInternetAcceuil()

    def __supprSiteWeb(self):
        site = self.__menuSiteWeb.getValue()
        if self.__gestUser.removeSite(site):
            messagebox.showinfo("Paramètres", "Le site a bien été supprimé")
        self.__viewInternetAcceuil()

    # Methode Micro

    def __viewMicroAcceuil(self):
        self.__clearAll()
        self.__microFrame.pack()
        self.__backFrame.pack()
        self.__microAcceuil.pack()
        self.__microSound.pack_forget()
        self.__microTigerWord.pack_forget()
        self.__microVoicePrint.pack_forget()
        self.__microViewSave.pack_forget()
        self.__microViewWordSave.pack_forget()
        self.__windows.update()

    def __viewMicroSound(self):
        self.__microAcceuil.pack_forget()
        self.__microSound.pack()
        self.__microTigerWord.pack_forget()
        microEnable = self.__gestUser.getSoundMicro()
        if microEnable == "1":
            self.__btnMicroSoundChangeEtat.configure(text="Désactiver le son")
        else :
            self.__btnMicroSoundChangeEtat.configure(text="Activer le son")

    def __viewMicroTigerWord(self):
        self.__microAcceuil.pack_forget()
        self.__microSound.pack_forget()
        self.__microVoicePrint.pack_forget()
        self.__microViewSave.pack_forget()
        self.__microViewWordSave.pack_forget()

        self.__microTigerWord.pack()

        nbTriger = len(self.__gestUser.getListWord())

        self.__btnTrigerWordVoicePrint1.place_forget()
        self.__btnTrigerWordVoicePrint2.place_forget()
        self.__btnTrigerWordVoicePrint3.place_forget()

        if nbTriger == 0:
            self.__btnTrigerWordVoicePrint1.placeCenter()
        elif nbTriger == 1:
            self.__btnTrigerWordVoicePrint1.placeCenterLeft()
            self.__btnTrigerWordVoicePrint2.placeRightCenter()
        else :
            self.__btnTrigerWordVoicePrint1.placeCenterLeft()
            self.__btnTrigerWordVoicePrint2.placeCenter()
            self.__btnTrigerWordVoicePrint3.placeRightCenter()
        self.__windows.update()


    def __viewVoicePrint(self,mode:int):
        self.__microTigerWord.pack_forget()
        self.__microVoicePrint.pack()
        listWord = self.__gestUser.getListWord()
        nb = len(listWord)
        self.__btnSaveVoicePrint.place_forget()
        self.__btnSupprVoicePrint.place_forget()
        self.__btnViewVoicePrint.place_forget()
        match mode :
            case 1 :
                self.__labelVoicePrint.configure(text="Gestion empreinte vocale 1")
                if nb == 0:
                    self.__btnSaveVoicePrint.placeCenter()
                else :
                    self.__btnSupprVoicePrint.placeLeftCenter()
                    self.__btnViewVoicePrint.placeRightCenter()
                    self.__btnViewVoicePrint.configure(command=lambda : self.__viewSaveWord(1))
                    self.__btnSupprVoicePrint.configure(command=lambda :self.__supprTrigerWord(1))
            case 2 :
                self.__labelVoicePrint.configure(text="Gestion empreinte vocale 2")
                if nb == 1:
                    self.__btnSaveVoicePrint.placeCenter()
                else :
                    self.__btnSupprVoicePrint.placeLeftCenter()
                    self.__btnViewVoicePrint.placeRightCenter()
                    self.__btnViewVoicePrint.configure(command=lambda: self.__viewSaveWord(2))
                    self.__btnSupprVoicePrint.configure(command=lambda: self.__supprTrigerWord(2))
            case 3 :
                self.__labelVoicePrint.configure(text="Gestion empreinte vocale 3")
                if nb == 2:
                    self.__btnSaveVoicePrint.placeCenter()
                else :
                    self.__btnSupprVoicePrint.placeLeftCenter()
                    self.__btnViewVoicePrint.placeRightCenter()
                    self.__btnViewVoicePrint.configure(command=lambda: self.__viewSaveWord(3))
                    self.__btnSupprVoicePrint.configure(command=lambda: self.__supprTrigerWord(3))

    def __saveVoicePrint(self):
        self.__threadSaveVoicePrint = th.Thread(target=self.__recordTrigerWord)
        self.__threadSaveVoicePrint.start()
        self.__microTigerWord.pack_forget()
        self.__microVoicePrint.pack_forget()
        self.__microDuringSave.pack_forget()
        self.__microDuringSave.pack()
        self.__windows.update()
        self.__windows.after(100, self.__duringSaveVoicePrint)

    def __recordTrigerWord(self):
        self.__varOutTriger =  self.__arrVoice.listen()

        if self.__varOutTriger == 0 :
            self.__outTexteMicro = self.__arrVoice.getTextMicro()

    def __duringSaveVoicePrint(self):
        if self.__threadSaveVoicePrint.is_alive():
            self.__windows.after(100, self.__duringSaveVoicePrint)
            self.__windows.update()
        else:
            if self.__varOutTriger == 0:
                self.__microTigerWord.pack_forget()
                self.__microVoicePrint.pack_forget()
                self.__microDuringSave.pack_forget()
                self.__microViewSave.pack()
                self.__labelWordVoicePrint.configure(text="Mot enregistré : " + self.__outTexteMicro)
            else:
                self.__microVoicePrint.pack()
            self.__threadSaveVoicePrint = th.Thread()

    def __saveTigerWord(self):
        self.__viewMicroAcceuil()
        if self.__gestUser.addWord(self.__outTexteMicro):
            messagebox.showinfo("Paramètres","Le mot déclencheur a bien été enregistré.")

    def __viewSaveWord(self,mode:int):
        self.__microAcceuil.pack_forget()
        self.__microSound.pack_forget()
        self.__microTigerWord.pack_forget()
        self.__microVoicePrint.pack_forget()
        self.__microViewSave.pack_forget()
        self.__microViewWordSave.pack()
        self.__windows.update()

        word = self.__gestUser.getListWord()[mode-1]
        self.__labelWordViewSave.configure(text="Le mot enregistré est : "+word)

    def __supprTrigerWord(self,mode:int):
        self.__viewMicroAcceuil()

        word = self.__gestUser.getListWord()[mode-1]

        if not self.__gestUser.removeWord(word):
            messagebox.showinfo("Paramètres", "Le mot déclencheur n'a pas pu être supprimé.")

    def __changeMicroSound(self):
        microEnable = self.__gestUser.getSoundMicro()
        if microEnable == "1":
            self.__gestUser.setSoundMicro(False)
        else :
            self.__gestUser.setSoundMicro(True)
        self.__viewMicroAcceuil()

    def gettigerWordSet(self):
        nb = len(self.__gestUser.getListWord())
        if (nb == 0):
            return False
        else :
            return True

    # Methode IA

    def __viewIAAcceuil(self):
        self.__clearAll()
        self.__iaAcceuil.pack()
        self.__iaDownload.pack_forget()
        self.__iaChoose.pack_forget()
        self.__duringDownloadModel.pack_forget()
        self.__iaFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __viewIAChoose(self):
        self.__clearAll()
        self.__iaAcceuil.pack_forget()
        self.__iaDownload.pack_forget()

        listModel = self.__gestUser.get_model_downloaded()
        if len(listModel) == 0:
            messagebox.showerror("Erreur", "Aucun modèle n'a été téléchargé")
            self.__viewIAAcceuil()

        del self.__menuChooseIAModel
        self.__menuChooseIAModel = aOptionMenu(self.__iaChoose,value = listModel)
        self.__menuChooseIAModel.placeCenter()

        self.__iaChoose.pack()
        self.__iaFrame.pack()
        self.__duringDownloadModel.pack_forget()
        self.__backFrame.pack()
        self.__windows.update()

    def __setModelToUse(self):
        model = self.__menuChooseIAModel.getValue()
        if self.__gestUser.set_ia_model(model):
            messagebox.showinfo("Paramètres","Le modèle a bien été enregistré")
        self.__initBtnEnableIAMode()
        self.__viewIAAcceuil()

    def __getStateIAMode(self):
        if self.__gestUser.get_use_ia() == 1 :
            return True
        else :
            return False

    def __viewDownloadIA(self):
        self.__clearAll()
        self.__iaAcceuil.pack_forget()
        self.__iaChoose.pack_forget()

        self.__iaDownload.pack()

        for widget in self.__downloadIA.winfo_children():
            widget.destroy()

        listModel = self.__gestUser.get_list_model_ia_available()
        modelDownloader = self.__gestUser.get_model_downloaded()

        for i in listModel:
            if i not in modelDownloader:
                self.__availableDownloadModel(i)

        self.__iaFrame.pack()
        self.__backFrame.pack()
        self.__duringDownloadModel.pack_forget()
        self.__windows.update()

    def __availableDownloadModel(self,model:str):
        modelData = self.__gestUser.get_data_model_ia_available(model)
        l = aFrame(self.__downloadIA,fg_color="#DFE2EB")
        l.pack(fill="x", padx=5, pady=2)

        title = aLabel(l,text=f"{modelData[0]}\n({model})",police_size=25,justify="left")
        title.grid(row=0, column=0, sticky="w")

        d = aLabel(l,text=modelData[2],wraplength=300,justify="left")
        d.grid(row=1, column=0, sticky="w")

        btn = aButton(l,text="Télécharger",command=lambda:self.__downloadModel(model))
        btn.placeRightCenter()

    def __downloadModel(self,model:str):

        self.__theardDownloadModel = th.Thread(target=self.__gestUser.download_ia_model,args=(model,))

        self.__duringDownloadModel.pack()
        self.__iaAcceuil.pack_forget()
        self.__iaDownload.pack_forget()
        self.__iaChoose.pack_forget()
        self.__iaFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

        self.__theardDownloadModel.start()

        self.__windows.after(100,self.__updateDownloadModel)


    def __updateDownloadModel(self):
        if self.__theardDownloadModel.is_alive():
            self.__windows.after(100,self.__updateDownloadModel)
            self.__windows.update()
        else :
            messagebox.showinfo("Paramètres","Le modèle a bien été téléchargé")
            self.__viewIAAcceuil()


    def __set_enable_ia_mode(self):
        v = bool(self.__btnEnableIA.getValue())
        self.__gestUser.set_use_ia(v)

    # Partie github

    def __viewGithub(self):
        self.__clearAll()

        if self.__gestUser.getTokenGithub() == "":
            self.__btnToken.configure(text="Enregistrer le token\nGitHub",
                                      command=self.__viewAddTokenGithub)
        else :
            self.__btnToken.configure(text="Supprimer le token\nGitHub",
                                      command=self.__delToken)

        self.__githubAcceuil.pack()
        self.__githubFrame.pack()
        self.__githubToken.pack_forget()
        self.__backFrame.pack()
        self.__windows.update()

    def __viewAddTokenGithub(self):
        v = messagebox.askyesno("Paramètres","Avez-vous généré le token GitHub ?")
        if not v :
            webbrowser.open("https://github.com/settings/tokens/new")

        self.__githubAcceuil.pack_forget()
        self.__githubToken.pack()
        self.__githubFrame.pack()
        self.__backFrame.pack()
        self.__windows.update()

    def __saveToken(self):
        token = self.__eToken.getEntry().get()
        if token == "":
            messagebox.showerror("Erreur","Le token ne peut pas être vide")
        else :
            if self.__gestUser.setTokenGithub(token):
                messagebox.showinfo("Paramètres","Le token a bien été enregistré")

        self.__eToken.getEntry().delete(0,END)
        self.__viewGithub()

    def __delToken(self):
        if self.__gestUser.delTokenGithub():
            messagebox.showinfo("Paramètres","Le token GitHub a bien été supprimé")
        self.__viewGithub()