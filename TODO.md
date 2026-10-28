# TODO — Arrera Gazelle (Migration ANN v4.0 & Modularisation Python)

Ce document détaille toutes les étapes et modifications techniques nécessaires pour faire évoluer **Arrera Gazelle** vers sa nouvelle version compatible avec **ANN v4.0** (`ann-core`), et le transformer en **module Python installable** (`pyproject.toml`).

---

## 🎯 Objectifs principaux

1. **Découplage complet et suppression du code dupliqué** : Retirer l'ancienne base de code ANN v3 embarquée (`brain/`, `fnc/`, `neuron/`, etc.) au profit de la dépendance externe officielle `ann-core`.
2. **Modularisation Python** : Convertir le projet en un package Python autonome installable via `pip` (`pyproject.toml`), utilisable directement par les assistants (Arrera SIX, Arrera Ryley, etc.) via `from arrera_gazelle import arrera_gazelle`.
3. **Compatibilité avec l'API ANN v4 (Headless Core)** : Adapter les appels aux méthodes de configuration utilisateur qui ne gèrent plus les boîtes de dialogue Tkinter dans le Core (`setWorkFolder`, `setVideoDownloadFolder`, `setSoft`, nouvelles adresses complètes, catalogue 9 modèles GGUF et recommandation matérielle).
4. **Utilisation du package officiel `arrera-tk`** : Utiliser le paquet pip `arrera-tk` plutôt qu'une version locale obsolète dans `librairy/`.

---

## 📋 Checklist des tâches

