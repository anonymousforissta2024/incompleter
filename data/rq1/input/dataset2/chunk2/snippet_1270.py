#Source: https://stackoverflow.com/questions/69448637/amazon-sagemaker-typeerror-cant-pickle-dict-keys-objects
sc = SparkContext(appName='microsegment-job')
rdd = sc.textFile(dataset_path)
header = rdd.first()
cols = header.split(delimiter)

cols_dict = {cols[i]: i for i in range(len(cols))}

other_kpis = []
for i in cols:
    if i in filter_cond or i == 'CONSUMER_ID':
        continue
    if i == 'eventids':
        break
    other_kpis.append(i)

def return_row(z):
    temp = z.split(delimiter)
    row = [float(temp[cols_dict[kpi]]) if temp[cols_dict[kpi]] != '' else 0.0 for kpi in (kpi_list + other_kpis)] + [
        temp[cols_dict['eventids']]] + [temp[cols_dict['conversions']]]
    return row

rdd_splitted = rdd.filter(lambda z: header not in z).map(return_row)
eids = rdd_splitted.flatMap(lambda x: x[len(x) - 2].split("|")).distinct().collect() # Exception thrown in this line