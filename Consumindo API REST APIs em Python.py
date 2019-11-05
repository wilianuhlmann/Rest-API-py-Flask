#!/usr/bin/env python
# coding: utf-8

# In[41]:


import json
import requests


# # Get /Hoteis

# In[42]:


URL = 'http://127.0.0.1:5000'


# In[43]:


resposta_hoteis = requests.request('GET', URL + '/hoteis') # Pode ser passado parametros tbm de consulta


# In[44]:


resposta_hoteis.status_code


# In[45]:


hoteis = resposta_hoteis.json()


# In[46]:


hoteis['hoteis']


# In[47]:


hoteis['hoteis'][0]


# In[48]:


len(hoteis['hoteis'])


# In[49]:


lista_hoteis = hoteis['hoteis']


# In[50]:


for hotel in lista_hoteis:
    print(hotel['nome'])


# # Mercado Livre

# In[51]:


ML_URL = 'https://api.mercadolibre.com/sites'


# In[52]:


ML_URL = 'https://api.mercadolibre.com/sites/MLB/categories'


# In[53]:


ML_URL = 'https://api.mercadolibre.com/categories/MLB1403' # Informações sobre categoria


# In[54]:


lista_sites = requests.request('GET', ML_URL)


# In[55]:


lista_sites


# In[56]:


lista_sites.json()


# In[57]:


endpoint_cadastro = URL + '/cadastro'


# In[58]:


endpoint_cadastro


# In[59]:


body_cadastro = {
    'login': 'wilian',
    'senha': 'wilian'
}


# In[60]:


headers_cadastro = {
    'Content-Type': 'application/json'
}


# In[61]:


resposta_cadastro = requests.request('POST', endpoint_cadastro, json=body_cadastro, headers=headers_cadastro)


# In[62]:


resposta_cadastro


# In[63]:


resposta_cadastro.json()


# # Login

# In[94]:


endpoint_login = URL + '/login'


# In[95]:


body_login = {
    'login': 'admin',
    'senha': 'admin'
}


# In[96]:


headers_login = {
    'Content-Type': 'application/json'
}


# In[97]:


resposta_login = requests.request('POST', endpoint_login, json=body_cadastro, headers=headers_login)


# In[98]:


resposta_login


# In[99]:


token = resposta_login.json()


# In[100]:


token['access_token']


# # CRUD /hoteis/{hotel_id}

# In[101]:


endpoint_hotel_id = URL + '/hoteis/meuhotel2'


# In[102]:


endpoint_hotel_id


# In[103]:


body_hotel_id = {
    'nome': 'Meu Hotel',
    'estrelas': 4.8,
    'diaria': 398.20,
    'cidade': 'Santos'
}


# In[104]:


headers_hotel_id = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer' + token['access_token']
}


# In[105]:


resposta_hotel_id = requests.request('PUT', endpoint_hotel_id, json=body_hotel_id, headers=headers_hotel_id)


# In[76]:


resposta_hotel_id


# In[77]:


resposta_hotel_id.json


# # /usuarios/{user_id}

# In[106]:


endpoint_user_id = URL + '/usuarios/1'


# In[107]:


endpoint_user_id


# In[108]:


headers_user_id = {
    'Content-Type': 'application/json',
    'Authorization': 'Beares' + token['access_token']
}


# In[109]:


resposta_user_id = requests.request('GET', endpoint_user_id)


# In[110]:


resposta_user_id = requests.request('DELETE', endpoint_user_id, headers=headers_user_id)


# In[111]:


resposta_user_id.status_code


# In[112]:


resposta_user_id.json()


# In[ ]:





# In[ ]:





# In[ ]:




