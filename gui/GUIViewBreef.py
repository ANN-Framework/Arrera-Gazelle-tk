import threading
from tkinter.messagebox import showerror
import threading as th
from gui.guibase import GuiBase,gestionnaire
from librairy.arrera_tk import *

class GUIViewBreef(GuiBase):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Breef")
        self.__readVar = ""
        self.__out_breef = None
        self.__thRead = th.Thread()
        self.__thLoad = th.Thread()

    def _mainframe(self):
        # Configuration de la fenetre
        self._screen.grid_rowconfigure(0, weight=1)
        self._screen.grid_columnconfigure(0, weight=1)
        # Frame
        self.__main_frame = aFrame(self._screen)

        self.__load_frame = aFrame(self._screen)

        weatherFrame = aFrame(self.__main_frame)
        alertFrame = aFrame(weatherFrame)

        tasksContainer = aFrame(self.__main_frame,fg_color=self.__main_frame.cget("fg_color"))
        taskFrame = aFrame(tasksContainer,fg_color=weatherFrame.cget("fg_color"))
        taskProjectFrame = aFrame(tasksContainer,fg_color=weatherFrame.cget("fg_color"))

        # Configuration
        self.__main_frame.grid_columnconfigure(0, weight=1)
        self.__main_frame.grid_rowconfigure(0, weight=0)
        self.__main_frame.grid_rowconfigure(1, weight=0)
        self.__main_frame.grid_rowconfigure(2, weight=1)
        self.__main_frame.grid_rowconfigure(3, weight=0)
        self.__main_frame.grid_rowconfigure(4, weight=0)

        self.__load_frame.grid_rowconfigure(0, weight=1)
        self.__load_frame.grid_columnconfigure(0, weight=1)

        weatherFrame.rowconfigure(0, weight=1)
        weatherFrame.rowconfigure(1, weight=1)
        weatherFrame.rowconfigure(2, weight=1)
        weatherFrame.columnconfigure(0, weight=1)
        weatherFrame.columnconfigure(1, weight=1)
        weatherFrame.columnconfigure(2, weight=1)

        alertFrame.columnconfigure(0, weight=1)
        alertFrame.rowconfigure(0, weight=1)
        alertFrame.rowconfigure(1, weight=1)
        alertFrame.rowconfigure(2, weight=1)

        taskFrame.columnconfigure(0, weight=1)
        taskFrame.rowconfigure(1, weight=1)

        taskProjectFrame.columnconfigure(0, weight=1)
        taskProjectFrame.rowconfigure(1, weight=1)

        tasksContainer.grid_columnconfigure(0, weight=1, uniform="tasks")
        tasksContainer.grid_columnconfigure(1, weight=1, uniform="tasks")
        tasksContainer.grid_rowconfigure(0, weight=1)

        # Widgets
        labelTitle = aLabel(self.__main_frame,text=self._gestionnaire.getName()+" : Breef",police_size=35)
        btnRead = aButton(self.__main_frame,text="Lire",size=25,command=self.__readBreef)

        # Load
        label_load = aLabel(self.__load_frame,text="Chargement du breef en cours...",police_size=25)

        # Meteo
        self.__labelLogoMeteo = aLabel(weatherFrame,text="Logo")

        self.__lnameTown = aLabel(weatherFrame,text="Ville",justify="left",police_size=25)
        self.__ltemp = aLabel(weatherFrame,text="Temperature",justify="left",police_size=25)
        self.__lweather = aLabel(weatherFrame,text="description",justify="left",police_size=25)

        self.__lAlertRed = aLabel(alertFrame,text="Alerte",justify="left",police_size=25)
        self.__lAlertOrange = aLabel(alertFrame,text="Alerte",justify="left",police_size=25)
        self.__lAlertYellow = aLabel(alertFrame,text="Alerte",justify="left",police_size=25)
        self.__lNoAlert = aLabel(alertFrame,text="Aucune d'alerte",justify="left",police_size=25)

        # Task
        lTitleTask = aLabel(taskFrame,text="Tâches du jour",police_size=30)
        self.__fViewTask = aScrollableFrame(taskFrame)

        lTitleTaskProject = aLabel(taskProjectFrame,text="Tâches sur les projets",police_size=30)
        self.__fViewTaskProject = aScrollableFrame(taskProjectFrame)
        # Placement
        labelTitle.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        weatherFrame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        tasksContainer.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        btnRead.grid(row=4, column=0, sticky="ew", padx=10, pady=(5, 10))

        taskFrame.grid(row=0, column=0, sticky="nsew", padx=(0, 5), pady=0)
        taskProjectFrame.grid(row=0, column=1, sticky="nsew", padx=(5, 0), pady=0)

        alertFrame.grid(row=0, column=2, sticky="ne", padx=(4, 8), pady=(8, 2))
        self.__labelLogoMeteo.grid(row=0, column=0, sticky="nw", padx=(8, 4), pady=(8, 2))
        self.__lnameTown.grid(row=1, column=0, sticky="w", padx=(8, 4), pady=(2, 8))
        self.__ltemp.grid(row=1, column=1, sticky="", padx=4, pady=4)
        self.__lweather.grid(row=2, column=2, sticky="se", padx=(4, 8), pady=(2, 8))

        lTitleTask.grid(row=0, column=0, sticky="n", pady=(10, 6))
        self.__fViewTask.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

        lTitleTaskProject.grid(row=0, column=0, sticky="n", pady=(10, 6))
        self.__fViewTaskProject.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

        label_load.grid(row=0, column=0)

    def activeBreef(self):
        self.active()
        self.__load_frame.grid(row=0, column=0, sticky="nsew")
        self.__thLoad = threading.Thread(target=self.__load_breef)
        self.__thLoad.start()
        self._screen.update()
        self._screen.after(100, self.__update_during_load_breef)

    def __load_breef(self):
        self.__out_breef = self._gestionnaire.getGestFNC().getFNCBreef().morningBreef()

    def __update_during_load_breef(self):
        if self.__thLoad.is_alive():
            self._screen.update()
            self._screen.after(100,self.__update_during_load_breef)
        else :
            self._screen.update()
            if self.__out_breef is None:
                showerror("Erreur", "Impossible de charger le breef du jour")
                self._screen.destroy()
            else:
                self.__load_frame.grid_forget()
                self.__main_frame.grid(row=0, column=0, sticky="nsew")

                self.__selectMeteo(self.__out_breef)
                self.__setTask(self.__fViewTask, self.__out_breef["task"])
                self.__setReadForTask(self.__out_breef["task"])
                self.__setTaskProjet(self.__out_breef["tacheProjet"])


    def __setTask(self,frame:ctk.CTkFrame,listTask:list):

        for w in frame.winfo_children():
            w.destroy()

        if len(listTask) != 0:
            for i,task in enumerate(listTask):
                ltask = aLabel(frame,text=f"- {task}",justify="left")
                ltask.grid(row=i, column=0, sticky="w", padx=8, pady=4)
        else:
            ltask = aLabel(frame,text="Aucune tâche à faire !",justify="left")
            ltask.grid(row=0, column=0, sticky="w", padx=8, pady=4)

    def __setTaskProjet(self,taskProject:dict):
        listTask = []
        listKey = list(taskProject.keys())
        for key in listKey:
            for tache in taskProject[key]:
                listTask.append(f"{tache} (Projet : {key})")
        self.__setTask(self.__fViewTaskProject,listTask)
        if len(listTask) != 0:
            if len(listTask) == 1:
                self.__readVar += f"Tu as une tâche à faire sur tes projets qui est {listTask[0]}."
            else :
                self.__readVar += f"Tu as {len(listTask)} tâches à faire sur tes projets. qui sont "
                for i,task in enumerate(listTask):
                    if i == 0:
                        self.__readVar += task
                    elif i == len(listTask)-1:
                        self.__readVar += f" et {task}."
                    else:
                        self.__readVar += f", {task}"

    def __selectMeteo(self,out:dict):
        meteoDict = out["meteo"]
        self.__lnameTown.configure(text=meteoDict["ville"])
        self.__ltemp.configure(text=str(meteoDict["temperature"])+"°C")
        self.__lweather.configure(text=meteoDict["weather"])

        self.__readVar = f"La meteo à {meteoDict["ville"]} est {meteoDict["weather"]} avec une temperature de {meteoDict["temperature"]}°C. "

        try :
            imgMeteo = aImage(path_light=meteoDict["icon"],width=100,height=100)
            self.__labelLogoMeteo.configure(image=imgMeteo,text="")
        except Exception as e:
            imgMeteo = aImage(path_light=self._gestionnaire.getConfigFile().asset+"meteo/meteo-error.png",
                              width=100, height=100)
            self.__labelLogoMeteo.configure(image=imgMeteo,text="")

        self.__lNoAlert.grid(row=1, column=0, sticky="ew", padx=8, pady=4)

        if meteoDict["redAlert"]:
            listAlterte = meteoDict["redAlert"]
            for i in range(len(listAlterte)):
                if i == 0:
                    self.__lAlertRed.configure(text=listAlterte[i])
                else:
                    self.__lAlertRed.configure(text=self.__lAlertRed.cget("text")+"\n"+listAlterte[i])
            self.__lNoAlert.grid_forget()
            self.__lAlertRed.grid(row=0, column=0, sticky="new", padx=8, pady=(8, 4))
            self.__readVar += "Fais attention, il y a une alerte rouge aujourd'hui. "

        if meteoDict["orangeAlert"]:
            listAlterte = meteoDict["orangeAlert"]
            for i in range(len(listAlterte)):
                if i == 0:
                    self.__lAlertOrange.configure(text=listAlterte[i])
                else:
                    self.__lAlertOrange.configure(text=self.__lAlertRed.cget("text")+"\n"+listAlterte[i])
            self.__lNoAlert.grid_forget()
            self.__lAlertOrange.grid(row=1, column=0, sticky="ew", padx=8, pady=4)
            self.__readVar += "Fais attention, il y a une alerte orange aujourd'hui. "

        if meteoDict["yellowAlert"]:
            listAlterte = meteoDict["yellowAlert"]
            for i in range(len(listAlterte)):
                if i == 0:
                    self.__lAlertYellow.configure(text=listAlterte[i])
                else:
                    self.__lAlertYellow.configure(text=self.__lAlertRed.cget("text")+"\n"+listAlterte[i])
            self.__lNoAlert.grid_forget()
            self.__lAlertYellow.grid(row=2, column=0, sticky="sew", padx=8, pady=(4, 8))
            self.__readVar += "Fais attention, il y a une alerte jaune aujourd'hui. "

    def __setReadForTask(self,listTask:list):
        if len(listTask) != 0:
            if len(listTask) == 1:
                self.__readVar += f"Tu as une tâche à faire aujourd'hui qui est {listTask[0]}."
            else :
                self.__readVar += f"Tu as {len(listTask)} tâches à faire aujourd'hui qui sont "
                for i,task in enumerate(listTask):
                    if i == 0:
                        self.__readVar += task
                    elif i == len(listTask)-1:
                        self.__readVar += f" et {task}."
                    else:
                        self.__readVar += f", {task}"
        else:
            self.__readVar += "Tu n'as aucune tâche à faire aujourd'hui. "

    def __readBreef(self):
        self.__thRead = th.Thread(target=self._gestionnaire.getArrVoice().say(self.__readVar))
        self._screen.after(10,self.__updateScreen)


    def __updateScreen(self):
        if self.__thRead.is_alive():
            self._screen.update()
            self._screen.after(100,self.__updateScreen)
        else:
            self._screen.update()
            self._screen.focus()
            self.__thRead = th.Thread()

