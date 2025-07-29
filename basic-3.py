import streamlit as st
import pandas as pd
import numpy as np

st.title("🏗️ Streamlit Layout & Containers")

# Sidebar
st.sidebar.title("📋 Sidebar")
st.sidebar.write("This is the sidebar")

sidebar_option = st.sidebar.selectbox(
    "Choose an option:",
    ["Option 1", "Option 2", "Option 3"]
)

sidebar_slider = st.sidebar.slider("Sidebar slider:", 0, 100, 50)

# Columns
st.header("📊 Columns Layout")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Column 1")
    st.write("This is the first column")
    st.button("Button 1")

with col2:
    st.subheader("Column 2")
    st.write("This is the second column")
    chart_data = pd.DataFrame(
        np.random.randn(10, 1),
        columns=['Data']
    )
    st.line_chart(chart_data)

with col3:
    st.subheader("Column 3")
    st.write("This is the third column")
    option = st.selectbox("Choose:", ["A", "B", "C"])

# Different column ratios
st.header("⚖️ Custom Column Ratios")

col_a, col_b = st.columns([1, 2])  # 1:2 ratio

with col_a:
    st.write("Narrow column (1/3)")

with col_b:
    st.write("Wide column (2/3)")
    st.bar_chart(np.random.randn(10, 2))

# Containers
st.header("📦 Containers")

# Container
container = st.container()
container.write("This is inside a container")
container.bar_chart(np.random.randn(10, 2))

# Empty container (placeholder)
placeholder = st.empty()

# We can add content to placeholder later
import time
for i in range(5):
    placeholder.metric("Counter", i)
    time.sleep(1)

placeholder.write("Counting complete!")

# Expander
st.header("📁 Expander")

with st.expander("Click to expand"):
    st.write("This content is hidden by default")
    st.write("You can put any Streamlit elements here")
    
    data = pd.DataFrame({
        'x': np.random.randn(50),
        'y': np.random.randn(50)
    })
    
    st.scatter_chart(data)

# Tabs
st.header("📑 Tabs")

tab1, tab2, tab3 = st.tabs(["📈 Chart", "🗃 Data", "⚙️ Config"])

with tab1:
    st.subheader("A chart")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)

with tab2:
    st.subheader("Raw data")
    st.write(chart_data)

with tab3:
    st.subheader("Configuration")
    st.slider("Number of rows:", 1, 50, 20)
    st.selectbox("Chart type:", ["Line", "Bar", "Area"])

# Metrics
st.header("📊 Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Temperature", "70°F", "1.2°F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
col4.metric("Pressure", "1013 hPa", "0.5 hPa")

# Status containers
st.header("🚦 Status Containers")

# Success container
with st.container():
    st.success("Operation completed successfully!")
    st.write("All systems are running normally.")

# Warning container
with st.container():
    st.warning("Low disk space detected")
    st.write("Please free up some space.")

# Info container  
with st.container():
    st.info("New feature available!")
    st.write("Check out the latest updates.")

# Show sidebar selection result
st.header("📋 Sidebar Results")
st.write(f"You selected: {sidebar_option}")
st.write(f"Slider value: {sidebar_slider}")