import streamlit as st
import re
import google.generativeai as genai

apiKey = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=apiKey)

def get_score(description,resume):
  
  prompt = f"You are a Hiring Manager Reviewing Resumes. Your task is to evaluate a candidate's resume based on how well it matches a given job description. Return only a score out of 100 like an ATS along with an explanation of what is strong or lacking in the resume. Also provide Actionable suggestions (3–5 bullet points) that would help the candidate improve their resume to better match the job. Job Description: {description} Resume Content: {resume}. Provide the output in the format of Score:, Strengths:, Weaknesses:, and Suggestions:. Give only 1-3 points (word limit:100) for each strength and weakness and 3-5 points (word limit:250) for suggestions."
  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(prompt)

  score_match = re.search(r"Score:\s*(\d+)", response.text)
  strength_match = re.search(r"Strengths:(.*?)(Weaknesses:|Suggestions:|$)", response.text, re.DOTALL)
  weakness_match = re.search(r"Weaknesses:(.*?)(Suggestions:|$)", response.text, re.DOTALL)
  suggestions_match = re.search(r"Suggestions:(.*)", response.text, re.DOTALL)

  score = int(score_match.group(1)) if score_match else None
  strength = strength_match.group(1).rstrip() if strength_match else ""
  weakness = weakness_match.group(1).rstrip() if weakness_match else ""
  suggestions = suggestions_match.group(1).rstrip() if suggestions_match else ""

  return score, strength, weakness, suggestions
