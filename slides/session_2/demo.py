txt = """year;country;measure
2018;"france";950.0
2019;"france";960.0
2020;"france";1000.0
2018;"usa";2500.0
2019;"usa";2150.0
2020;"usa";2300.0
"""



open('annoying_dummy_file.csv','w').write(txt)


import pandas as pd

df = pd.read_csv("annoying_dummy_file.csv", sep=';'    
)

df.to_csv("export.csv")



# import dbnomics

import dbnomics
df = dbnomics.fetch_series('AMECO/ZUTN/EA19.1.0.0.0.ZUTN')


