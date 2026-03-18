import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Misión Especial: Fufu", page_icon="🎮")

# Estilos personalizados para un look "Gamer/Romántico"
st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">🎮 BIENVENIDA AL NIVEL: EL PERDÓN DE FUFU 🎮</p>', unsafe_allow_html=True)

# Inicializar el estado del juego
if 'level' not in st.session_state:
    st.session_state.level = 1

# --- NIVEL 1: EL ACERTIJO ---
if st.session_state.level == 1:
    st.subheader("Etapa 1: La Llave de la Sinceridad")
    st.write("Para avanzar, debes resolver este acertijo sobre nosotros:")
    st.info("Soy algo que no se puede ver, pero que tú llenas por completo. Soy lo que siento cada vez que escucho tu nombre. ¿Qué soy?")
    
    respuesta = st.text_input("Escribe tu respuesta aquí:").lower().strip()
    if st.button("Verificar"):
        if "amor" in respuesta:
            st.success("¡Correcto! Mi amor por ti es la energía de este juego.")
            time.sleep(1)
            st.session_state.level = 2
            st.rerun()
        else:
            st.error("Inténtalo de nuevo... (Pista: Es lo que siento por ti)")

# --- NIVEL 2: LOS ELOGIOS ---
elif st.session_state.level == 2:
    st.subheader("Etapa 2: El Inventario de Maravillas")
    st.write("Para desbloquear el siguiente nivel, admite que estas cosas son ciertas sobre ti:")
    
    c1 = st.checkbox("Eres la chica más inteligente que conozco.")
    c2 = st.checkbox("Tu sonrisa ilumina hasta mi día más oscuro.")
    c3 = st.checkbox("Eres lo mejor que me ha pasado en la vida.")
    
    if st.button("Desbloquear"):
        if c1 and c2 and c3:
            st.balloons()
            st.session_state.level = 3
            st.rerun()
        else:
            st.warning("¡Debes marcar todas! Porque todas son verdad.")

# --- NIVEL 3: EL PERDÓN ---
elif st.session_state.level == 3:
    st.subheader("Etapa Final: El Boss del Perdón")
    st.write("Fufu, sé que he cometido errores, pero tú eres mi jugadora favorita. Este mensaje es para pedirte perdón de todo corazón.")
    
    st.write("> **\"Eres mi mundo, y no hay partida que valga la pena si no es a tu lado. Te amo mucho.\"**")
    
    option = st.radio("¿Aceptas mis disculpas y reiniciamos nuestra partida?", ["...", "Sí, acepto", "Tal vez (pero di que sí)"])
    
    if option == "Sí, acepto":
        st.subheader("🏆 ¡MISIÓN CUMPLIDA! 🏆")
        st.write("Ahora que estamos bien... tengo la pregunta más importante de todas:")
        st.markdown("### **¿Quieres jugar juntos hoy?**")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Puedes cambiar esto por un gif o video de ustedes
        if st.button("VOLVER A EMPEZAR"):
            st.session_state.level = 1
            st.rerun()

