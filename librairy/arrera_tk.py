import customtkinter as ctk
from tkinter import *
from PIL import Image
import webbrowser as wb
import platform
import os
import subprocess
import sys
from typing import Union, Callable

from customtkinter import CTkCanvas, CTkImage

VERSIONARRERATK = "2.1.0"


# Fonction pour gerer les resource sur mac os
def resource_path(relative_path):
    if platform.system() == "Darwin":
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
    else:
        return relative_path

# Class de placement custome

def copie_text(text:str):
    current_os = platform.system()
    text_to_copy = str(text)

    try:
        if current_os == "Windows":
            subprocess.run(['clip'], input=text_to_copy, check=True, text=True)

        elif current_os == "Darwin":
            subprocess.run(['pbcopy'], input=text_to_copy, check=True, text=True)

        elif current_os == "Linux":
            try:
                subprocess.run(['xclip', '-selection', 'clipboard'], input=text_to_copy, check=True, text=True)
            except FileNotFoundError:
                subprocess.run(['xsel', '--clipboard', '--input'], input=text_to_copy, check=True, text=True)

        return True

    except Exception as e:
        print(f"Erreur lors de la copie système : {e}")
        return False




class placement_Tool_Kit_internet:
    def placeCenter(self):
        self.place(relx=0.5, rely=0.5, anchor='center')

    def placeLeftCenter(self):
        self.place(relx=0, rely=0.5, anchor='w')

    def placeRightCenter(self):
        self.place(relx=1, rely=0.5, anchor='e')

    def placeTopCenter(self):
        self.place(relx=0.5, rely=0, anchor='n')

    def placeBottomCenter(self):
        self.place(relx=0.5, rely=1, anchor='s')

    def placeCenterOnWidth(self, y: int = 0):
        if (y == 0):
            return
        else:
            self.place(relx=0.5, y=y, anchor='n')

    def placeWidgetCenteredAtBottom(self, x_offset=1):
        self.place(relx=0.5, rely=1, x=-x_offset, anchor="s")

    def placeBottomRight(self):
        self.place(relx=1, rely=1, anchor='se')

    def placeBottomLeft(self):
        self.place(relx=0, rely=1, anchor='sw')

    def placeTopRight(self):
        self.place(relx=1, rely=0, anchor='ne')

    def placeTopLeft(self):
        self.place(relx=0, rely=0, anchor='nw')

    def placeCenterRight(self):
        self.place(relx=1, rely=0.5, anchor='e')

    def placeCenterLeft(self):
        self.place(relx=0, rely=0.5, anchor='w')

    def placeLeftBottomNoStick(self):
        self.place(relx=0, rely=1, anchor='sw', x=10, y=-10)

    def placeRightBottomNoStick(self):
        self.place(relx=1, rely=1, anchor='se', x=-10, y=-10)

    def placeBottomCenterNoStick(self):
        self.place(relx=0.5, rely=1, anchor='s', x=0, y=-10)

    # Pack

    def pack(self, xExpand: bool = False, yExpand: bool = False, **kwargs):
        if xExpand and yExpand:
            kwargs.update({'expand': True, 'fill': 'both'})
        elif xExpand:
            kwargs.update({'expand': True, 'fill': 'x'})
        elif yExpand:
            kwargs.update({'expand': True, 'fill': 'y'})

        super().pack(**kwargs)

    def packLeft(self, xExpand: bool = False, yExpand: bool = False, **kwargs):
        self.pack(xExpand=xExpand, yExpand=yExpand, side="left", **kwargs)

    def packRight(self, xExpand: bool = False, yExpand: bool = False, **kwargs):
        self.pack(xExpand=xExpand, yExpand=yExpand, side="right", **kwargs)

    def packTop(self, xExpand: bool = False, yExpand: bool = False, **kwargs):
        self.pack(xExpand=xExpand, yExpand=yExpand, side="top", **kwargs)

    def packBottom(self, xExpand: bool = False, yExpand: bool = False, **kwargs):
        self.pack(xExpand=xExpand, yExpand=yExpand, side="bottom", **kwargs)


# Image

class aImage(ctk.CTkImage):
    def __init__(self, width: int, height: int, path_light: str, path_dark: str = ""):
        if path_dark != "":
            super().__init__(light_image=Image.open(resource_path(path_light)),
                             dark_image=Image.open(resource_path(path_dark)),
                             size=(width, height))
        else:
            super().__init__(light_image=Image.open(resource_path(path_light)), size=(width, height))


# Widget

class aLabel(placement_Tool_Kit_internet, ctk.CTkLabel):
    def __init__(self, master, text: str = "Arrera Label", police_size: int = 0, dark_color: str = "",
                 light_color: str = "", light_text_color: str = "", dark_text_color: str = "",image : CTkImage = None, **kwargs):
        super().__init__(master, text=text, **kwargs)
        if police_size != 0:
            self.configure(font=("Roboto", police_size, "bold"))

        if dark_color != "" and light_color != "":
            self.configure(fg_color=(light_color, dark_color))

        if dark_text_color != "" and light_text_color != "":
            self.configure(text_color=(light_text_color, dark_text_color))

        if image is not None:
            self.configure(image=image,text="")

class aButton(placement_Tool_Kit_internet, ctk.CTkButton):
    def __init__(self, master, text: str = "Arrera Button", width: int = 140, height: int = 40, command=None,
                 size: int = 0, dark_color: str = "", light_color: str = "", light_text_color: str = "",
                 dark_text_color: str = "", **kwargs):
        super().__init__(master, text=text, width=width, height=height, command=command, **kwargs)
        if size != 0:
            self.configure(font=("Roboto", size, "bold"))

        if dark_color != "" and light_color != "":
            self.configure(fg_color=(light_color, dark_color))

        if dark_text_color != "" and light_text_color != "":
            self.configure(text_color=(light_text_color, dark_text_color))


class aCheckBox(placement_Tool_Kit_internet, ctk.CTkCheckBox):
    def __init__(self, master, boolean_value: bool, **kwargs):
        if boolean_value:
            self.__bVar = BooleanVar(master, value=True)
        else:
            self.__bVar = BooleanVar(master, value=True)
        super().__init__(master, variable=self.__bVar, text="Arrera CheckBox", **kwargs)

    def getBooleanVar(self):
        return self.__bVar

    def setFalse(self):
        self.__bVar.set(False)

    def setTrue(self):
        self.__bVar.set(True)


class aRadioButton(placement_Tool_Kit_internet, ctk.CTkRadioButton):
    def __init__(self, master, text: str = "Arrera RadioButton", variable=None, value=0, command=None, **kwargs):
        super().__init__(master, text=text, variable=variable, value=value, command=command, **kwargs)


class aEntry(placement_Tool_Kit_internet, ctk.CTkEntry):
    def __init__(self, master, police_size: int = 15, width: int = 20, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=("Roboto", police_size, "bold"))
        self.configure(width=width)


class aText(placement_Tool_Kit_internet, ctk.CTkTextbox):
    def __init__(self, master, police_size: int = 15, center: bool = False, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=("Roboto", police_size, "normal"))

        if center:
            self._textbox.tag_configure("center", justify="center")
            self._textbox.tag_add("center", "0.0", "end")

    def disable_textbox(self):
        self.configure(state="disabled")

    def enable_textbox(self):
        self.configure(state="normal")
        self.focus()

    def insert_text(self, text: str):
        self.configure(state="normal")
        self.insert("1.0", text)
        self.configure(state="disabled")

    def centre_text(self):
        self._textbox.tag_configure("center", justify="center")


