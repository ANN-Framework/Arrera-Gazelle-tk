from fnc.fncBase import fncBase,gestionnaire
import pyperclip

class fncOrthographe(fncBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire)
        self.__tool_launched = False
        self.__gest_ia = None
        if gestionnaire.getUserConf().get_use_ia():
            self.__tool_launched = True
            self.__gest_ia = gestionnaire.getGestIA()

        self.__text_no_corrected = None
        self.__text_corrected = None

    def corrected_text(self,texte:str):
        if self.__tool_launched:
            if texte == "":
                return False

            if self.__gest_ia.load_help("orthographe"):
                self.__text_no_corrected = texte

                if self.__gest_ia.correted_text(self.__text_no_corrected):
                    self.__text_corrected = self.__gest_ia.get_reponse_ia()
                    return True
                else :
                    return False

            else:
                return False

        else :
            return False

    def getCorrections(self):
        return self.__text_corrected

    def get_text_no_corrected(self):
        return self.__text_no_corrected

    def copyCorrections(self):
        if not self.__tool_launched:
            return False
        if self.__text_corrected is None:
            return False
        try :
            pyperclip.copy(self.__text_corrected)
            return True
        except Exception as e:
            return False

    def getToolLaunched(self):
        return self.__tool_launched