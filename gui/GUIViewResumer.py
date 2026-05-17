from gui.GUIView import GUIView,gestionnaire

class GUIViewResumer(GUIView):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Resumer")

    def __manageTexte(self, dict:dict=None,list:list=None, intIn:int=0):
        """
        12 : Reussite du resumer actulités
        18 : Resumer tache / agenda
        19 : Resumer all ok
        """
        self._textBox.enableTextBox()
        match intIn:
            case 12:
                if dict is not None:
                    actu = dict["actu"]
                    meteo = dict["meteo"]

                    texteMeteo = f"La météo actuelle à {meteo['ville']} est de {meteo['temperature']}°C avec {meteo['weather']}.\n"
                    texteActu = "Voici les dernières actualités :\n\n"

                    for i in actu:
                        texteActu += f"- {i}\n"

                    self._textBox.getTextBox().delete(1.0, "end")
                    self._textBox.getTextBox().insert("end", f"{texteActu}\n")
                    self._textBox.getTextBox().insert("end", texteMeteo)
                    self._textBox.disableTextBox()
                    self._textRead = f"{texteActu} {texteMeteo}"
                    return True
                else:
                    return False
            case 18:
                if list is not None:
                    task = list
                    texteTask = "Voici les tache qui reste a faire : \n\n"
                    if len(task) == 0:
                        texteTask = "Aucune tache a faire !"
                    else:
                        for i in task:
                            texteTask += f"- {i}\n"

                    self._textBox.getTextBox().delete(1.0, "end")
                    self._textBox.getTextBox().insert("end", texteTask)
                    self._textBox.disableTextBox()
                    self._textRead = texteTask
                    return True
                else:
                    return False
            case 19:
                if dict is not None:
                    actu = dict["actu"]
                    meteo = dict["meteo"]
                    task = dict["task"]

                    texteActu = "Voici les dernières actualités :\n\n"
                    for i in actu:
                        texteActu += f"- {i}\n"
                    texteMeteo = f"La météo actuelle à {meteo['ville']} est de {meteo['temperature']}°C avec {meteo['weather']}.\n"
                    texteTask = "\nVoici les tache qui reste a faire : \n\n"
                    if len(task) == 0:
                        texteTask = "Aucune tache a faire !"
                    else:
                        for i in task:
                            texteTask += f"- {i}\n"

                    self._textBox.getTextBox().delete(1.0, "end")
                    self._textBox.getTextBox().insert("end", texteActu + "\n" + texteMeteo + "\n" + texteTask)
                    self._textBox.disableTextBox()
                    self._textRead = f"{texteActu} {texteMeteo} {texteTask}"
                    return True
                else :
                    self._textBox.disableTextBox()
                    return False
            case _:
                self._textBox.disableTextBox()
                return False

    def activeView(self,dict:dict=None,list:list=None, intIn:int=0):
        self.active()
        self._titleLabel.configure(text="Resumer")
        self.__manageTexte(dict,list,intIn)