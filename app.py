import streamlit as st

# Set up the page tab
st.set_page_config(page_title="For Audrey ❤️", page_icon="🌹", layout="centered")

# --- CUSTOM CSS: FONTS, STYLING, AND CLEANUP ---
page_theme = """
<style>
/* Import beautiful Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap');

/* 1. Hide Streamlit's default header, menu, and footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* 2. Soft background color */
[data-testid="stAppViewContainer"] {
    background-color: #fff0f5; 
}

/* 3. Main Letter Text (Playfair Display) */
p, li, span, div {
    font-family: 'Playfair Display', serif !important;
    font-size: 18px !important;
    line-height: 1.8 !important; /* Adds nice spacing between lines */
    color: #333333;
}

/* 4. Titles and Headers (Dancing Script) */
h1, h2, h3 {
    font-family: 'Dancing Script', cursive !important;
    color: #d11141 !important;
    font-size: 45px !important;
}

/* 5. Button Styling */
.stButton>button {
    border-radius: 20px;
    border: 2px solid #d11141;
    color: white !important;
    background-color: #ff4b4b;
    font-family: 'Playfair Display', serif !important;
    transition: 0.3s;
}
.stButton>button:hover {
    box-shadow: 0 0 15px #ff4b4b;
    border-color: #ff4b4b;
}

/* 6. Make the photo look like a polaroid/styled frame */
img {
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}
</style>
"""
st.markdown(page_theme, unsafe_allow_html=True)

# --- FALLING HEARTS ANIMATION ---
falling_hearts_css = """
<style>
.heart {
    position: fixed;
    font-size: 1.5rem;
    top: -10vh;
    z-index: 9999;
    animation: fall linear infinite;
    pointer-events: none; /* Ensures you can still click things behind the hearts */
}
@keyframes fall {
    0% { top: -10vh; transform: translateX(0) rotate(0deg); opacity: 1; }
    100% { top: 110vh; transform: translateX(20px) rotate(360deg); opacity: 0; }
}
/* Different falling speeds, delays, and positions for a natural look */
.h1 { left: 10%; animation-duration: 7s; animation-delay: 0s; }
.h2 { left: 25%; animation-duration: 5s; animation-delay: 2s; }
.h3 { left: 40%; animation-duration: 8s; animation-delay: 1s; }
.h4 { left: 60%; animation-duration: 6s; animation-delay: 3s; }
.h5 { left: 75%; animation-duration: 9s; animation-delay: 0.5s; }
.h6 { left: 90%; animation-duration: 7.5s; animation-delay: 2.5s; }
</style>

<div class="heart h1">❤️</div>
<div class="heart h2">💖</div>
<div class="heart h3">💕</div>
<div class="heart h4">✨</div>
<div class="heart h5">❤️</div>
<div class="heart h6">💖</div>
"""

# Inject the CSS and HTML into the app
st.markdown(falling_hearts_css, unsafe_allow_html=True)

# Center the title
st.markdown("My Dearest SourPatch 💖", unsafe_allow_html=True)

st.write("---")

# Your love letter goes here
st.write("""
I hope you enjoyed this little surprise I put together, obviously you said yes which is why you are reading this, or maybe no in which case we’ll see, haha! I apologize for taking so long, but I was very nervous and scared that maybe you’d reject me. Truth is I really want this to work, it doesn't matter how long it takes. I want to grow beside you, because you also encourage and push me to be more. 

We may have moved on fast, and it’s only been half a year, but I haven’t had as much fun and desire to improve more in these past couple months. I could tell you how beautiful you are, that sparkle in your eye, your infectious laugh, I can’t just help but admire you every chance I get hoping I get to keep you. Life’s very unpredictable, and regardless of what may happen, whatever the future holds, I will love and cherish every moment I get to spend with you! 

As I write this my heart races, you truly have always left me nervous from the first time we kissed, each and everytime I try something new with you, the random side quests and activities we decide to do. I really fell hard for you and I’ll keep falling over and over again. You’re someone I never expected to meet, never thought I’d have, you were a light I never thought I’d see.

I am grateful to have met you and I really hope that this life lets me keep you. As delusional as it may seem, I will grow alongside you and we’ll achieve everything we set for our individual selves and together.


I can now proudly call you my Novia!!!!

**Te amo Audrey**, *I’ll cherish you for as long as I get too!*

""")

# Optional: Add a picture of you two! 
# Just save an image as 'us.jpg' in the same folder and uncomment the next lines:
from PIL import Image
image = Image.open('us.jpg')
st.image(image, caption='My favorite picture of us', use_container_width=True)

st.write("---")

import time # Add this to the very top of your file with your imports!

# ... (your existing letter code) ...

if st.button("Click here for a surprise!"):
    # 1. A fun loading sequence
    progress_text = "Calculating exactly how much I love you..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.03) # Adjust speed here
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    # Clear the bar once it hits 100%
    time.sleep(1)
    my_bar.empty()
    
    # 2. The grand reveal
    st.error("🚨 SYSTEM OVERLOAD: Unquantifiable Amount of Love Detected! 🚨")
    st.markdown("### 💖♾️")
    
    # 3. Optional: Add an audio file of 'your song'
    # To do this, upload an mp3 file to your GitHub folder and uncomment the line below:
    # st.audio("our_song.mp3")