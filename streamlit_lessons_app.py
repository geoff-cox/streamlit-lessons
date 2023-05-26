import glob
import os
import re

import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

md_files = sorted(
    [int(x.strip("Lesson-").strip(".md")) for x in glob.glob1(f"lessons", "*.md")]
)

# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("streamlit-logo-secondary-colormark-darktext.png"))

st.markdown("# Streamlit Practice Lessons")

finished_lessons = (1, 2, 3, 4)

# Markdown files for the summaries and lessons
# summary_list = [f"Summary {x}" for x in md_files]
summary_list = [f"Summary {md_files[n-1]}" for n in finished_lessons]
# lesson_list = [f"Lesson {x}" for x in md_files]
lesson_list = [f"Lesson {md_files[n-1]}" for n in finished_lessons]

# Sidebar
sel_lesson = st.sidebar.selectbox(
    "Choose a Lesson", lesson_list, key="lesson"
)

# Get Lesson number
sel_lesson_num = int(sel_lesson.split()[-1])

# Display selected content
st.sidebar.header("Lesson Summary")
with open(f"summaries/{summary_list[sel_lesson_num - 1]}.md", "r") as f:
    st.sidebar.markdown(f.read())

st.markdown(f"# {sel_lesson}")
with open(f"lessons/{sel_lesson}.md", "r") as f:
    st.markdown(f.read())
if os.path.isfile(f"lessons/figures/{sel_lesson}.csv"):
    st.markdown("---")
    st.markdown("### Figures")
    df = pd.read_csv(f"lessons/figures/{sel_lesson}.csv", engine="python")
    for i in range(len(df)):
        st.image(f"lessons/images/{df.img[i]}")
        st.info(f"{df.figure[i]}: {df.caption[i]}")
