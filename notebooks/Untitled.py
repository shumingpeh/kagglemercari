
# coding: utf-8


import pandas as pd
import numpy as np



raw_data = (
    pd.read_csv('../data/train.tsv', sep='\t')
)



raw_data.head()


# # TODO:
# 
# ## Justin
# - clean category_name into 3 (n) sub cats
# - item condition id = https://www.mercari.com/help_center/article/316/
# - exclude price with 0 or error
# - find brand name from description or item description
# - those without brand name will be clustered together with brand name
# - assume categorization is correct for first iteration
# - find age of product from item name or description if possible
# 
# 
# 
# ## Shuming
# - age of product from item description if possible
# - text sentiment analysis from item description --> this correlates with item condition








































