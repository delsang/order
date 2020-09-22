import pandas as pd
from pathlib import Path


# path to price list
def supliers_pricelist():
    dir_to_pricelist = '/Users/Delphine/Desktop/work/Price Lists'
    p_pricelist = Path(dir_to_pricelist)

    pricelist = pd.read_csv(p_pricelist/'All Suppliers Price List.csv')
    pricelist = pricelist.drop(['Unnamed: 0'], axis=1)
    pricelist.astype({'Item No.':'str'}).dtypes
    return pricelist

# path to the daily orders .csv file
def daily_ordercsv():
    dir_to_downloads = '/Users/Delphine/downloads'
    p_downloads = Path(dir_to_downloads)
    orders = pd.read_csv(p_downloads/'zapier-order-sheet - daily-orders.csv')
    return orders
