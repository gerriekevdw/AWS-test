from multiprocessing import Pipe
from multiprocessing import Process
from multiprocessing.connection import _ConnectionBase

def lambda_handler(event, context):

        # results: List[pd.DataFrame] = []
        # paths: List[str] = []
        # prefix_objs = self.s3_resource.objects.filter(Prefix=prefix)

        # for obj in prefix_objs:
        #     paths.append(obj.key)

        # if len(prefix_objs) == 0:
        #     print(f"No objects found for {prefix}")

        # # Split in batches
        # for i in range(0, len(paths), batchsize_json_files):
        #     paths_batch = paths[i : i + batchsize_json_files]
        #     sub_results = self.read_json_files_to_df(paths_batch)
        #     results = results + sub_results
        #     gc.collect()

        # logging.log(
        #     logging.INFO, f"len raw data frames: {len(results)} for prefix {prefix}"
        # )

        # if len(results) > 0:
        #     return pd.concat(results, sort=False).reset_index(drop=True)

        # return None

        
        # results = []
        # processes = []
        # connections = []

        # for path in paths:
        #     parent_conn, child_conn = Pipe()
        #     connections.append(parent_conn)

        #     process = Process(target=self.read_json_to_df, args=(path, child_conn))
        #     processes.append(process)

        # for process in processes:
        #     process.start()

        # for conn in connections:
        #     try:
        #         df = conn.recv()
        #         if df is not None:
        #             results.append(df)

        #         conn.close()

        #     except EOFError:
        #         conn.close()
        #         pass

        # for process in processes:
        #     process.join()

        # return results


        
        # try:
        #     obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
        #     df = pd.read_json(obj["Body"], convert_dates=False)
        #     conn.send(df)
        #     conn.close()
        #     return
        # except ClientError:
        #     time.sleep(backoff)
        #     self.read_json_to_df(key, conn, backoff * 2)
        # except:  # noqa E722 ## Ignore use of bare 'except' for Flake8
        #     err = sys.exc_info()[0]
        #     logging.exception(f"Exception reading {key}: {err}")
        #     conn.send(None)
        #     conn.close()
        #     return
    return True

