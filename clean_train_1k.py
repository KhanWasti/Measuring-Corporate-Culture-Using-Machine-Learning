# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:38:55 2023

@author: Joao Ji Won Lee
"""

#from clean_and_train import clean_file

import pandas as pd
import numpy as np

feather_data_path = r'/Users/Joao Ji Won Lee/Desktop/10K_NLP-main/10k_item1_text.feather'

filing_data = pd.read_feather(feather_data_path)



item1_df = filing_data[filing_data['item1_text'] != 'undefined']
item1_df=item1_df[item1_df['item1_text']!='None']
item1_df = item1_df[item1_df['sec_company_name']=='NORDSTROM INC']
l1 = item1_df['item1_text'].values.tolist()
print (''.join(l1))
f = open("Item_1_text_Nordstrom.txt", "w")

f.write(''.join(l1))

f.close()

