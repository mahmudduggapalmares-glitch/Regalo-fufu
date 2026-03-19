import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Para Ti", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #000000; }
    iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

html_final =
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { margin: 0; overflow: hidden; background: #000; font-family: 'serif'; color: white; touch-action: manipulation; }
        canvas { position: fixed; top: 0; left: 0; z-index: 1; }
        .main-content {
            position: relative; z-index: 5;
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            height: 100vh; text-align: center;
            pointer-events: none;
        }
        .poem-box { pointer-events: auto; padding: 20px; }
        .star-clickable {
            position: absolute; width: 30px; height: 30px; 
            z-index: 10; display: flex; align-items: center; justify-content: center;
            cursor: pointer;
        }
        .star-inner { 
            width: 5px; height: 5px; background: white; border-radius: 50%; 
            box-shadow: 0 0 15px #fff, 0 0 25px #fff; 
            animation: twinkle 2s infinite ease-in-out;
        }
        @keyframes twinkle { 0%, 100% { opacity: 0.3; transform: scale(0.8); } 50% { opacity: 1; transform: scale(1.2); } }
        #message-display {
            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
            background: rgba(0,0,0,0.8); backdrop-filter: blur(10px);
            padding: 25px; border-radius: 15px; border: 1px solid #444;
            display: none; z-index: 100; text-align: center; width: 80%; color: #fff;
        }
    </style>
</head>
<body>
    <canvas id="starCanvas"></canvas>
    <div id="message-display"></div>

    <div class="main-content">
        <div class="poem-box">
            <h1 style="font-weight:100; letter-spacing:4px; margin-bottom:0;">Perdóname</h1>
            <p style="font-style:italic; color:#aaa; font-size:0.9rem;">Toca las estrellas para escuchar y leer mi corazón</p>
        </div>
    </div>

    <div id="player"></div>

    <script>
        // Cargar la API de YouTube para control total
        var tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

        var player;
        function onYouTubeIframeAPIReady() {
            player = new YT.Player('player', {
                height: '0', width: '0',
                videoId: 'soRmpPJOIwo',
                playerVars: { 'autoplay': 1, 'loop': 1, 'playlist': 'soRmpPJOIwo' },
                events: { 'onReady': onPlayerReady }
            });
        }
        function onPlayerReady(event) {
            // El navegador bloqueará el play automático, así que sonará al primer clic
        }

        // Dibujo de estrellas de fondo
        const canvas = document.getElementById('starCanvas');
        const ctx = canvas.getContext('2d');
        let w = canvas.width = window.innerWidth;
        let h = canvas.height = window.innerHeight;
        const bgStars = Array.from({length: 100}, () => ({ x: Math.random()*w, y: Math.random()*h, r: Math.random()*1 }));
        function draw() {
            ctx.clearRect(0,0,w,h); ctx.fillStyle = "white";
            bgStars.forEach(s => { ctx.globalAlpha = 0.5; ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI*2); ctx.fill(); });
            requestAnimationFrame(draw);
        }
        draw();

        const frases = [
            "Te amo más que a nada en este mundo.",
            "Extraño cada segundo que pasamos juntos.",
            "Me duele el alma haberte fallado.",
            "Eres y serás siempre mi único gran amor.",
            "Daría mi vida por recuperar tu sonrisa.",
            "Perdón por ser un tonto y no valorarte."
        ];

        frases.forEach((texto) => {
            const container = document.createElement('div');
            container.className = 'star-clickable';
            container.style.top = (Math.random() * 70 + 15) + '%';
            container.style.left = (Math.random() * 85 + 5) + '%';
            
            const dot = document.createElement('div');
            dot.className = 'star-inner';
            container.appendChild(dot);

            container.onclick = () => {
                // ACTIVAR MÚSICA AL TOCAR CUALQUIER ESTRELLA
                if (player && player.playVideo) { player.playVideo(); }
                
                const display = document.getElementById('message-display');
                display.innerText = texto;
