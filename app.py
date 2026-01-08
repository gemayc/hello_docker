import streamlit as st
import random
import os
import pandas as pd


# 📁 Carpeta y archivo donde se guardarán los nombres
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "nombres.txt")

# Crear la carpeta si no existe
os.makedirs(DATA_DIR, exist_ok=True)


# 🎨 Configuración de la página
st.set_page_config(
    page_title="Hello Docker 🐳",
    page_icon="🐳",
    layout="centered"
)

#  CSS - Diseño minimalista y moderno
st.markdown(
    """
    <style>
    /* Importar fuente moderna */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Fondo con gradiente animado */
    .main {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Container principal */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    
    /* Card principal con efecto neumórfico */
    .main-card {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 3rem;
        box-shadow: 
            20px 20px 60px rgba(102, 126, 234, 0.3),
            -20px -20px 60px rgba(255, 255, 255, 0.5);
        margin: 2rem 0;
        text-align: center;
    }
    
    /* Emoji animado */
    .whale-emoji {
    font-size: 6rem;
    animation: wave 2s ease-in-out infinite;
    display: block;           /* Cambié de inline-block a block */
    text-align: center;       /* Añadido */
    margin: 0 auto;          /* Añadido */
}
    
    @keyframes wave {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(-10deg); }
        75% { transform: rotate(10deg); }
    }
    
    /* Título principal */
    h1 {
        color: #667eea;
        font-size: 3rem !important;
        font-weight: 700;
        margin: 1rem 0 0.5rem 0 !important;
        text-align: center;
    }
    
    /* Subtítulo */
    .subtitle {
        color: #6b7280;
        font-size: 1.2rem;
        font-weight: 300;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Divisor decorativo */
    .divider {
        height: 3px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
        border-radius: 10px;
    }
    
    /* Input estilizado */
    .stTextInput > div > div > input {
        border: 2px solid #e5e7eb;
        border-radius: 15px;
        padding: 1rem;
        font-size: 1.1rem;
        text-align: center;
        transition: all 0.3s ease;
        background: #f9fafb;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
        background: white;
    }
    
    /* Botón mejorado */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1rem 3rem;
        font-size: 1.2rem;
        font-weight: 600;
        border-radius: 50px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
        cursor: pointer;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    /* Alertas personalizadas */
    .stAlert {
        border-radius: 15px;
        border: none;
        padding: 1.5rem;
        font-size: 1.1rem;
        text-align: center;
        animation: fadeIn 0.5s ease;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Info cards */
    .info-card {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateX(10px);
    }
    
    .info-card h3 {
        color: #667eea;
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
    }
    
    .info-card p {
        color: #4b5563;
        font-size: 1rem;
        margin: 0;
    }
    
    /* Footer mejorado */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.2);
    }
    
    .footer-text {
        color: #667eea;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .tech-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        margin: 0.3rem;
        font-size: 0.9rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* Stats contador */
    .stats {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-label {
        color: #6b7280;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# 🐳 Contenido principal
st.markdown("<div class='main-card'>", unsafe_allow_html=True)

# Emoji animado
st.markdown("<div class='whale-emoji'>🐳</div>", unsafe_allow_html=True)

# Título y subtítulo
st.title("Hello Docker")
st.markdown("<p class='subtitle'>Tu primera aplicación containerizada</p>", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Input y botón
name = st.text_input("", placeholder="✨ Escribe tu nombre aquí...", label_visibility="collapsed")

if st.button("🚀 ¡Saludar!"):
    if name:
        greetings = [
            f"🎉 ¡Hola {name}! Bienvenido/a al mundo Docker",
            f"👋 ¡Qué tal {name}! Estás dentro de un contenedor",
            f"🌟 ¡Hola {name}! Docker es genial, ¿verdad?",
            f"🚀 ¡Hey {name}! Tu app está corriendo en Docker"
        ]
        st.success(random.choice(greetings))
        st.balloons()
        
                # 💾 Guardar el nombre en el archivo
        with open(DATA_FILE, "a", encoding="utf-8") as f:
            f.write(name + "\n")

    else:
        st.warning("⚠️ No olvides escribir tu nombre")

# 📋 Mostrar nombres guardados en tabla

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        names = f.read().splitlines()

    if names:
        df = pd.DataFrame(
            {
                "👤 Nombre": names
            }
        )

        st.table(df)
    else:
        st.info("Aún no hay nombres guardados.")
else:
    st.info("Aún no hay datos guardados.")


st.markdown("</div>", unsafe_allow_html=True)

# Stats visuales
st.markdown(
    """
    <div class='stats'>
        <div class='stat-item'>
            <div class='stat-number'>100%</div>
            <div class='stat-label'>Portable</div>
        </div>
        <div class='stat-item'>
            <div class='stat-number'>∞</div>
            <div class='stat-label'>Escalable</div>
        </div>
        <div class='stat-item'>
            <div class='stat-number'>⚡</div>
            <div class='stat-label'>Rápido</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Cards informativos
st.markdown(
    """
    <div class='info-card'>
        <h3>🐍 Python + Streamlit</h3>
        <p>Aplicación web moderna y reactiva</p>
    </div>
    
    <div class='info-card'>
        <h3>🐳 Docker Container</h3>
        <p>Empaquetado y listo para ejecutar en cualquier lugar</p>
    </div>
    
    <div class='info-card'>
        <h3>☁️ Docker Hub</h3>
        <p>Comparte tu aplicación con el mundo</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown(
    """
    <div class='footer'>
        <p class='footer-text'>🐳 Aplicación ejecutándose en contenedor Docker</p>
        <div>
            <span class='tech-badge'>🐍 Python</span>
            <span class='tech-badge'>🎈 Streamlit</span>
            <span class='tech-badge'>🐳 Docker</span>
        </div>
        <p style='margin-top: 1rem; color: #9ca3af; font-size: 0.9rem;'>Hecho con ❤️ para aprender Docker</p>
    </div>
    """,
    unsafe_allow_html=True
)