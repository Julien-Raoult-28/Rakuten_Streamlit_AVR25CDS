from importlib.resources import path
import streamlit as st
import joblib


st.set_page_config(
    page_title="Rakuten AVR25CDS",   # titre affiché dans l'onglet du navigateur
    page_icon="images/favicon_Rakuten.png",             # emoji ou chemin vers une icône .png
    layout="wide"               # optionnel : wide ou centered
)

st.markdown("""
    <div style="
    position: fixed;   /* fixe le bandeau en haut */
    top: 60px;
    left: 100px;
    width: 100%;       /* s'étend sur toute la largeur */
    height: 70px;      /* hauteur du bandeau */
    display: flex;     /* active Flexbox */
    align-items: center; /* centre verticalement */
    justify-content: center; /* centre horizontalement */
    background-color: #efefef; 
    z-index: 1000;      /* pour rester au-dessus des autres éléments */
">
    <h3 style="color: #bf0000; margin: 0;">
        Classification des données produits multimodales de Rakuten France
    </h3>
</div>

<!-- Evite que le contenu soit caché par le bandeau -->
<div style="margin-top:70px;"></div>
""", unsafe_allow_html=True)

# --- TRAIT SEPARATION ---

st.markdown("""
            ---
  """, unsafe_allow_html=True)

# --------------------- STYLE PERSONNALISÉ POUR LE MENU DE GAUCHE SIDEBAR ---
st.markdown("""
    <style>
    /* Couleur de fond de la sidebar */
    section[data-testid="stSidebar"] {
        background-color: #efefef;   
    }

    /* Couleur du texte dans la sidebar */
    section[data-testid="stSidebar"] * {
        color: #bf0000 !important;    
    }
    </style>
""", unsafe_allow_html=True)




# === LOGO + SOMMAIRE DANS LA SIDEBAR ===
# --- Sidebar ---
with st.sidebar:
    st.image("images/rakuten.png", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("Sommaire")

    pages = ["Présentation du projet","Exploration", "Préparation", "Modélisation - texte", "Modélisation - image","Tester le modèle"]
    page = st.radio("", pages)

    # --- Auteurs ---
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        """
        **Auteurs :**  
        Angella FONTAINE  
        Fatiha IDDER  
        Julien RAOULT
        """,
        unsafe_allow_html=True
    )


# --- TITRE DE CHAQUE PAGE ---
def affiche_bandeau(titre, couleur_fond="#bf0000"):
    st.markdown(f"""
        <div style="
            /*background-color: {couleur_fond};*/
            padding: 3px;
            border-radius: 5px;
            text-align: center;
            height:60px;
        ">
            <h3 style="color: #bf0000; margin: 0;">{titre}</h3>
        </div>
        <br>
    """, unsafe_allow_html=True)



