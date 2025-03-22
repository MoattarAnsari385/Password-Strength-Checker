import re
import streamlit as st

st.set_page_config(page_title='Ultimate Password Strength Checker', page_icon="🛡️", layout="centered")                                                   
st.title("🛡️ Secure Password Checker")
st.markdown("""
## 🔒 Enhance Your Password Security! 👋🏻  
Wondering if your password is strong enough? Use this tool to analyze its strength  
and get valuable tips to make it more secure.  
Let's create a **robust and unbreakable password** together! 🚀            
""")

password = st.text_input("Enter your Password", type="password")

st.markdown("""
    <style>
    div.stButton > button { 
        background-color: #00bcd4 !important; 
        color: #fff !important;
        display: block;
        margin: 0 auto;  
        border-radius: 8px;
        font-weight: 700;
    }
    h1 { margin-bottom : 5px; }
    .stMarkdown { margin-top: -5px; }
    
    div.stButton > button:hover { 
    background-color: transparent !important; 
    color: #eee !important;
    }
    </style>
""", unsafe_allow_html=True)

if st.button('Check Strength'):
    feedback = []
    score = 0
    if password:
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password should be at least 8 characters long.")

        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("❌ Password should contain both uppercase and lowercase letters.")

        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append('❌ Password should contain at least one digit.')

        if re.search(r"[#$&!@=()*?~]", password):
            score += 1
        else:
            feedback.append('❌ Password should contain at least one special character (e.g., !@#$%^&*?~).')

        st.progress(score / 4)

        if score == 4:
            st.success("✅ Great job! Your password is **strong** and secure. 🎉")
        elif score == 3:
            st.warning("🟡 Your password is **moderate**. Consider making it stronger for better security.")
        else:
            st.error("🔴 Your password is **weak**! Please improve it to enhance security.")

        if feedback:
            st.markdown("## 🛠️ Improvement Suggestions.\n")
            for tip in feedback:
                st.error(tip)
    else:
        st.info("Please enter your password to get started.")
