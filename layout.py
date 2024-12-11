# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:27:02 2024

@author: gelliott
"""
import streamlit as st
import pandas as pd

class page_layout():
    

    def __init__(self,process_function, source_txt=""):
        self.__process_function__ = process_function
        self.__source__ = source_txt
        
    def get_page_block_layout(self):
        #brand_img = str(PurePath(__file__).with_name("S&A.png"))

        source, destination = st.columns(2)
        with source:
            source_txt = st.text_area(value=self.__source__)
        
        with destination:
            col_width_input = st.select_box(
                options = [x for x in range(11,5,-1)]
            )
        
        # with gr.Blocks(theme=gr.themes.Default(), fill_height=True, fill_width=True) as layout:
        #     submit_btn = None
        #     with gr.Row():
        #             #gr.Markdown("# S&A RAG AI Demo")
        #             gr.HTML("""
        #             <h1 align='center'>Ritual Learning</h1>
        #             <p align='left'></p>
        #             """)
        #     with gr.Row() as row:
        #         with gr.Column(scale=1) as col1:
        #             input_txt = gr.Textbox(
        #                 value=self.__source__,
        #                 lines=30,
        #                 placeholder="Source Text",
        #                 container=False,
        #                 submit_btn="Submit"
        #             )
                    
        #         with gr.Column(scale=1) as col2:
        #             col_width_input = gr.Dropdown(
        #                 label="Column Width:",
        #                 choices=[x for x in range(11,5,-1)],
        #                 multiselect=False
        #             )
        #             # with gr.Tab() as output_tab:
        #             #     output_dataframe = gr.DataFrame(value=pd.DataFrame())
        #                 # output_txt = gr.Textbox(
        #                 #     lines=30,
        #                 #     placeholder="Learning Text",
        #                 #     container=False
        #                 # )
        #         #input_txt.submit(self.generate_dataframes,[input_txt,output_tab],output_tab)
        #         #submit_btn = gr.Button()
        #         #output_txt.submit(process_function,[input_txt],[output_dataframe])
                    
            
    
        #             @gr.render(inputs=[input_txt,col_width_input],triggers=[input_txt.submit])
        #             def generate_dataframes(input_txt,col_width):
        #                 output_df = self.__process_function__(input_txt)
        #                 df_pages = []
        #                 start_col = 0
        #                 for col in range(col_width,output_df.shape[1] + 1,9):
        #                     df_pages.append(output_df.iloc[:,start_col:col:1])
        #                     start_col += col_width
        #                 #Capture any remaining columns that are missed due to the step size
        #                 if output_df.shape[1] % col_width > 0:
        #                     df_pages.append(output_df.iloc[:,start_col:])
        #                 else:
        #                     pass
        #                 # gr.Textbox(label="Array Length",value=len(df_pages))
        #                 for idx,df in enumerate(df_pages):
        #                     with gr.Tab(label=f"Page {idx+1}"):
        #                         gr.DataFrame(df)
                                
        #                     #return df_pages[0]
    
        #     layout.queue()
        #     return layout
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    