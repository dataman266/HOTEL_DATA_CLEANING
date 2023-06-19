#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np


# In[10]:


file_path = "D:\\Project\\Hotel_Demand\\hotel_bookings.csv"


# In[22]:


missing_value = ["undefined"]
hotel_data = pd.read_csv(file_path)
hotel_data


# In[18]:


hotel_data.columns


# In[24]:


hotel_data.shape


# In[26]:


hotel_data.info()


# In[27]:


hotel_data['reservation_status_date'] = pd.to_datetime(hotel_data['reservation_status_date'])


# In[32]:


type(hotel_data['reservation_status_date'][0])


# In[34]:


hotel_data['arrival_date'] = pd.to_datetime(hotel_data.arrival_date_year.astype(str) + '/' + hotel_data.arrival_date_month.astype(str) + '/' + hotel_data.arrival_date_day_of_month.astype(str))
hotel_data


# In[39]:


type(hotel_data['arrival_date'][0])


# In[40]:


hotel_data.drop(['arrival_date_day_of_month', 'arrival_date_month', 'arrival_date_year'], axis = 1, inplace = True)
hotel_data


# In[42]:


hotel_data.info()


# In[43]:


np.sum(hotel_data.isnull())


# In[45]:


hotel_data.children[hotel_data.children !=hotel_data.children].index.values


# In[55]:


missing_values = hotel_data.isnull().sum()
missing_values


# In[56]:


total_cells = np.product(hotel_data.shape)
total_missing = missing_values.sum()
(total_missing/total_cells)*100


# In[59]:


for col in hotel_data.columns:
    if np.sum(hotel_data[col].isnull()) > (hotel_data.shape[0] * 0.7):
        hotel_data.drop(columns = col, inplace = True, axis = 1)
print(hotel_data.shape)


# In[61]:


hotel_data.shape[0]*0.7


# In[67]:


hotel_data.drop(['arrival_date_week_number'], axis = 1, inplace = True)
hotel_data


# In[69]:


hotel_data.dropna(subset=['agent'], inplace=True)
hotel_data


# In[71]:


mean_children = hotel_data['children'].mean()
mean_children


# In[72]:


hotel_data['children'].fillna(mean_children, inplace = True)


# In[76]:


hotel_data['children'].isnull().sum()


# In[79]:


hotel_data['children'] = hotel_data['children'].apply(np.floor)


# In[80]:


hotel_data['children'].isnull().sum()


# In[84]:


np.sum(hotel_data.isnull())


# In[97]:


hotel_data['country'].fillna(method = 'bfill', axis = 0, inplace = True)


# In[98]:


hotel_data.isnull().sum()


# In[100]:


new_file_path = "D:\\Project\\Hotel_Demand\\cleaned_hotel_bookings.csv"

# Saved cleaned dataset to a new file
hotel_data.to_csv(new_file_path, index=False, header=True)


# In[ ]:





# In[ ]:





# In[ ]:




