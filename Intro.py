import streamlit as st
from PIL import Image


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Portafolio de Interfaces Multimodales",
    page_icon="🎀",
    layout="wide"
)


# ============================================================
# ESTILOS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');


/* ============================================================
   COLORES
   ============================================================ */

:root {
    --rosa-principal: #D9899B;
    --rosa-oscuro: #A95F72;
    --rosa-claro: #F9E4E9;
    --rosa-suave: #FFF5F7;
    --rosa-borde: #EBC3CC;
    --texto: #4A3D42;
    --gris-rosa: #786A6F;
    --blanco: #FFFFFF;
}


/* ============================================================
   FONDO
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            #FBE8ED 0%,
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 20%,
            #F9E1E7 0%,
            transparent 25%
        ),
        #FFF8FA;

    font-family: 'Quicksand', sans-serif;
    color: var(--texto);
}


.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ============================================================
   TÍTULOS
   ============================================================ */

h1,
h2,
h3,
h4 {
    font-family: 'Quicksand', sans-serif !important;
    color: var(--texto) !important;
}


.portfolio-title {
    text-align: center;

    font-size: 3.4rem;

    font-weight: 700;

    color: #A95F72;

    margin-bottom: 0.3rem;
}


.portfolio-subtitle {
    text-align: center;

    font-size: 1.15rem;

    color: #786A6F;

    margin-bottom: 2rem;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #F9E4E9 0%,
            #FFF0F3 55%,
            #F5DDE3 100%
        );

    border-right: 2px solid #EBC3CC;
}


section[data-testid="stSidebar"] *,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] * {

    color: #4A3D42 !important;

}


section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {

    font-weight: 700 !important;

}


/* ============================================================
   TARJETAS DE PROYECTOS
   ============================================================ */

.project-card {

    background: rgba(255,255,255,0.90);

    border: 2px solid #F0D5DB;

    border-radius: 22px;

    padding: 1.3rem;

    margin-bottom: 1.5rem;

    box-shadow:
        0 8px 25px rgba(170, 100, 120, 0.08);

    transition: 0.2s ease;

}


.project-card:hover {

    border-color: #D9899B;

    box-shadow:
        0 10px 30px rgba(170, 100, 120, 0.14);

}


/* ============================================================
   SUBTÍTULOS DE PROYECTOS
   ============================================================ */

.stSubheader {

    color: #A95F72 !important;

}


/* ============================================================
   IMÁGENES
   ============================================================ */

[data-testid="stImage"] {

    border-radius: 18px;

}


/* ============================================================
   ENLACES
   ============================================================ */

a {

    color: #B9687D !important;

    font-weight: 700;

    text-decoration: none;

}


a:hover {

    color: #8F4F61 !important;

    text-decoration: underline;

}


/* ============================================================
   DIVISORES
   ============================================================ */

hr {

    border: none;

    border-top: 2px dashed #EBC3CC;

    margin: 2rem 0;

}


/* ============================================================
   COLUMNAS
   ============================================================ */

[data-testid="column"] {

    padding: 0.4rem;

}


/* ============================================================
   MENSAJES
   ============================================================ */

div[data-testid="stAlert"] {

    border-radius: 15px;

}


/* ============================================================
   RESPONSIVE
   ============================================================ */

