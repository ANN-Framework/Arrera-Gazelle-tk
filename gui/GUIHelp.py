from gui.GUIView import GUIView,gestionnaire

class GUIHelp(GUIView):
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Aide")

    def activeHelp(self, texte:str):
        self.active()
        self._textBox.enableTextBox()
        self._textBox.getTextBox().delete(1.0, "end")
        self._textBox.getTextBox().insert("end", texte)
        self._textBox.disableTextBox()
        self._titleLabel.configure(text="Aide")
        self._textRead = texte