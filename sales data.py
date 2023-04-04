#!/usr/bin/env python
# coding: utf-8

# In[1]:


stock = 999
product_sold = 888
target = 888

target_hit = product_sold == target
print("Did the product reach its sales target?")
print("Sales target reached")

current_stock = stock - product_sold
in_stock = current_stock != 0
print("Product in stock: ")
print("Product available")

