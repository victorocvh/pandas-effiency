import glob
import pandas as pd 
from datetime import datetime
from memory_profiler import profile 
# """
# For 1GB of files to be concated with simple pd.concat it uses around 7GB of ram memory.  
# """

files = glob.glob('data-files/*.csv')

def generate_iterator(files: iter) -> iter:
    for file in files: 
        df = pd.read_csv(file, skiprows=[0])
        yield df 

dfs = generate_iterator(files)

@profile()
def concat_dataframes(dfs: iter):
    df_list = [df for df in dfs]
    t1 = datetime.now()
    main_df = pd.concat(df_list, axis=0, sort=False)
    t2 = datetime.now()
    total = t2-t1 
    print(f'Tempo de execução: {total}' )
    return main_df 

main_df = concat_dataframes(dfs)
print('conseguiu!')
