#!/usr/bin/env python
# coding: utf-8

# In[9]:


#importing packages as per requirements. 
import pandas as pd
import string

def web_traffic_transfer(root_url):   #function to parameterize the root_url 
        
    alphabet_list = list(string.ascii_lowercase) #return a list of all lowercase letters to handle the files for the challenge. 
    combined_df = pd.DataFrame() #create an empty DataFrame object to store all the files.
    
    for i in alphabet_list:
        url = root_url + i + ".csv"
        df = pd.read_csv(url)
        combined_df = pd.concat([df, combined_df], ignore_index=True)
        #ignore_index = True will ignore existing index and will generate a new index for the output file.

    pivot_output_df = pd.pivot_table(combined_df, values = 'length', 
                               index=['user_id'], columns = 'path').reset_index().fillna(0) #fillna used to replace missing data with 0
    return pivot_output_df



root_url = "https://public.wiwdata.com/engineering-challenge/data/" #url can be changed as per requirements.
output_file = web_traffic_transfer(root_url)

output_file.to_csv('wiw_final_traffic.csv',index=False) #output files saved as 'wiw_final_traffic.csv' on your local desktop.


# In[ ]:




