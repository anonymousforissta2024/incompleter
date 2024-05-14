#Source: https://stackoverflow.com/questions/60049527/shutting-down-manager-error-attributeerror-forkawarelocal-object-has-no-attr
import multiprocessing

import pandas as pd
import numpy as np


def add_empty_dfs_to_shared_dict(shared_dict, key):
    shared_dict[key] = pd.DataFrame()


def edit_df_in_shared_dict(shared_dict, namespace, ind):
    row_to_insert = namespace.df.loc[ind]
    df = shared_dict[ind]
    df[ind] = row_to_insert
    shared_dict[ind] = df


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    shared_dict = manager.dict()
    namespace = manager.Namespace()

    n = 100
    dataframe_to_be_shared = pd.DataFrame({
        'player_id': list(range(n)),
        'data': np.random.random(n),
    }).set_index('player_id')

    namespace.df = dataframe_to_be_shared

    for i in range(n):
        add_empty_dfs_to_shared_dict(shared_dict, i)

    jobs = []
    for i in range(n):
        p = multiprocessing.Process(
            target=edit_df_in_shared_dict,
            args=(shared_dict, namespace, i)
        )
        jobs.append(p)
        p.start()

    for p in jobs:
        p.join()

    print(shared_dict[1])