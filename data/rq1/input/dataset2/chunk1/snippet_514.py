#Source: https://stackoverflow.com/questions/48244659/multiprocessing-cannot-write-list-to-csv-typeerror-applyresult-object-is-n
from multiprocessing import Pool
import csv
pool = Pool()

nodes = [['1001', '2008-01-06T02:12:13Z', ['']],
        ['1002', '2008-01-06T02:13:55Z', ['']],
        ['1003', '2008-01-06T02:13:00Z',  ['Lion', 'Rhinoceros', 'Leopard', 'Panda']],
        ['1004', '2008-01-06T02:15:20Z', ['Lion', 'Leopard', 'Eagle', 'Panda', 'Tiger']],
        ['1005', '2008-01-06T02:15:48Z', ['Lion', 'Panda', 'Cheetah', 'Goat', 'Tiger']],
        ['1006', '2008-01-06T02:13:30Z', ['']],
        ['1007', '2008-01-06T02:13:38Z', ['Cheetah', 'Tiger', 'Goat']]]

def nodes_to_links(nodes_list):
    output_list = []
    for ii, elem in enumerate(nodes_list[:-1]):
        for jj in range(ii + 1, len(nodes_list)):
            common = set(elem[-1]).intersection(
                set(nodes_list[jj][-1]))
            if len(common) > 0 and common != {''}:
                output_list.append([elem[0], nodes_list[jj][0], ','.join(map(str, list(common)))])
    return output_list

#links = nodes_to_links(nodes) ###This works perfect without multiprocessing
links = pool.apply_async(nodes_to_links, (nodes))  ### This works if I don't write the list "links" to a csv, but not otherwise

# Write links to a csv file
def writeCSV(list_to_write, OutputFileName):
    file = open(OutputFileName, 'w', newline='')
    writer = csv.writer(file, quotechar='"', delimiter=';',quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in list_to_write:
        writer.writerow(row)

writeCSV(links,'output_files/test.csv')