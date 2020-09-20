import pandas as pd
import re
from pathlib import Path

# This function reads the csv file and extracts the sku numbers and quantities needed
# it returns a data frame with 2 columns : sku# and quantity.



def sku_qty_processing() :
    #upload and read file for the downloads folder, get index size
    dir_to_downloads = '/Users/Delphine/downloads'
    p_downloads = Path(dir_to_downloads)
    orders = pd.read_csv(p_downloads/'zapier-order-sheet - daily-orders.csv')
    
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
