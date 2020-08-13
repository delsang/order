import pandas as pd
import re

def sku_qty_processing() :
    #upload and read file, get index size
    orders = pd.read_csv('zapier-order-sheet-daily-orders.csv', dtype=str)
    index_size = len(orders.index)

    #create new order file
    sku_qty = pd.DataFrame(columns=['Sku', 'Quantity'])

    # find the sku numbers and quantities
    i = 0
    j=0

    for i in range(0, index_size):
        text = orders['Text'][i]
        sku = re.findall('<p class="sku" style="margin-top: 0; margin-bottom: 0;">SKU: (.*)</p>', text)
        quantity = re.findall('<td class="item-qty" style="font-family: \'Open Sans\',\'Helvetica Neue\',Helvetica,Arial,sans-serif; vertical-align: top; text-align: center;">(.*)</td>', text)

        #add the skus and quantities to the sku_qty dataframe
        for j in range(0, len(sku)):
            sku_qty = sku_qty.append({'Sku':sku[j], 'Quantity':quantity[j]}, ignore_index=True)
            j+1

        i+1

    return sku_qty