# === CONTENU DES PAGES ===
#---------------------------------------PAGE PRESENTATION DU PROJET -----------------------------------------
if page == pages[0] : 
  affiche_bandeau("Présentation du projet", "#bf0000")
  st.write("""
###  Contexte Rakuten  

Rakuten est un des plus grands acteurs mondiaux du e-commerce, créé en 1997, 
avec plus de **1,3 milliard d’utilisateurs** dans son écosystème international.
Le **Rakuten Institute of Technology (RIT)** mène des recherches en apprentissage automatique,
vision par ordinateur, NLP et HCI, avec des équipes à Tokyo, Paris, Boston, Singapour et Bengaluru.  
           
### Objectif du projet  
           
Créer un modèle capable de **classer automatiquement les produits** du catalogue Rakuten France
dans leur code type produit (prdtypecode), en utilisant du texte (titre, description) et/ou des images.
C’est un problème de **classification multimodale** à grande échelle.  
           
### Contexte du challenge  

Catégoriser les produits est un enjeu crucial pour les marketplaces (recherche, recommandation, compréhension des requêtes).
Les approches manuelles ou basées sur des règles ne sont pas scalables.
Le défi est difficile à cause de :  
&nbsp;&nbsp;&nbsp;&nbsp;• Données textuelles bruyantes  
&nbsp;&nbsp;&nbsp;&nbsp;• Images variées et hétérogènes  
&nbsp;&nbsp;&nbsp;&nbsp;• Grand nombre de classes  
&nbsp;&nbsp;&nbsp;&nbsp;• Distribution déséquilibrée  
&nbsp;&nbsp;&nbsp;&nbsp;• Qualité inégale des informations fournies par les vendeurs  
Le challenge consiste à exploiter texte + image pour construire un classifieur performant.  
           
### Description du problème  

Pour chaque produit (avec titre, image, parfois description), prédire son prdtypecode.  
Exemple : Klarstein Présentoir 2 Montres… → catégorie produit 1500.  
Les données ressemblent à :  
&nbsp;&nbsp;&nbsp;&nbsp;• Designation : titre du produit  
&nbsp;&nbsp;&nbsp;&nbsp;• Description : texte descriptif (souvent manquant)  
&nbsp;&nbsp;&nbsp;&nbsp;• Productid et imageid : permettent de retrouver l’image  
&nbsp;&nbsp;&nbsp;&nbsp;• Image : une seule image par produit  
&nbsp;&nbsp;&nbsp;&nbsp;• Prdtypecode : label à prédire  
           
### Jeu de données  

Rakuten fournit environ 99 000 produits :  
&nbsp;&nbsp;&nbsp;&nbsp;• X_train (84 916) : textes + images  
&nbsp;&nbsp;&nbsp;&nbsp;• Y_train : prdtypecode pour chaque id  
&nbsp;&nbsp;&nbsp;&nbsp;• X_test (13 812) : textes + images à prédire  
&nbsp;&nbsp;&nbsp;&nbsp;• images.zip : dossier contenant toutes les images (train/test séparées)  
           
### Objectif  
L'objectif est d'obtenir un F1-score supérieur à **0,8113 sur les données textuelles**.  
Pour les **images**, l'objectif est d'atteindre un F1-score supérieur à **0,5534**.
""")
#---------------------------------------PAGE EXPLORATION DE LA DONNEE -----------------------------------------
if page == pages[1] : 
  affiche_bandeau("Exploration des données", "#bf0000")
  st.write("""
### Exploration de la donnée textuelle  

#### 🔎 Visualisation du dataset  
Structure du dataset X  
""")
  st.image("images/Visualisation_X.png", use_container_width=True)
  st.write("""
Structure du dataset Y  
""")
  st.image("images/Visualisation_Y.png", use_container_width=False)
  st.write("""
#### ✅ Qualité de la donnée 
Lors de l'exploration du dataset nous identifions plusieurs problèmes de qualité de
données. Pour chaque problème nous décidons des actions à entreprendre dans la phase de
préparation des données.  
           
**1🔹 Valeurs manquantes**  
            
Nous remarquons plusieurs valeurs manquantes dans la colonne description (35% des données). Le champ
désignation est quant à lui toujours renseigné. Plusieurs stratégie s'offrent à nous :  
&nbsp;&nbsp;&nbsp;&nbsp;• Imputation par une chaîne vide ou une valeur par défaut (ex: "Pas de description
disponible").  
&nbsp;&nbsp;&nbsp;&nbsp;• Suppression des lignes si le pourcentage reste gérable après analyse.  
&nbsp;&nbsp;&nbsp;&nbsp;• Concaténation de la colonne désignation avec description pour créer un seul champ texte.  
           
Après des textes de modélisation lors de la phase de test nous remarquons de meilleurs résulats
lorsque nous concaténons les deux champs. Nous choisissons donc cette stratégie.  
           
**2🔹 Répartition des classes (prdtypecode)**  
           
Nous observons un déséquilibre important entre les différentes classes. Certaines classes
sont surreprésentées tandis que d'autres sont très peu présentes. Cela peut biaiser le
modèle lors de l'entraînement.  
""")
  st.image("images/Repartition_des_classes.png", use_container_width=False)
  st.write("""
Plusieurs options sont possibles :  
&nbsp;&nbsp;&nbsp;&nbsp;• Suréchantillonnage des classes minoritaires (duplication de lignes, trduction en anglais,
re-traduction en français)  
&nbsp;&nbsp;&nbsp;&nbsp;• Sous-échantillonnage des classes majoritaires (suppression de lignes)  
&nbsp;&nbsp;&nbsp;&nbsp;• Utilisation de techniques avancées comme SMOTE pour générer des exemples synthétiques.  
&nbsp;&nbsp;&nbsp;&nbsp;• Utilisation de class_weight dans le modèle pour gérer le déséquilibre.  
  
Après différents tests nous optons pour un class_weight="balanced" avec LinearSVC.  
           
**2🔹 Détection des langues**  
           
Nous constatons la présence de plusieurs langues dans les champs textes (français, anglais,
espagnol, italien, allemand...). Pour l'efficacité du modèle nous décidons de tout
traduire en français.  
           
**🔹 Balises HTML et Stopwords dans les textes**  
           
Nous remarquons la présence de balises HTML dans les champs textes. Elles n'apportent
aucune valeur ajoutée pour le modèle et sont même contre-productives. Nous décidons de toutes les
supprimer.  
Les Stopwords sont des mots courants (le, la, et, de, à...) qui n'apportent pas
d'information pertinente pour la classification. Nous décidons de les supprimer aussi.  
""")
  st.image("images/Stopwords.png", use_container_width=True)
  st.write("""
**🔹 Conclusion**  

L'analyse exploratoire des données nous montre qu'il est très important avant de commencer
l'entraînement du modèle de passer par une phase de préparation des données rigoureuse.  
Nous remarquons plusieurs problèmes de qualité de données dans le dataset textuel. Nous
avons identifié des stratégies pour chaque problème qui seront mises en œuvre dans la phase
de préparation des données afin d'améliorer la qualité des données avant l'entraînement du
modèle.  
           
---  
### Exploration de la donnée image  
           
A venir ...
""")

