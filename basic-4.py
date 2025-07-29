import streamlit as st
import time

st.title("🔄 Session State & Interactivity")

# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'name' not in st.session_state:
    st.session_state.name = ""

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Counter Example
st.header("🔢 Counter Example")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Increment"):
        st.session_state.counter += 1

with col2:
    if st.button("➖ Decrement"):
        st.session_state.counter -= 1

with col3:
    if st.button("🔄 Reset"):
        st.session_state.counter = 0

st.write(f"**Current Count: {st.session_state.counter}**")

# Form Example
st.header("📝 Form Example")

with st.form("my_form"):
    st.write("Fill out this form:")
    
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    email = st.text_input("Email")
    
    # Form submit button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.session_state.name = name
        st.success(f"Form submitted! Hello {name}, age {age}")

# Display stored name
if st.session_state.name:
    st.write(f"Stored name: **{st.session_state.name}**")

# Chat-like Interface
st.header("💬 Chat Interface")

# Message input
new_message = st.text_input("Enter a message:", key="message_input")

col1, col2 = st.columns([1, 4])

with col1:
    if st.button("Send 📤"):
        if new_message:
            st.session_state.messages.append({
                'time': time.strftime("%H:%M:%S"),
                'message': new_message
            })
            # Clear the input by rerunning
            st.rerun()

with col2:
    if st.button("Clear Chat 🗑️"):
        st.session_state.messages = []
        st.rerun()

# Display messages
if st.session_state.messages:
    st.subheader("Messages:")
    for i, msg in enumerate(reversed(st.session_state.messages[-10:])):  # Show last 10 messages
        st.write(f"**{msg['time']}:** {msg['message']}")

# Callbacks Example
st.header("🎯 Callbacks")

def increment_counter():
    st.session_state.counter += 10

def decrement_counter():
    st.session_state.counter -= 10

col1, col2 = st.columns(2)

with col1:
    st.button("Add 10", on_click=increment_counter, key="add_10")

with col2:
    st.button("Subtract 10", on_click=decrement_counter, key="sub_10")

# Widget with key and callback
st.header("🎚️ Widget Callbacks")

def update_name():
    st.session_state.display_name = st.session_state.name_input.upper()

if 'display_name' not in st.session_state:
    st.session_state.display_name = ""

st.text_input(
    "Enter your name:",
    key="name_input",
    on_change=update_name
)

if st.session_state.display_name:
    st.write(f"Your name in CAPS: **{st.session_state.display_name}**")

# Progress Tracker
st.header("📈 Progress Tracker")

if 'progress' not in st.session_state:
    st.session_state.progress = 0

def advance_progress():
    if st.session_state.progress < 100:
        st.session_state.progress += 10

def reset_progress():
    st.session_state.progress = 0

col1, col2 = st.columns(2)

with col1:
    st.button("Advance Progress", on_click=advance_progress)

with col2:
    st.button("Reset Progress", on_click=reset_progress)

# Progress bar
progress_bar = st.progress(st.session_state.progress / 100)
st.write(f"Progress: {st.session_state.progress}%")

if st.session_state.progress >= 100:
    st.success("🎉 Progress Complete!")
    st.balloons()

# Debug: Show all session state
st.header("🔍 Debug: Session State")

if st.checkbox("Show session state"):
    st.write("Current session state:")
    st.write(dict(st.session_state))