# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:27:02 2024

@author: gelliott
"""
import streamlit as st
import streamlit_scrollable_textbox as stx
import pandas as pd
from text_processor import (
    list_documents,
    load_text_file,
    process_text,
    process_words,
    row_reset_required
)

class page_layout():
    

    def __init__(self,process_function=None, ritual_list={}, source_txt=None):
        self.__process_function__ = process_function
        self.__source__ = source_txt
        self.__ritual_list__ = ritual_list
        self.__data_frame__ = None
        self.__text__ = None
        self.controls = {}
        with st.sidebar:
            self.controls["document list"] = st.selectbox(
                label="Select ritual",
                options = self.__ritual_list__
            )
            self.controls["col width input"] = st.selectbox(
                label="Select number of output columns per page",
                options = [x for x in range(11,5,-1)]
            )
            self.controls["grid layout"] = st.radio(
                    label="Select preffered grid layout",
                    options = ["Across, Down","Down, Across"]
            )
            self.controls["word length"] = st.radio(
                    label="Select number of characters per word",
                    options=["1","2","All","Remove vowels"]
            
            )
            #self.__data_frame__, self.__text__ = self.__get_processed_text__()
    
    def __get_processed_text__(self):
        char_len = 1
        match self.controls["word length"]:
            case "All":
                char_len = 1000
            case "Remove vowels":
                char_len = 1000
            case _:
                char_len = int(self.controls["word length"])
        
        return process_text(self.source_txt,char_len)
    
    @st.fragment()
    def get_text(self):
        if self.__data_frame__ is None or self.__text__ is None:
            self.__data_frame__, self.__text__ = self.__get_processed_text__()
        else:
            pass
        text_box = stx.scrollableTextbox(
            key="destination",
            text=self.__text__,
            height=400
        ) 
        return text_box

    @st.fragment()
    def get_dataframes(self):
        df_pages = []
        start_col = 0
        col_width = self.controls["col width input"]
        #Process source text
        output_df = pd.DataFrame()
        if self.__data_frame__ is None or self.__text__ is None:
            self.__data_frame__, self.__text__ = self.__get_processed_text__()
        else:
            pass
        output_df = self.__data_frame__

        for col in range(col_width,output_df.shape[1] + 1,col_width):
            df_pages.append(output_df.iloc[:,start_col:col:1])
            start_col += col_width
        #Capture any remaining columns that are missed due to the step size
        if output_df.shape[1] % col_width > 0:
            df_pages.append(output_df.iloc[:,start_col:])
        else:
            pass
        
        tabs = [f"Page {x+1}" for x in range(0,len(df_pages))]
        tabs = st.tabs(tabs)
        for idx,tab in enumerate(tabs):
            with tab:
                st.dataframe(df_pages[idx])

        return tabs

    def get_page_block_layout(self, source_txt=None, destination_txt=""):
        
        if source_txt is not None:
            self.source_txt = source_txt
        elif source_txt is None and self.source_txt is not None:
            self.source_txt = ""
        else:
            pass
        source, destination = st.columns([1,1])

        #with source:
        self.controls["source txt"] = stx.scrollableTextbox(
            key="source",
            text=source_txt,
            height=200
        )
        # self.controls["Destination txt"] = stx.scrollableTextbox(
        #     key="destination",
        #     text=self.get_text(),
        #     height=200
        # ) 
        #with destination:
        self.get_text()
        self.get_dataframes()

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    