df = pd.DataFrame({'A':{0:'a', 1:'b', 2:'c'},
                   'B':{0: 1, 1:3, 2: 5},
                   'C':{0:1, 1: 4, 2: 6}
                   })

pd.melt(df, id_vars =['A'], value_vars=['B'])


pd.melt(df, id_vars =['A'], value_vars=['B','C'], var_name='variavel_nome', value_name='valor_nome')
