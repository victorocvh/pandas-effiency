import glob
import pandas as pd 
import pyarrow as pa 
import pyarrow.parquet as pq 
from memory_profiler import profile 
import psutil
import os 
import dask.dataframe as dd

files = glob.glob('data-files/*.csv')


def check_process_memory():
    processo = psutil.Process(os.getpid())
    uso_memoria = processo.memory_info().rss / 2**20
    print(f'uso {uso_memoria:.2f}MB')

@profile()
def csv_to_parquet(files: iter) -> None: 
    t1 = datetime.now()
    pqwriter = None 
    first_file = True 

    for file in files:
        for i, df in enumerate(pd.read_csv(file, chunksize=1000000)):
            df = df.astype(str)

            if first_file:
                schema = pa.Schema.from_pandas(df)

                pqwriter = pq.ParquetWriter('output.parquet', schema=schema)
                table = pa.Table.from_pandas(df, schema=schema)
                pqwriter.write_table(table)
                first_file = False
            else: 
                table = pa.Table.from_pandas(df, schema=schema)
                pqwriter.write_table(table)
            check_process_memory()
    pqwriter.close()
        
    t2 = datetime.now()
    total = t2 - t1 
    print(f'Tempo de execução: {total}')


csv_to_parquet(files)

df = dd.read_parquet('output.parquet')

print(df['rideable_type'].unique().compute())