class aTextScrollable(placement_Tool_Kit_internet, ctk.CTkFrame):
    def __init__(self, master,police_size: int = 15):
        super().__init__(master)
        self.configure(border_width=0)

        self.__textbox = ctk.CTkTextbox(self, wrap="word", state="disabled")
        scrollbar = ctk.CTkScrollbar(self, command=self.__textbox.yview)
        self.__textbox.configure(yscrollcommand=scrollbar.set)

        self.__textbox.configure(font=("Roboto", police_size, "normal"))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.__textbox.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)
        scrollbar.grid(row=0, column=1, sticky="ns", padx=(0, 10), pady=10)

    def getTextBox(self):
        return self.__textbox

    def enableTextBox(self):
        self.__textbox.configure(state="normal")
        self.__textbox.focus()

    def disableTextBox(self):
        self.__textbox.configure(state="disabled")


class aEntryLengend(placement_Tool_Kit_internet, ctk.CTkFrame):
    def __init__(self, master, text: str = "Arrera Entry Legend", bg: str = "", fg: str = "", police_size: int = 15,
                 width: int = 200, gridUsed: bool = False):
        super().__init__(master)
        text = text + ":  "
        self.__label = aLabel(self, text=text, font=("Roboto", police_size, "bold"))


        if bg == "":
            bg = master.cget("fg_color")

        self.configure(fg_color=bg)
        self.__label.configure(fg_color=bg)

        if fg != "":
            self.__label.configure(text_color=fg)

        self.__entry = aEntry(self, police_size=police_size, width=width)

        if gridUsed:
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=0)
            self.__label.grid(row=0, column=0, sticky="w", padx=(8, 6), pady=6)
            self.__entry.grid(row=0, column=1, sticky="ew", padx=(6, 8), pady=6)
        else:
            self.__label.pack(side="left")
            self.__entry.pack(side="right")

    def getEntry(self):
        return self.__entry

    def changeColorLabel(self, bg: str = "", fg: str = ""):
        if bg != "":
            self.__label.configure(fg_color=bg)

        if fg != "":
            self.__label.configure(text_color=fg)

    def changeTextLabel(self, text: str):
        self.__label.configure(text=text)

    def changePoliceLabel(self, font: (str, int, str) = ("Roboto", 15, "bold")):
        self.__label.configure(font=font)


class aOptionMenu(placement_Tool_Kit_internet, ctk.CTkOptionMenu):
    def __init__(self, master, value: list, police_size: int = 15, bg: str = "", fg: str = "", width: int = 200,
                 **kwargs):
        self.__var = StringVar()

        super().__init__(master, values=value, variable=self.__var, **kwargs)

        if bg != "":
            self.configure(fg_color=bg)

        if fg != "":
            self.configure(text_color=fg)

        self.configure(font=("Roboto", police_size, "bold"))

        self.__var.set(value[0])

    def getValue(self):
        return self.__var.get()

    def changeColor(self, bg: str = "", fg: str = ""):
        if bg != "":
            self.configure(fg_color=bg)

        if fg != "":
            self.configure(text_color=fg)

    def changePolice(self, font: (str, int, str) = ("Roboto", 15, "bold")):
        self.configure(font=font)

    def set_text(self, text: str):
        self.__var.set(text)


class aOptionMenuLengend(placement_Tool_Kit_internet, ctk.CTkFrame):
    def __init__(self, master, values: list, text: str = "Arrera OptionMenu Legend", bg: str = "", fg: str = "",
                 police_size: int = 15, gridUsed: bool = False):
        super().__init__(master)
        text = text + ":  "
        self.__label = aLabel(self, text=text, font=("Roboto", police_size, "bold"))

        self.configure(fg_color=master.cget("fg_color"))

        if bg != "":
            self.__label.configure(fg_color=bg)
        else :
            self.__label.configure(fg_color=master.cget("fg_color"))

        if fg != "":
            self.__label.configure(text_color=fg)

        self.__optionMenu = aOptionMenu(self, value=values, police_size=police_size, bg=bg, fg=fg)

        if gridUsed:
            self.grid_columnconfigure(0, weight=0)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=0)
            self.__label.grid(row=0, column=0, sticky="w", padx=(8, 6), pady=6)
            self.__optionMenu.grid(row=0, column=1, sticky="ew", padx=(6, 8), pady=6)
        else:
            self.__label.pack(side="left")
            self.__optionMenu.pack(side="right")

    def getOptionMenu(self):
        return self.__optionMenu

    def getValue(self):
        return self.__optionMenu.getValue()

    def changeColorLabel(self, bg: str = "", fg: str = ""):
        if bg != "":
            self.__label.configure(fg_color=bg)

        if fg != "":
            self.__label.configure(text_color=fg)

    def changeTextLabel(self, text: str):
        self.__label.configure(text=text)

    def set_text(self, text: str):
        self.__optionMenu.set_text(text)

    def changePoliceLabel(self, font: (str, int, str) = ("Roboto", 15, "bold")):
        self.__label.configure(font=font)


