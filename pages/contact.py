import streamlit as st
import smtplib, ssl
from email.message import EmailMessage

def send_email_smtp(payload: dict) -> bool:
    try:
        cfg = st.secrets["email"]
        msg = EmailMessage()
        msg["Subject"] = f"[Portfolio] {payload['subject']}"
        msg["From"] = cfg["user"]
        msg["To"] = cfg["to"]
        msg.set_content(
            "New contact message from your portfolio:\n\n"
            f"Name: {payload['name']}\n"
            f"Email: {payload['email']}\n"
            f"Subject: {payload['subject']}\n\n"
            f"Message:\n{payload['message']}\n"
        )

        context = ssl.create_default_context()
        with smtplib.SMTP(cfg["smtp_server"], cfg["smtp_port"]) as server:
            server.starttls(context=context)   # activa TLS
            server.login(cfg["user"], cfg["password"])
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False


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
        
        ok = send_email_smtp(st.session_state["contact_payload"])
        if ok:
            st.success("Your message was sent successfully. I’ll get back to you soon!")
        else:
            st.error("There was a problem sending your message. Please try again later.")

st.markdown("""
    - **Email:** julianfcr0@gmail.com
    - **LinkedIn:** https://linkedin.com/in/julian-camacho-429a43249
""")
