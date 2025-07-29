import streamlit as st
import pandas as pd
import numpy as np

# Basic Streamlit Elements
st.title("🚀 Streamlit Fundamentals")
st.header("Learning Streamlit Step by Step")
st.subheader("Basic Elements")

# Text elements
st.text("This is plain text")
st.markdown("This is **bold** and *italic* text")
st.markdown("You can also use markdown with `code` blocks")

st.code("""
def hello_world():  
    print("Hello, Streamlit!")
""", language='python')

# Divider
st.divider()

# Display data
st.subheader("📊 Data Display")

# Create sample data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Tokyo', 'Paris']
})

# Display dataframe
st.dataframe(data)

# Display table (static)
st.table(data.head(2))

# Display JSON
st.json({'name': 'Streamlit', 'version': '1.28', 'language': 'Python'})

# Divider
st.divider()

# Charts
st.subheader("📈 Simple Charts")

# Line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)

# Bar chart
st.bar_chart(chart_data)

# Area chart
st.area_chart(chart_data)

# Divider
st.divider()

# Status elements
st.subheader("🎯 Status Elements")

st.success("This is a success message!")
st.info("This is an info message!")
st.warning("This is a warning message!")
st.error("This is an error message!")

# Progress bar
import time

progress_bar = st.progress(0)
status_text = st.empty()

for i in range(101):
    progress_bar.progress(i)
    status_text.text(f'Progress: {i}%')
    time.sleep(0.1)

status_text.text('Complete!')

# Balloons celebration
if st.button("🎈 Celebrate!"):
    st.balloons()