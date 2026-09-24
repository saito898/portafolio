import streamlit as st
from PIL import Image
import os
import random

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------------

st.set_page_config(
    page_title="Portafolio de Interfaces Multimodales",
    page_icon="🎀",
    layout="wide"
)

# ---------------------------------------------------------
# ESTILO GENERAL
# ---------------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Quicksand', sans-serif;
}

/* Fondo general */
.stApp {
    background: #FFF7FA;
}

/* Ocultar menú y footer */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ------------------------------
   SIDEBAR
------------------------------ */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #F8C8D8 0%,
        #FCE3EB 100%
    );
}

section[data-testid="stSidebar"] * {
    color: #4A2632 !important;
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    font-weight: 700;
}

/* ------------------------------
   TÍTULO PRINCIPAL
------------------------------ */

.main-title {
    text-align: center;
    color: #B84C70;
    font-size: 42px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #79515E;
    font-size: 18px;
    margin-bottom: 35px;
}

/* ------------------------------
   TÍTULOS DE PROYECTOS
------------------------------ */

h2, h3 {
    color: #B84C70 !important;
    font-weight: 700 !important;
}

/* ------------------------------
   TEXTO
------------------------------ */

p {
    color: #59444C;
    font-size: 15px;
    line-height: 1.6;
}

/* ------------------------------
   IMÁGENES
------------------------------ */

img {
    border-radius: 18px;
}

/* ------------------------------
   BOTONES / ENLACES
------------------------------ */

a {
    color: #B84C70 !important;
    font-weight: 700;
    text-decoration: none;
}

a:hover {
    color: #8F3858 !important;
    text-decoration: underline;
}

/* ------------------------------
   TARJETAS
------------------------------ */

.project-card {
    background: #FFFFFF;
    border: 2px solid #F3D5DF;
    border-radius: 20px;
    padding: 18px;
    margin-bottom: 25px;
    box-shadow: 0px 5px 15px rgba(184, 76, 112, 0.08);
    transition: 0.3s ease;
}

.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 8px 20px rgba(184, 76, 112, 0.15);
}

/* ------------------------------
   SEPARADOR
------------------------------ */

