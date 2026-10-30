# Arrera Gazelle

[English version](README_en.md)

Arrera Gazelle est l'interface graphique utilisant Arrera TK en version 2 qui a pour but d'être l'interface graphique des paramètres pour l'Arrera Neuron Network.

Son but final est d'être l'interface graphique des assistants Arrera SIX, Arrera Ryley et Arrera Copilote.

## Intégration

Pour intégrer Arrera Gazelle à votre projet d'assistant, il faut :

Télécharger l'archive qui contient un dossier `lib` où se trouve la version d'Arrera TK, le fichier Python `arrera_gazelle.py` qui est le fichier qui contient l'interface des paramètres, et enfin le fichier JSON `conf-setting.json` qui est le fichier de configuration d'Arrera Gazelle.

/!\ Arrera Gazelle n'utilise pas la même version de Arrera TK que Arrera Neuron Network (V1 pour Arrera Neuron Network et V2 pour Arrera Gazelle).

### Explication du fichier de configuration

```json
{
    "listGenre":["monsieur","madame","maitre"],
    "iconSoft": "asset/logo-six.png",
    "listMoteurRecherche": ["google","brave","duckduckgo","qwant","ecosia","bing","perplexity"],
    "github_integration": "1",
    "micro_use": "1"
}
```

`listGenre` : Liste des genres ou civilités que l'utilisateur peut choisir.
`iconSoft` : Chemin relatif vers l'icône utilisée par le logiciel.
`listMoteurRecherche` : Liste des moteurs de recherche disponibles pour l'assistant.
`github_integration` : Indicateur ("1" pour activé, "0" pour désactivé) permettant d'activer les fonctionnalités liées à GitHub.
`micro_use` : Indicateur ("1" pour activé, "0" pour désactivé) permettant d'activer l'utilisation du microphone.

### Initialisation et Utilisation

L'initialisation de l'objet `arrera_gazelle` se fait en passant plusieurs paramètres essentiels :
1.  Une fenêtre `aTk` ou `aTopLevel` (issue de `arrera_tk`) qui servira de conteneur principal.
2.  Un objet `gestionnaire` (issu de `gestionnaire.gestion`) configuré avec les paramètres de l'assistant (nom, langue, chemins, etc.).
3.  Le chemin vers le fichier de configuration JSON (`conf-setting.json`).

Voici un exemple d'initialisation typique (basé sur `src/setting_assistant.py`) :

```python
from arrera_gazelle.arrera_gazelle import arrera_gazelle
from lib.arrera_tk import aTk

# ... import de votre gestionnaire ...

# Création de la fenêtre principale
windows = aTk(theme_file="asset/theme/theme_bleu_blanc.json")

# Initialisation de l'interface Gazelle
# windows : la fenêtre parente
# create_conf() : fonction retournant l'objet gestionnaire configuré
# "json_conf/conf-setting.json" : chemin vers le fichier de config
gui = arrera_gazelle(windows, create_conf(), "json_conf/conf-setting.json")

# Configuration de la taille de la fenêtre
windows.maxsize(500, 400)
windows.minsize(500, 400)

# Définition des actions personnalisées
# Action pour le bouton "Retour" principal (ici, fermer la fenêtre)
gui.passFNCQuit(lambda: windows.destroy())
# Action pour le clic sur l'icône de l'assistant
gui.passFNCBTNIcon(lambda: print("Icon"))

# Activation de l'interface (affichage)
gui.active()

# Lancement de la boucle principale
windows.mainloop()
```

L'objet `arrera_gazelle` gère ensuite l'affichage et la navigation entre les différents menus de configuration (Général, Utilisateur, Météo, IA, GPS, Recherche, Web, Logiciels, Micro, GitHub) en fonction des drapeaux activés dans le fichier de configuration.
