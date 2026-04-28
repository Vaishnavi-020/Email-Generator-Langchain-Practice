from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
import os
import certifi
import streamlit as st
from dotenv import load_dotenv
from EmailOuput import EmailOut

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()

llm=HuggingFaceEndpoint(
    model="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_ACCESS_TOKEN")
)

model=ChatHuggingFace(llm=llm)

st.header("Email Generator")

st.subheader("Email Purpose:")
tone=st.selectbox("Select the tone of the mail",["Select...","formal","confident","friendly","persuasive","business","professional","Other"])
purpose=st.selectbox("Select the purpose of the mail",["Select...","General Business and professional","Customer support and technical",""
"Recruitment and Career","Project management and tech teams","Academic and university","Others"])

st.subheader("About sender")
name=st.text_input("name:")
background=st.text_input("background:")

st.subheader("About Receiver")
receiver_role=st.text_input("Reciever:")
company=st.text_input("Company:")

extra_context=st.text_area("Any additional information: (For good response you may consider providing a little bit of information about the email that you want.)")

template=PromptTemplate(template = """
You are an expert professional email writer.

Write a {tone} email for the following purpose:
{purpose}

Sender details:
- Name: {name}
- Background: {background}

Receiver details:
- Role: {receiver_role}
- Organization: {company}

Additional context:
{extra_context}

Instructions:
- Keep the email concise (150–200 words)
- Maintain a professional and polite tone
- Avoid generic phrases
- Personalize based on the context
- Include a clear call-to-action

Return the output in the following structured format:
- subject
- greeting
- body
- closing
""")

input_variables=["tone","purpose","name","background","receiver_role","company","extra_context"]

prompt=template.invoke({
    'tone':tone,
    'purpose':purpose,
    'name':name,
    'background':background,
    'receiver_role':receiver_role,
    'company':company,
    'extra_context':extra_context
})

if st.button("Summarize"):
    result=model.invoke(prompt)
    st.write(result.content)