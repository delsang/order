import pandas as pd

def codes_group_by(content):
    #content = ['EVE10501.TK x 3', 'CC528748 x 1', '53631 x 4', '69890.TK x 2', 'CC528748 x 1']

    df = pd.DataFrame(content, columns = ['code'])

    df = df.join(
        df.code.str.rsplit(n=2 , expand=True).rename(
            columns={0: 'product code', 1: 'times', 2: 'quantities'}
        )
    )

    df = df.drop(['code', 'times'], axis = 1)
    df= df.dropna(axis=0)
    df = df.astype({"quantities": int})


    df = df.groupby(by='product code', as_index = False ).sum()


    codes_list = []
    i=0

    def convertTuple(tup):
        str =  ''.join(tup)
        return str

    for i in df.index:
        code_plus_quantities = df['product code'][i], ' x ' , str(df['quantities'][i])
        code_plus_quantities = convertTuple(code_plus_quantities)
        codes_list.append(code_plus_quantities)
        i+1


    return(codes_list)
