import pandas as pd
from moq import moq_process

def get_order_toplace():

    df = moq_process()
    codes_list = []
    i=0

    def convertTuple(tup):
        str =  ''.join(tup)
        return str

    for i in df.index:
        code_plus_quantities = df['Sku'][i], ' x ' , str(int(df['To Order'][i]))
        code_plus_quantities = convertTuple(code_plus_quantities)
        codes_list.append(code_plus_quantities)
        i+1

    return codes_list
