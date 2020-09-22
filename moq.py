import pandas as pd
import numpy as np
import math
import re
from pathlib import Path


for i in range (0, sku_qty_size):

    price_list_line = pricelist.loc[pricelist['Item No.'] == sku_qty['Sku'][i]]
    item = pricelist.loc[price_list_line.index]
    qty_needed = int(sku_qty['Quantity'][i])


    # Dealing with the cutlery having to be ordered in dozens only

    if ((price_list_line['Unit']  == 'Doz').all() | (price_list_line['Unit']  == 'DOZ').all()):

        to_order = math.ceil(qty_needed / 12)
        sku_qty.at[i, 'To Order'] = to_order


    else :

    # The product code is on the price list, make the calculations based on MOQ
    # Most of products will follow this

        moq = int(item['MOQ'][item.index[0]])
        to_order = math.ceil(qty_needed / moq) * moq
        sku_qty.at[i, 'To Order'] = to_order


sku_qty