class aHourPickers(placement_Tool_Kit_internet, ctk.CTkFrame):
    def __init__(self, master,minute_pickers:bool = False, **kwargs):
        super().__init__(master,fg_color=master.cget("fg_color"),**kwargs)

        if not minute_pickers:
            hours = [f"{h:02d}" for h in range(24)]
        else :
            hours = [f"{h:02d}" for h in range(60)]

        minutes = [f"{m:02d}" for m in range(60)]

        self.__hour = aOptionMenu(self, value=hours, width=10)
        self.__minute = aOptionMenu(self, value=minutes, width=10)

        label = aLabel(self, text=" : ", font=("Roboto", 20, "bold"))

        self.__hour.pack(side="left")
        label.pack(side="left")
        self.__minute.pack(side="left")

    def getValueHour(self):
        return self.__hour.getValue()

    def getValueMinute(self):
        return self.__minute.getValue()

    def setValueMinute(self, minute:str):
        self.__minute.set(minute)

    def setValueHour(self,hour:str):
        self.__hour.set(hour)


class aSwicht(placement_Tool_Kit_internet, ctk.CTkSwitch):
    def __init__(self, master, text="Arrera Button Swicht", default_value: bool = False, **kwargs):
        self.__var = BooleanVar(value=default_value)
        super().__init__(master, text=text, variable=self.__var, onvalue=True, offvalue=False, **kwargs)
        self.configure(font=("Roboto", 15, "bold"))

    def setOn(self):
        self.__var.set(True)

    def setOff(self):
        self.__var.set(False)

    def getValue(self):
        return self.__var.get()

    def change_text(self, text=""):
        if text != "":
            self.configure(text=text)


# Frame / Canvas

class aFrame(placement_Tool_Kit_internet, ctk.CTkFrame):
    def __init__(self, master, corner_radius: int = 20, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=corner_radius)


class aScrollableFrame(placement_Tool_Kit_internet, ctk.CTkScrollableFrame):
    def __init__(self, master, corner_radius: int = 20, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=corner_radius)


class aCanvas(ctk.CTkCanvas):
    def __init__(self, master):
        super().__init__(master)


class aBackgroundImage(ctk.CTkFrame):
    def __init__(self, master, background_light: str, background_dark: str = "", height: int = 600, width: int = 800,
                 **kwargs):
        super().__init__(master, **kwargs)

        self.__size = (width, height)
        self.configure(width=width, height=height, border_width=0)

        # Création de l'image initiale
        background = self._create_ctk_image(background_light, background_dark)

        # Sauvegarde de l'image pour éviter le garbage collection
        self.__current_image = background

        # Utilisation d'un CTkLabel pour afficher l'image
        # Note: Assure-toi que aLabel accepte l'argument 'image' ou utilise ctk.CTkLabel
        self.__label = ctk.CTkLabel(self, text="", image=background)
        self.__label.place(relx=0.5, rely=0.5, anchor='center')

    def _create_ctk_image(self, light_path: str, dark_path: str):
        """Méthode interne pour générer l'objet CTkImage correctement"""
        # Si dark_path est vide, on utilise l'image light pour les deux modes
        path_for_dark = dark_path if dark_path != "" else light_path

        return ctk.CTkImage(
            light_image=Image.open(resource_path(light_path)),
            dark_image=Image.open(resource_path(path_for_dark)),
            size=self.__size
        )

    def change_background(self, background_light: str, background_dark: str = ""):
        """Permet de changer dynamiquement les images de fond"""
        new_background = self._create_ctk_image(background_light, background_dark)

        # Sauvegarde de la nouvelle image pour éviter le garbage collection
        self.__current_image = new_background

        self.__label.configure(image=new_background)


