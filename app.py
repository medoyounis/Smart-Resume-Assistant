#field to insert Job Description
#Upload resume PDF
#Convert PDF to image --> processing --> Google Gemini Pro
from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai
import pyttsx3
engine = pyttsx3.init()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel("gemini-pro-vision")
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text
#convert the pdf to image
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
#streamlit app
st.set_page_config(page_title="Mohammed's ATS Resume Analysis")
st.header("Resume Analysis System by Mohammed Younis")
input_text=st.text_area("Job Description:",key="input")
uploaded_file=st.file_uploader("Upload your resume in PDF Format", type=["pdf"])
if uploaded_file is not None:
    st.write("PDF was uploaded successfully")
on = st.toggle('Activate Text to Speech')
submit1=st.button("Tell me about the resume")
submit2=st.button("What are all the keywords for this job and which ones are missing")
submit3 = st.button("How can I improve my resume")
submit4 = st.button("Write a cover letter for this job")
submit5 = st.button("Ask me an interview question using this job description?")
submit6 = st.button("Does the resume contain any grammatical or spelling errors? or any formatting issues?")
submit7=st.button("How to standout?")
submit8=st.button("How to tailor this resume better?")
Additional=st.text_input("Additional Questions?")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""
input_prompt2 = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,what are all the keywords for this job, and which ones are missing from the resume?
what is the percentage for the match between the resume and the job description?

"""
input_prompt3 = """
#  You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
#   Please share your professional evaluation on how the candidate can improve his resume to make it more suitable for the job requirements.
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
"""


input_prompt4 = """
You are an experienced Technical Human Resource Manager,your task is to review the provided resume and the job description. 
  Please write a cover letter for this job using the provided resume.
"""
input_prompt5= """
You are an experienced Technical Human Resource Manager,your task is to review the provided resume and the job description. 
  Please ask me interview question using both the job description and the provided resume?
"""
input_prompt6= """
You are an experienced Technical Human Resource Manager,your task is to review the provided resume and check if the resume contains any grammatical or spelling errors, typos, or formatting issues.
"""
input_prompt7 = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. using the resume and job description, how can the candidate standout.
"""
input_prompt8 = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. after you read the resume and the job description, is it possible to rewrite some of the bullet points that are in the resume to make them more suitable to what the hiring company wants in the ideal candidate.
make sure to only rewrite bulletpoints that are in the resume to make them more suitable for this job. do not write anything that is not in the resume.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
        if on:
            engine.say(response)
            engine.runAndWait()
    else:
        st.write("Please upload the resume")
elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
        if on:
            engine.say(response)
            engine.runAndWait()
    else:
        st.write("Please upload the resume")
elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
        if on:
            engine.say(response)
            engine.runAndWait()
    else:
        st.write("Please upload the resume")
elif submit4:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt4,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
        if on:
            engine.say(response)
            engine.runAndWait()
    else:
        st.write("Please upload the resume")
elif submit5:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt5,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
        if on:
            engine.say(response)
            engine.runAndWait()
    else:
        st.write("Please upload the resume")
elif submit6:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt6,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
        if on:
            engine.say(response)
            engine.runAndWait()
    else:
        st.write("Please upload the resume")
elif submit7:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt7,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
        if on:
            engine.say(response)
            engine.runAndWait()
    else:
        st.write("Please upload the resume")
elif submit8:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt8,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
        if on:
            engine.say(response)
            engine.runAndWait()
    else:
        st.write("Please upload the resume")
elif Additional:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(Additional,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
        if on:
            engine.say(response)
            engine.runAndWait()
    else:
        st.write("Please upload the resume")