#---------------------------------------PAGE PREPARATION DE LA DONNEE -----------------------------------------
if page == pages[2] : 
  affiche_bandeau("Préparation des données", "#bf0000")
  st.write("""
### Split des données
Après l'exploration nous décidons de splitter nos données répartit en 80% (train) et 20%
(test) avant le nettoyage des données.  
Nous générons donc 2 fichiers à partir de \"X_train_update.csv\" (fichier source original) :  
🔹 \"X_train_non_nettoye_80.csv\"  
🔹 \"X_test_non_nettoye_20.csv\"

---
### Préparation des données X_train_80

Suite à l'analyse exploratoire des données nous avons identifié plusieurs actions à faire
dans la préparation des données avant de commencer à entraîner le modèle.

**1🔹 Création d'une colonne fusionnée de \"designation\" et \"description\"**  

Nous avons constaté environ que 35% des données de \"description\" étaient vides. Donc
nous avons fait le choix de fusionner les colonnes \"designation\" et \"description\" qui sont
toutes deux des champs textes. Nous ne supprimons pas la colonne \"description\" car elle
contient des données complémentaires à \"designation\" qui permettront au modèle
d'être plus performant.

**2🔹 Supprimer les balises HTML**  

Nous avons relevé la présence de balises HTML dans le champ \"description\". Elles n'ont
pas d'utilité pour le modèle et sont même contre-productives. Par conséquent nous
supprimons toutes les balises présentes.

**3🔹 Détection de la langue (ajout d'une colonne précisant la langue)**  

L'exploration a remonté la présence de texte en différentes langues. Donc nous ajoutons
une étape qui prédit la langue présente dans le texte et la précise dans une colonne
ajoutée. Ceci permettra par la suite de traduire en français toutes les lignes qui ne sont
pas en \"fr\".  
Certaines données sont en plusieurs langues. Exemple : une description en français avec
des mots anglais. Pour ce type de cas nous identifions la donnée comme \"fr\" et donc non
traduite.

**4🔹 Traduction des champs non fr (s'exécute que si la nouvelle colonne langue** 
n'est pas en \"fr\")

Pour la traduction nous utilisons GoogleTranslator et faisons une sauvegarde toutes les
200 lignes traduites pour ne pas perdre l'avancée en cas d'échec.

**5🔹 Suppression de la ponctuation et des stopwords** 

Certains mots viennent polluer le modèle comme \"le\", \"la\", \"et\" etc... Nous supprimons
ces mots (stop words). Nous supprimons tous les accents, la ponctuation. On met tout en
minuscules. On supprime les espaces en trop, les répétitions.  
Nous faisons des exceptions où nous transformons \"n°\" en \"numero\" car cette donnée
est utile pour la prédiction des magazines. Nous gardons les chiffres car ils sont aussi
utiles pour les magazines, jeux vidéo.

**6🔹 Rééquilibrage des classes**  
           
L'exploration a mis en évidence un déséquilibre des classes. Donc nous utiliserons plutôt  
un **class weight = balanced** dans le modèle qui gérera ce déséquilibre des classes.

**7🔹 Ensuite nous gardons que les colonnes utiles pour le modèle et sauvegardons
un fichier \"X_train_80_clean.csv\"**

---
### Préparation des données X_test_20
Nous appliquons quasiment le même code que pour X_train_80 sauf que nous ne faisons
pas de rééquilibrage des classes donc les étapes sont les suivantes :  

1🔹 Création d'une colonne fusionnée de \"designation\" et \"description\"  
2🔹 Supprimer les balises HTML  
3🔹 Détection de la langue (ajout d'une colonne précisant la langue)  
4🔹 Traduction des champs non fr (s'exécute que si la nouvelle colonne langue
n'est pas en "fr")  
5🔹 Suppression de la ponctuation et des stopwords  
6🔹 Ensuite nous gardons que les colonnes utiles pour le test et sauvegardons un
fichier \"X_test_20_clean.csv\"
        """
    )


