import streamlit as st
import pandas as pd

# 1. SETUP
st.set_page_config(page_title="The Python Launchpad", page_icon="🚀", layout="wide")

# 2. SIDEBAR
with st.sidebar:
    st.header("⚙️ Pilot Settings")
    pilot_name = st.text_input("Enter Pilot Name:")
    rank = st.selectbox("Select Your Rank:", ["Cadet", "Rookie", "Captain", "Commander"])

    st.write(f"**Status:** Ready for launch, {rank}!")

    st.divider()
    st.write("### Mission Controls")
    dark_mode = st.toggle("Enable Stealth Mode")

# 3. MAIN PAGE HEADER
st.title("🚀 The Python Launchpad")
st.write(f"Welcome to mission control, **{pilot_name if pilot_name else 'Pilot'}**.")

st.divider()

# 4. DATA SECTION
st.subheader("📊 Your Learning Velocity")
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Lines of Code": [10, 25, 15, 40, 60, 85, 100],
}
df = pd.DataFrame(data)
st.line_chart(df.set_index("Day"))

st.divider()

# 5. INTERACTIVE COLUMNS
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Mission Checklist")
    tasks = ["Install Python", "Setup VS Code", "Understand Loops", "Build Data Chart"]
    for task in tasks:
        st.checkbox(task)

with col2:
    st.subheader("📝 Mission Log")
    user_notes = st.text_area(
        "Write a note about what you learned today:",
        "Today I mastered Streamlit columns...",
    )
    if st.button("Save Log"):
        st.toast("Log saved to memory!")

st.divider()

# 6. FOOTER ACTION
if st.button("INITIATE LAUNCH SEQUENCE"):
    st.balloons()
    st.success(f"Mission Success! Site created for {pilot_name if pilot_name else 'Pilot'}.")
    st.balloons()
# --- MISSION BRIEFING (The "About" Section) ---
with st.expander("📖 View Mission Briefing"):
    st.write("""
        Welcome to The Python Launchpad! This is your mission control center for learning Python in a fun and interactive way. 
        Here, you can track your learning progress, manage your coding tasks, and log your journey as you ascend through the ranks of Python mastery. 
        Whether you're a Cadet just starting out or a Commander ready to conquer complex projects, this site is designed to support your growth as a Python pilot. 
        Buckle up and enjoy the ride!
    """)