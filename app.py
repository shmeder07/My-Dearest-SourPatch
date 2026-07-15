import streamlit as st

# Set up the page tab
st.set_page_config(page_title="To My Beautiful Girl ❤️", page_icon="💌")

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

Te amo Audrey, I’ll cherish you for as long as I get too!

""")

# Optional: Add a picture of you two! 
# Just save an image as 'us.jpg' in the same folder and uncomment the next lines:
from PIL import Image
image = Image.open('us.jpg')
st.image(image, caption='My favorite picture of us', use_container_width=True)

st.write("---")

# A fun interactive element
if st.button("For You"):
    st.balloons() # This triggers a cool balloon animation on screen!
    st.success("I love you endlessly! 💕")