#---------------------------------------PAGE MODELISATION TEXTE-----------------------------------------
if page == pages[3] : 
  affiche_bandeau("Modélisation sur le texte", "#bf0000")
  st.write("""

#### 🔹 Choix des données  

Dans un premier temps, nous avons utilisé des données préparées vues précédemment :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• **Nettoyage des balises HTML** pour ne conserver que le texte pertinent.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Suppression des **stopwords**.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• **Traduction** des textes en français afin d’uniformiser le langage.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Concaténation des champs **designation** et **description** en une seule colonne texte.           
 
Ensuite, pour gérer le déséquilibre des classes, nous avons choisi d’harmoniser la
volumétrie par classe entre **1000 et 4000 produits**.Donc pour les classes 
surdimensionnées nous avons effectué des suppressions de données et pour les classes 
sous dimensionnées nous avons dupliqué aléatoirement des lignes. 

---

####  🔹 Entraînement de modèles 

Le modèle initial consistait en une vectorisation TF-IDF combinée à un modèle de classification 
Logistic Regression, entraîné sur les données préparées du champ concaténant designation et description.  
Ce modèle a atteint un score f1 weighted **78,39 %**.  
Ensuite, nous avons testé **TF-IDF combiné à LinearSVC**, avec un score de **78,55 %**.  
""")
  st.image("images/Matrice_confusion_texte.png", use_container_width=True)    
  st.write("""      
Après analyse des erreurs via une matrice de confusion, nous avons remarqué que certaines
catégories étaient souvent confondues entre elles, notamment les sous-catégories de Livres et de Jeux vidéo.
Pour tenter d’améliorer les performances, nous avons ajouté des features
spécifiques pour ces catégories.  

De plus nous avons fait machine arrière pour gérer le déséquilibre des classes en choisissant de tout garder mais 
d’utiliser class_weight="balanced" dans le LinearSVC. Nous avons aussi ajouté des paramètres à TF-IDF 
sur les mots et les caractères (word_tfidf et char_tfidf) : **Score : 81,72%**  

---

####  🔹 Optimisation des paramètres  

Pour continuer, nous avons testé plusieurs paramètres différents pour **TF-IDF** et **LinearSVC** :  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Word n-gram : 1,2 / 1,3  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Char n-gram : 3,5 / 2,4 / 4,6  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Max features : 120 000 / 80 000 / 150 000  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Min_df : 1 / 2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• LinearSVC C : 1.5 / 1.6 / 1.8 / 2.0  

**Meilleure combinaison retenue** :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•  Word n-gram : 1,2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•  Char n-gram : 3,5  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•  Max features : 120 000  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•  Min_df : 1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•  LinearSVC C : 1.5  

Pour un score de **83,06 %**.

---

####  🔹 Tests de modèles Deep Learning  

Ensuite nous avons voulu essayer des modèles de deep learning (XGBoost, Random Forest, CamenBERT). 
La difficulté est surtout liée à nos machines. Nous n’étions pas assez bien équipés pour lancer des
modèles de ce type : l’entraînement dure des heures, la mémoire surcharge et l'entraînement s'arrête,
sur des GPU cloud des time-out nous freinaient dans nos apprentissages.  

Nous avons tant bien que mal réussi à avoir des résultats mais avec le minimum de paramètres :   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•  XGBoost : 79%  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•  CamenBERT : 77%  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;•  Random Forest : jamais réussi à aller au bout.    

---

#### 🔹 Amélioration du modèle TF-IDF + LinearSVC  

Étant bloqué par la puissance de nos machines nous avons tenté d’améliorer le modèle TF-IDF + LinearSVC.
N’y arrivant pas, nous prenons la décision de tester notre meilleur modèle sur les données brut tel quel
et ensuite avancer par étape pour la transformation des données :   
""")
  st.markdown("""
&nbsp;&nbsp;&nbsp;&nbsp;• Données brut - sur champ désignation :
<span style='color:green; font-weight:bold;'>⭡ 83,75%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données sans balise HTML et Stopwords :
<span style='color:red; font-weight:bold;'>⭣ 82,38%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données brut - sur champ désignation sans Features dans le modèle :
<span style='color:green; font-weight:bold;'>⭡ 83,70%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données sans balise HTML et Stopwords sans Features dans le modèle :
<span style='color:red; font-weight:bold;'>⭣ 82,40%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données brut - sans features - désignation+description :
<span style='color:green; font-weight:bold;'>⭡ 84,92%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données brut - sans features - désignation avec 2 fois plus de poids que description :
<span style='color:green; font-weight:bold;'>⭡ 85,61%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données brut - sans features - désignation avec 3 fois plus de poids que description :
<span style='color:green; font-weight:bold;'>⭡ 85,71%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données brut - sans features - désignation avec 4 fois plus de poids que description :
<span style='color:green; font-weight:bold;'>⭡ 85,75%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données brut - sans features - désignation avec 5 fois plus de poids que description :
<span style='color:red; font-weight:bold;'>⭣ 85,70%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données brut - sans features - désignation x4 + description + unité de mesure :
<span style='color:green; font-weight:bold;'>⭡ 85,81%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données brut - sans features - désignation x4 + description + unité de mesure + ajout de poids des 3 premiers mots de désignation :
<span style='color:green; font-weight:bold;'>⭡ 86,06%</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Données brut - sans features - désignation x4 + description + unité de mesure + ajout de poids des 3 premiers mots de désignation : changement de méthode (pondération directement dans le TF-IDF) : Meilleur score : <span style='color:green; font-weight:bold;'>⭡ 86,22%</span>  
Je ne fais plus de concaténation à la main mais je choisis une approche Pipeline + ColumnTransformer, donc chaque feature est une méthode indépendante, bien séparée, traçable et réutilisable.
""", unsafe_allow_html=True)

  st.image("images/Graphique_des_modeles.png", use_container_width=True)  


  st.write("""
---

####  🔹 Soumission au challenge  

Nous avons soumis notre meilleur modèle en phase de test au challenge Rakuten et obtenu le score de **87,41%**. Pour rappel il fallait un score de 81,13% pour la réussite de ce challenge.  

---

#### 🔹 Autres modèles  

Nous avons souhaité tester notre meilleur modèle sur les données d'entraînement en regroupant certaines classes. Toutes les classes concernant les livres en une seule classe et pareil pour les jeux vidéo et consoles. Nous avons aussi regroupé en une seule classe les jeux de sociétés et les jouets pour enfants :   

&nbsp;&nbsp;&nbsp;&nbsp;• **Livres** : Livres loisirs et société + Lots Livres & Magazines + Magazines + Livres littérature et fiction  
&nbsp;&nbsp;&nbsp;&nbsp;• **Jeux vidéo** : Jeux vidéo + Accessoires jeux vidéo + Jeux vidéo & Consoles + Lots consoles & jeux  
&nbsp;&nbsp;&nbsp;&nbsp;• **Jeux & Enfants** : Jouets & Enfant + Jeux de société  
  
**Score obtenu : 90,91 %**.

""")
#---------------------------------------PAGE MODELISATION TEXTE-----------------------------------------
if page == pages[4] : 
  affiche_bandeau("Modélisation sur le texte", "#bf0000")
  st.write("""
           

""")
#---------------------------------------PAGE TESTER LE MODELE (version simplifiée) -----------------------------------------


