import streamlit as st
import pandas as pd
from layout import (
    page_layout
)
from text_processor import (
    list_documents,
    load_text_file,
    process_text,
    process_words,
    row_reset_required
)

st.title("🎈 On The Square - Ritual Learning - 1st Degree")

page = page_layout(ritual_list=list_documents("ea/"))
doc_name = page.controls["document list"]
st.header(f"{st.session_state.role} - {doc_name}.")
doc_text = load_text_file(f"ea/{doc_name}.txt")
page.get_page_block_layout(source_txt=doc_text)