### 1. Nettoyage architectural (Suppression du code dupliqué de ANN v3)
- [ ] **Supprimer les dossiers clonés du moteur ANN v3** devenus obsolètes :
  - `brain/`
  - `fnc/`
  - `neuron/`
  - `objet/`
  - `instruction_ia/`
  - `keyword/`
  - `language/`
  - `gestionnaire/`
  - `config/`
  - `gui/` (ancienne interface Tkinter v3)
  - `librairy/` (en particulier l'ancien `arrera_tk.py` et les utilitaires redondants)
- [ ] **Nettoyer les assets non utilisés** :
  - Conserver uniquement les icônes nécessaires à Gazelle (`icon.png`, `logo-six.png`, `logo.png`, `baniere.png`) et les thèmes dans `asset/theme/`.
  - Supprimer les dossiers d'icônes importés de ANN (`asset/meteo/`, `asset/calendar/`, `asset/horloge/`, `asset/tache/`, `asset/work/`, `asset/sound/`).

---

### 2. Packaging Python (`pyproject.toml` & structure de module)
- [ ] **Restructurer le code source en package Python** :
  - Renommer/déplacer `setting_gui/` vers `arrera_gazelle/` (ou structure standard `src/arrera_gazelle/`).
  - Créer `arrera_gazelle/__init__.py` pour exposer la classe principale :
    ```python
    from .arrera_gazelle import arrera_gazelle

    __all__ = ["arrera_gazelle"]
    ```
- [ ] **Créer le fichier `pyproject.toml`** :
  - Configurer `setuptools` comme build-backend.
  - Définir les métadonnées (nom : `arrera-gazelle`, version : `4.0.0`).
  - Déclarer les dépendances strictes :
    ```toml
    [build-system]
    requires = ["setuptools>=61.0"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "arrera-gazelle"
    version = "4.0.0"
    description = "Interface graphique Tkinter des paramètres pour les assistants Arrera (compatible ANN v4)"
    readme = "README.md"
    requires-python = ">=3.10"
    dependencies = [
        "ann-core @ git+https://github.com/ANN-Framework/Arrera-Neuron-Network-Core.git@version4.0",
        "arrera-tk>=3.0.0",
        "customtkinter",
        "pillow"
    ]

    [tool.setuptools.packages.find]
    where = ["."]
    include = ["arrera_gazelle*"]

    [tool.setuptools.package-data]
    "*" = ["*.json", "*.png"]
    ```
- [ ] **Mettre à jour `requirements.txt`** pour les besoins de développement local :
  ```txt
  # Dépendance Core (en local : pip install -e ../ArreraNeuronNetwork)
  ann-core @ git+https://github.com/ANN-Framework/Arrera-Neuron-Network-Core.git@version4.0
  arrera-tk>=3.0.0
  customtkinter
  pillow
  ```

---

### 3. Modifications du code source (`arrera_gazelle.py`)

#### A. Importations externes
- [ ] Remplacer l'import local `from librairy.arrera_tk import *` par le module officiel :
  ```python
  from arrera_tk import *
  from tkinter import filedialog, messagebox
  ```
- [ ] Importer les modules du Core depuis `ann-core` :
  ```python
  from librairy.travailJSON import jsonWork
  from gestionnaire.gestion import gestionnaire
  ```

#### B. Adaptation aux méthodes Headless de `gestUserSetting`
Le Core v4 étant 100% headless (aucun appel `tkinter` dans `ann-core`), l'interface Gazelle doit se charger d'ouvrir les sélecteurs graphiques et passer les chemins obtenus :
- [ ] **Dossier de travail (`__addWorkFolder`)** :
  - Remplacer `self.__gestUser.setWorkFolder()` par :
    ```python
    folder = filedialog.askdirectory(title="Sélectionner le dossier de travail Arrera Work")
    if folder:
      if self.__gestUser.setWorkFolder(folder):
        messagebox.showinfo("Paramètres", "Le dossier de travail a bien été enregistré")
    ```
- [ ] **Dossier de téléchargement (`__addDownloadFolder`)** :
  - Remplacer `self.__gestUser.setVideoDownloadFolder()` par :
    ```python
    folder = filedialog.askdirectory(title="Sélectionner le dossier de téléchargement")
    if folder:
      if self.__gestUser.setVideoDownloadFolder(folder):
        messagebox.showinfo("Paramètres", "Le dossier de téléchargement a bien été enregistré")
    ```
- [ ] **Ajout de logiciels (`__addSoft`)** :
  - Dans ANN v4, `setSoft(soft: str, path: str)` requiert le chemin d'accès vers l'exécutable.
  - Ajouter la sélection de fichier :
    ```python
    path = filedialog.askopenfilename(
      title=f"Sélectionner le programme pour {soft}",
      filetypes=[("Exécutables / Applications", "*.*")]
    )
    if path:
      if self.__gestUser.setSoft(soft, path):
        messagebox.showinfo("Paramètres", "Le logiciel a bien été ajouté")
    ```

#### C. Adresses géographiques & météo (Nouvelle API v4)
- [ ] Remplacer les anciens appels dépréciés (`getAdresseDomicile`, `setAdresseDomicile`, `getLieuDomicile`, etc.) par les méthodes normalisées d'ANN v4 :
  - Domicile : `self.__gestUser.set_home_adresse(adresse, code_postal, ville)`
  - Travail : `self.__gestUser.set_work_adresse(adresse, code_postal, ville)`
  - Getters associés : `get_full_adress_home()`, `get_town_home()`, `get_postal_home()`, `get_full_adress_work()`, `get_town_work()`, `get_postal_work()`.
  - Mettre à jour l'interface pour permettre la saisie de l'adresse complète (rue, code postal, ville).

#### D. Gestion des modèles IA (Catalogue 9 modèles & Recommandation matérielle)
- [ ] **Catalogue étendu** :
  - Le catalogue v4 intègre désormais 9 modèles officiels (3 Gemma 4, 3 Mistral, 3 Qwen 2.5).
  - Vérifier que la liste déroulante et les fiches descriptives affichent correctement les 9 modèles via `get_list_model_ia_available()` et `get_data_model_ia_available(model)`.
- [ ] **Recommandation matérielle automatique** :
  - Utiliser `self.__gestUser.get_recommended_ia_model()` pour suggérer ou pré-sélectionner le modèle adapté à la configuration matérielle (RAM, VRAM, CPU).
- [ ] **Activation / Désactivation du mode IA** :
  - En v4, l'activation est déterminée par la présence d'un modèle actif (`set_ia_model(model)` charge l'IA et active le mode ; `set_ia_model("")` décharge l'IA).
  - Remplacer l'usage de l'ancien `set_use_ia()` (qui n'existe plus en v4) par la gestion du modèle actif.
- [ ] **Modèles personnalisés GGUF (optionnel)** :
  - Possibilité d'intégrer un champ pour télécharger un modèle GGUF via URL directe avec `download_custom_ia_model(name, url, description)`.

#### E. Synthèse vocale Piper TTS (Voix hors-ligne)
- [ ] **Sélection de voix** :
  - ANN v4 intègre le moteur Piper TTS avec voix sélectionnables.
  - Ajouter dans la section Micro/Audio de Gazelle un sélecteur permettant de choisir la voix de l'assistant :
    - Liste : `self.__gestUser.get_list_voice_available()`
    - Voix active : `self.__gestUser.get_voice_selected()`
    - Sauvegarde : `self.__gestUser.set_voice(voice)`

---

### 4. Mise à jour des scripts de test et d'exemple

- [ ] **Mettre à jour `src/setting_assistant.py` et `main.py`** :
  - Adapter l'instanciation de `confNeuron` en retirant les paramètres supprimés en v4 (`assistant_color`, `assistant_texte_color`).
  - Utiliser les nouvelles importations modulaires :
    ```python
    from arrera_tk import aTk
    from arrera_gazelle import arrera_gazelle
    from config.confNeuron import confNeuron
    from gestionnaire.gestion import gestionnaire
    ```

---

### 5. Documentation
- [ ] Mettre à jour `README.md` et `README_en.md` pour refléter l'installation via `pip install arrera-gazelle` et l'intégration avec `ann-core` v4.
