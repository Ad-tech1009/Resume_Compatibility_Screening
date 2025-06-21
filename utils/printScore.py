import streamlit as st
import plotly.graph_objects as go
import time
import re

def bullet_points(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    lines = text.replace("* ", "\n* ").strip().split('\n')
    html_list = "<ul>"
    for line in lines:
        if line.startswith("*"):
            line = line.lstrip("* ").strip()
            html_list += f"<li>{line}</li>"
    html_list += "</ul>"
    return html_list

def display_score_gauge(score):
    col1, col2 = st.columns(2)
    with col1:
      gauge_placeholder = st.empty()
      for scr in range(0, score + 1):
        gradient_steps = [{"range": [i, i + 1], "color": f"rgb({255 - int(i * 2.55)}, {int(i * 2.55)}, 0)"} for i in range(0, scr)]
        gradient_steps += [{"range": [scr,100], "color": "rgb(0,0,0)"}]
        fig = go.Figure(go.Indicator(
          mode="gauge+number",
          value=score,
          number={"font": {"size": 120, "color": "White", "family": "Arial"}},
          domain={'x': [0, 1], 'y': [0, 1]},
          gauge={
              'axis': {'range': [0, 100], 'tickwidth': 0, 'tickcolor': 'black', 'tickvals': [] },
              'borderwidth': 0,
              'bar': {'color': 'rgba(0, 0, 0, 0)', 'thickness': 0.00001},
              'steps': gradient_steps
          }
      ))
        fig.update_layout(paper_bgcolor="black", plot_bgcolor="black")
        gauge_placeholder.plotly_chart(fig, use_container_width=True)
        time.sleep(0.05)
    with col2:
        feedback = [["Very Poor Match", "Your resume does not align with the job description. Consider tailoring your skills and experiences."],
          ["Poor Match", "There are major gaps between your resume and the job description. Significant improvement is needed."],
          ["Fair Match", "Your resume shows some relevance, but it can be improved with more targeted content."],
          ["Good Match", "Your resume aligns well with the job description. Just a few improvements can make it great!"],
          ["Perfect Match", "Excellent resume! It matches the job description very closely and demonstrates strong alignment."]]
        color = ["#FF4B4B","#FF944B","#FFD54B","#9EFF4B","#4BFF8F"]

        st.markdown(
            f"""
            <div style="height: 400px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background-color: black; border-radius: 16px; padding: 30px; margin-left: 60px;">
                <h1 style="color: {color[score//20]}; font-size: 36px;">{feedback[score//20][0]}</h1>
                <p style="color: white; font-size: 18px;">{feedback[score//20][1]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
      
def display_strength_weakness(strength,weakness):
  col1, col2 = st.columns(2)
  with col1:
    st.markdown(f"""
      <div style='background-color:black; padding: 20px; border-radius: 10px; color: white; margin-top: 20px; height: 400px; display: flex; flex-direction: column; justify-content: flex-start; overflow-y: auto;
      box-shadow: inset 4px 0 10px rgba(57, 255, 20, 0.6),  /* left glow */inset -4px 0 10px rgba(57, 255, 20, 0.6); /* right glow */'>
            <h4 style='color: lightgreen; text-align: center;'>Strengths</h4>
            {bullet_points(strength)}
        </div>
    """, unsafe_allow_html=True)
  with col2:
    st.markdown(f"""
      <div style='background-color:black; padding: 20px; border-radius: 10px; color: white; margin-top: 20px; height: 400px; display: flex; flex-direction: column; justify-content: flex-start; overflow-y: auto;
      box-shadow: inset 4px 0 10px rgba(255, 20, 60, 0.6),  /* left glow */inset -4px 0 10px rgba(255, 20, 60, 0.6); /* right glow */'>
            <h4 style='color: tomato; text-align: center;'>Weaknesses</h4>
            {bullet_points(weakness)}
        </div>
    """, unsafe_allow_html=True)
    
def display_suggestions(suggestions):
  st.markdown(f"""
    <div style='background-color:black; padding: 20px; border-radius: 10px; color: white; margin-top: 20px;
    box-shadow: inset 4px 0 10px rgba(0, 191, 255, 0.6),  /* left glow */inset -4px 0 10px rgba(0, 191, 255, 0.6); /* right glow */'>
        <h4 style='color: deepskyblue; text-align: center;'>Suggestions for Improvement</h4>
        {bullet_points(suggestions)}
    </div>
  """, unsafe_allow_html=True)
