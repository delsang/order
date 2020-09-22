import pandas as pd
import math
from list_to_panda import order_to_pd
from paths import supliers_pricelist


def moq_process():
    df = order_to_pd()
    pricelist = supliers_pricelist()

    for i in range (0, len(df.index)):
        #try:
        price_list_line = pricelist.loc[pricelist['Item No.'] == df['Sku'][i]]
        item = pricelist.loc[price_list_line.index]
        #index_item = item.index[0]
        qty_needed = int(df['Quantity'][i])

        #except:
            # The product code isn't on the price list, order the quantity originally ordered
         #   sku_qty.at[i, 'To Order'] = qty_needed

        #continue

        # Dealing with the cutlery having to be ordered in dozens only

        if ((price_list_line['Unit']  == 'Doz').all() | (price_list_line['Unit']  == 'DOZ').all()):

            to_order = math.ceil(qty_needed / 12)
            df.at[i, 'To Order'] = to_order


        else :

        # The product code is on the price list, make the calculations based on MOQ
        # Most of products will follow this

            moq = int(item['MOQ'][item.index[0]])
            to_order = math.ceil(qty_needed / moq) * moq
            df.at[i, 'To Order'] = to_order


    return df
