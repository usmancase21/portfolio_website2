import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
#genai.configure(api_key="AIzaSyA2JOVwQCH2_LTI9nLBUKgxq9pBqx8309E")
model =genai.GenerativeModel('gemini-1.5-flash')
 

 
col1, col2 = st.columns(2)
 
with col1:
    st.subheader("Hi :wave:")
    st.title("I am aiza")
 
with col2:
    st.image("images/2.jpeg")
 
st.title(" ")
persona = """
        You are Aiza AI bot. You help people answer questions about your self (i.e Aiza)
        Answer as if you are responding. donot answer in second or third person
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Aiza: 
         
        Aiza is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Generative AI.
        He teaches in MUST and Home schooling and educating over  Million developers, hobbyists and students. Aiza obtained his Bachelor’s degree in Software Engineering from MUST Mirpur(AJK) and expertise in AI and Python.
        She loves coding in languages like Python, React, Javascript, NextJS, FastAPi, Data Visualization, Data Analytics, Deep learning, Machine Learning, Computer Vision, Drone Programming.
        Aiza's Email: Aizajunaid189@gmail.com
        Aiza's Instagram: https://www.instagram.com/aiza.9
        Aiza's Github :https://github.com/aizajunaid
        """
st.title("aiza's AI Bot")


user_question=st.text_input("Ask anything about me")
if st.button("ASK❓", use_container_width=400):
    prompt = persona + "here is the question the user asked"+user_question
    response = model.generate_content(prompt)
    st.write(response.text)
 
st.title(" ")
 
col1, col2 = st.columns(2)
with col1:
    st.subheader("Baby cartoons")
    st.write("Best channel for toddlers")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")
 
 
st.title(" ")
 
st.title("My Setup")
st.image("images/2.jpeg")

st.write("")
st.title("My skills")
st.slider("programming",0,100,70)
st.slider("Teaching",0,100,85)
st.slider("Robotics",0,100,75)

st.write("")
st.title("Gallery")

col1, col2, col3 =st.columns(3)

with col1:
    st.image("images/1.jpeg")
    st.image("images/3.jpeg")
    st.image("images/4.jpeg")
with col2:
  st.image("images/5.jpeg")
  st.image("images/6.jpeg")
  st.image("images/7.jpeg")
 
with col3:
   st.image("images/2.jpeg")
   st.image("images/3.jpeg")
   st.image("images/6.jpeg")

st.write("")
st.subheader("CONTACT")
st.title("For any queries,please contact me at")
st.write("xyzpakistan31@gmail.com")