@media (max-width: 768px) {

    .portfolio-title {

        font-size: 2.5rem;

    }

    .portfolio-subtitle {

        font-size: 1rem;

    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CONFETI AL CARGAR LA PÁGINA
# ============================================================

st.markdown("""
<script>
setTimeout(function() {

    const emojis = ["🎀", "🌸", "💗", "✨", "🌷", "💕"];

    for (let i = 0; i < 45; i++) {

        const confetti = document.createElement("div");

        confetti.innerHTML =
            emojis[Math.floor(Math.random() * emojis.length)];

        confetti.style.position = "fixed";
        confetti.style.left = Math.random() * 100 + "vw";
        confetti.style.top = "-30px";
        confetti.style.fontSize =
            (15 + Math.random() * 18) + "px";

        confetti.style.zIndex = "9999";

        confetti.style.pointerEvents = "none";

        confetti.style.animation =
            "fall " +
            (2 + Math.random() * 3) +
            "s linear forwards";

        document.body.appendChild(confetti);

        setTimeout(function() {
            confetti.remove();
        }, 5500);
    }

}, 300);


const style = document.createElement("style");

style.innerHTML = `
@keyframes fall {

    0% {
        transform:
            translateY(0)
            rotate(0deg);

        opacity: 1;
    }

    100% {
        transform:
            translateY(110vh)
            rotate(360deg);

        opacity: 0;
    }

}
`;

document.head.appendChild(style);

</script>
""", unsafe_allow_html=True)


# ============================================================
# TÍTULO PRINCIPAL
# ============================================================

st.markdown(
    '<div class="portfolio-title">'
    '🎀 Portafolio de Interfaces Multimodales'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="portfolio-subtitle">'
    'Una colección de proyectos desarrollados durante las clases ✨'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.subheader("🎀 Salomé Arango")

    st.write(
        "A continuación encontrarán las páginas que he "
        "realizado durante las clases."
    )


# ============================================================
# COLUMNAS
# ============================================================

col1, col2, col3 = st.columns(3)


# ============================================================
# COLUMNA 1
# ============================================================

with col1:

    # --------------------------------------------------------
    # ANÁLISIS DE TEXTO
    # --------------------------------------------------------

    st.subheader("Análisis de texto")

    image = Image.open(
        "analisisdetexto.webp"
    )

    st.image(
        image,
        width=190
    )

    st.write(
        "Con la siguiente página se realiza un análisis "
        "del texto que se le ingrese."
    )

    url = "https://textico.streamlit.app/"

    st.write(
        f"Texto [Enlace]({url})"
    )


    # --------------------------------------------------------
    # RECONOCIMIENTO DE OBJETOS
    # --------------------------------------------------------

    st.subheader("Reconocimiento de objetos")

    image = Image.open(
        "imagenanime.jfif"
    )

    st.image(
        image,
        width=200
    )

    st.write(
        "En el siguiente enlace veremos cómo se detectan "
        "objetos en imágenes."
    )

    url = (
        "https://detector-de-imagenes-3.streamlit.app/"
    )

    st.write(
        f"Reconocimiento [Enlace]({url})"
    )


    # --------------------------------------------------------
    # PRIMERA PÁGINA
    # --------------------------------------------------------

    st.subheader("Primera página")

    image = Image.open(
        "peachygoma.png"
    )

    st.image(
        image,
        width=200
    )

    st.write(
        "En la siguiente página veremos el primer "
        "acercamiento que tuve con GitHub y Streamlit."
    )

    url = (
        "https://interfaces-multimodales1-primera-app.streamlit.app/"
    )

    st.write(
        f"Primera página: [Enlace]({url})"
    )


    # --------------------------------------------------------
    # TRADUCTOR DE CARTELES
    # --------------------------------------------------------

    st.subheader("Traductor de carteles")

    image = Image.open(
        "chibipaises.jfif"
    )

    st.image(
        image,
        width=200
    )

    st.write(
        "La siguiente página es un traductor de imágenes, "
        "perfecto si eres extranjero en un país con otro idioma."
    )

    url = (
        "https://interfaces-multimodales1-primera-app.streamlit.app/"
    )

    st.write(
        f"Carteles: [Enlace]({url})"
    )


# ============================================================
# COLUMNA 2
# ============================================================

with col2:

    # --------------------------------------------------------
    # RECONOCIMIENTO ÓPTICO DE CARACTERES
    # --------------------------------------------------------

    st.subheader(
        "Reconocimiento óptico de caracteres"
    )

    image = Image.open(
        "ocr.webp"
    )

    st.image(
        image,
        width=200
    )

    st.write(
        "En la siguiente página veremos una aplicación "
        "que convierte los textos de imágenes a texto."
    )

    url = (
        "https://lectorimagenes-salito.streamlit.app/"
    )

    st.write(
        f"OCR: [Enlace]({url})"
    )


    # --------------------------------------------------------
    # RECONOCIMIENTO DE IMÁGENES
    # --------------------------------------------------------

    st.subheader(
        "Reconocimiento de imágenes"
    )

    image = Image.open(
        "animetech.avif"
    )

    st.image(
        image,
        width=190
    )

    st.write(
        "En el siguiente enlace veremos cómo se pueden "
        "analizar imágenes usando agentes de Teachable Machine."
    )

    url = (
        "https://modelo-detector-personas.streamlit.app/"
    )

    st.write(
        f"Agente: [Enlace]({url})"
    )


    # --------------------------------------------------------
    # NUBE DE PALABRAS
    # --------------------------------------------------------

    st.subheader(
        "Nube de palabras"
    )

    image = Image.open(
        "nubedepalabras.jpg"
    )

    st.image(
        image,
        width=200
    )

    st.write(
        "En el siguiente enlace veremos cómo tomar un texto "
        "y convertirlo en una nube de palabras."
    )

    url = (
        "https://nubecitadepalabras.streamlit.app/"
    )

    st.write(
        f"Nube: [Enlace]({url})"
    )


# ============================================================
# COLUMNA 3
# ============================================================

with col3:

    # --------------------------------------------------------
    # TEXTO A AUDIO
    # --------------------------------------------------------

    st.subheader(
        "Texto a audio"
    )

    image = Image.open(
        "fabula.jfif"
    )

    st.image(
        image,
        width=190
    )

    st.write(
        "En la siguiente página veremos una aplicación "
        "que convierte el texto en audio, con un enfoque "
        "infantil para convertir cuentos."
    )

    url = (
        "https://pagina2-experimento.streamlit.app/"
    )

    st.write(
        f"Cuentos: [Enlace]({url})"
    )


    # --------------------------------------------------------
    # ANÁLISIS DE SENTIMIENTO
    # --------------------------------------------------------

    st.subheader(
        "Análisis de sentimiento"
    )

    image = Image.open(
        "emojis.avif"
    )

    st.image(
        image,
        width=200
    )

    st.write(
        "La siguiente página analiza las emociones que se "
        "ingresan según la polaridad."
    )

    url = (
        "https://sentimentalismo-gifs.streamlit.app/"
    )

    st.write(
        f"Sentimientos: [Enlace]({url})"
    )


    # --------------------------------------------------------
    # TRADUCTOR
    # --------------------------------------------------------

    st.subheader(
        "Traductor"
    )

    image = Image.open(
        "duolingo.png"
    )

    st.image(
        image,
        width=200
    )

    st.write(
        "Esta página traduce el audio que se le ingrese."
    )

    url = (
        "https://traductorcito-de-idiomas.streamlit.app/"
    )

    st.write(
        f"Traductorcito: [Enlace]({url})"
    )
