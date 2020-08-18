import pandas as pd

def orders_business_critical():
    orders = pd.read_csv('zapier-order-sheet-daily-orders.csv', dtype=str)
    index_size = len(orders.index)

    #look into the ['Text'] column for the term "business critical", return bolean
    def isbizcrit(text):
        status = "Business Critical"
        if status in text:
            return True
        else:
            return False

    # create status dataframe
    status_order = pd.DataFrame(columns=['Order Number', 'bizcrit'])

    # looping to get the simplified order number (last 5 digits) and status in status_order
    i=0

    for i in range(0, index_size):
        text = orders['Text'][i]
        order_number = orders['order #'][i].split('20000',1)[1]
        iscrit = isbizcrit(text)
        status_order = status_order.append({'Order Number':order_number, 'bizcrit':iscrit}, ignore_index=True)

        i+1

    # return the biz crits order numbers as a list
    j=0
    biz_crit_orders = []

    for j in range(0, index_size):
        if status_order['bizcrit'][j] == True:
            biz_crit_orders.insert(j, status_order['Order Number'][j])
            j+1

    return(biz_crit_orders)
