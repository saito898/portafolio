import os
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
import time
import glob

from gtts import gTTS
from googletrans import Translator


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Traductorcito 🌸",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
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
    --rosa: #EFA7B5;
    --rosa-claro: #FBE3E8;
    --rosa-suave: #FFF3F5;

    --verde: #8EAF91;
    --verde-claro: #E5F0E5;
    --verde-suave: #F3F8F2;

    --crema: #FFFDFC;

    --texto: #3F4540;
    --gris: #737873;

    --borde-rosa: #F0C8D0;
    --borde-verde: #C8DCC9;
}


/* ============================================================
   FONDO GENERAL
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            #FBE3E8 0%,
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 20%,
            #E5F0E5 0%,
            transparent 25%
        ),
        #FFFDFC;

    font-family: 'Quicksand', sans-serif;
    color: var(--texto);
}


.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #FBE3E8 0%,
            #F5E9EA 45%,
            #E5F0E5 100%
        );

    border-right: 3px solid #E7C7CE;
}


/* TODOS LOS TEXTOS DEL SIDEBAR */

section[data-testid="stSidebar"] *,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] * {
    color: #303530 !important;
}


section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 700 !important;
}


/* ============================================================
   TÍTULOS
   ============================================================ */

h1,
h2,
h3,
h4 {
    font-family: 'Quicksand', sans-serif !important;
    color: #3F4540 !important;
}


.main-title {
    text-align: center;
    font-size: 3.7rem;
    font-weight: 700;

    color: #B96F80;

    margin-bottom: 0.2rem;
}


.main-subtitle {
    text-align: center;
    font-size: 1.25rem;
    font-weight: 500;

    color: #6E786F;

    margin-bottom: 2rem;
}


/* ============================================================
   TARJETAS
   ============================================================ */

.card {
    background: rgba(255,255,255,0.92);

    border-radius: 25px;

    padding: 1.8rem;

    border: 2px solid #F0DADF;

    box-shadow:
        0 10px 30px rgba(80, 70, 70, 0.08);

    margin-bottom: 1.5rem;
}


.card-green {
    background: #F5F9F4;

    border: 2px solid #D5E4D5;

    border-radius: 25px;

    padding: 1.8rem;

    box-shadow:
        0 10px 30px rgba(80, 100, 80, 0.07);

    margin-bottom: 1.5rem;
}


/* ============================================================
   IMAGEN
   ============================================================ */

.image-box {
    background: #FFFFFF;

    padding: 1rem;

    border-radius: 25px;

    border: 2px solid #F0DADF;

    box-shadow:
        0 8px 25px rgba(80, 70, 70, 0.08);

    margin-bottom: 2rem;
}


/* ============================================================
   BOTÓN BOKEH
   ============================================================ */

.bk-btn {
    border-radius: 18px !important;
}


/* ============================================================
   BOTONES STREAMLIT
   ============================================================ */

.stButton > button {
    background: linear-gradient(
        135deg,
        #D98E9F,
        #BFA7A0
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 16px !important;

    font-family: 'Quicksand', sans-serif !important;

    font-size: 1.05rem !important;

    font-weight: 700 !important;

    padding: 0.7rem 1.5rem !important;

    box-shadow:
        0 5px 0 #B97888;

    transition: 0.2s ease;
}


.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 7px 0 #B97888;
}


.stButton > button:active {
    transform: translateY(3px);

    box-shadow:
        0 2px 0 #B97888;
}


/* ============================================================
   SELECTBOX
   ============================================================ */

div[data-baseweb="select"] > div {
    background: #FFFFFF !important;

    border: 2px solid #D5E2D5 !important;

    border-radius: 14px !important;

    color: #3F4540 !important;
}


div[data-baseweb="select"] * {
    color: #3F4540 !important;
}


/* ============================================================
   CHECKBOX
   ============================================================ */

.stCheckbox label {
    color: #4D554E !important;

    font-weight: 600 !important;
}


/* ============================================================
   AUDIO
   ============================================================ */

audio {
    width: 100%;

    border-radius: 15px;
}


/* ============================================================
   TEXTO DE RESULTADO
   ============================================================ */

.output-text {
    background: #FFF7F8;

    border-left: 5px solid #D98E9F;

    border-radius: 15px;

    padding: 1.2rem;

    color: #4A4F4B;

    margin-top: 1rem;
}


/* ============================================================
   ETIQUETAS
   ============================================================ */

.section-label {
    display: inline-block;

    background: #E5F0E5;

    color: #617563;

    padding: 0.4rem 0.9rem;

    border-radius: 20px;

    font-size: 0.9rem;

    font-weight: 700;

    margin-bottom: 0.7rem;
}


