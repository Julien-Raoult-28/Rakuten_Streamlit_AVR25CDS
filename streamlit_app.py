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

# --------------------------------------------- STYLE PERSONNALISÉ POUR LE MENU DE GAUCHE SIDEBAR ---------------------------------------------------------------------------
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

    pages = ["Présentation du projet","Exploration et préparation", "Modélisation - texte", "Tester le modèle texte", "Modélisation - image","Tester le modèle image", "Perspectives"]
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
#---------------------------------------------------------------PAGE PRESENTATION DU PROJET -----------------------------------------------------------------------------
#---------------------------------------------------------------PAGE PRESENTATION DU PROJET -----------------------------------------------------------------------------
#---------------------------------------------------------------PAGE PRESENTATION DU PROJET -----------------------------------------------------------------------------
#---------------------------------------------------------------PAGE PRESENTATION DU PROJET -----------------------------------------------------------------------------
#---------------------------------------------------------------PAGE PRESENTATION DU PROJET -----------------------------------------------------------------------------
#---------------------------------------------------------------PAGE PRESENTATION DU PROJET -----------------------------------------------------------------------------
#---------------------------------------------------------------PAGE PRESENTATION DU PROJET -----------------------------------------------------------------------------
if page == pages[0] : 
  affiche_bandeau("Présentation du projet", "#bf0000")
  st.markdown("""
<style>
/* Centrage horizontal des onglets */
div[data-baseweb="tab-list"] {
    justify-content: center;
    gap: 24px;   /* espace horizontal entre les onglets */
}

/* Bouton d’onglet */
button[data-baseweb="tab"] {
    padding-top: 8px;
    padding-bottom: 10px;
    min-height: 72px;
}

/* Texte des onglets */
button[data-baseweb="tab"] > div {
    font-size: 14px;
    font-weight: 600;
    text-align: center;
    white-space: pre-line;
    line-height: 1.2;
}

/* Onglet actif */
button[data-baseweb="tab"][aria-selected="true"] > div {
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)


  tabs = st.tabs([
        "🏢\nContexte Rakuten",
        "🏁\nObjectif du projet",
        "💼\nContexte métier",
        "⚙️\nContexte technique",
        "💶\nContexte économique",
        "🔬\nContexte scientifique"
    ])
  
###  Contexte Rakuten --------------------------------------------------------------------------------------------
  with tabs[0]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;          
    ">
 

Rakuten est un des plus grands acteurs mondiaux du e-commerce, créé en 1997, 
avec plus de **1,3 milliard d’utilisateurs** dans son écosystème international.  
                
Le **Rakuten Institute of Technology (RIT)** mène des recherches en apprentissage automatique,
vision par ordinateur, NLP et HCI, avec des équipes à Tokyo, Paris, Boston, Singapour et Bengaluru.  
</div>
""", unsafe_allow_html=True)    
          
### Objectif du projet  ------------------------------------------------------------------------------------------------
  with tabs[1]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;       
    ">
                       
Créer un modèle capable de **classer automatiquement les produits** du catalogue Rakuten France
dans leur code type produit (prdtypecode), en utilisant du texte (titre, description) et/ou des images.
C’est un problème de **classification à grande échelle**.  
                
L'objectif est d'obtenir un F1-score supérieur à **0,8113 sur les données textuelles**.  
Pour les **images**, l'objectif est d'atteindre un F1-score supérieur à **0,5534**.  
</div>
""", unsafe_allow_html=True)    
            
### Contexte métier  ------------------------------------------------------------------------------------------------
  with tabs[2]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;        
    ">
                  
Le challenge Rakuten vise à automatiser la classification de produits e‑commerce à partir
d’images et de descriptions textuelles.  
                
**Dans un contexte opérationnel, cette automatisation permet :**  

<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> D’accélérer la mise en ligne des produits.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> De réduire les erreurs de catégorisation.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> D’améliorer la qualité des listings.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> D’optimiser le référencement interne et la navigation client.   
</ul>
</div>
""", unsafe_allow_html=True) 
               
### Contexte technique------------------------------------------------------------------------------------------------
  with tabs[3]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;          
    ">
                   
<strong>Le projet repose sur :</strong>  
           
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Un dataset de <strong>84 916 annonces et images</strong>.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Une variable cible (prdtypecode) comportant <strong>27 classes déséquilibrées</strong>.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Des descriptions textuelles de longueur très variable (de 0 à 12 451 caractères),
incluant des balises HTML, des langues multiples et des stopwords, ce qui
complexifie leur traitement direct.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Des images hétérogènes souvent bruitées, floues ou sombres.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Un environnement limité ( <strong>CPU 4 cœurs, pas de GPU</strong>), nécessitant des solutions
optimisées pour garantir des performances élevées malgré les ressources restreintes.  
</ul>
</div>
""", unsafe_allow_html=True) 
               
### Contexte économique  ------------------------------------------------------------------------------------------------
  with tabs[4]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;          
    ">
                    
**La catégorisation manuelle est coûteuse :**  
           
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong>Charge humaine</strong> : Processus chronophage nécessitant une intervention manuelle
pour chaque produit.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong>Risque d’erreur</strong> : Taux d’erreur élevé en raison de la subjectivité et de la complexité
des 27 classes.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong>Impact direct</strong> : Les erreurs de catégorisation réduisent la visibilité des produits,
affectant la conversion et la satisfaction client.  
</ul>
</div>
""", unsafe_allow_html=True) 
    
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;          
    ">     
                      
**Un modèle performant permet de :**  
           
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Réduire les coûts opérationnels liés à la catégorisation manuelle.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Améliorer la qualité et la cohérence des listings.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Augmenter le taux de conversion grâce à un référencement interne optimisé.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Offrir une meilleure expérience utilisateur via une navigation intuitive.  
</ul> 
</div>
""", unsafe_allow_html=True)  
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;          
    ">     
                                    
**Bénéfices d’un modèle automatisé :**  
           
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Gain de temps significatif : Réduction du temps de traitement.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Réallocation des ressources : Les équipes peuvent se concentrer sur des tâches
à plus forte valeur ajoutée (ex : optimisation des fiches produits, stratégie marketing).  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Réduction des coûts opérationnels : Moins d’heures consacrées à la
catégorisation manuelle et aux corrections.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Amélioration de la réactivité : Mise en ligne plus rapide des nouveaux produits,
ce qui booste la compétitivité et la satisfaction client.  
</ul>
</div>
""", unsafe_allow_html=True) 
    
### Contexte scientifique------------------------------------------------------------------------------------------------
  with tabs[5]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;         
    ">
                 
**Le projet s’inscrit dans plusieurs domaines clés du machine learning et de la data science :**  
           
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong>Vision par ordinateur</strong> : pour analyser des images hétérogènes et extraire des
features visuelles robustes.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong> Transfer learning</strong> : pour adapter des modèles pré-entraînés (ex : MobileNetV2) aux
contraintes du projet (27 classes, pas de GPU).  
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong> Détection d’outliers</strong> : pour identifier et écarter les images inutilisables (floues,
sombres, mal cadrées) et les doublons, améliorant ainsi la qualité du dataset.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong> Analyse de qualité d’images</strong>.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong> Classification supervisée multiclasse</strong> : pour prédire la catégorie produit avec une
métrique adaptée au déséquilibre des classes (F1-score pondéré).  
</ul>
</div>
""", unsafe_allow_html=True) 
#--------------------------------------------------------------PAGE EXPLORATION DE LA DONNEE ----------------------------------------------------------------
#--------------------------------------------------------------PAGE EXPLORATION DE LA DONNEE ----------------------------------------------------------------
#--------------------------------------------------------------PAGE EXPLORATION DE LA DONNEE ----------------------------------------------------------------
#--------------------------------------------------------------PAGE EXPLORATION DE LA DONNEE ----------------------------------------------------------------
#--------------------------------------------------------------PAGE EXPLORATION DE LA DONNEE ----------------------------------------------------------------
if page == pages[1]:

    affiche_bandeau("Exploration et préparation des données", "#bf0000")

    st.markdown("""
    <style>
    div[data-baseweb="tab-list"] {
        justify-content: center;
        gap: 24px;
    }

    button[data-baseweb="tab"] {
        padding-top: 8px;
        padding-bottom: 10px;
        min-height: 72px;
    }

    button[data-baseweb="tab"] > div {
        font-size: 14px;
        font-weight: 600;
        text-align: center;
        white-space: pre-line;
        line-height: 1.2;
    }

    button[data-baseweb="tab"][aria-selected="true"] > div {
        font-weight: 800;
    }
    </style>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "🔎\nExploration des Données",
        "📦\nPréparation des Données",
        "📊\nVisualisations"
    ])

    # =================== Exploration des Données ========================================================================================================================================
    with tabs[0]:
        import streamlit as st 
        import base64
        # Charger image
        with open("images/Repartition_des_classes.png", "rb") as img_file2:
            img_bytes2 = img_file2.read()
            encoded = base64.b64encode(img_bytes2).decode()

        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
            padding:20px;
            border-left:6px solid #bf0000;
            border-radius:15px;
            margin: 20px auto;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            font-family: 'Segoe UI';
            width:85%;
">
<strong>Données :</strong>
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> 85 000 images et textes.
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Classes déséquilibrées (ex : classe 2583 = 10 000 exemples, classe 1180 = 500 exemples).
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Textes : longueurs variables, balises HTML, stopwords.
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Images : floues, sombres, mal cadrées.
</ul>  
                                     
<strong>Problématiques :</strong>
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Déséquilibre des classes.Bruit dans les données (textes et images).
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Doublons et conflits de labels.
</ul>
                    
<h3 style="color:#bf0000;">📊 Visualisation du déséquilibre</h3>
<div style="text-align:center;"><img src="data:image/png;base64,{encoded}" style="width:70%; object-fit:contain;"/></div>
</div>
""", unsafe_allow_html=True)


# ================= Préparation des données ======================================================================================================
    with tabs[1]:
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
            padding:20px;
            border-left:6px solid #bf0000;
            border-radius:15px;
            margin: 20px auto;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            font-family: 'Segoe UI';
            width:85%;
        ">

<strong>Images :</strong>
                    
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Correction EXIF, crop, resize (224x224).
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Détection des images vides/floues.
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Déduplication (hachage MD5).
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Normalisation ImageNet.
</ul>

<strong>Textes :</strong>
                    
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Nettoyage : suppression des balises HTML et stopwords.
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Traduction en français.
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Extraction des unités de mesure (ex : "500g").
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Vectorisation TF-IDF (ngrams mots + caractères).
</ul>

<strong>Gestion du Déséquilibre :</strong>
                    
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Rééchantillonnage (4 000 exemples/classe).
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Pondération (class_weight="balanced").
</ul>
                    


</div>
""", unsafe_allow_html=True)

# ================= Visualisation ======================================================================================================
    with tabs[2]:
        import streamlit as st 
        import base64
        # Charger image
        with open("images/f_corrélation_métrique_visuelle.png", "rb") as img_file:
            img_bytes = img_file.read()
            encoded = base64.b64encode(img_bytes).decode()
        with open("images/f_brightness.png", "rb") as img_file2:
            img_bytes2 = img_file2.read()
            encoded2 = base64.b64encode(img_bytes2).decode()
        with open("images/f_contrast.png", "rb") as img_file3:
            img_bytes3 = img_file3.read()
            encoded3 = base64.b64encode(img_bytes3).decode()
        with open("images/f_entropy.png", "rb") as img_file4:
            img_bytes4 = img_file4.read()
            encoded4 = base64.b64encode(img_bytes4).decode()
        with open("images/f_stopword.png", "rb") as img_file5:
            img_bytes5 = img_file5.read()
            encoded5 = base64.b64encode(img_bytes5).decode()

        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
            padding:20px;
            border-left:6px solid #bf0000;
            border-radius:15px;
            margin: 20px auto;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            font-family: 'Segoe UI';
            width:85%;
        ">

<strong>Images :</strong>
                    
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Heatmap des corrélations : brightness 🔁 entropy (0.92), blur_score 🔁 edge_ratio (-0.72).
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Distributions : luminosité (bimodale), contraste (unimodale), entropie (étalée).
</ul>

