import streamlit as st
import google.generativeai as genai
import os

# --- السطر السحري لحل مشكلة السكرين شوتس ---
# ده بيجبر المكتبة تكلم السيرفر المستقر مباشرة
os.environ["GOOGLE_GENERATIVE_AI_NETWORK_ENDPOINT"] = "generativelanguage.googleapis.com"

# حط الـ API Key بتاعك هنا
MY_API_KEY = "AIzaSyCOdFVcx0W2pdlfh5uDTq-v5DN2zD2ZfWU" 

genai.configure(api_key=MY_API_KEY)

# استخدام الموديل باسمه المباشر
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="X ASSISTANT v2", page_icon="⚡")

# دخول شيك سريع
st.markdown("<h1 style='text-align: center; color: #00f2fe;'>🚀 X ASSISTANT v2</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الشات
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# منطقة الكتابة
if prompt := st.chat_input("تؤمرني بإيه يا حريف؟"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # طلب الرد بطريقة مجردة لتفادي أخطاء النسخ
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("السيرفر لسه مأكسد!")
            st.info(f"الخطأ الجديد: {e}")
          
