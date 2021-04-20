#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import base64
import pandas as pd
#1. connect the user excel file
Data = pd.read_excel('Log_In_File.xlsx')

#2. Checking the data
ID = Data.iloc[0]['After'].encode('utf-8')

if ID == '':
    pass

else:
    
    #3. pick up ID from cell C2 and decrypt the ID to B2
    ID = Data.iloc[0]['After'].encode('utf-8')
    Data.loc[Data.index==0,'Before'] = base64.b64decode(ID).decode('utf-8')

    #4. pick up Password from cell C3 and encrypt the Password to B3
    Password = Data.iloc[1]['After'].encode('utf-8')
    Data.loc[Data.index==1,'Before'] = base64.b64decode(Password).decode('utf-8')

    #5. clear the ID at C2 and Password at B3
    Data.loc[Data.index == 0,'After'] = ''
    Data.loc[Data.index == 1,'After'] = ''

    #6. save the file
    Data.to_excel("Log_In_File.xlsx",index=False)


# In[ ]:




