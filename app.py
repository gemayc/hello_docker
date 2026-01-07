import streamlit as st

# 🎨 Configuración general de la página
st.set_page_config(
    page_title="Hello Docker",
    page_icon="🐳",
    layout="centered"
)

# 🎨 CSS simple para mejorar el aspecto
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }
    h1 {
        color: #0DB7ED;
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: #4A5568;
        font-size: 18px;
    }
     .card {
        background-color: #9ADCF3; 
        padding: 20px;
        border-radius: 12px;
        # border-left: 6px solid #0DB7ED;
        box-shadow: 0px 4px 10px rgba(13, 183, 237, 0.15);
        margin-top: 20px;
    </style>
    """,
    unsafe_allow_html=True
)

# 🐳 Título
st.title("🐳 Hello Docker")
st.markdown(
    "<p class='subtitle'>Mini aplicación web en Python con Streamlit</p>",
    unsafe_allow_html=True
)

# 📦 Tarjeta principal
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.write(
    "Esta es una **mini aplicación web** creada para aprender Docker. "
    "Se ejecuta dentro de un contenedor y se puede compartir fácilmente con cualquier persona."
)

name = st.text_input("👤 Escribe tu nombre")

if st.button("🚀 Saludar"):
    if name:
        st.success(f"Hola {name} 👋 Bienvenida/o al mundo Docker 🐳")
    else:
        st.warning("Por favor, escribe tu nombre para continuar 🙂")

st.markdown("</div>", unsafe_allow_html=True)

#  Sección extra visual
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 ¿Qué estamos aprendiendo aquí?")
st.markdown(
    """
    - Cómo ejecutar una app web en Python  
    - Cómo meterla dentro de Docker  
    - Cómo compartirla con Docker Hub  
    """
)
st.markdown("</div>", unsafe_allow_html=True)

#  Footer
st.markdown("---")
st.caption("Aplicación ejecutándose dentro de un contenedor Docker 🐳")
