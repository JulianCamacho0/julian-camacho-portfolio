import streamlit as st


st.subheader("📬 Contact")


st.markdown("""
You can reach out to me directly through this page by sending me a message, or you can contact me using any of the options below.  
""")
st.markdown('I’m always open to connecting, collaborating, or discussing new ideas.')

with st.form("contact_form"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    subject = st.text_input("Subject")
    message = st.text_area("Message", height=160)
    submitted = st.form_submit_button("Send", type='primary', width='stretch')

if submitted:
    if not name or not email or not message:
        st.error("Please fill in your name, email, and message.")
    else:
        st.session_state["contact_payload"] = {
            "name": name.strip(),
            "email": email.strip(),
            "subject": subject.strip() or "Portfolio contact",
            "message": message.strip(),
        }
        st.success("Thanks! Sending your message…")

st.markdown("""
    - **Email:** julianfcr0@gmail.com
    - **LinkedIn:** https://linkedin.com/in/julian-camacho-429a43249
""")
