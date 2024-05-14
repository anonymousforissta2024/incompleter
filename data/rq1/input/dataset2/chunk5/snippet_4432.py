#Source: https://stackoverflow.com/questions/64748436/typeerror-not-supported-between-instances-of-float-and-synchronized
if __name__ == "__main__":
    start_time =  multiprocessing.Value( 'd', 0.0)
    time_t = multiprocessing.Value('d', 0.005)
    producer(all_client, q[0], time_t, start_time, t)