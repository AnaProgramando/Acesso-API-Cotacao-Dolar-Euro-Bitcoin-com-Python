#!/usr/bin/env python
# coding: utf-8

# In[33]:

import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']["bid"]
cotacao_euro = cotacoes['EURBRL']["bid"]
cotacao_bitcoin = cotacoes['BTCBRL']["bid"]

print("\n Cotação do Dólar Americano/Real Brasileiro: ", cotacao_dolar)
print("\n Cotação do Euro/Real Brasileiro: ", cotacao_euro)
print("\n Cotação do Bitcoin/Real Brasileiro: ", cotacao_bitcoin)
print("\n Cotações sem formatação: \n",cotacoes)