<strong>Textes :</strong>
                    
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Nuage de mots : stopwords dominants ("de", "pour").
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Longueurs des textes : très variables (0 à 12 451 caractères).
</ul>
<h4 style="color:#bf0000;text-align:center;">📊 Corrélation entre métriques visuelles</h4>
<div style="text-align:center;margin-bottom:50px;"><img src="data:image/png;base64,{encoded}" style="width:70%; object-fit:contain;"/></div>
<h4 style="color:#bf0000;text-align:center;">📊 Distribution globale de brightness</h4>
<div style="text-align:center;margin-bottom:50px;"><img src="data:image/png;base64,{encoded2}" style="width:70%; object-fit:contain;"/></div>
<h4 style="color:#bf0000;text-align:center;">📊 Distribution globale de contrast</h4>
<div style="text-align:center;margin-bottom:50px;"><img src="data:image/png;base64,{encoded3}" style="width:70%; object-fit:contain;"/></div>
<h4 style="color:#bf0000;text-align:center;">📊 Distribution globale de entropy</h4>
<div style="text-align:center;margin-bottom:50px;margin-bottom:50px;"><img src="data:image/png;base64,{encoded4}" style="width:70%; object-fit:contain;"/></div>
<h4 style="color:#bf0000;text-align:center;">📊 Mots les plus fréquents dans désignation</h4>
<div style="text-align:center;margin-bottom:50px;"><img src="data:image/png;base64,{encoded5}" style="width:70%; object-fit:contain;"/></div>

</div>
""", unsafe_allow_html=True)


#=======================================PAGE MODELISATION TEXTE==================================================================================================
#=======================================PAGE MODELISATION TEXTE==================================================================================================
#=======================================PAGE MODELISATION TEXTE==================================================================================================
#=======================================PAGE MODELISATION TEXTE==================================================================================================
#=======================================PAGE MODELISATION TEXTE==================================================================================================
#=======================================PAGE MODELISATION TEXTE==================================================================================================
if page == pages[2] : 
  affiche_bandeau("Modélisation sur le texte", "#bf0000")
  st.markdown("""
<style>
div[data-baseweb="tab-list"] {
    justify-content: center;
    gap: 28px;
}

button[data-baseweb="tab"] {
    position: relative;
    padding-top: 8px;
    padding-bottom: 10px;
    min-height: 72px;
    padding-left: 12px;   /* espace avant le texte */
}

/* Flèche par défaut */
button[data-baseweb="tab"]::after {
    content: "➜";
    position: absolute;
    right: -28px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 18px;
    font-weight: 700;
    color: grey;
}

/* Pas de flèche sur le dernier onglet */
button[data-baseweb="tab"]:last-of-type::after {
    content: "";
}

button[data-baseweb="tab"] > div {
    font-size: 14px;
    font-weight: 600;
    text-align: center;
    white-space: pre-line;
    line-height: 1.2;
}

button[data-baseweb="tab"][aria-selected="true"] > div {
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)

  tabs = st.tabs([
        "💻\nChoix\ndes données",
        "🕓\nEntraînement\nde modèles",
        "⚙️\nOptimisation\ndes paramètres",
        "🔧\nTest de modèles\nDeep Learning",
        "📈\nAmélioration du modèle\nTF-IDF + LinearSVC",
        "🎯\nSoumission\nau challenge",
        "📥\nAutres\nmodèles",
    ])
  
#### 🔹 Choix des données ===================================================================================
  with tabs[0]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;            
    ">
 

Dans un premier temps, nous avons utilisé des données préparées vues précédemment :  
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong>Nettoyage des balises HTML</strong> pour ne conserver que le texte pertinent.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Suppression des <strong>stopwords</strong>.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> <strong>Traduction</strong> des textes en français afin d’uniformiser le langage.  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Concaténation des champs <strong>designation</strong> et <strong>description</strong> en une seule colonne texte.           
</ul>
                
Ensuite, pour gérer le déséquilibre des classes, nous avons choisi d’harmoniser la
volumétrie par classe entre **1000 et 4000 produits**.Donc pour les classes 
surdimensionnées nous avons effectué des suppressions de données et pour les classes 
sous dimensionnées nous avons dupliqué aléatoirement des lignes. 


</div>
""", unsafe_allow_html=True) 
    
  import streamlit as st
  import base64

# Charger l'image et la convertir en base64
  with open("images/Matrice_confusion_texte.png", "rb") as img_file2:
    img_bytes2 = img_file2.read()
    encoded = base64.b64encode(img_bytes2).decode()

####  🔹 Entraînement de modèles ===================================================================================
  with tabs[1]:
    st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;             
    ">
                
Le modèle initial consistait en une vectorisation TF-IDF combinée à un modèle de classification 
Logistic Regression, entraîné sur les données préparées du champ concaténant designation et description.  
Ce modèle a atteint un score f1 weighted **78,39 %**.  
Ensuite, nous avons testé **TF-IDF combiné à LinearSVC**, avec un score de **78,55 %**.  
                
<div><img src="data:image/png;base64,{encoded}" style="width:100%; height:100%; object-fit:contain;"/></div>
                
</div>
""", unsafe_allow_html=True) 
     
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;          
    ">
                      
