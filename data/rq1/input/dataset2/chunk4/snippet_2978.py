#Source: https://stackoverflow.com/questions/75141095/streamlit-spacy-causing-attributeerror-pathdistribution-object-has-no-attr
import streamlit as st
import fitz

def load_file(file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")    
    text = []
    with doc:
        for page in doc:
            text.append(page.get_text())
        text = "\n".join(text)
    return text

#####################################################################   

st.title("Test app")

col1, col2 = st.columns([1,1], gap='small')

with col1:
    with st.expander("Description -", expanded=True):
        st.write("This is the description of the app.")
    
with col2:
    with st.form(key="my_form"):
        uploaded_file = st.file_uploader("Upload",type='pdf', accept_multiple_files=False, label_visibility="collapsed")
        submit_button = st.form_submit_button(label="Process")        

#####################################################################        
        
col1, col2 = st.columns([1,3], gap='small')

with col1:
    st.header("Metrics")

with col2:
    st.header("Text")
    
    if uploaded_file is not None:
        text = load_file(uploaded_file)
        st.text_area(text)