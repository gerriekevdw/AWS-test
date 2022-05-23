from concurrent.futures import process
import gc
import sys
import numpy as np
import pandas as pd
from multiprocessing import Pipe
from multiprocessing import Process
from multiprocessing.connection import _ConnectionBase

def values_to_df(value, batch_nr, value_nr, connection:_ConnectionBase):
    print(f'This is batch nr {batch_nr} - value nr {value_nr}:  {value}')
    
    try:
        df = pd.DataFrame({'batch': batch_nr, 'value': value, 'value_nr': value_nr}, index=[0])
        connection.send(df)
        connection.close()
        return
    except:
        err = sys.exc_info()[0]
        print(f"Exception {batch_nr}: {value_nr} - {err}")
        connection.send(None)
        connection.close()
        return 
        
def process_batch(batch, batch_nr):
    results = []
    processes = []
    connections = []

    value_nr = 0
    for value in batch:
        parent_conn, child_conn = Pipe()
        connections.append(parent_conn)

        process = Process(target=values_to_df, args=(value, batch_nr, value_nr, child_conn))
        processes.append(process)

    for process in processes:
        process.start()

    for conn in connections:
        try:
            df = conn.recv()
            if df is not None:
                results.append(df)

            conn.close()

        except EOFError:
            conn.close()
            pass

    for process in processes:
        process.join()

    return results


def lambda_handler(event, context):
    # Get number of parallel processes to run, default 25
    batch_size = event.get('batch', 25)
    nr_total = event.get('total', 150)
    
    values = np.random.rand(nr_total)
    
    results = []
    batch_nr = 0
    for i in range(0, len(values), batch_size):
        values_batch = values[i: i + batch_size]
        sub_results = process_batch(values_batch, batch_nr)
        results = results + sub_results
        gc.collect()
        batch_nr += 1
    

        if len(results)>0:
            final_result = pd.concat(results, ignore_index=True)
            print(f"Shape final result: {final_result.shape}")
            print(final_result.groupby('batch')['value_nr'].agg(['size', 'min', 'max']).to_string())
        
        else:
            final_result = None
            print("No final result")

    return True

