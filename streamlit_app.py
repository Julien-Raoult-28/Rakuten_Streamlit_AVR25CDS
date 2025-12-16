from importlib.resources import path
import streamlit as st
import joblib


st.set_page_config(
    page_title="Rakuten AVR25CDS",   # titre affiché dans l'onglet du navigateur
    page_icon="images/favicon_Rakuten.png",             # emoji ou chemin vers une icône .png
    layout="centered"               # optionnel : wide ou centered
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

    pages = ["Présentation du projet","Exploration", "Préparation", "Modélisation","Tester le modèle"]
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
&nbsp;&nbsp;&nbsp;&nbsp;• Suréchantillonnage des classes minoritaires (duplucation de lignes, trduction en anglais,
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

#---------------------------------------PAGE MODELISATION -----------------------------------------
if page == pages[3] : 
  affiche_bandeau("Modélisation sur le texte", "#bf0000")
  st.write("""

#### Notre modèle se caractérise en 4 points :  
1🔹 TF-IDF sur les mots  
2🔹 TF-IDF sur les caractères  
3🔹 Features heuristiques spécifiques aux jeux vidéo  
4🔹 SVM linéaire (LinearSVC)  
5🔹 Résultat du modèle lors du test

---

#### 1🔹 TF-IDF sur les mots  
           
🔸 TF-IDF signifie Term Frequency – Inverse Document Frequency.  
🔸 Il transforme chaque texte en vecteur numérique où chaque dimension
correspond à un mot ou un bigramme (paire de mots).  
🔸 L’idée :  
&nbsp;&nbsp;&nbsp;&nbsp;• TF (Term Frequency) : un mot fréquent dans un texte obtient un score
élevé.  
&nbsp;&nbsp;&nbsp;&nbsp;• IDF (Inverse Document Frequency) : un mot très courant dans tous les
textes (comme “le”, “et”) est moins important.  
🔸 Résultat : les mots qui sont spécifiques et informatifs pour une catégorie de
produit ont plus de poids.  
           
#### 2🔹 TF-IDF sur les caractères  
           
🔸 Même principe que TF-IDF sur les mots, mais appliqué à des séquences de
caractères (3 à 5 lettres consécutives).  
🔸 Objectif :  
&nbsp;&nbsp;&nbsp;&nbsp;• Capturer des variantes orthographiques, fautes de frappe ou abréviations.  
&nbsp;&nbsp;&nbsp;&nbsp;• Exemple : “PlayStation” → “pla”, “lay”, “ays”, …  
&nbsp;&nbsp;&nbsp;&nbsp;• Utile quand les noms de produits peuvent être écrits de façons légèrement  
différentes.  
           
#### 3🔹 Features heuristiques spécifiques aux jeux vidéo  
           
🔸 Ce sont des indicateurs binaires (0 ou 1) ajoutés aux vecteurs TF-IDF pour
enrichir le modèle.  
🔸 Exemple d’indicateurs :  
&nbsp;&nbsp;&nbsp;&nbsp;• Présence de plateformes : ps4, xbox, switch, etc.  
&nbsp;&nbsp;&nbsp;&nbsp;• Présence de éditeurs : Ubisoft, EA, Rockstar…  
&nbsp;&nbsp;&nbsp;&nbsp;• Présence de franchises célèbres : Fifa, Call of Duty, Zelda…  
&nbsp;&nbsp;&nbsp;&nbsp;• Indicateurs édition spéciale : collector, deluxe, goty…  
&nbsp;&nbsp;&nbsp;&nbsp;• Présence de PEGI ou d’une année de sortie récente (>2000)  
           
🔸 Ces features aident le modèle à différencier les jeux vidéo des autres produits,
comme les films ou les livres. 
            
Exemple avec le mot nintendo dans un texte : Dans les features heuristiques GameHeuristicFeatures : « nintendo » est dans la liste platform_kw. Si le texte contient ce
mot (après mise en minuscules et suppression des accents), la feature has_platform
prend la valeur 1. Cela ajoute une information binaire supplémentaire au vecteur de
caractéristiques. Les deux types de signaux (poids TF-IDF et indicateur binaire) sont
fusionnés dans FeatureUnion et passés au classifieur LinearSVC. Le SVM ne décide pas
directement « nintendo = catégorie X », mais il utilise ces valeurs comme entrées pour
calculer un score pour chaque classe. Si « nintendo » est fortement corrélé à une
catégorie dans les données d’entraînement, son poids et/ou l’indicateur binaire vont
influencer la décision finale en faveur de cette catégorie.  
           
#### 4🔹 SVM linéaire (LinearSVC)  
           
🔸 SVM (Support Vector Machine) : un modèle qui sépare les données en
différentes catégories en trouvant une frontière optimale dans l’espace des
caractéristiques.  
🔸 LinearSVC : SVM avec un hyperplan linéaire, efficace pour les grands vecteurs
creux (comme les TF-IDF).  
🔸 Avantages :  
&nbsp;&nbsp;&nbsp;&nbsp;• Rapide et efficace pour des données textuelles volumineuses.  
&nbsp;&nbsp;&nbsp;&nbsp;• Gère les classes déséquilibrées grâce à class_weight="balanced".  
(Contradictoire avec notre rééquilibrage des classes en sur ou sous
dimensionnant mais nous nous en sommes rendu compte après la phase de
préparation des données. Donc le rééquilibrage sera supprimé de la phase
préparatoire et class_weight="balanced" sera directement dans le modèle
d'entraînement)  
&nbsp;&nbsp;&nbsp;&nbsp;• Peut être combiné avec des features supplémentaires (TF-IDF +
heuristiques).  
           
**En gros, le pipeline fonctionne ainsi :**   
🔸 1.Transformer chaque texte en vecteur numérique avec TF-IDF sur mots +
caractères.  
🔸 2.Ajouter des features spécifiques aux jeux vidéo.  
🔸 3.Le SVM linéaire apprend à séparer les catégories de produits dans cet espace
de caractéristiques et gère le déséquilibre des classes.  
         
#### 5🔹 Résultat du modèle lors du test 
🔸 Le modèle obtient un F1-score de 82,91%, dépassant l'objectif de 81,13%  
🔸 Le modèle est moins performant sur l'univers des jeux (jeux vidéos, Jeux de
rôles, jeux de société) et les livres (Livres loisirs & société, Littérature, Lots livres &
magazines)  
🔸 Prochaine étape :  
&nbsp;&nbsp;&nbsp;&nbsp;• Analyser les mauvaises prédictions, trouver des features pour aider le
modèle à mieux prédire ces classes.  
&nbsp;&nbsp;&nbsp;&nbsp;• Entraîner le modèle en utilisant un GPU pour accélérer les calculs.  
&nbsp;&nbsp;&nbsp;&nbsp;• Tester les performances du modèle sur GPU et CPU.  
&nbsp;&nbsp;&nbsp;&nbsp;• Entraîner et évaluer le modèle avec CamemBERT et Random Forest pour
comparer leurs performances avec le modèle actuel TF-IDF + LinearSVC.   
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