# Fenetre

class aTk(ctk.CTk):
    def __init__(self, title: str = "ArreraTK", width: int = 800, height: int = 600, resizable: bool = False,
                 icon: str = "", theme_file: str = "theme/theme_default.json", **kwargs):
        super().__init__(**kwargs)
        ctk.set_appearance_mode("System")
        try:
            ctk.set_default_color_theme(resource_path(theme_file))
        except Exception as e:
            print(e)
            ctk.set_default_color_theme("dark-blue")

        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable, resizable)

        if icon != "":
            icon = resource_path(icon)
            if platform.system() == "Windows":
                if os.path.splitext(icon)[1].lower() == '.ico':
                    self.iconbitmap(icon)
            elif os.path.splitext(icon)[1].lower() == '.png':
                self.iconphoto(True, PhotoImage(file=icon))


class aTopLevel(ctk.CTkToplevel):
    def __init__(self, title: str = "Arrera TopLevel", width: int = 400, height: int = 300, resizable: bool = False,
                 icon: str = "", **kwargs):
        super().__init__(**kwargs)

        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable, resizable)

        if icon != "":
            icon = resource_path(icon)
            if platform.system() == "Windows":
                if os.path.splitext(icon)[1].lower() == '.ico':
                    self.iconbitmap(icon)
            elif os.path.splitext(icon)[1].lower() == '.png':
                self.iconphoto(True, PhotoImage(file=icon))


class windows_about(ctk.CTkToplevel):
    def __init__(self, nameSoft: str, iconFile: str, version: str, copyright: str, linkSource: str, linkWeb: str):
        super().__init__()
        self.title("A propos : " + nameSoft)
        self.maxsize(400, 300)
        self.minsize(400, 300)

        icon = ctk.CTkImage(light_image=Image.open(resource_path(iconFile)), size=(100, 100))
        mainFrame = aFrame(self, width=400, height=250, border_width=0, corner_radius=0)
        frameBTN = aFrame(self, width=400, height=50, border_width=0, corner_radius=0)
        frameLabel = aFrame(self, border_width=0, corner_radius=0)

        labelIcon = aLabel(mainFrame, image=icon, text="")
        labelSoft = aLabel(frameLabel, text=nameSoft + " version " + version, font=("Roboto", 20))
        labelVersion = aLabel(frameLabel, text="Arrera TK version " + VERSIONARRERATK, font=("Roboto", 13))
        labelCopy = aLabel(mainFrame, text=copyright, font=("Roboto", 13))

        btnLinkSource = aButton(frameBTN, text="Source code", command=lambda: wb.open(linkSource),
                                font=("Roboto", 13, "bold"))
        btnLinkWeb = aButton(frameBTN, text="Web site", command=lambda: wb.open(linkWeb),
                             font=("Roboto", 13, "bold"))

        labelIcon.placeTopCenter()
        labelSoft.pack()
        labelVersion.pack()
        labelCopy.placeBottomCenter()

        frameLabel.placeCenter()
        mainFrame.pack(side="top")
        frameBTN.pack(side="bottom")

        btnLinkSource.placeRightCenter()
        btnLinkWeb.placeLeftCenter()


def placeLeftTop(widget):
    widget.place(relx=0, rely=0, anchor='nw')


def placeRightTop(widget):
    widget.place(relx=1, rely=0, anchor='ne')


def placeLeftBottom(widget):
    widget.place(relx=0, rely=1, anchor='sw')


def placeRightBottom(widget):
    widget.place(relx=1, rely=1, anchor='se')


def placeCenter(widget):
    widget.place(relx=0.5, rely=0.5, anchor='center')


