from gestionnaire.gestion import gestionnaire

class gestFNC:
    def __init__(self, gestionnaire: gestionnaire):
        # Import
        # Fichier de fonction
        from fnc.fonctionTache import fncArreraTache, CArreraDate
        from fnc.fonctionRecherche import fncArreraSearch
        from fnc.fonctionArreraDownload import fncArreraVideoDownload
        from fnc.fonctionCalendar import fncCalendar
        from fnc.fonctionGPS import fncGPS
        from fnc.fonctionMeteo import fncMeteo
        from fnc.fonctionActu import fncActualiter
        from fnc.fonctionHorloge import fncHorloge
        from fnc.fonctionLecture import fncLecture
        from fnc.fonctionRadio import fncRadio
        from fnc.fonctionTraduction import fncTraduction
        from fnc.fonctionOrthographe import fncOrthographe
        from fnc.fonctionCalculatrice import fncCalculatrice
        from fnc.fonctionCodeHelp import fncCodehelp
        from fnc.fonctionArreraWork import fncArreraWork
        from fnc.fonctionBreef import fncBreef
        from fnc.fonctionOPEN import fonctionOpen
        # Fichier de GUI

        # ______________ Initialisation des fonctions ______________
        self.__gestionnaire = gestionnaire

        # Librairy
        self.__libDate = CArreraDate()
        # Fonction de tache
        self.__taskAssistant = fncArreraTache(self.__gestionnaire,
                                              self.__libDate,
                                              self.__gestionnaire.getEmplacemntfileTache())
        # Fonction de recherche
        self.__searchAssistant = fncArreraSearch(self.__gestionnaire)
        # Fonction de telechargement de video youtube
        self.__downloaderYoutube = fncArreraVideoDownload(self.__gestionnaire)
        # Fonction Agenda
        self.__calendar = fncCalendar(self.__gestionnaire)
        # Fonction GPS
        self.__gps = fncGPS(self.__gestionnaire)
        # Fonction Meteo
        self.__meteo = fncMeteo(self.__gestionnaire,self.__gps)
        # Fonction Actualité
        self.__actu = fncActualiter(self.__gestionnaire,"3b43e18afcf945888748071d177b8513")
        # Fonction horloge
        self.__horloge = fncHorloge(self.__gestionnaire)
        # Fonction de lecture
        self.__read = fncLecture(self.__gestionnaire)
        # Fonction de radio
        self.__radio = fncRadio(self.__gestionnaire)
        # Fonction de traduction
        self.__traduction = fncTraduction(self.__gestionnaire)
        # Fonction d'orthographe
        self.__orthographe = fncOrthographe(self.__gestionnaire)
        # Fonction de calculatrice
        self.__calculatrice = fncCalculatrice(self.__gestionnaire)
        # Fonction de code help
        self.__codehelp = fncCodehelp(self.__gestionnaire)
        # Fonction work
        self.__work = fncArreraWork(self.__gestionnaire)
        # Fonction breef
        self.__breef = fncBreef(self.__gestionnaire)
        # Fonction open
        self.__open = fonctionOpen(self.__gestionnaire)

    def initTaskProject(self, fileTask: str):
        # Initialisation des fonctions
        from fnc.fonctionTache import fncArreraTache
        return fncArreraTache(self.__gestionnaire,self.__libDate,fileTask)

    def getFNCTask(self):
        return self.__taskAssistant

    def getFNCSearch(self):
        return self.__searchAssistant

    def getFNCDownload(self):
        return self.__downloaderYoutube

    def getFNCCalendar(self):
        return self.__calendar

    def getFNCGPS(self):
        return self.__gps

    def getFNCMeteo(self):
        return self.__meteo

    def getFNCActu(self):
        return self.__actu

    def getFNCHorloge(self):
        return self.__horloge

    def getFNCRead(self):
        return self.__read

    def getFNCRadio(self):
        return self.__radio

    def getFNCTraduction(self):
        return self.__traduction

    def getFNCOrthographe(self):
        return self.__orthographe

    def getFNCCalculatrice(self):
        return self.__calculatrice

    def getFNCCodeHelp(self):
        return self.__codehelp

    def getFNCWork(self):
        return self.__work

    def getFNCBreef(self):
        return self.__breef

    def getFNCOpen(self):
        return self.__open