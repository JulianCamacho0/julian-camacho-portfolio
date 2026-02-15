import streamlit as st
from utils import *

if 'utils' not in st.session_state:
    st.session_state.utils = Utils()

@st.cache_resource
def load_image(path: str):
    return st.session_state.utils.load_image(path)

def home():
    st.subheader("Hi, I'm Julian Camacho — a Data Engineer and Mathematician.")
    _ , center, _ = st.columns([1,2,1])
    with center:
        st.image(
            load_image("images/main_image.png")
        )
    st.divider()
    st.text('This website is my personal portfolio.')
    st.text('''
    Here you’ll find a collection of my work, technical projects, and the tools I’ve built. It’s designed to showcase my experience, share what I’m learning, and give you a clear view of the type of engineering I enjoy doing.
    ''')
    st.text('You will also find more about who I am, including my academic background, passions, skills, and professional experience.')
    st.divider()
    st.markdown(""" 
        By the way, I built this entire website using Streamlit, a lightweight and powerful Python framework for building data apps. You can explore the full source code [here](https://github.com/JulianCamacho0/julian-camacho-portfolio).
    """)

if __name__ == '__main__':

    home_page = st.Page(home, icon=':material/home:', title='Home')
    about_me_page = st.Page('pages/aboutMe.py', icon=':material/article_person:', title='About Me')
    experinece_page = st.Page('pages/experience.py', icon=':material/work_history:', title='Experience')
    projects_page = st.Page('pages/project.py', icon=':material/rocket_launch:', title='Projects')
    blog_page = st.Page('pages/blog.py', icon=':material/post:', title='Blog')
    contact_page = st.Page('pages/contact.py', icon=':material/contact_page:', title='Contact')

    pg = st.navigation([home_page, about_me_page, projects_page, contact_page])

    pg.run()