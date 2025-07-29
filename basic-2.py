import streamlit as st
import datetime

st.title("🎛️ Streamlit Input Widgets")

# Text inputs
st.header("📝 Text Inputs")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

message = st.text_area("Write a message:", height=100)
if message:
    st.write(f"Your message: {message}")

password = st.text_input("Enter password:", type="password")

# Number inputs
st.header("🔢 Number Inputs")

age = st.number_input("How old are you?", min_value=0, max_value=120, value=25)
st.write(f"You are {age} years old")

rating = st.slider("Rate your experience (1-10):", 1, 10, 5)
st.write(f"Your rating: {rating}")

price_range = st.select_slider(
    "Select price range:",
    options=['$', '$$', '$$$', '$$$$'],
    value='$$'
)

# Selection widgets
st.header("🎯 Selection Widgets")

# Radio buttons
transport = st.radio(
    "How do you commute?",
    ["Car", "Bus", "Train", "Bike", "Walk"]
)
st.write(f"You selected: {transport}")

# Selectbox (dropdown)
city = st.selectbox(
    "Which city do you live in?",
    ["New York", "London", "Tokyo", "Paris", "Mumbai"]
)

# Multiselect
colors = st.multiselect(
    "What are your favorite colors?",
    ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"],
    default=["Blue", "Green"]
)

if colors:
    st.write("You selected:", colors)

# Checkbox
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing!")

# Date and time
st.header("📅 Date and Time")

birthday = st.date_input("When is your birthday?")
meeting_time = st.time_input("What time is the meeting?")

# File uploader
st.header("📁 File Upload")

uploaded_file = st.file_uploader(
    "Choose a file",
    type=['txt', 'csv', 'xlsx', 'json']
)

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write(f"File name: {uploaded_file.name}")
    st.write(f"File size: {uploaded_file.size} bytes")

# Buttons
st.header("🔘 Buttons")

if st.button("Primary Button", type="primary"):
    st.success("Primary button clicked!")

if st.button("Secondary Button"):
    st.info("Secondary button clicked!")

# Download button
csv_data = "name,age,city\nAlice,25,NYC\nBob,30,LA"
st.download_button(
    label="Download CSV file",
    data=csv_data,
    file_name="sample_data.csv",
    mime="text/csv"
)

# Display all values
st.header("📋 Summary of Your Inputs")

if name:
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Transport:** {transport}")
    st.write(f"**City:** {city}")
    st.write(f"**Rating:** {rating}")
    st.write(f"**Birthday:** {birthday}")
    
    if colors:
        st.write(f"**Favorite Colors:** {', '.join(colors)}")