def placeLeftCenter(widget):
    widget.place(relx=0, rely=0.5, anchor='w')


def placeRightCenter(widget):
    widget.place(relx=1, rely=0.5, anchor='e')


def placeTopCenter(widget):
    widget.place(relx=0.5, rely=0, anchor='n')


def placeBottomCenter(widget):
    widget.place(relx=0.5, rely=1, anchor='s')


def placeCenterOnWidth(widget, y: int = 0):
    if y == 0:
        return
    else:
        widget.place(relx=0.5, y=y, anchor='n')


def placeWidgetCenteredAtBottom(widget, x_offset=1):
    widget.place(relx=0.5, rely=1, x=-x_offset, anchor="s")


def placeBottomRight(widget):
    widget.place(relx=1, rely=1, anchor='se')


def placeBottomLeft(widget):
    widget.place(relx=0, rely=1, anchor='sw')


def placeTopRight(widget):
    widget.place(relx=1, rely=0, anchor='ne')


def placeTopLeft(widget):
    widget.place(relx=0, rely=0, anchor='nw')


def placeCenterRight(widget):
    widget.place(relx=1, rely=0.5, anchor='e')


def placeCenterLeft(widget):
    widget.place(relx=0, rely=0.5, anchor='w')


def placeLeftBottomNoStick(widget):
    widget.place(relx=0, rely=1, anchor='sw', x=10, y=-10)


def placeRightBottomNoStick(widget):
    widget.place(relx=1, rely=1, anchor='se', x=-10, y=-10)


def placeBottomCenterNoStick(widget):
    widget.place(relx=0.5, rely=1, anchor='s', x=0, y=-10)


# Pack

def pack(widget, xExpand: bool = False, yExpand: bool = False):
    if xExpand and yExpand:
        widget.pack(expand=True, fill="both")
    elif xExpand:
        widget.pack(expand=True, fill="x")
    elif yExpand:
        widget.pack(expand=True, fill="y")
    else:
        widget.pack()


def packLeft(widget, xExpand: bool = False, yExpand: bool = False):
    if xExpand and yExpand:
        widget.pack(expand=True, fill="both", side="left")
    elif xExpand:
        widget.pack(expand=True, fill="x", side="left")
    elif yExpand:
        widget.pack(expand=True, fill="y", side="left")
    else:
        widget.pack(side="left")


def packRight(widget, xExpand: bool = False, yExpand: bool = False):
    if xExpand and yExpand:
        widget.pack(expand=True, fill="both", side="right")
    elif xExpand:
        widget.pack(expand=True, fill="x", side="right")
    elif yExpand:
        widget.pack(expand=True, fill="y", side="right")
    else:
        widget.pack(side="right")


def packTop(widget, xExpand: bool = False, yExpand: bool = False):
    if xExpand and yExpand:
        widget.pack(expand=True, fill="both", side="top")
    elif xExpand:
        widget.pack(expand=True, fill="x", side="top")
    elif yExpand:
        widget.pack(expand=True, fill="y", side="top")
    else:
        widget.pack(side="top")


def packBottom(widget, xExpand: bool = False, yExpand: bool = False):
    if xExpand and yExpand:
        widget.pack(expand=True, fill="both", side="bottom")
    elif xExpand:
        widget.pack(expand=True, fill="x", side="bottom")
    elif yExpand:
        widget.pack(expand=True, fill="y", side="bottom")
    else:
        widget.pack(side="bottom")

# Objet pour gerer les touche de clavier

class keyboad_manager:
    def __init__(self,master:Union[aTk,aTopLevel]):
        self.__dict_key_fonction = {}# Shema key:fonction
        self.__w = master

    def __gest_keyboad(self, event):
        if event.keycode in self.__dict_key_fonction:
            self.__dict_key_fonction[event.keycode]()

    def add_key(self,key:int,fonction:Callable):
        if not self.__dict_key_fonction:
            self.__w.bind("<Key>",self.__gest_keyboad)

        self.__dict_key_fonction[key] = fonction