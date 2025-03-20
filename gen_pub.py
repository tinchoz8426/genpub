import streamlit as st
from groq import Groq

# Inicializar Groq con la clave del entorno
groq = Groq(api_key=st.secrets["API_KEY_GROQ"])

def generate_creative_post(texto_entrada):
    """Genera una publicación creativa basada en el texto de entrada"""
    response = groq.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {"role": "system", "content": "Eres un experto en marketing digital y creación de contenido social. Tu tarea es convertir el texto proporcionado en una publicación creativa y atractiva para redes sociales."},
            {"role": "user", "content": f"Texto de entrada: {texto_entrada}\nCrea una publicación que incluya emojis, hashtags relevantes y un tono atractivo para engagement."}
        ]
    )
    return response.choices[0].message.content

def main():
    st.title("✨ Generador de Publicaciones Creativas para Redes Sociales ✨")
    
    # Agregar una explicación en la sidebar
    with st.sidebar:
        st.header("Bienvenido a nuestro generador de publicaciones creativas")
        st.markdown("""
        Esta herramienta utiliza la potencia de Groq para generar contenido atractivo para redes sociales.
        Ingrese su texto en el campo de entrada y obtenga una publicación creativa en segundos.
        """)
    
    with st.expander("Ingrese su texto aquí"):
        texto_entrada = st.text_area("Texto de entrada", height=150)
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.markdown("### Publicación Generada")
        if texto_entrada:
            try:
                publicacion = generate_creative_post(texto_entrada)
                st.markdown(publicacion)
            except Exception as e:
                st.error(f"Error al generar la publicación: {str(e)}")
    
    with col2:
        if st.button(" Generar Publicación Aleatoria 🎰"):
            response = groq.chat.completions.create(
                model="mixtral-8x7b-32768",
                messages=[
                    {"role": "system", "content": "Eres un experto en marketing digital y creación de contenido social. Crea una publicación creativa y atractiva para redes sociales."},
                    {"role": "user", "content": "Crea una publicación aleatoria sobre un tema interesante y actual."}
                ]
            )
            st.markdown(response.choices[0].message.content)

if __name__ == "__main__":
    main()