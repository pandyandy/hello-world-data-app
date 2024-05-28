# Importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

# Title and Description
st.markdown(
    """
    <div style="text-align: right;">
        <img src="https://assets-global.website-files.com/5e21dc6f4c5acf29c35bb32c/5e21e66410e34945f7f25add_Keboola_logo.svg" alt="Keboola Logo" width="150">
    </div>
    """, unsafe_allow_html=True)

st.title('Hello, World!')
st.caption("""
This app is designed to be your friendly guide to the basics of Streamlit – whether you're a beginner or just looking to refresh your skills, this app will walk you through essential Streamlit concepts and demonstrate some of the most popular widgets and features you can use to create interactive web apps.
""")

# Section 1: Streamlit Basics
st.header("1. Text Elements")
st.markdown("""
- **Title & Headers:** `st.title`, `st.header`, `st.subheader`
- **Text & Markdown:** `st.write`, `st.markdown`, `st.text`
""")

# Demonstrating Headers and Text
col1, col2 = st.columns(2)
with col1:
    st.subheader("Examples:")
with col2:
    st.code('st.subheader("Examples:")', language="python")

col1, col2 = st.columns(2)
with col1:
    st.write("This is an example of `st.write`.")
with col2:
    st.code('st.write("This is an example of `st.write`.")', language="python")

col1, col2 = st.columns(2)
with col1:
    st.markdown("This is an example of **Markdown**.")
with col2:
    st.code('st.markdown("This is an example of **Markdown**.")', language="python")

# Section 2: Input Widgets
st.header("2. Input Widgets")

# Button
st.subheader("Button")
col1, col2 = st.columns(2)
with col1:
    if st.button("Click me!"):
        st.write("Button clicked!")
with col2:
    st.code("""
if st.button("Click me!"):
    st.write("Button clicked!")
""", language="python")

# Checkbox
st.subheader("Checkbox")
col1, col2 = st.columns(2)
with col1:
    checkbox_state = st.checkbox("Check me!")
    if checkbox_state:
        st.write("Checkbox is checked!")
with col2:
    st.code("""
checkbox_state = st.checkbox("Check me!")
if checkbox_state:
    st.write("Checkbox is checked!")
""", language="python")

# Radio buttons
st.subheader("Radio")
col1, col2 = st.columns(2)
with col1:
    radio_choice = st.radio("Choose an option:", ("Option 1", "Option 2", "Option 3"))
    st.write(f"You selected: {radio_choice}")
with col2:
    st.code("""
radio_choice = st.radio("Choose an option:", ("Option 1", "Option 2", "Option 3"))
st.write(f"You selected: {radio_choice}")
""", language="python")

# Selectbox
st.subheader("Selectbox")
col1, col2 = st.columns(2)
with col1:
    selectbox_choice = st.selectbox("Choose another option:", ["Choice A", "Choice B", "Choice C"])
    st.write(f"You selected: {selectbox_choice}")
with col2:
    st.code("""
selectbox_choice = st.selectbox("Choose another option:", ["Choice A", "Choice B", "Choice C"])
st.write(f"You selected: {selectbox_choice}")
""", language="python")

# Multiselect
st.subheader("Multiselect")
col1, col2 = st.columns(2)
with col1:
    multiselect_choices = st.multiselect("Select multiple options:", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected: {multiselect_choices}")
with col2:
    st.code("""
multiselect_choices = st.multiselect("Select multiple options:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {multiselect_choices}")
""", language="python")

# Slider
st.subheader("Slider")
col1, col2 = st.columns(2)
with col1:
    slider_value = st.slider("Choose a value:", 0, 100, 50)
    st.write(f"Slider value: {slider_value}")
with col2:
    st.code("""
slider_value = st.slider("Choose a value:", 0, 100, 50)
st.write(f"Slider value: {slider_value}")
""", language="python")

# Toggle
st.subheader("Toggle")
col1, col2 = st.columns(2)
with col1:
    toggle = st.toggle("Show Sidebar")
    if toggle:
        st.write("Sidebar shown.")
        st.sidebar.header("Sidebar")
        st.sidebar.write("You can also use the sidebar with `st.sidebar`.")
        st.sidebar.code("""
        st.sidebar.header("Sidebar")
        st.sidebar.write("You can also use the sidebar with `st.sidebar`.")
        """, language="python")
with col2:
    st.code("""
toggle = st.toggle("Show Sidebar")
if toggle:
    st.write("Sidebar shown.")
""", language="python")


# Date input
st.subheader("Date Input")
col1, col2 = st.columns(2)
with col1:
    date_value = st.date_input("Select a date:", date.today())
    st.write(f"Selected date: {date_value}")
with col2:
    st.code("""
date_value = st.date_input("Select a date:", date.today())
st.write(f"Selected date: {date_value}")
""", language="python")

# Number input
st.subheader("Number Input")
col1, col2 = st.columns(2)
with col1:
    number_value = st.number_input("Enter a number:", value=10)
    st.write(f"Input number: {number_value}")
with col2:
    st.code("""
number_value = st.number_input("Enter a number:", value=10)
st.write(f"Input number: {number_value}")
""", language="python")

# File Uploader Example
st.subheader("File Uploader")
uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Data uploaded.")
    st.dataframe(df)
st.code("""
uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Data uploaded.")
    st.dataframe(df)
""", language="python")

# Section 3: Interactive Data Display
st.header("3. Interactive Data Display")

# Dataframe
st.subheader("DataFrame")
col1, col2 = st.columns(2)
with col1:
    data_frame = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
    st.dataframe(data_frame)
with col2:
    st.code("""
data_frame = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
st.dataframe(data_frame)
""", language="python")

# Line Chart
st.subheader("Line Chart")
col1, col2 = st.columns(2)
with col1:
    line_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
    st.line_chart(line_chart_data)
with col2:
    st.code("""
line_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(line_chart_data)
""", language="python")

# Bar Chart
st.subheader("Bar Chart")
col1, col2 = st.columns(2)
with col1:
    bar_chart_data = pd.DataFrame(np.random.randn(10, 3), columns=['Jan', 'Feb', 'Mar'])
    st.bar_chart(bar_chart_data)
with col2:
    st.code("""
bar_chart_data = pd.DataFrame(np.random.randn(10, 3), columns=['Jan', 'Feb', 'Mar'])
st.bar_chart(bar_chart_data)
""", language="python")

# Area Chart
st.subheader("Area Chart")
col1, col2 = st.columns(2)
with col1:
    area_chart_data = pd.DataFrame(np.random.randn(100, 3), columns=["A", "B", "C"])
    st.area_chart(area_chart_data)
with col2:
    st.code("""
area_chart_data = pd.DataFrame(np.random.randn(100, 3), columns=["A", "B", "C"])
st.area_chart(area_chart_data)
""", language="python")

# Final Remarks
st.subheader("That's it! 🎉")
st.caption("""
We hope you enjoyed exploring the basics of Streamlit with our 'Hello, World!' app. Now that you've seen how easy and powerful Streamlit can be, we encourage you to start building your own data apps. Happy coding! Team Keboola 💙
""")
