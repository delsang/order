import pandas as pd

def orders_business_critical():
    orders = pd.read_csv('zapier-order-sheet-daily-orders.csv', dtype=str)
    index_size = len(orders.index)

    #look into the ['Text'] column for the term "business critical". If it is found, print the order number
    def isbizcrit(text):
        status = "Business Critical"
        if status in text:
            return True
        else:
            return False

    # create status dataframe
    status_order = pd.DataFrame(columns=['Order Number', 'bizcrit'])

    # looping to get the simplified order number and status
    i=0

    for i in range(0, index_size):
        text = orders['Text'][i]
        order_number = orders['order #'][i].split('20000',1)[1]
        iscrit = isbizcrit(text)

        status_order = status_order.append({'Order Number':order_number, 'bizcrit':iscrit}, ignore_index=True)

        i+1

    # print the biz crits
    j=0

    for j in range(0, index_size):
        if status_order['bizcrit'][j] == True:
            print('Order', status_order['Order Number'][j], 'is a business critical')
        j+1
