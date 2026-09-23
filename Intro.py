import streamlit as st
from PIL import Image
st.title("Portafolio Interfaces Multimodales.")

with st.sidebar:
  st.subheader("Salomé Arango")
  parrafo = (
    "a continuación encontraran las paginas que he realizado durante las clases"
  )
  st.write(parrafo)


col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Analisis de texto")
 image = Image.open('analisisdetexto.webp')
 st.image(image, width=190)
 st.write("con la siguiente pagina se realiza un análisis del texto que se le ingrese") 
 url = "https://textico.streamlit.app/"
 st.write(f"texto [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos")
 image = Image.open('imagenanime.jfif')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://detector-de-imagenes-3.streamlit.app/"
 st.write(f"reconocimiento [Enlace]({url})")

 st.subheader("primera pagina")
 image = Image.open('peachygoma.png')
 st.image(image, width=200)
 st.write("en la siguiente pagina, veremos el primer acercamiento que tuve con github y streamlit") 
 url = "https://interfaces-multimodales1-primera-app.streamlit.app/"
 st.write(f"primera pagina: [Enlace]({url})")

 st.subheader("traductor de carteles")
 image = Image.open('chibipaises.jfif')
 st.image(image, width=200)
 st.write("la siguiente pagina es un traductor de imagenes, perfecto por si eres extrangero en un pais con otro idioma.") 
 url = "https://interfaces-multimodales1-primera-app.streamlit.app/"
 st.write(f"carteles: [Enlace]({url})")


with col2: 
 st.subheader("reconocimiento óptico de caracteres")
 image = Image.open('ocr.webp')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que convierte los textos de imagenes a texto.") 
 url = "https://lectorimagenes-salito.streamlit.app/"
 st.write(f" OCR: [Enlace]({url})")

 st.subheader("reconocmientos de imagenes")
 image = Image.open('animetech.avif')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar imagenes usando agentes de teachable machine.") 
 url = "https://modelo-detector-personas.streamlit.app/"
 st.write(f"agente [Enlace]({url})")

 st.subheader("nube de palabras")
 image = Image.open('nubedepalabras.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como tomar un texto y convertirlo en una nube de palabras") 
 url = "https://nubecitadepalabras.streamlit.app/"
 st.write(f"nube: [Enlace]({url})")


with col3: 
 st.subheader("Texto a Audio")
 image = Image.open('fabula.jfif')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que convierte el texto en audio, con un enfoque infantil, para convertir cuentos") 
 url = "https://pagina2-experimento.streamlit.app/"
 st.write(f"cuentos: [Enlace]({url})")

 st.subheader("Análisis de sentimiento")
 image = Image.open('emojis.avif')
 st.image(image, width=200)
 st.write("la siguiente pagina ánaliza las emociones que se ingresan, segun la polaridad") 
 url = "https://sentimentalismo-gifs.streamlit.app/"
 st.write(f"sentimientos: [Enlace]({url})")
 
 st.subheader("traductor")
 image = Image.open('duolingo.png')
 st.image(image, width=200)
 st.write("Esta pagina traduce el audio que se le ingrese") 
 url = "https://traductorcito-de-idiomas.streamlit.app/"
 st.write(f"traductorcito: [Enlace]({url})")