Après analyse des erreurs via une matrice de confusion, nous avons remarqué que certaines
catégories étaient souvent confondues entre elles, notamment les sous-catégories de Livres et de Jeux vidéo.
Pour tenter d’améliorer les performances, nous avons ajouté des features
spécifiques pour ces catégories.  

De plus nous avons fait machine arrière pour gérer le déséquilibre des classes en choisissant de tout garder mais 
d’utiliser class_weight="balanced" dans le LinearSVC. Nous avons aussi ajouté des paramètres à TF-IDF 
sur les mots et les caractères (word_tfidf et char_tfidf) : **Score : 81,72%**  
</div>
""", unsafe_allow_html=True) 


####  🔹 Optimisation des paramètres===================================================================================
  with tabs[2]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;            
    ">
 

Pour continuer, nous avons testé plusieurs paramètres différents pour **TF-IDF** et **LinearSVC** :  

<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Word n-gram : 1,2 / 1,3  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Char n-gram : 3,5 / 2,4 / 4,6  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Max features : 120 000 / 80 000 / 150 000  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> Min_df : 1 / 2  
<li><span style="color:#bf0000; font-size:18px;">⬥</span> LinearSVC C : 1.5 / 1.6 / 1.8 / 2.0  
</ul>
</div>
""", unsafe_allow_html=True) 
    st.write("""
           
           """)
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;           
    ">
                 
**Meilleure combinaison retenue** :  
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span>  Word n-gram : 1,2  
<li><span style="color:#bf0000; font-size:18px;">⬥</span>  Char n-gram : 3,5  
<li><span style="color:#bf0000; font-size:18px;">⬥</span>  Max features : 120 000  
<li><span style="color:#bf0000; font-size:18px;">⬥</span>  Min_df : 1  
<li><span style="color:#bf0000; font-size:18px;">⬥</span>  LinearSVC C : 1.5  
</ul>
Pour un score de <strong>83,06 %</strong>.
</div>
""", unsafe_allow_html=True) 
  

####  🔹 Tests de modèles Deep Learning  ===================================================================================
  with tabs[3]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;            
    ">
Ensuite nous avons voulu essayer des modèles de deep learning (XGBoost, Random Forest, CamenBERT). 
La difficulté est surtout liée à nos machines. Nous n’étions pas assez bien équipés pour lancer des
modèles de ce type : l’entraînement dure des heures, la mémoire surcharge et l'entraînement s'arrête,
sur des GPU cloud des time-out nous freinaient dans nos apprentissages.  
    
Nous avons tant bien que mal réussi à avoir des résultats mais avec le minimum de paramètres :   
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span> XGBoost : 79%  
<li><span style="color:#bf0000; font-size:18px;">⬥</span>  CamenBERT : 77%  
<li><span style="color:#bf0000; font-size:18px;">⬥</span>  Random Forest : jamais réussi à aller au bout.    
</ul>
</div>
""", unsafe_allow_html=True) 
    

#### 🔹 Amélioration du modèle TF-IDF + LinearSVC  ===================================================================================
  with tabs[4]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;         
    ">
                
Étant bloqué par la puissance de nos machines nous avons tenté d’améliorer le modèle TF-IDF + LinearSVC.
N’y arrivant pas, nous prenons la décision de tester notre meilleur modèle sur les données brut tel quel
et ensuite avancer par étape pour la transformation des données :   
</div>
""", unsafe_allow_html=True) 
    
    st.write("""
  
  
