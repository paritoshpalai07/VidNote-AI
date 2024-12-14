import streamlit as st
import google.generativeai as genai 
from youtube_transcript_api import YouTubeTranscriptApi

# --- PAGE SETUP ---
st.set_page_config(
    page_title="YouTube Summarizer",
    page_icon=":material/robot:",
    layout="centered"
)

# --- FUNCTION TO GET VIDEO ID ---
def get_video_id(str):
    list = str.split("https://youtu.be/")
    video_id = list[1].split("?si=")[0]
    return video_id

st.title("Lets get started!")

url = st.text_input("Paste the url of YouTube Video:")
btn = st.button("Get Notes!")

if btn:
    try:
        vid_id = get_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(vid_id, languages=['en','hi']) 
        success_msg =  st.success("Hang tight! Your notes are being crafted with the finest virtual quill and ink.")

        summary = ""
        for line in transcript:
            summary = summary + line["text"] + " "

        genai.configure(api_key=st.secrets["API_KEY"])

        model = genai.GenerativeModel('gemini-1.5-flash')

        prompt = f"X is the transcript of the youtube video. X : {summary}. I want to make notes of each topic in transcript and make all possible Q&A on each with answers"

        response = model.generate_content(prompt)

        response = response.text.replace("Transcript", "Video")
        response = response.replace("transcript", "video")
        if success_msg:
            success_msg.empty()
        st.write(response)
    except:
        st.warning("Sorry! Video Notes for this video cannot be generated")