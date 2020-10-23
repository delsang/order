import pandas as pd
import re
from pathlib import Path
from paths import daily_ordercsv
# This function reads the csv file and extracts the sku numbers and quantities needed
# it returns a data frame with 2 columns : sku# and quantity.


def sku_qty_processing() :
#upload and read file for the downloads folder, get index size
    daily_orders = daily_ordercsv()
    index_size = len(daily_orders.index)
    df = pd.DataFrame(columns=['order#', 'Text'])

# Modify the data frame to get rid of the useless text in the "order#"" column
    i=0
    for i in range(0, index_size):
        order_number = daily_orders['order #'][i].split('20000',1)[1]

        df = df.append({'order#':order_number, 'Text': daily_orders['Text'][i]}, ignore_index=True)

        i+1

# - Column A is the order number (same on all rows)
# - Column B sku number
# - Column C quantities of sku needed

    sku_qty = pd.DataFrame(columns=['Order#', 'Sku', 'Quantity'])

    k=0
    for k in range(0, index_size):
        text = df['Text'][k]
        order_number = df['order#'][k]
        sku = re.findall('<p class="sku" style="margin-top: 0; margin-bottom: 0;">SKU: (.*)</p>', text)
        quantity = re.findall('<td class="item-qty" style="font-family: \'Open Sans\',\'Helvetica Neue\',Helvetica,Arial,sans-serif; vertical-align: top; text-align: center;">(.*)</td>', text)
        k+1

        for i in range(0,len(sku)):
            sku_qty = sku_qty.append({'Sku':sku[i], 'Quantity':quantity[i], 'Order#':order_number}, ignore_index=True)



    return sku_qty
