import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Hello, This is team NOA (Najeeb & Omr). It's nice to meet you!",
    page_icon="👋",
)

st.write("# Welcome to our portfolios")

col1, col2 = st.columns([1, 1])

with col1:
    st.image('https://avatars.githubusercontent.com/u/44613678?v=4')
with col2:
    st.image('https://media.licdn.com/dms/image/D4E03AQGRSiRBWejC3w/profile-displayphoto-shrink_800_800/0/1692311569649?e=1701907200&v=beta&t=GKG81ijHzFa9BSPDszOoUpQEY0OmPHogny_w1_N5oZg')

important_links = '''

[Company Github](https://github.com/NOA2023) _as a main contributors_.,


Github:
[omr50](https://github.com/omr50),
[naa7](https://github.com/naa7)

Linkedin:
[naa7](https://www.linkedin.com/in/naa7/),
[omr50](https://www.linkedin.com/in/omr-abdelhamed/)
'''

st.markdown(important_links)
