import streamlit as st
import time 
import random 
from PIL import Image

# Set up the page tab
st.set_page_config(page_title="For Audrey ❤️", page_icon="🌹", layout="centered")

# --- CUSTOM CSS: FONTS, STYLING, AND CLEANUP ---
page_theme = """
<style>
/* Import beautiful Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap');

/* Hide Streamlit's default header, menu, and footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Soft background color */
[data-testid="stAppViewContainer"] {
    background-color: #fff0f5; 
}

/* Main Letter Text */
.stMarkdown p, .stMarkdown li, .stMarkdown span {
    font-family: 'Playfair Display', serif !important;
    font-size: 18px !important;
    letter-spacing: 0.3px;
    line-height: 1.8 !important;
    color: #333333;
}

/* Quote Block Styling */
blockquote {
    border-left: 3px solid #d11141;
    padding-left: 15px;
    color: #555555;
    font-style: italic;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* Titles and Headers */
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
    border-color: #ff4b4b;
}

/* Make the photo look like a polaroid */
img {
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}

/* --- MOBILE RESPONSIVE DESIGN & POLISH --- */
[data-testid="block-container"] {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 800px; 
}

@media (max-width: 768px) {
    [data-testid="block-container"] {
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
    }
    
    h1 {
        font-size: 38px !important; 
    }
    
    .stMarkdown p, .stMarkdown li, .stMarkdown span {
        font-size: 16px !important; 
        text-align: left !important; 
    }
    
    audio {
        width: 100% !important;
        outline: none !important;
    }
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
    pointer-events: none; 
}
@keyframes fall {
    0% { top: -10vh; transform: translateX(0) rotate(0deg); opacity: 1; }
    100% { top: 110vh; transform: translateX(20px) rotate(360deg); opacity: 0; }
}
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
st.markdown(falling_hearts_css, unsafe_allow_html=True)

# --- THE CONTENT ---

st.write("---") 
st.markdown("<h3 style='text-align: center;'>Press Play 🎶</h3>", unsafe_allow_html=True)
st.audio("our_song.mp3")

# Properly formatted title tag
st.markdown("<h1>My Dearest SourPatch 💖</h1>", unsafe_allow_html=True)

st.write("---")

st.write("""
I hope you enjoyed this little surprise I put together, obviously you said yes which is why you are reading this, or maybe no in which case we’ll see, haha! I apologize for taking so long, but I was very nervous and scared that maybe you’d reject me. Truth is I really want this to work, it doesn't matter how long it takes. I want to grow beside you, because you also encourage and push me to be more. 

We may have moved on fast, and it’s only been half a year, but I haven’t had as much fun and desire to improve more in these past couple months. I could tell you how beautiful you are, that sparkle in your eye, your infectious laugh, I can’t just help but admire you every chance I get hoping I get to keep you. Life’s very unpredictable, and regardless of what may happen, whatever the future holds, I will love and cherish every moment I get to spend with you! 

As I write this my heart races, you truly have always left me nervous from the first time we kissed, each and everytime I try something new with you, the random side quests and activities we decide to do. I really fell hard for you and I’ll keep falling over and over again. You’re someone I never expected to meet, never thought I’d have, you were a light I never thought I’d see.

I am grateful to have met you and I really hope that this life lets me keep you. As delusional as it may seem, I will grow alongside you and we’ll achieve everything we set for our individual selves and together.

I can now proudly call you my Novia!!!!

**Te amo Audrey**, *I’ll cherish you for as long as I get too!*
""")

st.markdown("""
> *"Accept the things to which fate binds you, and love the people with whom fate brings you together, but do so with all your heart."* — Marcus Aurelius
""")

# The Image
try:
    image = Image.open('us.jpg')
    st.image(image, caption='My favorite picture of us', use_container_width=True)
except FileNotFoundError:
    st.warning("Please make sure 'us.jpg' is uploaded to the same folder!")

st.write("---")

# --- MEMORY VAULT ---
st.markdown("<h3 style='text-align: center;'>📸 A Few of My Favorite Things</h3>", unsafe_allow_html=True)

with st.expander("My favorite memory so far..."):
    st.write("Write a little blurb here about a specific date or moment that stands out to you.")
    
with st.expander("What I noticed the very first time we met..."):
    st.write("Add another sweet note here!")

with st.expander("Just another reason I appreciate you..."):
    st.write("You can put a final thought, an inside joke, or another compliment in here!")

st.write("---")

# --- SIDE QUEST GENERATOR ---
st.markdown("<h3 style='text-align: center;'>🎲 Our Next Adventure</h3>", unsafe_allow_html=True)
st.write("Speaking of our random side quests... tap the button below to see what our next one is!")

if st.button("Generate our next Side Quest!"):
    quests = [
        "Late night ice cream and a drive 🍦",
        "Cook a brand new recipe together at home 🧑‍🍳",
        "Go for a walk and find a new coffee shop ☕",
        "Movie night, but you pick the movie and I bring the snacks 🍿",
        "A surprise activity planned entirely by me! ✨"
    ]
    st.success(f"**Your Quest:** {random.choice(quests)}")

st.write("---")

# --- FINAL SURPRISE BUTTON ---
if st.button("Click here for a surprise!"):
    progress_text = "Calculating exactly how much I love you..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.03) 
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    time.sleep(1)
    my_bar.empty()
    
    st.error("🚨 Cooked!: I am completely obssessed and overly in love with you 🚨")
    st.markdown("<h1>💖♾️</h1>", unsafe_allow_html=True)