hr {
    border: none;
    height: 2px;
    background: #F2CBD8;
    margin: 25px 0;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# CONFETI AUTOMÁTICO
# ---------------------------------------------------------

# Cada vez que Streamlit recarga la página se vuelve a generar.
confettis = [
    "🎀", "🌸", "💗", "✨", "🌷",
    "💕", "🎀", "🌸", "💖", "✨",
    "🌺", "💗", "🎀", "🌷", "💕",
    "✨", "🌸", "💞", "🎀", "🌺",
    "💗", "✨", "🌷", "💕", "🎀",
    "🌸", "💖", "✨", "🌺", "💗",
    "🎀", "🌷", "💕", "🌸", "✨",
    "💞", "🎀", "🌺", "💗", "🌷",
    "✨", "💕", "🌸", "🎀", "💖",
    "🌷", "✨", "💗", "🌺", "🎀"
]

confetti_html = ""

for i, emoji in enumerate(confettis):

    left = random.randint(0, 98)
    size = random.randint(18, 30)
    duration = random.uniform(3.5, 6.5)
    delay = random.uniform(0, 1.8)
    rotation = random.randint(360, 900)

    confetti_html += f"""
    <span class="confetti-piece"
        style="
            left: {left}%;
            font-size: {size}px;
            animation-duration: {duration}s;
            animation-delay: {delay}s;
            --rotation: {rotation}deg;
        ">
        {emoji}
    </span>
    """

st.markdown(f"""
<style>

.confetti-container {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    overflow: hidden;
    z-index: 999999;
}}

.confetti-piece {{
    position: fixed;
    top: -50px;
    opacity: 0;
    animation-name: caerConfetti;
    animation-timing-function: ease-in;
    animation-fill-mode: forwards;
    pointer-events: none;
}}

@keyframes caerConfetti {{

    0% {{
        transform: translateY(-50px) rotate(0deg);
        opacity: 0;
    }}

    10% {{
        opacity: 1;
    }}

    100% {{
        transform: translateY(110vh) rotate(var(--rotation));
        opacity: 0;
    }}
}}

</style>

<div class="confetti-container">
    {confetti_html}
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# FUNCIÓN PARA MOSTRAR IMÁGENES
# ---------------------------------------------------------

def mostrar_imagen(nombre, ancho=200):

    if os.path.exists(nombre):

        image = Image.open(nombre)

        st.image(
            image,
            width=ancho
        )

    else:

        st.warning(
            f"⚠️ No se encontró la imagen: {nombre}"
        )


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.subheader("🎀 Salomé Arango")

    st.write(
        "A continuación encontrarán las páginas "
        "que he realizado durante las clases."
    )

    st.markdown("---")

    st.write("💗 Portafolio de Interfaces Multimodales")


# ---------------------------------------------------------
# TÍTULO PRINCIPAL
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🎀 Portafolio de Interfaces Multimodales</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Una colección de proyectos desarrollados durante las clases ✨</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# COLUMNAS
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)


# =========================================================
# COLUMNA 1
# =========================================================

with col1:

    # -----------------------------
    # ANÁLISIS DE TEXTO
    # -----------------------------

    st.subheader("Análisis de texto")

    mostrar_imagen(
        "analisisdetexto.webp",
        190
    )

    st.write(
        "Con la siguiente página se realiza un análisis "
        "del texto que se le ingrese."
    )

    url = "https://textico.streamlit.app/"

    st.markdown(
        f"📝 [Ver análisis de texto]({url})"
    )


    # -----------------------------
    # RECONOCIMIENTO DE OBJETOS
    # -----------------------------

    st.subheader("Reconocimiento de objetos")

    mostrar_imagen(
        "imagenanime.jfif",
        200
    )

    st.write(
        "En el siguiente enlace veremos cómo se detectan "
        "objetos en imágenes."
    )

    url = "https://detector-de-imagenes-3.streamlit.app/"

    st.markdown(
        f"🔎 [Ver reconocimiento de objetos]({url})"
    )


    # -----------------------------
    # PRIMERA PÁGINA
    # -----------------------------

    st.subheader("Primera página")

    mostrar_imagen(
        "peachygoma.png",
        200
    )

    st.write(
        "En la siguiente página veremos el primer "
        "acercamiento que tuve con GitHub y Streamlit."
    )

    url = "https://interfaces-multimodales1-primera-app.streamlit.app/"

    st.markdown(
        f"🌸 [Ver primera página]({url})"
    )


    # -----------------------------
    # TRADUCTOR DE CARTELES
    # -----------------------------

    st.subheader("Traductor de carteles")

    mostrar_imagen(
        "chibipaises.jfif",
        200
    )

    st.write(
        "La siguiente página es un traductor de imágenes, "
        "perfecto por si eres extranjero en un país con otro idioma."
    )

    url = "https://interfaces-multimodales1-primera-app.streamlit.app/"

    st.markdown(
        f"🌎 [Ver traductor de carteles]({url})"
    )


# =========================================================
# COLUMNA 2
# =========================================================

with col2:

    # -----------------------------
    # OCR
    # -----------------------------

    st.subheader("Reconocimiento óptico de caracteres")

    mostrar_imagen(
        "ocr.webp",
        200
    )

    st.write(
        "En la siguiente página veremos una aplicación "
        "que convierte los textos de imágenes a texto."
    )

    url = "https://lectorimagenes-salito.streamlit.app/"

    st.markdown(
        f"📖 [Ver OCR]({url})"
    )


    # -----------------------------
    # RECONOCIMIENTO DE IMÁGENES
    # -----------------------------

    st.subheader("Reconocimiento de imágenes")

    mostrar_imagen(
        "animetech.avif",
        190
    )

    st.write(
        "En el siguiente enlace veremos cómo se pueden "
        "analizar imágenes usando agentes de Teachable Machine."
    )

    url = "https://modelo-detector-personas.streamlit.app/"

    st.markdown(
        f"🤖 [Ver reconocimiento de imágenes]({url})"
    )


    # -----------------------------
    # NUBE DE PALABRAS
    # -----------------------------

    st.subheader("Nube de palabras")

    mostrar_imagen(
        "nubedepalabras.jpg",
        200
    )

    st.write(
        "En el siguiente enlace veremos cómo tomar un texto "
        "y convertirlo en una nube de palabras."
    )

    url = "https://nubecitadepalabras.streamlit.app/"

    st.markdown(
        f"☁️ [Ver nube de palabras]({url})"
    )


# =========================================================
# COLUMNA 3
# =========================================================

with col3:

    # -----------------------------
    # TEXTO A AUDIO
    # -----------------------------

    st.subheader("Texto a audio")

    mostrar_imagen(
        "fabula.jfif",
        190
    )

    st.write(
        "En la siguiente página veremos una aplicación "
        "que convierte el texto en audio, con un enfoque "
        "infantil para convertir cuentos."
    )

    url = "https://pagina2-experimento.streamlit.app/"

    st.markdown(
        f"🔊 [Ver cuentos]({url})"
    )


    # -----------------------------
    # ANÁLISIS DE SENTIMIENTO
    # -----------------------------

    st.subheader("Análisis de sentimiento")

    mostrar_imagen(
        "emojis.avif",
        200
    )

    st.write(
        "La siguiente página analiza las emociones que "
        "se ingresan, según la polaridad."
    )

    url = "https://sentimentalismo-gifs.streamlit.app/"

    st.markdown(
        f"💗 [Ver análisis de sentimiento]({url})"
    )


    # -----------------------------
    # TRADUCTOR
    # -----------------------------

    st.subheader("Traductor")

    mostrar_imagen(
        "duolingo.png",
        200
    )

    st.write(
        "Esta página traduce el audio que se le ingrese."
    )

    url = "https://traductorcito-de-idiomas.streamlit.app/"

    st.markdown(
        f"🌐 [Ver Traductorcito]({url})"
    )


# ---------------------------------------------------------
# FINAL
# ---------------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#B84C70;
        font-size:16px;
        font-weight:600;
        padding:10px;
    ">
        🎀 Gracias por visitar mi portafolio 💗✨
    </div>
    """,
    unsafe_allow_html=True
)
