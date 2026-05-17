from neuron.CNeuronBase import neuronBase,gestionnaire

class neuroneMarkdown(neuronBase):
    def __init__(self, gestionnaire: gestionnaire):
        super().__init__(gestionnaire)
        self.__socket = self._gestionnaire.getSocketObjet()
        self.__gestIA = self._gestionnaire.getGestIA()
        self.__gestIA.loadIA()

    def neurone(self, requette: str):
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if self.__socket is not None:
            if "corection" in requette:
                if not self.__gestIA.get_ia_is_enable():
                    self._valeurOut = 1
                    self._listSortie = [self._language.getPhraseMarkdownt("1"),""]
                else :
                    self._valeurOut = 1
                    text = "\""+requette.replace("corection","").strip()+"\""
                    if self.__gestIA.correted_text(text):
                        if self.__gestIA.get_state_ia_reponse():
                            out_ia = self.__gestIA.get_reponse_ia()
                            if self.__socket.send_data_with_server_to("arrera_markdown","text "+out_ia):
                                self._listSortie = [self._language.getPhraseMarkdownt("3"), ""]
                                self._valeurOut = 1
                            else :
                                self._listSortie = [self._language.getPhraseMarkdownt("4"), ""]
                                self._valeurOut = 1
                        else :
                            self._listSortie = [self._language.getPhraseMarkdownt("2"), ""]
                            self._valeurOut = 1
                    else :
                        self._listSortie = [self._language.getPhraseMarkdownt("2"), ""]
                        self._valeurOut = 1