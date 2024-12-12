"""
Created on Mon Nov  4 10:16:28 2024

@author: gelliott
"""
from pathlib import Path, PurePath
from os import listdir, chdir
from os.path import isfile, join
import re
import pandas as pd
import csv

def list_documents(doc_path):
    included_extensions = ["txt"]
    # file_names = [fn for fn in listdir(doc_path)
    #             if isfile(join(doc_path, fn)) and any(fn.endswith(ext) for ext in included_extensions)]
    file_names = {fn.replace(".txt",""):fn for fn in listdir(doc_path)
                if isfile(join(doc_path, fn)) and any(fn.endswith(ext) for ext in included_extensions)}
    return file_names

def load_text_file(fname: str):
    source_txt = []
    with open(fname,"r") as f:
        for line in f:
            source_txt.append(line.strip("\n"))
    f.close()
    source_txt="\n".join(source_txt)
    return source_txt

def process_words(word,seperator,char_len=1):
    coded_words = {
        "FOR":"4",
        "TO":"2",
        "TOO":"2",
        "AND":"&",
    }
    if len(word) == 0: word = " "
    if word.upper() in coded_words.keys():
        word = coded_words[word.upper()]
        output_text = f"{word}{seperator}"
        
    elif re.match("[A-Z.]+[.,|;]", word) is not None:
        output_text = f"{word}{seperator}"
    elif re.match(".+([.,;]|'s)$",word) is not None:
        output_text = f"{word[0:char_len]}{word[-1]}{seperator}"
    else:
        output_text = f"{word[0:char_len]}{seperator}"
    return output_text

def row_reset_required(row_count, row_len, col_num, text_cols):
    if row_count >= row_len:
        col_num += 1
        text_cols[f"Read {col_num}"] = []
        row_count = 1
    else:
        row_count +=1
    
    return row_count, col_num, text_cols

def process_text(source_txt,char_len=1):
    if isinstance(source_txt, str):
        source_txt = source_txt.split("\n")
    output_text = ""
    #seperator = " "
    
    col_len = 3
    row_len = 20
    col_num = 1
    text_cols = {"Read 1":[]}
    row_count = 1
    #text_row = []
    excel_sheets = []
    cell_count = 0
    pattern = re.compile("([a-z]\.[A-Z])")
    for idx,line in enumerate(source_txt):
        if len(line) == 0:
            continue
        char_count = 1
        matches = pattern.search(line)
        if matches:
            for m in matches.groups():
                m1 = m.split(".")
                m1 = ". ".join(m1)
                line = line.replace(m,m1)
        else:
            pass
        
        for word in line.split(" "):
            
            #char_count += 1
            if char_count == col_len:
                #*****for testing*****
                cell_count += 1
                if idx >= 12:
                    pass
                #*********************
                char_count = 1
                output_text += process_words(word, "",char_len)
                text_cols[f"Read {col_num}"].append(output_text) 
                #text_row.append(output_text)
                output_text = ""
                #Row length
                #*****for testing*****
                if row_count >= 19:
                    pass
                #*********************
                row_count, col_num, text_cols = row_reset_required(row_count, row_len, col_num, text_cols)           
            else:
                char_count += 1
                output_text += process_words(word, "  ",char_len)
        
        #Capture the final row which may be shorter
        if len(output_text) > 0:
            text_cols[f"Read {col_num}"].append(output_text)
            output_text = ""
        else:
            pass
        #Pad the list if it is less than the row length required.
        pad_list = ["" for x in range(row_len - len(text_cols[f"Read {col_num}"]))]
        text_cols[f"Read {col_num}"].extend(pad_list)
        #Reset the row to start a new column as we have reached a paragraph or line end.
        #Only if there are still more lines to process.
        if (idx + 1) < len(source_txt):
            row_count, col_num, text_cols = row_reset_required(row_len, row_len, col_num, text_cols)
        # col_num += 1
        # row_count = 1

    page_df = pd.DataFrame(text_cols)
    page_df.to_csv("output.csv", index=False, quoting=csv.QUOTE_ALL)
    return page_df #text_cols

