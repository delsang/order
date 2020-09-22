import pandas as pd

# This function returns a list of the order to place

def order_to_pd():
    content = []
    while True:
        try:
            prod_codes = input()
            content.append(prod_codes)
        except EOFError:
            break

    df = pd.DataFrame(content, columns = ['ordering'])
    df = df.join(
            df.ordering.str.rsplit(n=2 , expand=True).rename(
                columns={0: 'Sku', 1: 'times', 2: 'Quantity'}
            )
        )
    df = df.drop(['ordering', 'times'], axis = 1)
    df= df.dropna(axis=0)
    df = df.astype({"Quantity": int})
    df = df.groupby(by='Sku', as_index = False ).sum()

    return df
