import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs([':material/book: Education', ':material/work_history: Professional Experience', ':material/accessibility: Featured Skills', ':material/mountain_flag: Climbing & Personal Growth'])

with tab1:
    st.markdown('### Education')
    st.markdown("""
        I have a strong academic foundation in mathematics, which shapes the way I think and approach problems. Studying
        mathematics taught me how to break complex ideas into structured components, reason with precision, and build solutions
        based on clarity and logic, all of which translate directly into the way I work as an engineer.
    """)

    with st.expander('Undergraduate Studies', icon=':material/book_4:', expanded=False):
        _,center,_ = st.columns(3)
        with center:
            st.image(
                st.session_state.utils.load_image('images/logo_escuela.png')
            )
        st.markdown("""
        I studied Mathematics on a merit‑based scholarship I earned thanks to my national ICFES exam results. I also began a double program in Systems Engineering, which I ultimately did not complete, but key courses like:
        """)
        st.markdown('- **Object‑Oriented Programming**: During OOP, I collaborated on a Java Snakes and Ladders game: https://github.com/JffMv/Game-Stairs-and-Snakes')
        st.markdown('-  **Algorithms and Data Structures**: Where I first got hooked on competitive programming. I joined a competitive programming team, competed nationally in 2022, and qualified for the regional round. This experience sharpened my algorithmic thinking, teamwork, and problem‑solving skills.')

    with st.expander('Postgraduate Studies', icon=':material/eyeglasses_2:', expanded=False):
        _,center,_ = st.columns(3)
        with center:
            st.image(
                st.session_state.utils.load_image('images/data2_science.png')
            )
        st.markdown("""
            After graduating in Mathematics with the second-highest GPA in my cohort, I was awarded a university scholarship to pursue a postgraduate degree at the same institution. I’m currently studying a Master’s in Data Science.
        """)
        st.markdown("""
            Although I’m not seeking a Data Scientist role, this program has deepened my understanding of machine learning algorithms and their practical implications (model behavior, evaluation, and limitations), which directly enhances my work as a Data Engineer.  I’m open to roles related to MLOps, where my engineering background, ML understanding, and data workflow experience naturally fit.
        """)

with tab3:
    st.markdown('### Featured Skills')
    st.markdown('This section highlights the professional and personal skills that define how I work and how I learn.')

    with st.expander('Self‑Taught & Continuous Learner', icon=':material/local_library:'):
        st.markdown("""
            I’m passionate about learning independently and staying up to date in a fast‑evolving tech landscape.  I’ve completed more than **10 professional certifications** across platforms such as **Udemy, Platzi, AWS Academy, Google Cloud Skill Boosts**, and others. You can view all my verified certifications here: 
            -  https://www.credential.net/profile/juliancamacho146783/wallet
            - https://www.credly.com/users/julian-camacho.ee830e72/edit#other
        """)
    with st.expander('Fast Learner', icon=':material/bolt:'):
        st.markdown("""
            I have the ability to quickly grasp new technical concepts and apply them in real-world situations. This enables me to adapt rapidly to new tools, environments, and challenges—delivering value from the early stages of any project.
        """)

with tab2:
    st.markdown('### Professional Experience')
    st.markdown('In this section, you’ll find an overview of my professional journey, including the roles I’ve taken on, the responsibilities I’ve led, and the impact of my work.')
    
    with st.expander(' University Lecturer ', icon=':material/school:'):
        st.markdown('######  University Lecturer — Escuela Colombiana de Ingeniería Julio Garavito.')
        _,center,_ = st.columns(3)
        with center:
            st.image(
                st.session_state.utils.load_image('images/logo_escuela.png')
            )
        _,_,der = st.columns(3)
        with der:
            st.markdown('**2025 – 2026 (present)**')
        st.markdown("""
            I worked as a university lecturer teaching first- and second‑year engineering students in subjects including **Linear Algebra**, **Integral Calculus**, **Differential Calculus**, and **Mathematical Models for Computer Science**. My responsibilities included:
        """)
        st.markdown("""
        - Designing and delivering course content, lectures, and hands‑on activities.  
        - Creating study materials, assignments, and assessments.  
        - Guiding students through foundational mathematical concepts essential for engineering and computer science.  
        - Supporting students in developing analytical thinking and problem‑solving skill
        """)
    
    with st.expander('Data Engineer', icon=':material/code:'):
        st.markdown('###### Data Engineer — Bancolombia (Talento B) ')
        _,center,_ = st.columns(3)
        with center:
            st.image(
                st.session_state.utils.load_image('images/bancolombia.png')
            )
        _,_,der = st.columns(3)
        with der:
            st.markdown('**08/2025 – 2026 (present)**')
        st.markdown("""
            As a Data Engineer in Bancolombia’s analytics and experimentation ecosystem, I have worked on both technical implementation and solution design for internal tools and data pipelines. Key contributions include:
        """)
        st.divider()
        st.markdown('- Developing **Atenea**, a Streamlit-based application for A/B testing experiment management')
        st.markdown("""
        Atenea is an internal application that simplifies and accelerates experimentation for analytics teams. It provides an intuitive interface for creating and managing A/B tests, with a backend built in Python, a Streamlit frontend, and data persistence on Apache Hadoop using Impala as the main query engine. 
        """)
        st.divider()
        st.markdown('- My current project is focused on the data quality monitoring stage of the **MLOps lifecycle**. ')
        st.markdown('We are developing a complete package built on top of Apache Spark to track, validate, and ensure the reliability of data used in machine learning pipelines. This solution aims to provide scalable, automated checks that support robust model performance in production environments.')



with tab4:
    st.markdown('### Climbing & Personal Growth')
    st.markdown('Outside of engineering, one of my biggest passions is rock climbing. It has become a discipline that teaches me far more than just movement, it constantly shapes how I approach challenges in my daily life.')
    with st.expander('Rock Climbing', icon=':material/mountain_flag:'):
        izq, der = st.columns(2)
        with izq:
            st.image(
                st.session_state.utils.load_image('images/climb2.png')
            )
        with der:
            st.subheader('Climbing has taught me:')
            st.markdown('''
            - patience and strategic thinking
            - how to stay calm under pressure
            - the value of incremental progress
            - resilience when facing difficult routes
            - discipline and consistency in training
            - how to handle failure constructively 
            ''')