""")
    
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;
">

<h3 style="color:#bf0000; margin-bottom:15px;">📊 Performance des modèles</h3>

<ul style="list-style:none; padding-left:0; margin:0;">

<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Données brut - sur champ désignation :
    <span style='color:#28a745; font-weight:bold; margin-left:auto;'>⭡ 83,75%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Données sans balise HTML et Stopwords :
    <span style='color:#dc3545; font-weight:bold; margin-left:auto;'>⭣ 82,38%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Données brut - sur champ désignation sans Features dans le modèle :
    <span style='color:#28a745; font-weight:bold; margin-left:auto;'>⭡ 83,70%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Données sans balise HTML et Stopwords sans Features dans le modèle :
    <span style='color:#dc3545; font-weight:bold; margin-left:auto;'>⭣ 82,40%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Données brut - sans features - désignation+description :
    <span style='color:#28a745; font-weight:bold; margin-left:auto;'>⭡ 84,92%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Données brut - désignation avec 2 fois plus de poids que description :
    <span style='color:#28a745; font-weight:bold; margin-left:auto;'>⭡ 85,61%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Données brut - désignation avec 3 fois plus de poids que description :
    <span style='color:#28a745; font-weight:bold; margin-left:auto;'>⭡ 85,71%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Données brut - désignation avec 4 fois plus de poids que description :
    <span style='color:#28a745; font-weight:bold; margin-left:auto;'>⭡ 85,75%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Données brut - désignation avec 5 fois plus de poids que description :
    <span style='color:#dc3545; font-weight:bold; margin-left:auto;'>⭣ 85,70%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Données brut - désignation x4 + description + unité de mesure :
    <span style='color:#28a745; font-weight:bold; margin-left:auto;'>⭡ 85,81%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Même modèle + ajout de poids sur les 3 premiers mots de désignation :
    <span style='color:#28a745; font-weight:bold; margin-left:auto;'>⭡ 86,06%</span>
</li>
<li style="margin-bottom:10px; display:flex; align-items:center;">
    <span style="color:#bf0000; font-size:18px; margin-right:10px;">⬥</span>
    Changement de méthode (pondération directement dans le TF-IDF) : Meilleur score :
    <span style='color:#28a745; font-weight:bold; margin-left:auto;'>⭡ 86,22%</span>
</li>

</ul>

</div>
""", unsafe_allow_html=True)

 
    
    st.write("""
  
  
""")
    
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;            
    ">
                   
Dans ce dernier modèle nous avons choisis une approche Pipeline + ColumnTransformer, donc chaque feature est une méthode indépendante, bien séparée, traçable et réutilisable.
</div>
""", unsafe_allow_html=True) 
    
    st.write("""
  
  
""")
    import streamlit as st
    import base64

# Charger l'image et la convertir en base64
    with open("images/Graphique_des_modeles2.png", "rb") as img_file2:
      img_bytes2 = img_file2.read()
      encoded = base64.b64encode(img_bytes2).decode()

    st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:85%;             
    ">
    <h3 style="color:#bf0000; margin-bottom:15px;">📊 Evolution chronologique des modèles testés</h3>

<div><img src="data:image/png;base64,{encoded}" style="width:100%; height:100%; object-fit:contain;"/></div>
</div>
""", unsafe_allow_html=True) 

    st.write("""
---
""")
    
####  🔹 Soumission au challenge  ===================================================================================
  import streamlit as st
  import base64

# Charger l'image et la convertir en base64
  with open("images/challenge.png", "rb") as img_file:
    img_bytes = img_file.read()
    encoded = base64.b64encode(img_bytes).decode()

  with tabs[5]:
    st.markdown(f"""
    <div style=" 
        background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
        padding:20px;
        border-left:6px solid #bf0000;
        border-radius:15px;
        margin: 20px auto;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        width:85%;  
        display:flex;
        align-items:center;       /* centrage vertical */
        gap:20px;                 /* espace entre texte et image */
        height:400px;             /* hauteur fixe */
    ">
        <div style="flex:1;">
            Nous avons soumis notre meilleur modèle en phase de test au challenge Rakuten 
            et obtenu le score de <b>87,41%</b>.<br><br>
            Pour rappel, il fallait un score de <b>81,13%</b> pour la réussite de ce challenge.
        </div>
        <div style="flex:1;">
            <img src="data:image/png;base64,{encoded}" style="width:100%; height:100%; object-fit:contain;"/>
        </div>
    </div>
    """, unsafe_allow_html=True)
  
