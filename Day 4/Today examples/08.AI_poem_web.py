import openai
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("OPENAI_AZURE_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

    
subject = st.text_input("주제를 입력하세요: ")
content = st.text_area("시를 작성할 내용을 입력하세요: ")

button_click = st.button("시 작성하기")

if button_click:
    with st.spinner("Wait for it...", show_time=True):
        response = openai.chat.completions.create(
            model="dev-gpt-4o-mini",
            temperature=0.7,
            max_tokens=300,
            messages=[
                {"role": "system", "content": "You are a AI poem."},
                {"role": "user", "content": "주제: " + subject + 
                                            "\n내용: " + content + 
                                            "\n시를 작성해 주세요."},
            ]
        )

        st.write(response.choices[0].message.content)