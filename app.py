import streamlit as st
from google import genai

# 🔑 API key
client = genai.Client(api_key="AIzaSyA3X7gNHlcUsoHW25KvLW5Co9RdbTDJ5ws")

# Page config
st.set_page_config(page_title="AI Study Assistant", page_icon="📚", layout="centered")

# Header
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>📚 AI Study Assistant</h1>
    <p style='text-align: center;'>Summarize notes • Generate questions • Learn faster 🚀</p>
""", unsafe_allow_html=True)

st.divider()

# Input Section
st.subheader("📝 Enter Study Content")
user_input = st.text_area("Paste your notes, homework, or exam content here:", height=200)

# Options
col1, col2 = st.columns(2)

with col1:
    task_type = st.selectbox("📌 Select Task", [
        "Summarize Notes",
        "Extract Key Points",
        "Generate Exam Questions",
        "Explain in Simple Language"
    ])

with col2:
    tone = st.selectbox("🎯 Select Tone", ["Simple", "Formal"])

st.divider()

# Generate Button
if st.button("✨ Generate AI Output"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        try:
            prompt = f"""
            You are an AI study assistant.

            Task: {task_type}
            Tone: {tone}

            Based on the input:
            - Summarize clearly
            - Extract key points
            - Generate exam questions if needed
            - Explain in simple language if asked

            Content:
            {user_input}
            """

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            st.success("✅ AI Generated Output")
            st.subheader("📊 Result")
            st.write(response.text)

        except:
            st.warning("⚠️ API limit reached. Showing demo output.")

            st.subheader("📊 Sample Output")

            st.markdown("""
### 🧾 Summary
Artificial Intelligence enables machines to perform tasks that require human intelligence.

### 🔑 Key Points
- AI is used in healthcare, education, and finance  
- Improves efficiency and accuracy  
- Raises ethical concerns  

### ❓ Exam Questions
1. What is Artificial Intelligence?  
2. Applications of AI  
3. Advantages and disadvantages of AI  
""")

# Footer
st.divider()
st.markdown("<p style='text-align: center;'>Made by Anjali 💙 | Promptathon 2026</p>", unsafe_allow_html=True)