#### 🔹 Autres modèles  ===================================================================================
  with tabs[6]:
    st.markdown("""
<div style=" 
        background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
        padding:20px;
        border-left:6px solid #bf0000;
        border-radius:15px;
        margin: 20px auto;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        width:85%;          
    ">
                
Nous avons souhaité tester notre meilleur modèle sur les données d'entraînement en regroupant certaines classes. Toutes les classes concernant les livres en une seule classe et pareil pour les jeux vidéo et consoles. Nous avons aussi regroupé en une seule classe les jeux de sociétés et les jouets pour enfants :   

<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong>Livres</strong> : Livres loisirs et société + Lots Livres & Magazines + Magazines + Livres littérature et fiction  
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong>Jeux vidéo</strong> : Jeux vidéo + Accessoires jeux vidéo + Jeux vidéo & Consoles + Lots consoles & jeux  
<li><span style="color:#bf0000; font-size:18px;">⬥</span><strong>Jeux & Enfants</strong> : Jouets & Enfant + Jeux de société  
</ul>  
<strong>Score obtenu : 90,91 %</strong>.

</div>
""", unsafe_allow_html=True) 
#=============================================================PAGE MODELISATION IMAGE===========================================================
#=============================================================PAGE MODELISATION IMAGE===========================================================
#=============================================================PAGE MODELISATION IMAGE===========================================================
#=============================================================PAGE MODELISATION IMAGE===========================================================
#=============================================================PAGE MODELISATION IMAGE===========================================================
#=============================================================PAGE MODELISATION IMAGE===========================================================
if page == pages[4] : 
  affiche_bandeau("Modélisation sur l'image", "#bf0000")
  st.write("""
           

""")
#=============================================================Tester le modèle image ===========================================================
#=============================================================Tester le modèle image===========================================================
#=============================================================Tester le modèle image===========================================================
#=============================================================Tester le modèle image===========================================================
#=============================================================Tester le modèle image===========================================================
#=============================================================Tester le modèle image===========================================================
if page == pages[5] : 
  affiche_bandeau("Tester le modèle image", "#bf0000")
  st.write("""
           

""")
#===========================================PAGE LIMITES ET PERSPECTIVES==========================================================================
#===========================================PAGE LIMITES ET PERSPECTIVES==========================================================================
#===========================================PAGE LIMITES ET PERSPECTIVES==========================================================================
#===========================================PAGE LIMITES ET PERSPECTIVES==========================================================================
#===========================================PAGE LIMITES ET PERSPECTIVES==========================================================================
#===========================================PAGE LIMITES ET PERSPECTIVES==========================================================================
if page == pages[6] : 
  affiche_bandeau("Perspectives", "#bf0000")
  st.markdown("""
<style>
/* Centrage horizontal des onglets */
div[data-baseweb="tab-list"] {
    justify-content: center;
    gap: 24px;   /* espace horizontal entre les onglets */
}

/* Bouton d’onglet */
button[data-baseweb="tab"] {
    padding-top: 8px;
    padding-bottom: 10px;
    min-height: 72px;
}

/* Texte des onglets */
button[data-baseweb="tab"] > div {
    font-size: 14px;
    font-weight: 600;
    text-align: center;
    white-space: pre-line;
    line-height: 1.2;
}

/* Onglet actif */
button[data-baseweb="tab"][aria-selected="true"] > div {
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)

  tabs = st.tabs([
        "🌐\nApproche Multimodale",
        "🕓\nAutres",
    ])
  
#### 🔹 Multimodale ===================================================================================
  with tabs[0]:
    st.markdown("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:20px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:100%;            
    ">
<h3>Approche Multimodale</h3>
Le cœur du système reposera sur notre meilleur modèle texte, basé sur TF-IDF et LinearSVC, qui capture efficacement l’information sémantique et reste le plus performant globalement.<br>
Les images seront traitées via ResNet50, mais avec un rôle complémentaire.<br>
<br>
Plutôt que de fusionner naïvement les modalités, nous introduirons une pondération asymétrique : 
<ul style="list-style: none; padding-left: 0;">                          
<li><span style="color:#bf0000; font-size:18px;">⬥</span>Le modèle texte a un poids plus élevé
<li><span style="color:#bf0000; font-size:18px;">⬥</span>Tandis que le modèle image intervient davantage sur les classes où le texte est historiquement en difficulté.<br>
<br>
Cette stratégie permettra d’exploiter la richesse visuelle lorsque le signal textuel est faible, tout en conservant la précision du texte quand il est pertinent.
Le résultat sera un modèle plus robuste, capable de mieux généraliser sur des cas complexes.
</div>
    """, unsafe_allow_html=True)
  with tabs[0]:
   import streamlit.components.v1 as components

   components.html("""
<div style="
    background: linear-gradient(135deg, #fdfdfd, #f0f0f0);
    padding:60px;
    border-left:6px solid #bf0000;
    border-radius:15px;
    margin: 20px auto;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    width:100%;            
    ">
<style>
.grid {
    display: grid;
    grid-template-columns: 160px 80px 180px 80px 180px;
    grid-template-rows: 80px 80px 80px;
    align-items: center;
    justify-items: center;
    margin: 40px auto;
}

.card {
    background: linear-gradient(135deg, #efefef, #efefef);
    border-radius: 14px;
    padding: 16px;
    width: 150px;
    text-align: center;
    color: #bf0000;
    font-size: 14px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.35);
}

.arrow {
    font-size: 26px;
    color: #bf0000;
}
</style>
<div><strong>🔹 Schéma de l'approche multimodale</strong></div>
<div class="grid">

    <!-- A1 -->
    <div class="card" style="grid-column:1; grid-row:1;">
        📝 Texte<br>
        ↓<br>
        TF-IDF<br>
        ↓<br>
        Vecteur Texte
    </div>

    <!-- B1 -->
    <div class="arrow" style="grid-column:2; grid-row:1;">
        ↘
    </div>

    <!-- A3 -->
    <div class="card" style="grid-column:1; grid-row:3;">
        🖼️ Image<br>
        ↓<br>
        ResNet50<br>
        ↓<br>
        Vecteur Image
    </div>

    <!-- B3 -->
    <div class="arrow" style="grid-column:2; grid-row:3;">
        ↗
    </div>

    <!-- C2 -->
    <div class="card" style="grid-column:3; grid-row:2;">
        🔗 Fusion
    </div>

    <!-- D2 -->
    <div class="arrow" style="grid-column:4; grid-row:2;">
        →
    </div>

    <!-- E2 -->
    <div class="card" style="grid-column:5; grid-row:2;">
        Vecteur Fusionné<br>
        ↓<br>
        RandomForest<br>
        ↓<br>
        🎯 Prédiction
    </div>
</div>
                   
<br><br>
                   
<div><strong>🔹 Amélioration progressive du F1-score</strong></div>                  
<style>
.table-container {
    margin: 10px 0;
    max-width: 850px;
}

table.model-table {
    width: 100%;
    border-collapse: collapse;
    background: linear-gradient(135deg, #fdfdfd, #f3f3f3);
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.model-table th {
    background-color: #bf0000;
    color: white;
    padding: 14px;
    font-size: 15px;
    text-align: center;
}

.model-table td {
    padding: 14px;
    font-size: 14px;
    color: #333;
    border-bottom: 1px solid #ddd;

    /* retour ligne auto */
    white-space: normal;
    word-wrap: break-word;
    overflow-wrap: break-word;
}

.model-table tr:last-child td {
    border-bottom: none;
}

.model-table tr:hover {
    background-color: #f8eaea;
}

.score {
    font-weight: bold;
    color: #bf0000;
    text-align: center;
}
</style>

<div class="table-container">
<table class="model-table">
    <thead>
        <tr>
            <th>Version</th>
            <th>F1-score</th>
            <th>Améliorations clés</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center;"><strong>V1</strong></td>
            <td class="score">0.665</td>
            <td>Modèle de base : <strong>RandomForest</strong> sans optimisation.</td>
        </tr>
        <tr>
            <td style="text-align:center;"><strong>V2</strong></td>
            <td class="score">0.682</td>
            <td>
                Équilibrage des classes (<code>class_weight="balanced"</code>)<br>
                + optimisation des hyperparamètres.
            </td>
        </tr>
        <tr>
            <td style="text-align:center;"><strong>V3</strong></td>
            <td class="score">0.734</td>
            <td>
                Réduction de dimension (<strong>PCA</strong>)<br>
                + recherche aléatoire des hyperparamètres
                (<strong>RandomizedSearchCV</strong>).
            </td>
        </tr>
    </tbody>
</table>
</div>
</div>
""", height=800)
  
#=======================================PAGE TESTER LE MODELE (version simplifiée) ===============================================================
#=======================================PAGE TESTER LE MODELE (version simplifiée) ===============================================================
#=======================================PAGE TESTER LE MODELE (version simplifiée) ===============================================================
#=======================================PAGE TESTER LE MODELE (version simplifiée) ===============================================================
#=======================================PAGE TESTER LE MODELE (version simplifiée) ===============================================================
#=======================================PAGE TESTER LE MODELE (version simplifiée) ===============================================================


if page == "Tester le modèle texte":
    import os
    import re
    import joblib
    import streamlit as st
    import pandas as pd
    import requests

    st.header("Tester le modèle texte (fonctionne que en local)")
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