/* ============================================================
   DIVISORES
   ============================================================ */

hr {
    border: none;

    border-top: 2px dashed #E5D5D8;

    margin: 2rem 0;
}


/* ============================================================
   MENSAJES
   ============================================================ */

div[data-testid="stAlert"] {
    border-radius: 16px;
}


/* ============================================================
   RESPONSIVE
   ============================================================ */

@media (max-width: 768px) {

    .main-title {
        font-size: 2.6rem;
    }

    .main-subtitle {
        font-size: 1rem;
    }

    .card,
    .card-green {
        padding: 1.2rem;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CARPETA TEMPORAL
# ============================================================

os.makedirs("temp", exist_ok=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🌸 Traductorcito")

    st.write(
        "Habla, elige los idiomas y deja que Traductorcito "
        "haga la magia. 🌿"
    )

    st.divider()

    st.subheader("🎙️ ¿Cómo funciona?")

    st.write(
        "1. Presiona **Escuchar**."
    )

    st.write(
        "2. Cuando escuches la señal, habla."
    )

    st.write(
        "3. Selecciona el idioma de entrada."
    )

    st.write(
        "4. Selecciona el idioma de salida."
    )

    st.write(
        "5. Presiona **Convertir**."
    )


# ============================================================
# ENCABEZADO
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🌸 TRADUCTORCITO'
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="main-subtitle">'
    'Escucho lo que quieres traducir 🌿'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# IMAGEN
# ============================================================

try:

    image = Image.open("duolingo.png")

    st.markdown(
        '<div class="image-box">',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(
        [1, 2, 1]
    )

    with col2:

        st.image(
            image,
            use_container_width=True
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

except FileNotFoundError:

    st.warning(
        "No se encontró la imagen 'duolingo.png'."
    )


# ============================================================
# INSTRUCCIÓN
# ============================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-label">'
    '🎤 Reconocimiento de voz'
    '</div>',
    unsafe_allow_html=True
)

st.subheader(
    "Toca el botón y habla"
)

st.write(
    "Presiona el botón y espera la señal. "
    "Cuando esté escuchando, di la frase que quieres traducir."
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# BOTÓN DE RECONOCIMIENTO DE VOZ
# ============================================================

stt_button = Button(
    label="🎤  Escuchar",
    width=300,
    height=50
)


stt_button.js_on_event(
    "button_click",
    CustomJS(code="""

        var recognition = new webkitSpeechRecognition();

        recognition.continuous = false;

        recognition.interimResults = true;

        recognition.lang = 'es-ES';


        recognition.onresult = function (e) {

            var value = "";

            for (
                var i = e.resultIndex;
                i < e.results.length;
                ++i
            ) {

                if (e.results[i].isFinal) {

                    value += e.results[i][0].transcript;

                }

            }


            if (value != "") {

                document.dispatchEvent(
                    new CustomEvent(
                        "GET_TEXT",
                        {
                            detail: value
                        }
                    )
                );

            }

        };


        recognition.onend = function() {

            console.log(
                "Reconocimiento detenido"
            );

        };


        recognition.start();

    """)
)


# ============================================================
# RESULTADO DEL RECONOCIMIENTO
# ============================================================

result = streamlit_bokeh_events(
    stt_button,

    events="GET_TEXT",

    key="listen",

    refresh_on_update=False,

    override_height=75,

    debounce_time=0
)


# ============================================================
# PROCESAR TEXTO
# ============================================================

if result:

    if "GET_TEXT" in result:

        text = str(
            result.get("GET_TEXT")
        )

        # ====================================================
        # TEXTO DETECTADO
        # ====================================================

        st.markdown(
            '<div class="card-green">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-label">'
            '💬 Texto detectado'
            '</div>',
            unsafe_allow_html=True
        )

        st.write(
            text
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


        # ====================================================
        # TRADUCTOR
        # ====================================================

        translator = Translator()


        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-label">'
            '🌎 Configuración'
            '</div>',
            unsafe_allow_html=True
        )


        st.subheader(
            "Elige los idiomas"
        )


        # ====================================================
        # IDIOMA DE ENTRADA
        # ====================================================

        in_lang = st.selectbox(

            "Idioma de entrada",

            (
                "Inglés",
                "Español",
                "Bengali",
                "Coreano",
                "Mandarín",
                "Japonés"
            )

        )


        if in_lang == "Inglés":

            input_language = "en"

        elif in_lang == "Español":

            input_language = "es"

        elif in_lang == "Bengali":

            input_language = "bn"

        elif in_lang == "Coreano":

            input_language = "ko"

        elif in_lang == "Mandarín":

            input_language = "zh-cn"

        elif in_lang == "Japonés":

            input_language = "ja"


        # ====================================================
        # IDIOMA DE SALIDA
        # ====================================================

        out_lang = st.selectbox(

            "Idioma de salida",

            (
                "Inglés",
                "Español",
                "Bengali",
                "Coreano",
                "Mandarín",
                "Japonés",
                "Ruso"
            )

        )


        if out_lang == "Inglés":

            output_language = "en"

        elif out_lang == "Español":

            output_language = "es"

        elif out_lang == "Bengali":

            output_language = "bn"

        elif out_lang == "Coreano":

            output_language = "ko"

        elif out_lang == "Mandarín":

            output_language = "zh-cn"

        elif out_lang == "Japonés":

            output_language = "ja"

        elif out_lang == "Ruso":

            output_language = "ru"


        # ====================================================
        # ACENTO
        # ====================================================

        english_accent = st.selectbox(

            "Acento",

            (
                "Defecto",
                "Español",
                "Reino Unido",
                "Estados Unidos",
                "Canada",
                "Australia",
                "Irlanda",
                "Sudáfrica"
            )

        )


        if english_accent == "Defecto":

            tld = "com"

        elif english_accent == "Español":

            tld = "com.mx"

        elif english_accent == "Reino Unido":

            tld = "co.uk"

        elif english_accent == "Estados Unidos":

            tld = "com"

        elif english_accent == "Canada":

            tld = "ca"

        elif english_accent == "Australia":

            tld = "com.au"

        elif english_accent == "Irlanda":

            tld = "ie"

        elif english_accent == "Sudáfrica":

            tld = "co.za"


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


        # ====================================================
        # FUNCIÓN TEXT TO SPEECH
        # ====================================================

        def text_to_speech(
            input_language,
            output_language,
            text,
            tld
        ):

            translation = translator.translate(
                text,
                src=input_language,
                dest=output_language
            )

            trans_text = translation.text


            tts = gTTS(
                trans_text,
                lang=output_language,
                tld=tld,
                slow=False
            )


            try:

                my_file_name = text[0:20]

            except:

                my_file_name = "audio"


            # Evitar caracteres problemáticos
            my_file_name = "".join(
                c for c in my_file_name
                if c.isalnum() or c in (" ", "_", "-")
            )


            if not my_file_name:

                my_file_name = "audio"


            archivo = (
                f"temp/{my_file_name}.mp3"
            )


            tts.save(archivo)


            return my_file_name, trans_text


        # ====================================================
        # MOSTRAR TEXTO
        # ====================================================

        display_output_text = st.checkbox(
            "Mostrar el texto traducido"
        )


        # ====================================================
        # BOTÓN CONVERTIR
        # ====================================================

        st.markdown(
            '<div style="margin-top: 1rem;">',
            unsafe_allow_html=True
        )


        if st.button(
            "🌿 Convertir",
            use_container_width=True
        ):

            try:

                with st.spinner(
                    "🌸 Preparando tu traducción..."
                ):

                    result_name, output_text = (
                        text_to_speech(
                            input_language,
                            output_language,
                            text,
                            tld
                        )
                    )


                # ============================================
                # AUDIO
                # ============================================

                audio_path = (
                    f"temp/{result_name}.mp3"
                )


                with open(
                    audio_path,
                    "rb"
                ) as audio_file:

                    audio_bytes = audio_file.read()


                st.success(
                    "✨ ¡Traducción lista!"
                )


                st.markdown(
                    '<div class="card-green">',
                    unsafe_allow_html=True
                )


                st.subheader(
                    "🎧 Tu audio"
                )


                st.audio(
                    audio_bytes,
                    format="audio/mp3",
                    start_time=0
                )


                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


                # ============================================
                # TEXTO DE SALIDA
                # ============================================

                if display_output_text:

                    st.markdown(
                        '<div class="output-text">',
                        unsafe_allow_html=True
                    )


                    st.subheader(
                        "💬 Texto traducido"
                    )


                    st.write(
                        output_text
                    )


                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )


            except Exception as e:

                st.error(
                    f"😿 No fue posible realizar la traducción: {e}"
                )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# LIMPIAR ARCHIVOS ANTIGUOS
# ============================================================

def remove_files(days):

    mp3_files = glob.glob(
        "temp/*mp3"
    )


    if len(mp3_files) != 0:

        now = time.time()

        seconds = days * 86400


        for f in mp3_files:

            try:

                if os.stat(f).st_mtime < (
                    now - seconds
                ):

                    os.remove(f)

            except:

                pass


remove_files(7)