if page == "Tester le modèle":
    import os
    import re
    import joblib
    import streamlit as st
    import pandas as pd
    import requests

    st.header("Tester le modèle")
    st.write("Entrez la désignation et la description du produit pour prédire sa catégorie :")

    # =========================
    # Inputs utilisateur
    # =========================
    designation_input = st.text_input("Désignation produit")
    description_input = st.text_area("Description produit", height=150)

    # ============================================================
    # FONCTIONS CUSTOM (nécessaires pour joblib.load)
    # ============================================================
    UNIT_PATTERN = r"(cm|mm|m|kg|g|mg|l|ml|cl|w|kw|v|mah|ah|hz|ghz|mhz|go|gb|to|tb|mp|px|fps|°c|°)"

    def get_designation(X):
        return X["designation"].fillna("").astype(str)

    def get_description(X):
        return X["description"].fillna("").astype(str)

    def first_words_series(X, n=3):
        return (
            X["designation"]
            .fillna("")
            .astype(str)
            .str.lower()
            .str.split()
            .str[:n]
            .str.join(" ")
        )

    def numbers_units_series(X):
        return (
            X["designation"]
            .fillna("")
            .astype(str)
            .str.lower()
            .str.findall(rf"\b\d+[.,]?\d*\s?{UNIT_PATTERN}\b")
            .str.join(" ")
        )

    # =========================
    # Chargement du modèle depuis Dropbox
    # =========================
    MODEL_URL = (
        "https://www.dropbox.com/scl/fi/oole37javo3jpageyx80v/"
        "modele_final_rakuten.pkl?rlkey=wh7c65m17gyivk7wy0jgu377k&dl=1"
    )
    MODEL_PATH = "modele_final_rakuten.pkl"

    @st.cache_resource
    def load_pipeline():
        if not os.path.exists(MODEL_PATH):
            with st.spinner("📥 Téléchargement du modèle..."):
                r = requests.get(MODEL_URL)
                r.raise_for_status()
                with open(MODEL_PATH, "wb") as f:
                    f.write(r.content)
        return joblib.load(MODEL_PATH)

    pipe = load_pipeline()

    # =========================
    # Chargement du mapping
    # =========================
    BASE_DIR = os.path.dirname(__file__)
    mapping_path = os.path.join(BASE_DIR, "Y_train_encode.csv")

    mapping_df = pd.read_csv(mapping_path)
    mapping_df = mapping_df.drop_duplicates(subset=["prdtypecode_encoded"])

    mapping = mapping_df.set_index("prdtypecode_encoded")["libelle_type_code"].to_dict()

    # =========================
    # Prédiction
    # =========================
    if st.button("Valider"):
        if not designation_input.strip() and not description_input.strip():
            st.warning("Veuillez saisir au moins la désignation ou la description.")
        else:
        # Création d'un DataFrame 1 ligne pour respecter le format du pipeline
            input_df = pd.DataFrame([{
                "designation": designation_input,
                "description": description_input
            }])

        # Prédiction
            pred = pipe.predict(input_df)[0]
            label = mapping.get(pred)

            if label:
                st.success(f"🔹 Catégorie prédite : **{label}**")
            else:
                st.success("🔹 Catégorie prédite : Non disponible")
