import pandas as pd
import list_to_panda
from list_to_panda import codes_group_by
from daily_orders import sku_qty_processing


#print list of sku and quantities for the csv uploaded that can be easily copied and pasted
# From daily_orders

sku_qty = sku_qty_processing()

sku = 0
print('\nList of Skus: \n')
for sku in range(len(sku_qty)):
    print(sku_qty['Sku'][sku])
    sku+1

print('\nQuantities: \n')
qty = 0
for qty in range(len(sku_qty)):
    print(sku_qty['Quantity'][qty])
    qty+1


# Once processed by the tff-stock-ordering-master, enter the needed products for final process

print("\n\n Enter/Paste the products needed from tff-stock-ordering-master, then Ctrl-Z to get the results.\n")

content = []
tomkin = []
trenton = []

#get input, stop when ctrl Z + enter is done
while True:
    try:
        prod_codes = input()
        content.append(prod_codes)
    except EOFError:
        break

codes_list = codes_group_by(content)


#returning codes_list

#separate the codes between Tomkin and Trenton (and the rest)
k = 0
for k in range(len(codes_list)):
    tk = '.TK'
    if codes_list[k].find(tk) == -1 :
        trenton.append(codes_list[k])
    else:
        tomkin.append(codes_list[k].replace('.TK',' '))
    k+1

# put them in order
# delete empty lines
# Addup codes that are the same
    # 1. trenton
trenton.sort()
trenton = list(filter(None, trenton))

    # 2. tomkin
tomkin.sort()
tomkin = list(filter(None, tomkin))

# print both as a list that I can easily copy and paste
print(" \n\n*** Trenton's code ***")
print("\n\nHi Trenton, \n\nCan we please pick up the following tomorrow at 10: \n ")
j = 0
for j in range(len(trenton)):
    print(trenton[j])
    j+1
print('\n \nThank you! ')

i = 0
print(" \n\n*** Tomkin's code ***")
print("\n\nHi Tomkin, \n\nCan we please order the following for delivery to our warehouse: \n ")
for i in range(len(tomkin)):
    print(tomkin[i])
    i+1
print('\n \nThank you! ')
