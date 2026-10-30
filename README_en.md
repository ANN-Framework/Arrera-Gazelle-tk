# Arrera-Gazelle

Arrera Gazelle is the graphical interface using Arrera TK version 2, intended to be the settings graphical interface for the Arrera Neuron Network.

Its final goal is to be the graphical interface for the assistants Arrera SIX, Arrera Ryley, and Arrera Copilote.

## Integration

To integrate Arrera Gazelle into your assistant project, you must:

Download the archive containing a `lib` folder where the Arrera TK version is located, the python file `arrera_gazelle.py` which contains the settings interface, and finally the json file `conf-setting.json` which is the configuration file for Arrera Gazelle.

/!\ Arrera Gazelle does not use the same version of Arrera TK as Arrera Neuron Network (V1 for Arrera Neuron Network and V2 for Arrera Gazelle).

### Configuration File Explanation

```json
{
    "listGenre":["monsieur","madame","maitre"],
    "iconSoft": "asset/logo-six.png",
    "listMoteurRecherche": ["google","brave","duckduckgo","qwant","ecosia","bing","perplexity"],
    "github_integration": "1",
    "micro_use": "1"
}
```

`listGenre`: List of genders or titles that the user can choose.
`iconSoft`: Relative path to the icon used by the software.
`listMoteurRecherche`: List of search engines available for the assistant.
`github_integration`: Indicator ("1" for enabled, "0" for disabled) to enable GitHub-related features.
`micro_use`: Indicator ("1" for enabled, "0" for disabled) to enable microphone usage.

### Initialization and Usage

The initialization of the `arrera_gazelle` object is done by passing several essential parameters:
1. An `aTk` or `aTopLevel` window (from `arrera_tk`) which will serve as the main container.
2. A `gestionnaire` object (from `gestionnaire.gestion`) configured with the assistant's parameters (name, language, paths, etc.).
3. The path to the JSON configuration file (`conf-setting.json`).

Here is a typical initialization example (based on `src/setting_assistant.py`):

```python
from arrera_gazelle.arrera_gazelle import arrera_gazelle
from lib.arrera_tk import aTk

# ... import your manager ...

# Creation of the main window
windows = aTk(theme_file="asset/theme/theme_bleu_blanc.json")

# Initialization of the Gazelle interface
# windows: the parent window
# create_conf(): function returning the configured manager object
# "json_conf/conf-setting.json": path to the config file
gui = arrera_gazelle(windows, create_conf(), "json_conf/conf-setting.json")

# Window size configuration
windows.maxsize(500, 400)
windows.minsize(500, 400)

# Definition of custom actions
# Action for the main "Back" button (here, close the window)
gui.passFNCQuit(lambda: windows.destroy())
# Action for clicking on the assistant icon
gui.passFNCBTNIcon(lambda: print("Icon"))

# Activation of the interface (display)
gui.active()

# Launching the main loop
windows.mainloop()
```

The `arrera_gazelle` object then manages the display and navigation between the different configuration menus (General, User, Weather, AI, GPS, Search, Web, Software, Micro, GitHub) depending on the flags enabled in the configuration file.
