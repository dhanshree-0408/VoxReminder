import streamlit as st
from streamlit_mic_recorder import mic_recorder
import whisper
import os
from processor import extract_info
from scheduler import trigger_notifications
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

# Initialize the Background Scheduler
if 'scheduler' not in st.session_state:
    st.session_state.scheduler = BackgroundScheduler()
    st.session_state.scheduler.start()

@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

# UI SETUP
st.set_page_config(page_title="VoxReminder AI", page_icon="🎙️")
st.title("🎙️ VoxReminder AI")
st.markdown("---")

# User Preferences
email_input = st.text_input("Enter Email for Alerts:", "example@gmail.com")
st.caption("Tip: Try 'Remind me to start the meeting in one minute'")

model = load_whisper()

# VOICE RECORDING
audio = mic_recorder(
    start_prompt="Record Reminder", 
    stop_prompt="Stop & Process", 
    key='recorder'
)

if audio:
    with st.spinner("AI is analyzing your voice..."):
        with open("input.wav", "wb") as f:
            f.write(audio['bytes'])
        
        # 1. Transcription (Whisper)
        result = model.transcribe("input.wav", fp16=False)
        transcript = result['text']
        st.info(f"**Detected:** {transcript}")

        # 2. Logic Parsing (Processor)
        task, alert_dt = extract_info(transcript)

        # 3. Validation & Scheduling
        if alert_dt and alert_dt > datetime.now():
            st.success(f"✅ **Scheduled:** {task}")
            st.write(f"⏰ **Alert set for:** {alert_dt.strftime('%I:%M:%S %p')}")
            
            # Schedule the background notification and email
            st.session_state.scheduler.add_job(
                trigger_notifications, 
                'date', 
                run_date=alert_dt, 
                args=[task, email_input]
            )
            st.toast("Reminder Locked In!")
        else:
            st.error("I heard you, but the time seems to be in the past or could not be parsed.")
        
        if os.path.exists("input.wav"):
            os.remove("input.wav")

st.markdown("---")
st.caption("Dhanshree Patel | AI Automation Project 2026")