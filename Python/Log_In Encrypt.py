#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import base64
import pandas as pd
#1. connect the user excel file
Data = pd.read_excel('Log_In_File.xlsx')

#2. Checking the data
ID = Data.iloc[0]['Before'].encode('utf-8')

if ID == '':
    pass

else:

    #3. pick up ID from cell B2 and encrypt the ID to C2
    Data.loc[Data.index==0,'After'] = base64.b64encode(ID).decode('utf-8')

    #4. pick up Password from cell B3 and encrypt the Password to C3
    Password = Data.iloc[1]['Before'].encode('utf-8')
    Data.loc[Data.index==1,'After'] = base64.b64encode(Password).decode('utf-8')

    #5. clear the ID at B2 and Password at B3
    Data.loc[Data.index == 0,'Before'] = ''
    Data.loc[Data.index == 1,'Before'] = ''

    #6. save the file
    Data.to_excel("Log_In_File.xlsx",index=False)

# In[ ]:




