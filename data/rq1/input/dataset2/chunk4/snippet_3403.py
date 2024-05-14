#Source: https://stackoverflow.com/questions/65603054/typeerror-while-using-pool-from-multiprocessing-python-3-7
import os
from multiprocessing import Pool

def _count(self, path):
    stats = dict.fromkeys(self._categories, 0)
    try:
        dir_list = os.listdir(path)
    except:
        # I do some warning here, but removed it for SSCCE
        return stats

    for element in dir_list:
        new_path = os.path.join(path, element)

        if os.path.isdir(new_path):
            add_stats = self._count(new_path)
            stats = self._sum_dicts([stats, add_stats])
        else:
            file_type = self._get_file_type(element)
            try:
                size = os.path.getsize(new_path)
            except Exception as e:
                # I do some warning here, but removed it for SSCCE
                continue

            stats[file_type] += size

    return stats

files = []
dirs = []
for e in dir_list:
    new_name = os.path.join(path, e)
    if os.path.isdir(new_name):
        dirs.append(new_name)
    else:
        files.append(new_name)

with Pool(processes=number_of_threats) as pool:
    res = pool.map(self._count, dirs)

self._stats = self._sum_dicts(res)