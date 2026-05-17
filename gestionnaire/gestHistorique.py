from librairy.travailJSON import *
from gestionnaire.gestion import gestionnaire
import os
from datetime import date,timedelta

DICTHIST = {}
LICTACTION = [
    "open_soft",
    "open_website",
    "open_mode",
    "close_mode",
    "open_project",
    "close_project"
]

class gestHistorique :
    def __init__(self,gestionnaire:gestionnaire):

        self.__contentHist = {}
        self.__todayHist = []
        self.__yesterdayHist = []

        self.__gestionnaire = gestionnaire

        self.__osDect = gestionnaire.getOSObjet()

        if self.__osDect.osLinux() or self.__osDect.osMac():
            home = os.path.expanduser("~")
            self.__histFilePath = str(home)+"/.config/arrera-assistant/user-hist.json"
        elif self.__osDect.osWindows():
            home = os.path.join(os.path.expanduser("~"), "AppData", "Roaming")
            self.__histFilePath = str(home) + "/arrera-assistant/user-hist.json"
        else :
            self.__userSettingPath = None

        if not os.path.isfile(self.__histFilePath):
            os.makedirs(os.path.dirname(self.__histFilePath), exist_ok=True)
            with open(self.__histFilePath, "x", encoding="utf-8") as f:
                json.dump(DICTHIST, f, ensure_ascii=False, indent=2)

        self.__fileHist = jsonWork(self.__histFilePath)

    def __load(self):
        try :
            self.__contentHist = self.__fileHist.getJSONDict()
            self.__fileHist.setDictOnJson(DICTHIST)
            return True
        except Exception as e :
            self.__contentHist = DICTHIST
            return False

    def saveHist(self):
        try :
            self.__fileHist.setDictOnJson({str(date.today()):self.__todayHist})
            return True
        except Exception as e :
            return False

    def loadHist(self):
        listStart = []
        if self.__load():
            today = str(date.today())
            yesterday = str(date.today() - timedelta(days=1))

            self.__todayHist = self.__contentHist.get(today,[])

            self.__yesterdayHist = self.__contentHist.get(yesterday,[])

            if self.__todayHist:
                for hist in self.__todayHist:
                    listStart = self.__testAction(hist,self.__todayHist,listStart)

            self.__todayHist = []
            if listStart:
                return True
            else :
                return False
        return None

    def __testAction(self,hist:str,listAction:list,listStart:list):
        listStart = listStart
        if "open_soft" in hist:
            soft = hist.replace("open_soft","").replace(":","").strip()
            if not str("soft" + soft) in listStart:
                self.__gestionnaire.getGestFNC().getFNCOpen().openSoft(soft)
                listStart.append("soft" + soft)
        elif "open_website" in hist:
            site = hist.replace("open_website","").replace(":","").strip()
            if not str("site" + site) in listStart:
                self.__gestionnaire.getGestFNC().getFNCOpen().openSaveWebSite(site)
                listStart.append("site" + site)
        elif "open_mode" in hist:
            mode = hist.replace("open_mode","").replace(":","").strip()
            if not str("mode" + mode) in listStart and not str("close_mode "+mode) in listAction:
                print(self.__gestionnaire.getSocketObjet().send_data_with_clien("launch " + mode))
                listStart.append("mode" + mode)
        elif "open_project" in hist:
            project = hist.replace("open_project","").replace(":","").strip()
            if not str("project" + project) in listStart and not str("close_project "+project) in listAction:
                self.__gestionnaire.getGestFNC().getFNCWork().openProjet(project)
                listStart.append("project" + project)

        return listStart


    def add_action(self,type:str,action:str):
        """
        :param type:
            - open_soft
            - open_website
            - open_mode
            - close_mode
            - open_project
            - close_project
        :param action:
        :return:
        """
        if type not in LICTACTION:
            return False
        if not action:
            return False

        self.__todayHist.append(type + " : " + action)
        return True