from gestionnaire.gestion import gestionnaire


class gestGUI:
    def __init__(self, gest: gestionnaire):
        self.__name_gui = None
        self.__gest = gest
        self.__parms = None
        self.__textOut = None
        self.__valOut = 0
        
        # Importation des GUI
        from gui.GUICalculatrice import GUICalculatrice
        from gui.GUIorthographe import GUIOrthographe
        from gui.GUIArreraDownload import GUIArreraDownload
        from gui.GUIAgenda import GUIAgenda
        from gui.GUIHorloge import GUIHorloge
        from gui.GUILecture import GUILecture
        from gui.GUITache import GUITache
        from gui.GUIArreraWork import GUIWork
        from gui.GUITraducteur import GuiTraducteur
        from gui.GUIViewResumer import GUIViewResumer
        from gui.GUIHelp import GUIHelp
        from gui.GUIViewBreef import GUIViewBreef

        # Calculatrice
        self.__guiCalculatrice = GUICalculatrice(self.__gest)
        # Correcteur d'orthographe
        self.__guiOrthographe = GUIOrthographe(self.__gest)
        # Arrera Download
        self.__guiArreraDownload = GUIArreraDownload(self.__gest)
        # Agenda
        self.__guiAgenda = GUIAgenda(self.__gest)
        # Horloge
        self.__guiHorloge = GUIHorloge(self.__gest)
        # Lecture
        self.__guiLecture = GUILecture(self.__gest)
        # Tâche
        self.__guiTache = GUITache(self.__gest)
        # Work
        self.__guiWork = GUIWork(self.__gest)
        # Traducteur
        self.__guiTraducteur = GuiTraducteur(self.__gest)
        # Resumer
        self.__guiResumer = GUIViewResumer(self.__gest)
        # Aide
        self.__guiHelp = GUIHelp(self.__gest)
        # Breef
        self.__guiBreef = GUIViewBreef(self.__gest)

        # Dictionnaire des actions
        self.__gui_actions = {
            "calculatrice_normal": lambda: self.__generic_try_action(
                self.__guiCalculatrice.activeCalcule,
                lambda: self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("7"),
                lambda: self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("8")
            ),
            "calculatrice_pythagore": lambda: self.__generic_try_action(
                self.__guiCalculatrice.activePythagore,
                lambda: self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("5"),
                lambda: self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("6")
            ),
            "calculatrice_complex": lambda: self.__generic_try_action(
                self.__guiCalculatrice.activeComplex,
                lambda: self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("3"),
                lambda: self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("4")
            ),
            "orthographe": self.__action_orthographe,
            "arrera_download": lambda: self.__generic_try_action(
                self.__guiArreraDownload.active,
                lambda: self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("1"),
                lambda: self.__gest.getLanguageObjet().getPhraseArreraSoftOpen("2")
            ),
            "agenda": lambda: self.__generic_action(
                self.__guiAgenda.active,
                lambda: self.__gest.getLanguageObjet().getPhraseTime("8")
            ),
            "agenda_add": lambda: self.__generic_action(
                self.__guiAgenda.activeAdd,
                lambda: self.__gest.getLanguageObjet().getPhraseTime("4")
            ),
            "agenda_delete": lambda: self.__generic_action(
                self.__guiAgenda.activeDel,
                lambda: self.__gest.getLanguageObjet().getPhraseTime("5")
            ),
            "horloge": lambda: self.__generic_action(
                self.__guiHorloge.active,
                lambda: self.__gest.getLanguageObjet().getPhraseTime("2")
            ),
            "minuteur": lambda: self.__generic_action(
                self.__guiHorloge.activeMinuteur,
                lambda: self.__gest.getLanguageObjet().getPhraseTime("3")
            ),
            "chrono": lambda: self.__generic_action(
                self.__guiHorloge.activeChrono,
                lambda: self.__gest.getLanguageObjet().getPhraseTime("1")
            ),
            "lecture": lambda: self.__generic_action(
                self.__guiLecture.active,
                lambda: self.__gest.getLanguageObjet().getPhraseService("6")
            ),
            "tache": lambda: self.__generic_action(
                self.__guiTache.active,
                lambda: self.__gest.getLanguageObjet().getPhraseTime("9")
            ),
            "tache_finish": lambda: self.__generic_action(
                self.__guiTache.activeFinish,
                lambda: self.__gest.getLanguageObjet().getPhraseTime("11")
            ),
            "tache_del": lambda: self.__generic_action(
                self.__guiTache.activeDel,
                lambda: self.__gest.getLanguageObjet().getPhraseTime("12")
            ),
            "work": lambda: self.__generic_try_action(
                self.__guiWork.activeAcceuil,
                lambda: self.__gest.getLanguageObjet().getPhraseOpenGUIWork("7"),
                lambda: self.__gest.getLanguageObjet().getPhraseOpenGUIWork("8")
            ),
            "work_projet": lambda: self.__generic_try_action(
                self.__guiWork.activeProjet,
                lambda: self.__gest.getLanguageObjet().getPhraseOpenGUIWork("1"),
                lambda: self.__gest.getLanguageObjet().getPhraseOpenGUIWork("2")
            ),
            "work_tableur": lambda: self.__generic_try_action(
                self.__guiWork.activeTableur,
                lambda: self.__gest.getLanguageObjet().getPhraseOpenGUIWork("3"),
                lambda: self.__gest.getLanguageObjet().getPhraseOpenGUIWork("4")
            ),
            "work_manage_tableur": lambda: self.__guiManageTableur(self.__parms),
            "work_read_tableur": lambda: self.__generic_bool_action(
                self.__guiWork.active_read_tableur,
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("21"),
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("22")
            ),
            "work_word": lambda: self.__generic_try_action(
                self.__guiWork.activeWord,
                lambda: self.__gest.getLanguageObjet().getPhraseOpenGUIWork("5"),
                lambda: self.__gest.getLanguageObjet().getPhraseOpenGUIWork("6")
            ),
            "work_word_read": lambda: self.__generic_try_action(
                self.__guiWork.active_read_word,
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkWord("9"),
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkWord("10")
            ),
            "work_word_write": lambda: self.__generic_try_action(
                self.__guiWork.active_write_word,
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkWord("7"),
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkWord("8")
            ),
            "tache_projet": lambda: self.__generic_bool_action(
                self.__guiWork.open_task_projet,
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("10", self.__gest.getGestFNC().getFNCWork().getNameProjet()),
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("11")
            ),
            "tache_projet_add": lambda: self.__generic_bool_action(
                self.__guiWork.open_task_projet_add,
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("12", self.__gest.getGestFNC().getFNCWork().getNameProjet()),
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("13")
            ),
            "tache_projet_del": lambda: self.__generic_bool_action(
                self.__guiWork.open_task_projet_del,
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("14", self.__gest.getGestFNC().getFNCWork().getNameProjet()),
                lambda: self.__gest.getLanguageObjet().getPhraseArreraWorkProjet("15")
            ),
            "traducteur": lambda: self.__generic_action(
                self.__guiTraducteur.active,
                lambda: self.__gest.getLanguageObjet().getPhraseOpenTraducteur()
            ),
            "resumer": self.__action_resumer,
            "aide": self.__action_aide,
            "breef": lambda: self.__generic_action(
                self.__guiBreef.activeBreef,
                lambda: self.__gest.getLanguageObjet().getPhraseMorningBreef("1")
            )
        }

    def setGUIActive(self, gui: str, parms=None):
        if gui in self.__gui_actions:
            self.__name_gui = gui
            self.__parms = parms
            return True
        else:
            return False

    def launch_gui(self):
        if self.__name_gui in self.__gui_actions:
            return self.__gui_actions[self.__name_gui]()
        return False

    def __generic_try_action(self, action, success_msg_provider, fail_msg_provider):
        try:
            action()
            self.__textOut = success_msg_provider()
            self.__valOut = 5
            return True
        except Exception:
            self.__textOut = fail_msg_provider()
            self.__valOut = 1
            return False

    def __generic_action(self, action, success_msg_provider):
        action()
        self.__textOut = success_msg_provider()
        self.__valOut = 5
        return True

    def __generic_bool_action(self, action, success_msg_provider, fail_msg_provider):
        if action():
            self.__textOut = success_msg_provider()
            self.__valOut = 5
            return True
        else:
            self.__textOut = fail_msg_provider()
            self.__valOut = 1
            return False

    def __action_orthographe(self):
        if self.__parms != "" and self.__gest.getGestFNC().getFNCOrthographe().getToolLaunched():
            self.__guiOrthographe.active()
            self.__guiOrthographe.setTexte(self.__parms)
            self.__textOut = self.__gest.getLanguageObjet().getPhraseService("3")
            self.__valOut = 5
            return True
        else:
            self.__textOut = self.__gest.getLanguageObjet().getPhraseService("4")
            self.__valOut = 1
            return False

    def __action_resumer(self):
        dicte = self.__parms[0]
        liste = self.__parms[1]
        intIn = self.__parms[2]
        self.__guiResumer.activeView(dict=dicte, list=liste, intIn=intIn)
        self.__textOut = self.__parms[3]
        self.__valOut = 5
        return True

    def __action_aide(self):
        self.__guiHelp.activeHelp(self.__parms[0])
        self.__textOut = self.__parms[1]
        self.__valOut = 5
        return True

    def __guiManageTableur(self, param: int):
        try:
            out = self.__guiWork.active_manage_tableur()
        except Exception:
            self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("8")
            self.__valOut = 1
            return False

        if 1 <= param <= 7:
            if out:
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur(str(5 + param * 2))
                self.__valOut = 5
                return True
            else:
                self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur(str(6 + param * 2))
                self.__valOut = 1
                return False
        else:
            self.__textOut = self.__gest.getLanguageObjet().getPhraseArreraWorkTableur("8")
            self.__valOut = 1
            return False

    def textOut(self):
        return self.__textOut

    def activeAgenda(self):
        self.__guiAgenda.active()

    def activeTache(self):
        self.__guiTache.active()

    def activeViewResumer(self, dict: dict = None, list: list = None, intIn: int = 0):
        self.__guiResumer.activeView(dict=dict, list=list, intIn=intIn)

    def activeHelp(self, texte: str):
        self.__guiHelp.activeHelp(texte)

    def activeBreef(self):
        self.__guiBreef.activeBreef()
