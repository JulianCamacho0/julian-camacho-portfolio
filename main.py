import streamlit as st
from PIL import Image, ImageFile
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

@st.cache_data
def load_image(rel_path: str):
    """
    Carga una imagen desde una ruta relativa a este archivo.
    Ejemplo: load_image("images/main_image.png")
    """
    img_path = BASE_DIR / rel_path  # Construye la ruta de forma portable
    return Image.open(img_path)


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


if __name__ == '__main__':

    home_page = st.Page(home, icon=':material/home:', title='Home')
    about_me_page = st.Page('pages/aboutMe.py', icon=':material/article_person:', title='About Me')
    experinece_page = st.Page('pages/experience.py', icon=':material/work_history:', title='Experience')
    projects_page = st.Page('pages/project.py', icon=':material/rocket_launch:', title='Projects')
    blog_page = st.Page('pages/blog.py', icon=':material/post:', title='Blog')
    contact_page = st.Page('pages/contact.py', icon=':material/contact_page:', title='Contact')

    pg = st.navigation([home_page, about_me_page, experinece_page, projects_page, contact_page])

    pg.run()