import streamlit as st
import time
from PIL import Image
from datetime import datetime

# Set up the page tab
st.set_page_config(page_title="For Audrey ❤️", page_icon="🌹", layout="centered")

# --- CUSTOM CSS: FONTS, STYLING, AND CLEANUP ---
page_theme = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap');

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* The Heartbeat Animation for the Music Player */
@keyframes heartbeat {
    0% { transform: scale(1); }
    50% { transform: scale(1.08); color: #ff4b4b; }
    100% { transform: scale(1); }
}
.pulse-text {
    animation: heartbeat 1.5s infinite;
    text-align: center;
    color: #d11141;
}

/* Frosted Glass Background Update */
[data-testid="stAppViewContainer"] { 
    background-image: url("https://images.unsplash.com/photo-1532932371123-928bc0091ec0?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8bG92ZXxlbnwwfHwwfHx8MA%3D%3D"); 
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="block-container"] {
    background-color: rgba(255, 255, 255, 0.85) !important; /* Semi-transparent white card */
    backdrop-filter: blur(10px); /* Blurs the background behind the card */
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(209, 17, 65, 0.15); /* Soft red shadow */
    margin-top: 3rem;
    margin-bottom: 3rem;
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 800px; 
}

/* Pitch Black Text for Perfect Legibility */
.stMarkdown p, .stMarkdown li, .stMarkdown span {
    font-family: 'Playfair Display', serif !important;
    font-size: 18px !important;
    font-weight: 500 !important; 
    letter-spacing: 0.3px;
    line-height: 1.8 !important;
    color: #000000 !important; 
}

/* Classic Manuscript Styling for the Quote */
blockquote {
    background-color: rgba(255, 250, 251, 0.9);
    border-left: 4px solid #d11141;
    padding: 20px 25px;
    color: #111111 !important;
    font-style: italic;
    font-size: 20px !important;
    box-shadow: 2px 4px 10px rgba(209, 17, 65, 0.1);
    border-radius: 0 12px 12px 0;
    margin: 30px 0;
}

h1, h2, h3 {
    font-family: 'Dancing Script', cursive !important;
    color: #d11141 !important;
    font-size: 45px !important;
    text-align: center;
}

/* Button Styling */
.stButton>button {
    border-radius: 20px;
    border: 2px solid #d11141;
    color: white !important;
    background-color: #ff4b4b;
    font-family: 'Playfair Display', serif !important;
    transition: 0.3s;
    width: 100%; 
}

.stButton>button:hover {
    box-shadow: 0 0 15px #ff4b4b;
    border-color: #d11141;
}

/* Keeps text visible when the button is actively being clicked */
.stButton>button:focus, .stButton>button:active {
    color: white !important;
    background-color: #d11141 !important;
    border-color: #d11141 !important;
}

img {
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}

/* Fix the invisible image captions */
[data-testid="caption"], [data-testid="stImageCaption"], figcaption {
    color: #111111 !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 16px !important;
    font-style: italic;
    font-weight: 600 !important;
    text-align: center;
}

/* Mobile Responsive Design Tweaks */
@media (max-width: 768px) {
    [data-testid="block-container"], [data-testid="stMainBlockContainer"] {
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
        width: 95% !important;
    }
    h1 { font-size: 38px !important; }
    .stMarkdown p, .stMarkdown li, .stMarkdown span {
        font-size: 16px !important; 
        text-align: left !important; 
    }
}
</style>
"""
st.markdown(page_theme, unsafe_allow_html=True)

# --- GLOBAL FALLING HEARTS ANIMATION ---
falling_hearts_css = """
<style>
.heart { position: fixed; font-size: 1.5rem; top: -10vh; z-index: 9999; animation: fall linear infinite; pointer-events: none; }
@keyframes fall { 0% { top: -10vh; transform: translateX(0) rotate(0deg); opacity: 1; } 100% { top: 110vh; transform: translateX(20px) rotate(360deg); opacity: 0; } }
.h1 { left: 10%; animation-duration: 7s; animation-delay: 0s; } .h2 { left: 25%; animation-duration: 5s; animation-delay: 2s; } .h3 { left: 40%; animation-duration: 8s; animation-delay: 1s; } .h4 { left: 60%; animation-duration: 6s; animation-delay: 3s; } .h5 { left: 75%; animation-duration: 9s; animation-delay: 0.5s; } .h6 { left: 90%; animation-duration: 7.5s; animation-delay: 2.5s; }
</style>
<div class="heart h1">❤️</div><div class="heart h2">💖</div><div class="heart h3">💕</div><div class="heart h4">✨</div><div class="heart h5">❤️</div><div class="heart h6">💖</div>
"""
st.markdown(falling_hearts_css, unsafe_allow_html=True)


# --- SESSION STATE TO TRACK PAGES ---
if 'page' not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

def load_image(image_name, caption_text):
    try:
        img = Image.open(image_name)
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.image(img, caption=caption_text, use_container_width=True)
    except FileNotFoundError:
        st.warning(f"Upload '{image_name}' to see the photo here!")

# --- GLOBAL AUDIO PLAYER ---
st.write("---")
st.markdown("<h3 class='pulse-text'>Press Play 🎶</h3>", unsafe_allow_html=True)
st.audio("our_song.mp3")
st.write("---")

# --- BOOKLET PAGES ---

# PAGE 0: THE COVER
if st.session_state.page == 0:
    st.markdown("<h1>My Dearest SourPatch 💖</h1>", unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("Open the Booklet 📖", on_click=next_page)

# PAGE 1: THE INTRODUCTION
elif st.session_state.page == 1:
    st.markdown("<h1>Chapter 1: The Surprise</h1>", unsafe_allow_html=True)
    
    st.write("""
    I hope you enjoyed this little surprise I put together, obviously you said yes which is why you are reading this, or maybe no in which case we’ll see, haha! I apologize for taking so long, but I was very nervous and scared that maybe you’d reject me. Truth is I really want this to work, it doesn't matter how long it takes. I want to grow beside you, because you also encourage and push me to be more. 
    """)
    
    load_image('us.jpg', 'Where it all started...')
    
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Previous", on_click=prev_page)
    with col2:
        st.button("Next Page ➡️", on_click=next_page)

# PAGE 2: THE FEELINGS
elif st.session_state.page == 2:
    st.markdown("<h1>Chapter 2: The Side Quests</h1>", unsafe_allow_html=True)
    
    st.write("""
    We may have moved on fast, and it’s only been half a year, but I haven’t had as much fun and desire to improve more in these past couple months. I could tell you how beautiful you are, that sparkle in your eye, your infectious laugh, I can’t just help but admire you every chance I get hoping I get to keep you. Life’s very unpredictable, and regardless of what may happen, whatever the future holds, I will love and cherish every moment I get to spend with you! 
    
    As I write this my heart races, you truly have always left me nervous from the first time we kissed, each and everytime I try something new with you, the random side quests and activities we decide to do. I really fell hard for you and I’ll keep falling over and over again. You’re someone I never expected to meet, never thought I’d have, you were a light I never thought I’d see.
    """)
    
    load_image('us2.jpg', 'My favorite side quest partner')

    start_date = datetime(2025, 11, 12) 
    days_together = (datetime.now() - start_date).days

    st.markdown(f"<h3 style='font-size: 24px;'>{days_together} days since I fell for you. Literally!</h3>", unsafe_allow_html=True)
    
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Previous", on_click=prev_page)
    with col2:
        st.button("Next Page ➡️", on_click=next_page)

# PAGE 3: THE FINALE
elif st.session_state.page == 3:
    st.markdown("<h1>Chapter 3: Novia</h1>", unsafe_allow_html=True)
    
    st.write("""
    I am grateful to have met you and I really hope that this life lets me keep you. As delusional as it may seem, I will grow alongside you and we’ll achieve everything we set for our individual selves and together.

    I can now proudly call you my Novia!!!!

    **Te amo Audrey**, *I’ll cherish you for as long as I get too!*
    """)
    
    st.markdown("""
    > *"Accept the things to which fate binds you, and love the people with whom fate brings you together, but do so with all your heart."* — Marcus Aurelius
    """)
    
    st.write("---")
    
    if st.button("Current Love Status!"):
        progress_text = "Calculating exactly how much I love you..."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.03) 
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        time.sleep(1)
        my_bar.empty()
        st.error("🚨 Cooked!: I am completely obsessed and overly in love with you 🚨")
        st.markdown("<h1>💖♾️</h1>", unsafe_allow_html=True)
    
    st.write("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("⬅️ Read it again", on_click=prev_page)