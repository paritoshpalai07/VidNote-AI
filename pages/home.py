import streamlit as st

st.set_page_config(
    page_title="YouTube Summarizer",
    page_icon=":material/robot:",
    layout="wide"
)

center = "style ='text-align: center;'"

# --- HERO SECTION ---
with st.container():
    st.html(f"<h1 {center}>Summarize YouTube Videos & Take Notes Effortlessly &#x1f3ac; &#x1f4dd; &#x26a1;</h1>")
    st.html(f"<p {center}>Save time &#x231b;, improve comprehension &#x1f9e0;, and learn faster &#x1f680; with our intelligent YouTube summarizer and note-taking tool.</p>")
    # col1, col2, col3 = st.columns([0.1,2,0.1])
    # col2.write("Save time :hourglass:, improve comprehension :brain:, learn faster :zap:, with our intelligent youtube summarizer and note-taking tool.")
# --- FEATURES SECTION ---
with st.container():
    st.write("---")
    st.subheader("Key Benefits :star2:")

    st.write("""
             - Automatic Summarization 🤖 :bookmark_tabs:
                 Generate concise summaries of any YouTube video, saving you hours of time.
             - Note-Taking :notebook:
                 Take notes directly within the tool and organize them effectively.
             - Highlight Key Points :mag_right:
                 Identify and highlight the most important concepts for effortless review.
             - Time-Saving :hourglass:
                 Cut down on video playback time and focus on the essential content.
             - Easy to Use :ok_hand:
                 Simple and intuitive interface, accessible to everyone.
             """)
    st.write("---")

with st.container():
    st.subheader("Technology ⚙ ")
    st.write("""
            - Python (Front-End : Streamlit)
             """)

    st.write("---")

with st.container():
    st.subheader("APIs 💻🔗")
    st.write("""
            - YouTube Transcript API : to get the transcript of the youtube video.
            - Gemini API : To generate the notes based on the youtube video transcript.
             """)
    st.write("---")

# col1, col2, col3 = st.columns([2,1,2])
# col2.write("Made with :heart: by Paritosh Palai")
st.html("<p style = 'text-align: center;'>Made with ❤ by Paritosh Palai</p>")
st.write("---")
    