import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Hello, This is team NOA (Najeeb & Omr). It's nice to meet you!",
    page_icon="👋",
)

st.write("# Welcome to DSNOA portfolio")

st.image("https://avatars.githubusercontent.com/u/146592612?s=200&v=4")

important_links = """

[Company Github](https://github.com/NOA2023) _as a main contributors_.,


Github:
[omr50](https://github.com/omr50),
[naa7](https://github.com/naa7)

Linkedin:
[naa7](https://www.linkedin.com/in/naa7/),
[omr50](https://www.linkedin.com/in/omr-abdelhamed/)
"""

st.markdown(important_links)
